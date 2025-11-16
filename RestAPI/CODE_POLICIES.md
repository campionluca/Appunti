# Code Policies - REST API

> Standard, convenzioni e best practices per design e implementazione REST API

## 📋 Indice
- [Design Principles](#design-principles)
- [URL Structure](#url-structure)
- [HTTP Methods](#http-methods)
- [Request & Response](#request--response)
- [Status Codes](#status-codes)
- [Error Handling](#error-handling)
- [Versioning](#versioning)
- [Security](#security)
- [Documentation](#documentation)

---

## Design Principles

### REST Principles
1. **Client-Server**: Separazione tra client e server
2. **Stateless**: Ogni richiesta contiene tutte le info necessarie
3. **Cacheable**: Le risposte devono indicare se sono cacheable
4. **Uniform Interface**: Interfaccia uniforme per tutte le risorse
5. **Layered System**: Architettura a livelli
6. **Code on Demand** (opzionale): Server può inviare codice eseguibile

### API Design Best Practices
- [ ] Usare nomi (sostantivi), non verbi negli URL
- [ ] Usare plurale per collezioni
- [ ] Risorse nidificate per relazioni
- [ ] Versioning nell'URL o headers
- [ ] Filtrare, ordinare, paginare collezioni
- [ ] Usare HTTP methods correttamente
- [ ] Fornire risposte consistenti

---

## URL Structure

### Resource Naming
```
# ✅ CORRETTO: Nomi al plurale, sostantivi
GET    /users              # List all users
GET    /users/123          # Get specific user
POST   /users              # Create user
PUT    /users/123          # Update user
DELETE /users/123          # Delete user

# ❌ SBAGLIATO: Verbi negli URL
GET    /getUsers
GET    /getUserById/123
POST   /createUser
```

### Nested Resources
```
# Risorse correlate
GET    /users/123/orders              # Get user's orders
GET    /users/123/orders/456          # Get specific order
POST   /users/123/orders              # Create order for user
DELETE /users/123/orders/456          # Delete user's order

# Limite nesting (max 2-3 livelli)
# ✅ CORRETTO
GET /users/123/orders/456/items

# ❌ EVITARE: Troppo nesting
GET /users/123/orders/456/items/789/details/abc
```

### Query Parameters
```
# Filtering
GET /users?status=active&role=admin

# Sorting
GET /users?sort=created_at&order=desc
GET /users?sort=-created_at              # - prefix per desc

# Pagination
GET /users?page=2&limit=20
GET /users?offset=40&limit=20

# Field selection
GET /users?fields=id,name,email

# Search
GET /users?q=john
GET /products?search=laptop

# Combined
GET /users?status=active&role=admin&sort=created_at&page=1&limit=20
```

### URL Structure Examples
```
# Resource operations
/api/v1/users                          # Users collection
/api/v1/users/{userId}                 # Specific user
/api/v1/users/{userId}/profile         # User profile
/api/v1/users/{userId}/orders          # User's orders

# Sub-resources
/api/v1/orders/{orderId}/items         # Order items
/api/v1/posts/{postId}/comments        # Post comments
/api/v1/categories/{catId}/products    # Category products

# Actions (when needed)
/api/v1/users/{userId}/activate        # POST: Activate user
/api/v1/orders/{orderId}/cancel        # POST: Cancel order
/api/v1/invoices/{invoiceId}/send      # POST: Send invoice

# Naming conventions
- Use lowercase
- Use hyphens (-) not underscores (_)
- No trailing slashes
- File extensions not needed (.json, .xml)
```

---

## HTTP Methods

### Method Usage
```
GET     - Retrieve resource(s) (safe, idempotent, cacheable)
POST    - Create new resource (not idempotent)
PUT     - Update/replace entire resource (idempotent)
PATCH   - Partial update resource (idempotent)
DELETE  - Delete resource (idempotent)
HEAD    - Like GET but without body
OPTIONS - Get allowed methods for resource
```

### Examples

#### GET - Retrieve
```http
# Get collection
GET /api/v1/users HTTP/1.1
Accept: application/json

Response: 200 OK
{
  "data": [
    { "id": 1, "name": "John Doe", "email": "john@example.com" },
    { "id": 2, "name": "Jane Smith", "email": "jane@example.com" }
  ],
  "meta": {
    "total": 2,
    "page": 1,
    "limit": 20
  }
}

# Get single resource
GET /api/v1/users/1 HTTP/1.1
Accept: application/json

Response: 200 OK
{
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2025-01-15T10:30:00Z"
  }
}
```

#### POST - Create
```http
POST /api/v1/users HTTP/1.1
Content-Type: application/json

{
  "name": "New User",
  "email": "newuser@example.com",
  "password": "securepassword123"
}

Response: 201 Created
Location: /api/v1/users/3
{
  "data": {
    "id": 3,
    "name": "New User",
    "email": "newuser@example.com",
    "created_at": "2025-01-16T14:20:00Z"
  }
}
```

#### PUT - Full Update
```http
PUT /api/v1/users/3 HTTP/1.1
Content-Type: application/json

{
  "name": "Updated User",
  "email": "updated@example.com",
  "role": "admin"
}

Response: 200 OK
{
  "data": {
    "id": 3,
    "name": "Updated User",
    "email": "updated@example.com",
    "role": "admin",
    "updated_at": "2025-01-16T15:00:00Z"
  }
}
```

#### PATCH - Partial Update
```http
PATCH /api/v1/users/3 HTTP/1.1
Content-Type: application/json

{
  "email": "newemail@example.com"
}

Response: 200 OK
{
  "data": {
    "id": 3,
    "name": "Updated User",
    "email": "newemail@example.com",
    "role": "admin",
    "updated_at": "2025-01-16T15:30:00Z"
  }
}
```

#### DELETE - Remove
```http
DELETE /api/v1/users/3 HTTP/1.1

Response: 204 No Content
```

---

## Request & Response

### Request Headers
```http
# Content negotiation
Accept: application/json
Content-Type: application/json

# Authentication
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
API-Key: your-api-key-here

# Caching
If-None-Match: "686897696a7c876b7e"
If-Modified-Since: Sat, 15 Jan 2025 10:00:00 GMT

# Custom headers (prefix with X-)
X-Request-ID: 550e8400-e29b-41d4-a716-446655440000
X-API-Version: 2.0
```

### Response Headers
```http
# Content type
Content-Type: application/json; charset=utf-8

# Caching
Cache-Control: max-age=3600, public
ETag: "686897696a7c876b7e"
Last-Modified: Sat, 15 Jan 2025 10:00:00 GMT

# Rate limiting
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1642248000

# CORS
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization

# Pagination (Link header)
Link: </api/v1/users?page=3>; rel="next", </api/v1/users?page=1>; rel="prev"
```

### Response Body Format
```json
// Successful response
{
  "data": {
    "id": 1,
    "name": "Resource Name",
    "attributes": {}
  },
  "meta": {
    "timestamp": "2025-01-16T10:00:00Z",
    "version": "1.0"
  }
}

// Collection response
{
  "data": [
    { "id": 1, "name": "Item 1" },
    { "id": 2, "name": "Item 2" }
  ],
  "meta": {
    "total": 100,
    "page": 1,
    "per_page": 20,
    "total_pages": 5
  },
  "links": {
    "self": "/api/v1/items?page=1",
    "next": "/api/v1/items?page=2",
    "last": "/api/v1/items?page=5"
  }
}
```

---

## Status Codes

### Success Codes (2xx)
```
200 OK                  - Successful GET, PUT, PATCH or DELETE
201 Created             - Successful POST (resource created)
202 Accepted            - Request accepted, processing async
204 No Content          - Successful request with no response body
206 Partial Content     - Partial GET (range request)
```

### Redirection Codes (3xx)
```
301 Moved Permanently   - Resource moved permanently
302 Found               - Temporary redirect
304 Not Modified        - Resource not modified (caching)
```

### Client Error Codes (4xx)
```
400 Bad Request         - Invalid request syntax
401 Unauthorized        - Authentication required
403 Forbidden           - Authenticated but not authorized
404 Not Found           - Resource not found
405 Method Not Allowed  - HTTP method not allowed
409 Conflict            - Request conflicts with current state
422 Unprocessable Entity- Validation errors
429 Too Many Requests   - Rate limit exceeded
```

### Server Error Codes (5xx)
```
500 Internal Server Error   - Generic server error
502 Bad Gateway            - Invalid response from upstream
503 Service Unavailable    - Service temporarily unavailable
504 Gateway Timeout        - Upstream timeout
```

### Status Code Examples
```http
# 200 OK - Successful retrieval
GET /api/v1/users/1
Response: 200 OK

# 201 Created - Resource created
POST /api/v1/users
Response: 201 Created
Location: /api/v1/users/123

# 204 No Content - Successful deletion
DELETE /api/v1/users/1
Response: 204 No Content

# 400 Bad Request - Invalid input
POST /api/v1/users
{ "email": "invalid-email" }
Response: 400 Bad Request

# 401 Unauthorized - Missing auth
GET /api/v1/users
Response: 401 Unauthorized

# 404 Not Found - Resource doesn't exist
GET /api/v1/users/999
Response: 404 Not Found

# 422 Unprocessable Entity - Validation failed
POST /api/v1/users
{ "email": "" }
Response: 422 Unprocessable Entity
```

---

## Error Handling

### Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "message": "Email is required",
        "code": "REQUIRED_FIELD"
      },
      {
        "field": "password",
        "message": "Password must be at least 8 characters",
        "code": "MIN_LENGTH"
      }
    ],
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2025-01-16T10:00:00Z"
  }
}
```

### Error Examples
```json
// 400 Bad Request
{
  "error": {
    "code": "BAD_REQUEST",
    "message": "Invalid request format",
    "details": "JSON parsing failed at line 3"
  }
}

// 401 Unauthorized
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required",
    "details": "Missing or invalid authorization token"
  }
}

// 403 Forbidden
{
  "error": {
    "code": "FORBIDDEN",
    "message": "Access denied",
    "details": "You don't have permission to access this resource"
  }
}

// 404 Not Found
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Resource not found",
    "details": "User with ID 123 does not exist"
  }
}

// 422 Validation Error
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Input validation failed",
    "details": [
      {
        "field": "email",
        "value": "invalid",
        "message": "Must be a valid email address",
        "code": "INVALID_EMAIL"
      }
    ]
  }
}

