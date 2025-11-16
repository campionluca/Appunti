# Code Policies - Docker

> Standard, convenzioni e best practices per Docker e containerizzazione

## 📋 Indice
- [Dockerfile Best Practices](#dockerfile-best-practices)
- [Image Naming](#image-naming)
- [Docker Compose](#docker-compose)
- [Security](#security)
- [Performance](#performance)
- [Multi-stage Builds](#multi-stage-builds)
- [Networking](#networking)
- [Volumes & Data](#volumes--data)

---

## Dockerfile Best Practices

### Basic Structure
```dockerfile
# Use specific version tags, not 'latest'
FROM node:18-alpine AS base

# Metadata
LABEL maintainer="your.email@example.com"
LABEL version="1.0.0"
LABEL description="Application description"

# Install system dependencies (combine into single layer)
RUN apk add --no-cache \
    python3 \
    make \
    g++

# Set working directory
WORKDIR /app

# Copy dependency files first (better caching)
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Change ownership
RUN chown -R nodejs:nodejs /app

# Switch to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD node healthcheck.js || exit 1

# Start command
CMD ["node", "server.js"]
```

### Layer Optimization
```dockerfile
# ❌ BAD: Multiple RUN commands create multiple layers
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get clean

# ✅ GOOD: Combine into single layer
RUN apt-get update && \
    apt-get install -y \
        curl \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ❌ BAD: Copy everything, then install
COPY . .
RUN npm install

# ✅ GOOD: Copy dependencies first for better caching
COPY package*.json ./
RUN npm ci
COPY . .
```

### .dockerignore
```
# Version control
.git
.gitignore
.gitattributes

# Dependencies
node_modules
npm-debug.log
yarn-error.log

# Testing
coverage
.nyc_output
*.test.js
__tests__

# Documentation
README.md
docs/
*.md

# IDE
.vscode
.idea
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Build artifacts
dist
build
*.log

# Environment files
.env
.env.local
.env.*.local

# Temporary files
tmp/
temp/
*.tmp
```

---

## Image Naming

### Naming Convention
```bash
# Format: [registry/][namespace/]repository[:tag]

# Examples:
myapp:latest
myapp:1.0.0
myapp:1.0.0-alpine
username/myapp:latest
registry.example.com/myapp:v1.2.3

# Best practices:
myapp:1.2.3                    # Semantic version
myapp:1.2.3-alpine             # Variant
myapp:sha-abc123               # Git commit SHA
myapp:prod                     # Environment
myapp:2025-01-16               # Date-based
```

### Tagging Strategy
```bash
# Tag with version
docker build -t myapp:1.0.0 .

# Tag with multiple tags
docker build -t myapp:1.0.0 -t myapp:latest .

# Tag specific variant
docker build -t myapp:1.0.0-alpine -f Dockerfile.alpine .

# Tag with registry
docker build -t registry.example.com/myapp:1.0.0 .

# Retag existing image
docker tag myapp:1.0.0 myapp:latest
docker tag myapp:1.0.0 registry.example.com/myapp:1.0.0
```

---

## Docker Compose

### docker-compose.yml Template
```yaml
version: '3.8'

# Define reusable configurations
x-logging: &default-logging
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"

x-healthcheck: &default-healthcheck
  interval: 30s
  timeout: 3s
  retries: 3
  start_period: 40s

services:
  # Application service
  app:
    build:
      context: .
      dockerfile: Dockerfile
      target: production
      args:
        - NODE_ENV=production
    image: myapp:${VERSION:-latest}
    container_name: myapp
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - backend
      - frontend
    volumes:
      - ./uploads:/app/uploads
      - app-logs:/var/log/app
    logging: *default-logging
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '1'
          memory: 512M

  # Database service
  db:
    image: postgres:15-alpine
    container_name: postgres
    restart: unless-stopped
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - backend
    logging: *default-logging
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d mydb"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Cache service
  redis:
    image: redis:7-alpine
    container_name: redis
    restart: unless-stopped
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - backend
    logging: *default-logging
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3

  # Nginx reverse proxy
  nginx:
    image: nginx:alpine
    container_name: nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - app
    networks:
      - frontend
    logging: *default-logging

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # No external access

volumes:
  postgres-data:
    driver: local
  redis-data:
    driver: local
  app-logs:
    driver: local
```

### Compose Commands
```bash
# Start services
docker-compose up
docker-compose up -d              # Detached mode
docker-compose up --build         # Rebuild images

# Stop services
docker-compose stop
docker-compose down               # Stop and remove
docker-compose down -v            # Also remove volumes

# View logs
docker-compose logs
docker-compose logs -f app        # Follow specific service
docker-compose logs --tail=100    # Last 100 lines

# Execute commands
docker-compose exec app sh
docker-compose exec db psql -U user -d mydb

# Scale services
docker-compose up -d --scale app=3

# Restart service
docker-compose restart app
```

---

## Security

### Security Best Practices
```dockerfile
# ✅ Use official base images
FROM node:18-alpine

# ✅ Specify exact versions
FROM node:18.19.0-alpine3.19

# ✅ Use minimal base images
FROM alpine:3.19           # Instead of ubuntu
FROM node:18-alpine        # Instead of node:18

# ✅ Run as non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs

# ✅ Don't include secrets in image
# Use environment variables or secrets management
ENV DATABASE_URL=${DATABASE_URL}

# ❌ NEVER do this:
ENV DATABASE_PASSWORD=mypassword
COPY .env .

# ✅ Scan images for vulnerabilities
# docker scan myapp:latest
# trivy image myapp:latest

# ✅ Use read-only root filesystem when possible
docker run --read-only myapp

# ✅ Drop capabilities
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE myapp

# ✅ Limit resources
docker run --memory="512m" --cpus="1.5" myapp
```

### Secrets Management
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    image: myapp
    secrets:
      - db_password
      - api_key
    environment:
      - DB_PASSWORD_FILE=/run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
  api_key:
    external: true  # From Docker secrets
```

---

## Performance

### Build Optimization
```dockerfile
# Use build cache effectively
# Order instructions from least to most frequently changing

FROM node:18-alpine

# 1. Install system dependencies (rarely changes)
RUN apk add --no-cache python3 make g++

# 2. Set working directory
WORKDIR /app

# 3. Copy dependency files (changes occasionally)
COPY package*.json ./

# 4. Install dependencies
RUN npm ci --only=production

# 5. Copy source code (changes frequently)
COPY . .

# 6. Build application (if needed)
RUN npm run build

CMD ["node", "dist/server.js"]
```

### BuildKit Features
```dockerfile
# Enable BuildKit: export DOCKER_BUILDKIT=1

# Mount cache for package managers
RUN --mount=type=cache,target=/root/.npm \
    npm ci --only=production

# Mount secrets (won't be in final image)
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm ci

# Parallel build stages
FROM base AS dependencies
RUN npm ci

FROM base AS build
COPY . .
RUN npm run build

FROM base AS production
COPY --from=dependencies /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
```

### Image Size Reduction
```dockerfile
# Multi-stage build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage - smaller image
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/server.js"]

# Result: ~150MB instead of ~900MB
```

---

## Multi-stage Builds

### Development vs Production
```dockerfile
# Development stage
FROM node:18 AS development
WORKDIR /app
COPY package*.json ./
RUN npm install  # Include dev dependencies
COPY . .
CMD ["npm", "run", "dev"]

# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
RUN npm prune --production  # Remove dev dependencies

# Production stage
FROM node:18-alpine AS production
WORKDIR /app
RUN addgroup -g 1001 nodejs && adduser -S nodejs -u 1001
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
USER nodejs
EXPOSE 3000
CMD ["node", "dist/server.js"]

# Testing stage
FROM builder AS test
RUN npm run test
```

### Build specific stage
```bash
# Development
docker build --target development -t myapp:dev .

# Production
docker build --target production -t myapp:prod .

# Run tests
docker build --target test -t myapp:test .
```

---

## Networking

### Network Types
```bash
# Bridge (default)
docker network create my-bridge

# Host (use host network)
docker run --network host myapp

# None (no networking)
docker run --network none myapp

# Custom bridge with subnet
docker network create --driver bridge \
  --subnet=172.28.0.0/16 \
  --gateway=172.28.0.1 \
  my-custom-network
```

### Network Configuration
```yaml
# docker-compose.yml
version: '3.8'

services:
  frontend:
    image: frontend
    networks:
      - public

  backend:
    image: backend
    networks:
      - public
      - private

  database:
    image: postgres
    networks:
      - private  # Not accessible from outside

networks:
  public:
    driver: bridge
  private:
    driver: bridge
    internal: true  # No external access
```

---

## Volumes & Data

### Volume Types
```bash
# Named volume (managed by Docker)
docker volume create mydata
docker run -v mydata:/data myapp

# Bind mount (host path)
docker run -v /host/path:/container/path myapp
docker run -v $(pwd):/app myapp

# Tmpfs mount (in-memory)
docker run --tmpfs /tmp myapp
```

### Volume Configuration
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    image: myapp
    volumes:
      # Named volume
      - data:/app/data

      # Bind mount
      - ./config:/app/config:ro  # Read-only

      # Tmpfs mount
      - type: tmpfs
        target: /tmp

      # Volume with options
      - type: volume
        source: uploads
        target: /app/uploads
        volume:
          nocopy: true

volumes:
  data:
    driver: local
  uploads:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /host/uploads
```

### Backup & Restore
```bash
# Backup volume
docker run --rm -v mydata:/data -v $(pwd):/backup \
  alpine tar czf /backup/backup.tar.gz -C /data .

# Restore volume
docker run --rm -v mydata:/data -v $(pwd):/backup \
  alpine tar xzf /backup/backup.tar.gz -C /data
```

---

## Note Aggiuntive

### Useful Commands
```bash
# Build
docker build -t myapp:latest .
docker build --no-cache -t myapp:latest .

# Run
docker run -d -p 3000:3000 --name myapp myapp:latest
docker run -it --rm myapp sh  # Interactive, remove after exit

# Inspect
docker inspect myapp
docker logs myapp
docker logs -f myapp  # Follow logs
docker stats myapp    # Resource usage

# Execute commands
docker exec myapp ls -la
docker exec -it myapp sh

# Clean up
docker system prune                # Remove unused data
docker system prune -a             # Remove all unused images
docker volume prune                # Remove unused volumes
docker image prune -a              # Remove all unused images
```

### Dockerfile Linting
```bash
# hadolint - Dockerfile linter
docker run --rm -i hadolint/hadolint < Dockerfile

# Common rules:
# DL3003: Use WORKDIR instead of cd
# DL3008: Pin package versions in apt-get
# DL3009: Delete apt cache
# DL3059: Multiple COPY commands
```

### Riferimenti
- Docker Documentation (docs.docker.com)
- Docker Best Practices (docs.docker.com/develop/dev-best-practices)
- Dockerfile Best Practices (docs.docker.com/develop/develop-images/dockerfile_best-practices)
- Docker Compose Documentation (docs.docker.com/compose)

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
