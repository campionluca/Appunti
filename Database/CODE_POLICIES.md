# Code Policies - Database & SQL

> Standard, convenzioni e politiche di scrittura per query SQL e design database

## 📋 Indice
- [Standard di Scrittura](#standard-di-scrittura)
- [Convenzioni di Nomenclatura](#convenzioni-di-nomenclatura)
- [Template di Query](#template-di-query)
- [Design Database](#design-database)
- [Best Practices](#best-practices)
- [Pattern di Programmazione](#pattern-di-programmazione)
- [Ottimizzazione](#ottimizzazione)
- [Sicurezza e Documentazione](#sicurezza-e-documentazione)

---

## Standard di Scrittura

### Formattazione SQL
- **Keywords**: UPPERCASE - `SELECT`, `FROM`, `WHERE`
- **Identifiers**: snake_case - `user_id`, `created_at`
- **Indentazione**: 2 o 4 spazi
- **Allineamento**: Allineare clausole principali
- **Una clausola per riga**: Per query complesse

### Stile del Codice
```sql
-- Query semplice
SELECT id, name, email
FROM users
WHERE active = TRUE
ORDER BY created_at DESC;

-- Query complessa con formattazione
SELECT
    u.id,
    u.name,
    u.email,
    COUNT(o.id) AS order_count,
    SUM(o.total) AS total_spent
FROM users AS u
    LEFT JOIN orders AS o ON u.id = o.user_id
WHERE
    u.active = TRUE
    AND u.created_at >= '2024-01-01'
GROUP BY
    u.id,
    u.name,
    u.email
HAVING COUNT(o.id) > 5
ORDER BY total_spent DESC
LIMIT 100;

-- CTE (Common Table Expression)
WITH active_users AS (
    SELECT id, name, email
    FROM users
    WHERE active = TRUE
),
recent_orders AS (
    SELECT user_id, COUNT(*) AS order_count
    FROM orders
    WHERE created_at >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY user_id
)
SELECT
    au.name,
    au.email,
    COALESCE(ro.order_count, 0) AS recent_orders
FROM active_users AS au
    LEFT JOIN recent_orders AS ro ON au.id = ro.user_id;
```

### Regole Generali
- [ ] Sempre usare explicit JOIN invece di implicit join
- [ ] Usare alias significativi per tabelle
- [ ] Terminare statement con punto e virgola
- [ ] Evitare SELECT *
- [ ] Usare UPPERCASE per keywords SQL

---

## Convenzioni di Nomenclatura

### Tabelle
- **Naming**: `snake_case`, plurale - Esempio: `users`, `order_items`
- **Junction tables**: `table1_table2` - Esempio: `users_roles`
- **Evitare prefissi**: ~~`tbl_users`~~, preferire `users`

### Colonne
- **Naming**: `snake_case` - Esempio: `first_name`, `created_at`
- **Primary Key**: `id` (o `table_name_id`)
- **Foreign Key**: `referenced_table_id` - Esempio: `user_id`, `order_id`
- **Boolean**: `is_` o `has_` prefix - Esempio: `is_active`, `has_verified`
- **Timestamps**: `created_at`, `updated_at`, `deleted_at`

### Indici
- **Naming**: `idx_table_column` - Esempio: `idx_users_email`
- **Unique**: `unq_table_column` - Esempio: `unq_users_email`
- **Foreign Key**: `fk_table_referenced` - Esempio: `fk_orders_users`

### Constraints
- **Primary Key**: `pk_table` - Esempio: `pk_users`
- **Foreign Key**: `fk_table_referenced` - Esempio: `fk_orders_users`
- **Check**: `chk_table_condition` - Esempio: `chk_users_age`
- **Unique**: `unq_table_column` - Esempio: `unq_users_email`

### Viste e Stored Procedures
- **Views**: `v_name` o `view_name` - Esempio: `v_active_users`
- **Stored Procedures**: `sp_action` - Esempio: `sp_create_user`
- **Functions**: `fn_name` - Esempio: `fn_calculate_total`
- **Triggers**: `trg_table_action` - Esempio: `trg_users_audit`

---

## Template di Query

### CREATE TABLE
```sql
-- ============================================================================
-- Table: users
-- Description: Stores user account information
-- Author: Nome Autore
-- Date: 2025-11-16
-- ============================================================================

CREATE TABLE IF NOT EXISTS users (
    -- Primary Key
    id              BIGSERIAL PRIMARY KEY,

    -- User Information
    email           VARCHAR(255) NOT NULL,
    username        VARCHAR(50) NOT NULL,
    first_name      VARCHAR(100),
    last_name       VARCHAR(100),

    -- Authentication
    password_hash   VARCHAR(255) NOT NULL,
    email_verified  BOOLEAN NOT NULL DEFAULT FALSE,

    -- Status
    is_active       BOOLEAN NOT NULL DEFAULT TRUE,
    is_deleted      BOOLEAN NOT NULL DEFAULT FALSE,

    -- Timestamps
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_login_at   TIMESTAMP,
    deleted_at      TIMESTAMP,

    -- Constraints
    CONSTRAINT unq_users_email UNIQUE (email),
    CONSTRAINT unq_users_username UNIQUE (username),
    CONSTRAINT chk_users_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$')
);

-- Indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_users_active ON users(is_active) WHERE is_active = TRUE;

-- Comments
COMMENT ON TABLE users IS 'User accounts and authentication information';
COMMENT ON COLUMN users.email IS 'User email address (unique, required)';
COMMENT ON COLUMN users.is_active IS 'Whether the user account is active';
```

### Foreign Key Relationship
```sql
-- ============================================================================
-- Table: orders
-- Description: Customer orders
-- ============================================================================

CREATE TABLE orders (
    id              BIGSERIAL PRIMARY KEY,
    user_id         BIGINT NOT NULL,

    -- Order Details
    order_number    VARCHAR(50) NOT NULL,
    status          VARCHAR(20) NOT NULL DEFAULT 'pending',
    total_amount    DECIMAL(10, 2) NOT NULL,

    -- Timestamps
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- Foreign Keys
    CONSTRAINT fk_orders_users
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    -- Constraints
    CONSTRAINT unq_orders_number UNIQUE (order_number),
    CONSTRAINT chk_orders_status CHECK (
        status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')
    ),
    CONSTRAINT chk_orders_amount CHECK (total_amount >= 0)
);

CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created_at ON orders(created_at);
```

### View Template
```sql
-- ============================================================================
-- View: v_active_user_orders
-- Description: Active users with their order statistics
-- ============================================================================

CREATE OR REPLACE VIEW v_active_user_orders AS
SELECT
    u.id AS user_id,
    u.email,
    u.username,
    COUNT(o.id) AS total_orders,
    SUM(o.total_amount) AS total_spent,
    MAX(o.created_at) AS last_order_date
FROM users AS u
    LEFT JOIN orders AS o ON u.id = o.user_id
WHERE
    u.is_active = TRUE
    AND u.is_deleted = FALSE
GROUP BY
    u.id,
    u.email,
    u.username;

COMMENT ON VIEW v_active_user_orders IS 'Summary of active users and their order statistics';
```

### Stored Procedure Template
```sql
-- ============================================================================
-- Procedure: sp_create_user
-- Description: Create a new user with validation
-- Parameters:
--   p_email - User email
--   p_username - Username
--   p_password_hash - Hashed password
-- Returns: user_id of created user
-- ============================================================================

CREATE OR REPLACE FUNCTION sp_create_user(
    p_email VARCHAR(255),
    p_username VARCHAR(50),
    p_password_hash VARCHAR(255)
)
RETURNS BIGINT
LANGUAGE plpgsql
AS $$
DECLARE
    v_user_id BIGINT;
BEGIN
    -- Validation
    IF p_email IS NULL OR p_username IS NULL OR p_password_hash IS NULL THEN
        RAISE EXCEPTION 'All parameters are required';
    END IF;

    -- Check if email already exists
    IF EXISTS (SELECT 1 FROM users WHERE email = p_email) THEN
        RAISE EXCEPTION 'Email already exists';
    END IF;

    -- Insert user
    INSERT INTO users (email, username, password_hash)
    VALUES (p_email, p_username, p_password_hash)
    RETURNING id INTO v_user_id;

    -- Log the creation
    INSERT INTO audit_log (table_name, action, record_id)
    VALUES ('users', 'CREATE', v_user_id);

    RETURN v_user_id;
END;
$$;
```

---

## Design Database

### Normalizzazione
```sql
-- Prima Forma Normale (1NF): Atomic values
-- ✅ CORRETTO
CREATE TABLE users (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- ❌ SBAGLIATO
CREATE TABLE users (
    id INT PRIMARY KEY,
    full_name VARCHAR(100)  -- Non atomico
);

-- Seconda Forma Normale (2NF): No partial dependencies
-- ✅ CORRETTO: Separate tables
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    order_date DATE
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    PRIMARY KEY (order_id, product_id)
);

-- Terza Forma Normale (3NF): No transitive dependencies
-- ✅ CORRETTO
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT
);

CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);
```

### Pattern Many-to-Many
```sql
-- Many-to-Many: Users and Roles
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE roles (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- Junction Table
CREATE TABLE users_roles (
    user_id BIGINT NOT NULL,
    role_id BIGINT NOT NULL,
    granted_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (user_id, role_id),

    CONSTRAINT fk_users_roles_user
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_users_roles_role
        FOREIGN KEY (role_id) REFERENCES roles(id)
        ON DELETE CASCADE
);
```

### Soft Delete Pattern
```sql
CREATE TABLE products (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,

    -- Soft delete
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
    deleted_at TIMESTAMP,
    deleted_by BIGINT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Index for active products only
CREATE INDEX idx_products_active
ON products(id)
WHERE is_deleted = FALSE;

-- View for active products
CREATE VIEW v_active_products AS
SELECT *
FROM products
WHERE is_deleted = FALSE;
```

---

## Best Practices

### Query Best Practices
- [ ] Usare prepared statements (prevenire SQL injection)
- [ ] Evitare N+1 queries (usare JOIN o batch loading)
- [ ] Limitare risultati con LIMIT/OFFSET
- [ ] Usare transazioni per operazioni multiple
- [ ] Indicizzare colonne usate in WHERE, JOIN, ORDER BY

### Schema Design
- [ ] Normalizzare per evitare ridondanza
- [ ] Denormalizzare strategicamente per performance
- [ ] Usare tipi di dato appropriati
- [ ] Definire constraints per integrità dati
- [ ] Pianificare per scalabilità

### Performance
- [ ] Creare indici su colonne frequentemente interrogate
- [ ] Evitare SELECT * (specificare colonne necessarie)
- [ ] Usare EXPLAIN per analizzare query plans
- [ ] Batch inserts invece di inserimenti singoli
- [ ] Usare connection pooling

---

## Pattern di Programmazione

### Pattern 1: Pagination
```sql
-- Offset-based pagination
SELECT id, name, email
FROM users
ORDER BY created_at DESC
LIMIT 20 OFFSET 40;  -- Page 3 (20 items per page)

-- Cursor-based pagination (better for large datasets)
SELECT id, name, email
FROM users
WHERE id > :last_seen_id  -- Cursor from previous page
ORDER BY id ASC
LIMIT 20;
```

### Pattern 2: Upsert (INSERT or UPDATE)
```sql
-- PostgreSQL
INSERT INTO users (id, email, name)
VALUES (1, 'user@example.com', 'John Doe')
ON CONFLICT (id)
DO UPDATE SET
    email = EXCLUDED.email,
    name = EXCLUDED.name,
    updated_at = CURRENT_TIMESTAMP;

-- MySQL
INSERT INTO users (id, email, name)
VALUES (1, 'user@example.com', 'John Doe')
ON DUPLICATE KEY UPDATE
    email = VALUES(email),
    name = VALUES(name),
    updated_at = CURRENT_TIMESTAMP;
```

### Pattern 3: Recursive CTE (Tree/Hierarchy)
```sql
-- Get all descendants of a category
WITH RECURSIVE category_tree AS (
    -- Base case: root category
    SELECT id, parent_id, name, 1 AS level
    FROM categories
    WHERE id = :root_category_id

    UNION ALL

    -- Recursive case: children
    SELECT c.id, c.parent_id, c.name, ct.level + 1
    FROM categories AS c
        INNER JOIN category_tree AS ct ON c.parent_id = ct.id
)
SELECT *
FROM category_tree
ORDER BY level, name;
```

### Pattern 4: Window Functions
```sql
-- Running total per user
SELECT
    user_id,
    order_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY user_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders;

-- Rank products by sales
SELECT
    product_id,
    product_name,
    total_sales,
    RANK() OVER (ORDER BY total_sales DESC) AS sales_rank,
    PERCENT_RANK() OVER (ORDER BY total_sales DESC) AS percentile
FROM product_sales;
```

---

## Ottimizzazione

### Indexing Strategies
```sql
-- Single column index
CREATE INDEX idx_users_email ON users(email);

-- Composite index (order matters!)
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Partial index (index only subset)
CREATE INDEX idx_active_users ON users(id)
WHERE is_active = TRUE;

-- Covering index (include additional columns)
CREATE INDEX idx_users_email_covering ON users(email)
INCLUDE (first_name, last_name);

-- Full-text search index
CREATE INDEX idx_products_search ON products
USING GIN (to_tsvector('english', name || ' ' || description));
```

### Query Optimization
```sql
-- ❌ LENTO: Function on indexed column
SELECT * FROM users
WHERE LOWER(email) = 'user@example.com';

-- ✅ VELOCE: Direct comparison (use functional index if needed)
SELECT * FROM users
WHERE email = 'user@example.com';

-- ❌ LENTO: OR conditions
SELECT * FROM users
WHERE first_name = 'John' OR last_name = 'Doe';

-- ✅ VELOCE: UNION ALL
SELECT * FROM users WHERE first_name = 'John'
UNION ALL
SELECT * FROM users WHERE last_name = 'Doe' AND first_name != 'John';

-- ❌ LENTO: Subquery in SELECT
SELECT
    u.name,
    (SELECT COUNT(*) FROM orders WHERE user_id = u.id) AS order_count
FROM users u;

-- ✅ VELOCE: JOIN with aggregation
SELECT
    u.name,
    COUNT(o.id) AS order_count
FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;
```

---

## Sicurezza e Documentazione

### SQL Injection Prevention
```sql
-- ❌ VULNERABILE
-- SQL dinamico senza parametri
query = "SELECT * FROM users WHERE email = '" + user_input + "'";

-- ✅ SICURO: Prepared statements (esempio in vari linguaggi)
-- PostgreSQL (psycopg2)
cursor.execute("SELECT * FROM users WHERE email = %s", (user_input,))

-- MySQL (mysql-connector)
cursor.execute("SELECT * FROM users WHERE email = %s", (user_input,))

-- Node.js (pg)
client.query("SELECT * FROM users WHERE email = $1", [user_input])
```

### Database Documentation
```sql
-- Commenti su tabelle
COMMENT ON TABLE users IS 'User account information and authentication';

-- Commenti su colonne
COMMENT ON COLUMN users.email IS 'Unique email address for user authentication';
COMMENT ON COLUMN users.is_active IS 'Soft delete flag - FALSE indicates deleted account';

-- Commenti su constraints
COMMENT ON CONSTRAINT chk_users_age ON users IS 'Users must be at least 18 years old';
```

### Migration Template
```sql
-- ============================================================================
-- Migration: 001_create_users_table
-- Description: Create users table with basic authentication
-- Author: Nome Autore
-- Date: 2025-11-16
-- ============================================================================

-- Up Migration
BEGIN;

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);

COMMIT;

-- Down Migration (Rollback)
-- BEGIN;
-- DROP TABLE IF EXISTS users;
-- COMMIT;
```

---

## Note Aggiuntive

### Database Systems
- **PostgreSQL**: Feature-rich, ACID compliant
- **MySQL/MariaDB**: Widely used, good performance
- **SQLite**: Embedded, serverless
- **SQL Server**: Enterprise, Microsoft ecosystem
- **Oracle**: Enterprise, complex features

### Tools
- **GUI**: pgAdmin, DBeaver, TablePlus
- **CLI**: psql, mysql, sqlcmd
- **Migration**: Flyway, Liquibase, Alembic
- **ORM**: Sequelize, TypeORM, SQLAlchemy, Hibernate

### Riferimenti
- PostgreSQL Documentation
- MySQL Reference Manual
- SQL Standard (ISO/IEC 9075)
- Database Design Best Practices

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