// 429 Rate Limit
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests",
    "details": "Limit of 100 requests per hour exceeded",
    "retry_after": 3600
  }
}

// 500 Internal Server Error
{
  "error": {
    "code": "INTERNAL_SERVER_ERROR",
    "message": "An unexpected error occurred",
    "request_id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

---

## Versioning

### URL Versioning
```
# Version in URL path (recommended)
/api/v1/users
/api/v2/users

# Major version only
/api/v1/...
/api/v2/...
```

### Header Versioning
```http
# Custom header
GET /api/users HTTP/1.1
API-Version: 2.0

# Accept header
GET /api/users HTTP/1.1
Accept: application/vnd.myapi.v2+json
```

### Query Parameter Versioning
```
# Version as query param (not recommended)
GET /api/users?version=2
```

### Deprecation Strategy
```http
# Deprecated endpoint
GET /api/v1/users HTTP/1.1

Response Headers:
Deprecation: true
Sunset: Sat, 31 Dec 2025 23:59:59 GMT
Link: </api/v2/users>; rel="alternate"

# Response body
{
  "data": [...],
  "meta": {
    "deprecated": true,
    "sunset": "2025-12-31T23:59:59Z",
    "message": "This endpoint is deprecated. Please use /api/v2/users"
  }
}
```

---

## Security

### Authentication
```http
# Bearer Token (JWT)
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# API Key
X-API-Key: your-api-key-here
API-Key: your-api-key-here

# Basic Auth (use HTTPS only!)
Authorization: Basic base64(username:password)

# OAuth 2.0
Authorization: Bearer <access_token>
```

### Input Validation
```javascript
// Validate all inputs
// - Type validation
// - Length limits
// - Format validation (email, URL, etc.)
// - Sanitize strings

// Example validation
{
  "email": {
    "type": "string",
    "format": "email",
    "required": true,
    "maxLength": 255
  },
  "age": {
    "type": "integer",
    "minimum": 0,
    "maximum": 150
  }
}
```

### Rate Limiting
```http
# Response headers
X-RateLimit-Limit: 100          # Max requests per window
X-RateLimit-Remaining: 95       # Remaining requests
X-RateLimit-Reset: 1642248000   # Reset timestamp

# When limit exceeded
HTTP/1.1 429 Too Many Requests
Retry-After: 3600

{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again in 1 hour"
  }
}
```

### Security Headers
```http
# HTTPS only
Strict-Transport-Security: max-age=31536000; includeSubDomains

# Prevent XSS
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block

# Content Security Policy
Content-Security-Policy: default-src 'self'

# CORS
Access-Control-Allow-Origin: https://trusted-domain.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 86400
```

### Best Practices
- [ ] Always use HTTPS in production
- [ ] Validate and sanitize all inputs
- [ ] Use parameterized queries (prevent SQL injection)
- [ ] Implement rate limiting
- [ ] Use authentication and authorization
- [ ] Don't expose sensitive data in URLs
- [ ] Log security events
- [ ] Keep dependencies updated

---

## Documentation

### OpenAPI/Swagger Example
```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
  description: API for managing users

servers:
  - url: https://api.example.com/v1
    description: Production server

paths:
  /users:
    get:
      summary: List all users
      description: Returns a paginated list of users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
                  meta:
                    $ref: '#/components/schemas/PaginationMeta'

    post:
      summary: Create a new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          $ref: '#/components/responses/BadRequest'
        '422':
          $ref: '#/components/responses/ValidationError'

  /users/{userId}:
    get:
      summary: Get user by ID
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
          example: 1
        name:
          type: string
          example: "John Doe"
        email:
          type: string
          format: email
          example: "john@example.com"
        created_at:
          type: string
          format: date-time

    CreateUserRequest:
      type: object
      required:
        - name
        - email
        - password
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 100
        email:
          type: string
          format: email
        password:
          type: string
          minLength: 8

  responses:
    BadRequest:
      description: Bad request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - bearerAuth: []
```

### API Documentation Best Practices
- [ ] Provide clear endpoint descriptions
- [ ] Document all parameters and their types
- [ ] Show request/response examples
- [ ] Document error responses
- [ ] Include authentication requirements
- [ ] Provide code examples in multiple languages
- [ ] Keep documentation up to date
- [ ] Use tools: Swagger/OpenAPI, Postman, ReDoc

---

## Note Aggiuntive

### Tools
- **Design**: Postman, Insomnia, Swagger Editor
- **Documentation**: Swagger UI, ReDoc, Stoplight
- **Testing**: Postman, REST Client, curl, HTTPie
- **Mocking**: JSON Server, Mockoon, Prism

### Riferimenti
- REST API Tutorial (restfulapi.net)
- HTTP Status Codes (httpstatuses.com)
- OpenAPI Specification (swagger.io/specification)
- RFC 7231 - HTTP/1.1 Semantics

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
