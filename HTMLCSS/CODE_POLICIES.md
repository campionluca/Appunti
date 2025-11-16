# Code Policies - HTML/CSS

> Standard, convenzioni e politiche di scrittura del codice per il libro su HTML e CSS

## 📋 Indice
- [Standard di Scrittura](#standard-di-scrittura)
- [Convenzioni di Nomenclatura](#convenzioni-di-nomenclatura)
- [Template di Codice](#template-di-codice)
- [Struttura dei File](#struttura-dei-file)
- [Best Practices](#best-practices)
- [Pattern di Design](#pattern-di-design)
- [Accessibilità](#accessibilità)
- [Commenti e Documentazione](#commenti-e-documentazione)

---

## Standard di Scrittura

### Formattazione
- **Indentazione**: 2 spazi (standard web)
- **Encoding**: UTF-8
- **Fine riga**: LF (Unix)
- **Lowercase**: Sempre minuscolo per tag e attributi HTML
- **Quotes**: Doppi apici per attributi HTML

### Stile del Codice

#### HTML
```html
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Descrizione della pagina">
  <title>Titolo Pagina</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="site-header">
    <nav class="navigation" aria-label="Main navigation">
      <ul class="nav-list">
        <li class="nav-item"><a href="#home">Home</a></li>
        <li class="nav-item"><a href="#about">About</a></li>
      </ul>
    </nav>
  </header>

  <main class="main-content">
    <section class="hero-section">
      <h1 class="hero-title">Welcome</h1>
      <p class="hero-description">Description text</p>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2025 Company Name</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

#### CSS
```css
/* === VARIABLES === */
:root {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --spacing-unit: 8px;
  --font-family-base: 'Helvetica Neue', Arial, sans-serif;
}

/* === RESET/BASE === */
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* === LAYOUT === */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-unit);
}

/* === COMPONENTS === */
.button {
  display: inline-block;
  padding: 12px 24px;
  background-color: var(--color-primary);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #0056b3;
}

.button:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

### Regole Generali
- [ ] Sempre dichiarare DOCTYPE
- [ ] Chiudere tutti i tag (anche self-closing in XHTML)
- [ ] Un elemento per riga per migliore leggibilità
- [ ] Usare HTML semantico
- [ ] Separare struttura (HTML), presentazione (CSS) e comportamento (JS)

---

## Convenzioni di Nomenclatura

### HTML
- **ID**: `kebab-case` - Esempio: `main-header`, `user-profile`
- **Classi**: `kebab-case` - Esempio: `nav-item`, `btn-primary`
- **Data attributes**: `kebab-case` - Esempio: `data-user-id`, `data-toggle`
- **File**: `kebab-case.html` - Esempio: `index.html`, `about-us.html`

### CSS
- **Classi**: `kebab-case` - Esempio: `.card-title`, `.btn-large`
- **ID**: `kebab-case` - Esempio: `#main-nav`, `#footer`
- **Custom properties**: `--kebab-case` - Esempio: `--primary-color`, `--spacing-lg`
- **Keyframes**: `kebab-case` - Esempio: `@keyframes fade-in`
- **File**: `kebab-case.css` - Esempio: `styles.css`, `components.css`

### Metodologia BEM (Opzionale ma consigliata)
```css
/* Block */
.card {}

/* Element */
.card__title {}
.card__body {}
.card__footer {}

/* Modifier */
.card--featured {}
.card__title--large {}
```

---

## Template di Codice

### Template HTML5 Base
```html
<!DOCTYPE html>
<html lang="it">
<head>
  <!-- Meta Tags -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Descrizione della pagina per SEO">
  <meta name="keywords" content="keyword1, keyword2, keyword3">
  <meta name="author" content="Nome Autore">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Titolo">
  <meta property="og:description" content="Descrizione">
  <meta property="og:image" content="image.jpg">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Titolo">
  <meta name="twitter:description" content="Descrizione">

  <!-- Title -->
  <title>Titolo Pagina | Nome Sito</title>

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="/favicon.png">

  <!-- Stylesheets -->
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/styles.css">

  <!-- Preconnect per font esterni -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
</head>
<body>
  <!-- Skip to main content per accessibilità -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Header -->
  <header class="site-header" role="banner">
    <!-- Header content -->
  </header>

  <!-- Main Navigation -->
  <nav class="main-nav" role="navigation" aria-label="Main navigation">
    <!-- Navigation content -->
  </nav>

  <!-- Main Content -->
  <main id="main-content" class="main-content" role="main">
    <!-- Page content -->
  </main>

  <!-- Footer -->
  <footer class="site-footer" role="contentinfo">
    <!-- Footer content -->
  </footer>

  <!-- Scripts -->
  <script src="js/main.js" defer></script>
</body>
</html>
```

### Template CSS Base
```css
/**
 * Stylesheet: Main Styles
 * Description: Stili principali del sito
 * Author: Nome Autore
 * Version: 1.0.0
 */

/* ==========================================
   TABLE OF CONTENTS
   1. CSS Variables
   2. Reset/Normalize
   3. Base Styles
   4. Layout
   5. Components
   6. Utilities
   7. Media Queries
   ========================================== */

/* === 1. CSS VARIABLES === */
:root {
  /* Colors */
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-success: #28a745;
  --color-danger: #dc3545;
  --color-warning: #ffc107;
  --color-info: #17a2b8;
  --color-text: #333333;
  --color-background: #ffffff;

  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;

  /* Typography */
  --font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
  --font-family-heading: Georgia, 'Times New Roman', serif;
  --font-family-mono: 'Courier New', monospace;

  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;

  /* Breakpoints */
  --breakpoint-sm: 576px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 992px;
  --breakpoint-xl: 1200px;

  /* Effects */
  --transition-speed: 0.3s;
  --border-radius: 4px;
  --box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* === 2. RESET/NORMALIZE === */
*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  font-size: 16px;
  -webkit-text-size-adjust: 100%;
}

body {
  margin: 0;
  font-family: var(--font-family-base);
  font-size: var(--font-size-base);
  line-height: 1.6;
  color: var(--color-text);
  background-color: var(--color-background);
}

/* === 3. BASE STYLES === */
h1, h2, h3, h4, h5, h6 {
  margin-top: 0;
  margin-bottom: var(--spacing-md);
  font-family: var(--font-family-heading);
  font-weight: 700;
  line-height: 1.2;
}

p {
  margin-top: 0;
  margin-bottom: var(--spacing-md);
}

a {
  color: var(--color-primary);
  text-decoration: none;
  transition: color var(--transition-speed);
}

a:hover,
a:focus {
  color: #0056b3;
  text-decoration: underline;
}

/* === 4. LAYOUT === */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-md);
}

/* === 5. COMPONENTS === */
/* Components here */

/* === 6. UTILITIES === */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* === 7. MEDIA QUERIES === */
@media (max-width: 768px) {
  /* Mobile styles */
}

@media (min-width: 769px) and (max-width: 1024px) {
  /* Tablet styles */
}

@media (min-width: 1025px) {
  /* Desktop styles */
}
```

---

## Struttura dei File

### Organizzazione Progetto
```
project/
├── index.html
├── about.html
├── css/
│   ├── reset.css
│   ├── variables.css
│   ├── base.css
│   ├── layout.css
│   ├── components/
│   │   ├── buttons.css
│   │   ├── cards.css
│   │   └── navigation.css
│   └── utilities.css
├── js/
│   └── main.js
├── images/
│   ├── logo.svg
│   └── hero.jpg
├── fonts/
└── assets/
```

### Ordine Import CSS
```css
/* 1. Reset/Normalize */
@import 'reset.css';

/* 2. Variables */
@import 'variables.css';

/* 3. Base styles */
@import 'base.css';

/* 4. Layout */
@import 'layout.css';

/* 5. Components */
@import 'components/buttons.css';
@import 'components/cards.css';

/* 6. Utilities */
@import 'utilities.css';
```

---

## Best Practices

### HTML
- [ ] Usare HTML semantico (header, nav, main, article, section, aside, footer)
- [ ] Un solo h1 per pagina
- [ ] Alt text per tutte le immagini
- [ ] Form labels associati correttamente
- [ ] Evitare div-itis (troppi div innestati)
- [ ] Validare con W3C Validator

### CSS
- [ ] Mobile-first approach
- [ ] Usare CSS custom properties per valori ripetuti
- [ ] Evitare !important quando possibile
- [ ] Preferire classi a ID per styling
- [ ] Raggruppare media queries
- [ ] Minimizzare specificità selettori

### Performance
- [ ] Minimizzare e comprimere CSS/JS
- [ ] Ottimizzare immagini (WebP, lazy loading)
- [ ] Usare CDN per librerie esterne
- [ ] Defer/async per script non critici
- [ ] Critical CSS inline per above-the-fold content

---

## Pattern di Design

### Responsive Design Patterns

```css
/* Pattern 1: Fluid Typography */
:root {
  --fluid-min-size: 1rem;
  --fluid-max-size: 2rem;
  --fluid-min-width: 20rem;
  --fluid-max-width: 80rem;
}

h1 {
  font-size: clamp(
    var(--fluid-min-size),
    calc(1rem + 2vw),
    var(--fluid-max-size)
  );
}

/* Pattern 2: CSS Grid Layout */
.grid-layout {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--spacing-lg);
}

/* Pattern 3: Flexbox Centering */
.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Pattern 4: Sticky Footer */
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
}

/* Pattern 5: Card Component */
.card {
  display: flex;
  flex-direction: column;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  overflow: hidden;
}

.card__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card__content {
  padding: var(--spacing-md);
  flex: 1;
}

.card__footer {
  padding: var(--spacing-md);
  border-top: 1px solid #eee;
}
```

### HTML Patterns

```html
<!-- Pattern 1: Responsive Images -->
<picture>
  <source srcset="image-large.webp" type="image/webp" media="(min-width: 1024px)">
  <source srcset="image-medium.webp" type="image/webp" media="(min-width: 768px)">
  <img src="image-small.jpg" alt="Description" loading="lazy">
</picture>

<!-- Pattern 2: Navigation Pattern -->
<nav class="main-nav" aria-label="Main navigation">
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu">
    <span class="sr-only">Menu</span>
  </button>
  <ul id="nav-menu" class="nav-list">
    <li><a href="#home" aria-current="page">Home</a></li>
    <li><a href="#about">About</a></li>
  </ul>
</nav>

<!-- Pattern 3: Card Grid -->
<div class="card-grid">
  <article class="card">
    <img src="image.jpg" alt="" class="card__image">
    <div class="card__content">
      <h2 class="card__title">Title</h2>
      <p class="card__description">Description</p>
    </div>
  </article>
</div>
```

---

## Accessibilità

### Linee Guida WCAG

```html
<!-- Skip Links -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<!-- ARIA Labels -->
<button aria-label="Close dialog">×</button>
<nav aria-label="Main navigation">...</nav>

<!-- ARIA Roles (solo quando necessario) -->
<div role="alert">Important message</div>

<!-- Form Accessibility -->
<form>
  <label for="email">Email:</label>
  <input
    type="email"
    id="email"
    name="email"
    aria-required="true"
    aria-describedby="email-help"
  >
  <span id="email-help">We'll never share your email</span>
</form>

<!-- Focus Indicators -->
<style>
:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

:focus:not(:focus-visible) {
  outline: none;
}

:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
</style>
```

### Checklist Accessibilità
- [ ] Contrast ratio minimo 4.5:1 per testo
- [ ] Tutti gli elementi interattivi raggiungibili da tastiera
- [ ] Focus indicators visibili
- [ ] Alt text per immagini informative
- [ ] Heading hierarchy corretta (h1 > h2 > h3)
- [ ] Form labels appropriati

---

## Commenti e Documentazione

### Commenti HTML
```html
<!-- === HEADER SECTION === -->
<header class="site-header">
  <!-- Logo and navigation -->
</header>

<!-- === MAIN CONTENT === -->
<main>
  <!-- Hero Section -->
  <section class="hero">
    <!-- Hero content here -->
  </section>

  <!-- Features Section -->
  <section class="features">
    <!-- TODO: Add animation to feature cards -->
  </section>
</main>

<!-- === FOOTER SECTION === -->
<footer class="site-footer">
  <!-- Footer links and copyright -->
</footer>
```

### Commenti CSS
```css
/**
 * Component: Button
 * Description: Reusable button styles
 * Usage: <button class="btn btn--primary">Click me</button>
 */
.btn {
  /* Base styles */
}

.btn--primary {
  /* Primary variant */
}

/* TODO: Add dark mode support */
/* FIXME: Button focus state not visible in Safari */
/* NOTE: This uses CSS Grid which requires modern browser */

/*
 * Multiline comment for
 * longer explanations
 */
```

---

## Note Aggiuntive

### Tool e Validatori
- **Validator**: W3C HTML Validator, W3C CSS Validator
- **Linter**: HTMLHint, Stylelint
- **Formatter**: Prettier
- **Accessibility**: aXe, WAVE, Lighthouse
- **Performance**: PageSpeed Insights, WebPageTest

### Browser Support
```css
/* Specificare browser target */
/* Browsers: last 2 versions, > 1%, not dead */

/* Feature queries per progressive enhancement */
@supports (display: grid) {
  .container {
    display: grid;
  }
}

/* Fallback per browser più vecchi */
.flex-container {
  display: block; /* Fallback */
  display: flex; /* Modern browsers */
}
```

### Riferimenti
- MDN Web Docs
- W3C Standards
- WCAG 2.1 Guidelines
- CSS Tricks
- A11y Project

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
