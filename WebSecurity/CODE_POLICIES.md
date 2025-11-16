# Code Policies - Web Security

> Standard, convenzioni e best practices per la sicurezza nelle applicazioni web

## 📋 Indice
- [OWASP Top 10](#owasp-top-10)
- [Authentication & Authorization](#authentication--authorization)
- [Input Validation](#input-validation)
- [Output Encoding](#output-encoding)
- [Session Management](#session-management)
- [Cryptography](#cryptography)
- [API Security](#api-security)
- [Security Headers](#security-headers)
- [Secure Coding](#secure-coding)

---

## OWASP Top 10

### 1. Broken Access Control
```javascript
// ❌ VULNERABLE: No authorization check
app.get('/admin/users', (req, res) => {
    const users = db.getAllUsers();
    res.json(users);
});

// ✅ SECURE: Verify authorization
app.get('/admin/users', requireAuth, requireRole('admin'), (req, res) => {
    const users = db.getAllUsers();
    res.json(users);
});

// ❌ VULNERABLE: IDOR (Insecure Direct Object Reference)
app.get('/users/:id/profile', (req, res) => {
    const profile = db.getProfile(req.params.id);
    res.json(profile);
});

// ✅ SECURE: Check ownership
app.get('/users/:id/profile', requireAuth, (req, res) => {
    if (req.user.id !== parseInt(req.params.id) && !req.user.isAdmin) {
        return res.status(403).json({ error: 'Forbidden' });
    }
    const profile = db.getProfile(req.params.id);
    res.json(profile);
});
```

### 2. Cryptographic Failures
```javascript
// ❌ VULNERABLE: Plain text password
db.createUser({ password: userPassword });

// ✅ SECURE: Hash password
const bcrypt = require('bcrypt');
const saltRounds = 12;
const hashedPassword = await bcrypt.hash(userPassword, saltRounds);
db.createUser({ password: hashedPassword });

// ✅ Verify password
const isValid = await bcrypt.compare(inputPassword, storedHash);

// ❌ VULNERABLE: Weak encryption
const encrypted = CryptoJS.AES.encrypt(data, 'weak-key');

// ✅ SECURE: Strong encryption with proper key management
const crypto = require('crypto');
const algorithm = 'aes-256-gcm';
const key = crypto.scrypt(password, salt, 32);
const iv = crypto.randomBytes(16);
const cipher = crypto.createCipheriv(algorithm, key, iv);
```

### 3. Injection
```javascript
// ❌ SQL INJECTION
const query = `SELECT * FROM users WHERE email = '${userInput}'`;
db.query(query);

// ✅ SECURE: Prepared statements
const query = 'SELECT * FROM users WHERE email = ?';
db.query(query, [userInput]);

// ❌ COMMAND INJECTION
const { exec } = require('child_process');
exec(`ping ${userInput}`);

// ✅ SECURE: Validate input, use libraries
const { spawn } = require('child_process');
const validInput = /^[a-zA-Z0-9.-]+$/.test(userInput);
if (!validInput) throw new Error('Invalid input');
const ping = spawn('ping', [userInput]);

// ❌ NoSQL INJECTION
db.users.find({ email: req.body.email });

// ✅ SECURE: Validate and sanitize
const email = String(req.body.email);
if (!/^[\w.-]+@[\w.-]+\.\w+$/.test(email)) {
    throw new Error('Invalid email');
}
db.users.find({ email });
```

### 4. Insecure Design
```javascript
// ✅ Implement security by design
// - Threat modeling
// - Secure architecture
// - Least privilege principle
// - Defense in depth
// - Fail securely

// Example: Rate limiting for login
const rateLimit = require('express-rate-limit');

const loginLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 5, // Max 5 requests per window
    message: 'Too many login attempts, please try again later',
    standardHeaders: true,
    legacyHeaders: false,
});

app.post('/login', loginLimiter, async (req, res) => {
    // Login logic
});
```

### 5. Security Misconfiguration
```javascript
// ❌ VULNERABLE: Default configurations
// - Default passwords
// - Unnecessary features enabled
// - Stack traces exposed
// - Directory listing enabled

// ✅ SECURE: Proper configuration
// Disable X-Powered-By header
app.disable('x-powered-by');

// Set secure headers
const helmet = require('helmet');
app.use(helmet());

// Don't expose errors in production
if (process.env.NODE_ENV === 'production') {
    app.use((err, req, res, next) => {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    });
} else {
    app.use((err, req, res, next) => {
        res.status(500).json({ error: err.message, stack: err.stack });
    });
}
```

### 6. Vulnerable Components
```bash
# ✅ Keep dependencies updated
npm audit
npm audit fix

# Use tools to check vulnerabilities
npm install -g snyk
snyk test
snyk monitor

# Pin dependency versions
# package.json
{
  "dependencies": {
    "express": "4.18.2",  # Exact version
    "helmet": "^7.0.0"    # Allow patches only
  }
}

# Use lock files
# package-lock.json
# yarn.lock
# pnpm-lock.yaml
```

### 7. Identification and Authentication Failures
```javascript
// ✅ Strong password requirements
const passwordSchema = {
    minLength: 12,
    minLowercase: 1,
    minUppercase: 1,
    minNumbers: 1,
    minSymbols: 1,
};

// ✅ Multi-factor authentication
const speakeasy = require('speakeasy');

// Generate secret
const secret = speakeasy.generateSecret();

// Verify token
const verified = speakeasy.totp.verify({
    secret: secret.base32,
    encoding: 'base32',
    token: userToken,
});

// ✅ Secure session management
const session = require('express-session');

app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
        secure: true,      // HTTPS only
        httpOnly: true,    // No JavaScript access
        maxAge: 3600000,   // 1 hour
        sameSite: 'strict' // CSRF protection
    }
}));
```

### 8. Software and Data Integrity Failures
```javascript
// ✅ Verify integrity of downloads/packages
// - Use SRI (Subresource Integrity) for CDN resources
<script
    src="https://cdn.example.com/lib.js"
    integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux..."
    crossorigin="anonymous">
</script>

// ✅ Verify package signatures
npm install --verify-signatures

// ✅ Use CI/CD security
// - Sign commits
// - Verify builds
// - Scan for vulnerabilities
```

### 9. Security Logging and Monitoring
```javascript
// ✅ Log security events
const winston = require('winston');

const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.File({ filename: 'security.log' })
    ]
});

// Log authentication events
app.post('/login', (req, res) => {
    logger.info('Login attempt', {
        email: req.body.email,
        ip: req.ip,
        userAgent: req.get('user-agent'),
        timestamp: new Date().toISOString()
    });

    // Login logic...

    if (loginSuccess) {
        logger.info('Login successful', { userId: user.id });
    } else {
        logger.warn('Login failed', { email: req.body.email, reason: 'invalid_credentials' });
    }
});

// Monitor for suspicious activity
// - Multiple failed logins
// - Access to sensitive resources
// - Unusual patterns
```

### 10. Server-Side Request Forgery (SSRF)
```javascript
// ❌ VULNERABLE: Unvalidated URL
app.get('/fetch', async (req, res) => {
    const url = req.query.url;
    const response = await fetch(url);
    res.send(await response.text());
});

// ✅ SECURE: Validate and whitelist
const { URL } = require('url');

const ALLOWED_HOSTS = ['api.example.com', 'cdn.example.com'];

app.get('/fetch', async (req, res) => {
    try {
        const url = new URL(req.query.url);

        // Check protocol
        if (url.protocol !== 'https:') {
            return res.status(400).json({ error: 'Only HTTPS allowed' });
        }

        // Check host whitelist
        if (!ALLOWED_HOSTS.includes(url.hostname)) {
            return res.status(400).json({ error: 'Host not allowed' });
        }

        // Prevent access to private IPs
        const ip = await dns.lookup(url.hostname);
        if (isPrivateIP(ip.address)) {
            return res.status(400).json({ error: 'Private IP not allowed' });
        }

        const response = await fetch(url.toString());
        res.send(await response.text());
    } catch (error) {
        res.status(400).json({ error: 'Invalid URL' });
    }
});
```

---

## Authentication & Authorization

### JWT Best Practices
```javascript
const jwt = require('jsonwebtoken');

// ✅ Generate JWT with proper settings
const token = jwt.sign(
    { userId: user.id, role: user.role },
    process.env.JWT_SECRET,
    {
        expiresIn: '1h',
        issuer: 'myapp',
        audience: 'myapp-users'
    }
);

// ✅ Verify JWT
const verifyToken = (token) => {
    try {
        return jwt.verify(token, process.env.JWT_SECRET, {
            issuer: 'myapp',
            audience: 'myapp-users'
        });
    } catch (error) {
        if (error.name === 'TokenExpiredError') {
            throw new Error('Token expired');
        }
        throw new Error('Invalid token');
    }
};

// ✅ Refresh token pattern
// Short-lived access token (15 min)
// Long-lived refresh token (7 days)
// Store refresh token in httpOnly cookie

// ❌ DON'T store sensitive data in JWT
// JWT is base64 encoded, not encrypted
```

### OAuth 2.0 / OpenID Connect
```javascript
// Use established libraries
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;

passport.use(new GoogleStrategy({
    clientID: process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    callbackURL: "https://yourapp.com/auth/google/callback"
  },
  function(accessToken, refreshToken, profile, cb) {
    // Find or create user
    User.findOrCreate({ googleId: profile.id }, function (err, user) {
      return cb(err, user);
    });
  }
));
```

---

## Input Validation

### Validation Strategies
```javascript
// ✅ Whitelist validation (preferred)
const allowedFields = ['name', 'email', 'age'];
const sanitizedInput = {};

for (const field of allowedFields) {
    if (input[field] !== undefined) {
        sanitizedInput[field] = input[field];
    }
}

// ✅ Type validation
const Joi = require('joi');

const schema = Joi.object({
    email: Joi.string().email().required(),
    password: Joi.string().min(12).required(),
    age: Joi.number().integer().min(0).max(150),
    website: Joi.string().uri(),
});

const { error, value } = schema.validate(userInput);
if (error) {
    throw new Error('Validation failed');
}

// ✅ Sanitize HTML
const DOMPurify = require('isomorphic-dompurify');

const clean = DOMPurify.sanitize(dirty, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'],
    ALLOWED_ATTR: ['href']
});

// ✅ Validate file uploads
const validateFile = (file) => {
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    const maxSize = 5 * 1024 * 1024; // 5MB

    if (!allowedTypes.includes(file.mimetype)) {
        throw new Error('Invalid file type');
    }

    if (file.size > maxSize) {
        throw new Error('File too large');
    }

    return true;
};
```

---

## Output Encoding

### XSS Prevention
```javascript
// ✅ Context-aware encoding

// HTML context
const escapeHtml = (unsafe) => {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
};

// JavaScript context
const escapeJS = (unsafe) => {
    return JSON.stringify(unsafe).slice(1, -1);
};

// URL context
const escapeURL = (unsafe) => {
    return encodeURIComponent(unsafe);
};

// Use templating engines with auto-escaping
// EJS, Handlebars, React, Vue (escape by default)

// ❌ Avoid innerHTML
element.innerHTML = userInput;  // XSS!

// ✅ Use textContent or framework methods
element.textContent = userInput;

// React automatically escapes
<div>{userInput}</div>  // Safe

// ✅ Content Security Policy
app.use(helmet.contentSecurityPolicy({
    directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'", "'unsafe-inline'"],
        styleSrc: ["'self'", "'unsafe-inline'"],
        imgSrc: ["'self'", "data:", "https:"],
    }
}));
```

---

## Session Management

### Secure Sessions
```javascript
const session = require('express-session');
const RedisStore = require('connect-redis')(session);
const redis = require('redis');

const redisClient = redis.createClient();

app.use(session({
    store: new RedisStore({ client: redisClient }),
    secret: process.env.SESSION_SECRET, // Strong random string
    resave: false,
    saveUninitialized: false,
    name: 'sessionId', // Don't use default 'connect.sid'
    cookie: {
        secure: true,       // HTTPS only
        httpOnly: true,     // No JavaScript access
        maxAge: 3600000,    // 1 hour
        sameSite: 'strict', // CSRF protection
        domain: 'example.com',
        path: '/'
    },
    rolling: true // Reset expiration on activity
}));

// ✅ Session fixation prevention
// Regenerate session ID on login
app.post('/login', (req, res) => {
    const user = authenticateUser(req.body);

    req.session.regenerate((err) => {
        if (err) return next(err);

        req.session.userId = user.id;
        res.json({ success: true });
    });
});

// ✅ Logout properly
app.post('/logout', (req, res) => {
    req.session.destroy((err) => {
        if (err) return next(err);
        res.clearCookie('sessionId');
        res.json({ success: true });
    });
});
```

---

## Cryptography

### Hashing
```javascript
// ✅ Password hashing with bcrypt
const bcrypt = require('bcrypt');

// Hash
const saltRounds = 12; // Increase as hardware improves
const hash = await bcrypt.hash(password, saltRounds);

// Verify
const isValid = await bcrypt.compare(password, hash);

// ✅ Argon2 (recommended for new projects)
const argon2 = require('argon2');

const hash = await argon2.hash(password, {
    type: argon2.argon2id,
    memoryCost: 2 ** 16,
    timeCost: 3,
    parallelism: 1
});

const isValid = await argon2.verify(hash, password);
```

### Encryption
```javascript
// ✅ Symmetric encryption (AES-256-GCM)
const crypto = require('crypto');

const encrypt = (text, password) => {
    const salt = crypto.randomBytes(16);
    const key = crypto.scryptSync(password, salt, 32);
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);

    let encrypted = cipher.update(text, 'utf8', 'hex');
    encrypted += cipher.final('hex');

    const authTag = cipher.getAuthTag();

    return {
        encrypted,
        salt: salt.toString('hex'),
        iv: iv.toString('hex'),
        authTag: authTag.toString('hex')
    };
};

const decrypt = (encryptedData, password) => {
    const salt = Buffer.from(encryptedData.salt, 'hex');
    const key = crypto.scryptSync(password, salt, 32);
    const iv = Buffer.from(encryptedData.iv, 'hex');
    const authTag = Buffer.from(encryptedData.authTag, 'hex');

    const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
    decipher.setAuthTag(authTag);

    let decrypted = decipher.update(encryptedData.encrypted, 'hex', 'utf8');
    decrypted += decipher.final('utf8');

    return decrypted;
};
```

---

## API Security

### API Authentication
```javascript
// ✅ API Key
const validateApiKey = (req, res, next) => {
    const apiKey = req.headers['x-api-key'];

    if (!apiKey || !isValidApiKey(apiKey)) {
        return res.status(401).json({ error: 'Invalid API key' });
    }

    next();
};

// ✅ Rate limiting
const rateLimit = require('express-rate-limit');

const apiLimiter = rateLimit({
    windowMs: 15 * 60 * 1000,
    max: 100,
    message: 'Too many requests',
    standardHeaders: true,
    legacyHeaders: false,
});

app.use('/api/', apiLimiter);

// ✅ CORS configuration
const cors = require('cors');

app.use(cors({
    origin: ['https://trusted-domain.com'],
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    allowedHeaders: ['Content-Type', 'Authorization'],
    credentials: true,
    maxAge: 86400
}));
```

---

## Security Headers

### Essential Headers
```javascript
const helmet = require('helmet');

app.use(helmet());

// Or configure individually:
app.use(helmet.contentSecurityPolicy({
    directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'", "trusted-cdn.com"],
        styleSrc: ["'self'", "'unsafe-inline'"],
        imgSrc: ["'self'", "data:", "https:"],
        connectSrc: ["'self'"],
        fontSrc: ["'self'"],
        objectSrc: ["'none'"],
        mediaSrc: ["'self'"],
        frameSrc: ["'none'"],
    }
}));

app.use(helmet.hsts({
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
}));

app.use(helmet.frameguard({ action: 'deny' }));
app.use(helmet.noSniff());
app.use(helmet.xssFilter());

// Additional headers
app.use((req, res, next) => {
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('X-Frame-Options', 'DENY');
    res.setHeader('X-XSS-Protection', '1; mode=block');
    res.setHeader('Referrer-Policy', 'no-referrer');
    res.setHeader('Permissions-Policy', 'geolocation=(), microphone=()');
    next();
});
```

---

## Secure Coding

### Checklist
- [ ] Validate all inputs (whitelist approach)
- [ ] Encode all outputs (context-aware)
- [ ] Use parameterized queries (prevent injection)
- [ ] Implement authentication and authorization
- [ ] Use HTTPS everywhere
- [ ] Secure session management
- [ ] Hash passwords with bcrypt/argon2
- [ ] Implement rate limiting
- [ ] Set security headers
- [ ] Keep dependencies updated
- [ ] Log security events
- [ ] Handle errors securely (no info leakage)
- [ ] Implement CSRF protection
- [ ] Validate file uploads
- [ ] Use Content Security Policy
- [ ] Regular security audits

---

## Note Aggiuntive

### Tools
- **SAST**: SonarQube, Snyk, Checkmarx
- **DAST**: OWASP ZAP, Burp Suite
- **Dependency Scan**: npm audit, Snyk, Dependabot
- **Penetration Testing**: Metasploit, Kali Linux tools

### Riferimenti
- OWASP Top 10 (owasp.org/www-project-top-ten)
- OWASP Cheat Sheets (cheatsheetseries.owasp.org)
- CWE Top 25 (cwe.mitre.org/top25)
- NIST Cybersecurity Framework

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
