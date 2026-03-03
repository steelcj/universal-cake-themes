# de-stijl-responsive-theme-accessible-v2-focus-enhanced.html

Excellent — now we add **Step 2: Visible Keyboard Focus Styling**.

This is one of the most impactful accessibility improvements you can make. It ensures:

- Keyboard users can see where they are
- Links are clearly interactive
- The design still feels intentional and De Stijl–aligned

We’ll keep it strong, geometric, and on-brand.

------

# Suggested File Name

```
de-stijl-responsive-theme-accessible-v2-focus-enhanced.html
```

Clear, progressive, versioned.

------

# What We’re Adding

1. High-contrast focus ring
2. Consistent outline style
3. Accessible hover/focus parity
4. Slight interaction polish

------

# Full Updated File (v2 – Focus Enhanced)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>De Stijl Responsive Theme – Accessible v2 (Focus Enhanced)</title>

<style>
:root {
  --black: #000;
  --white: #ffffff;
  --red: #d00000;
  --blue: #0033cc;
  --yellow: #f2c200;
  --focus: #ff00ff; /* Strong magenta focus ring */
  --line: 10px;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  background: var(--white);
  line-height: 1.6;
}

/* =========================
   Skip Link
========================= */

.skip-link {
  position: absolute;
  left: -9999px;
  top: auto;
  background: var(--yellow);
  color: var(--black);
  padding: 0.5rem 1rem;
  font-weight: bold;
  z-index: 1000;
}

.skip-link:focus {
  left: 10px;
  top: 10px;
}

/* =========================
   Global Focus Styles
========================= */

a:focus,
a:focus-visible,
button:focus,
button:focus-visible {
  outline: 4px solid var(--focus);
  outline-offset: 4px;
}

/* Optional hover parity */
a:hover {
  text-decoration: underline;
}

/* =========================
   Wrapper
========================= */

.wrapper {
  display: grid;
  min-height: 100vh;
  gap: var(--line);
  padding: var(--line);
  background: var(--black);
}

/* =========================
   Header
========================= */

header {
  background: var(--white);
  padding: 1.5rem;
}

nav {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

nav a {
  text-decoration: none;
  color: var(--black);
  font-weight: 600;
  padding: 0.5rem 0.75rem;
}

/* =========================
   Main Grid Desktop
========================= */

main {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: var(--line);
}

.block {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.block p {
  max-width: 65ch;
}

.red { background: var(--red); color: white; }
.blue { background: var(--blue); color: white; }
.yellow { background: var(--yellow); color: var(--black); }
.white { background: var(--white); }

.projects { grid-column: span 4; }
.areas { grid-column: span 2; }
.resources { grid-column: span 3; }
.about { grid-column: span 3; }

/* =========================
   Footer
========================= */

footer {
  background: var(--white);
  padding: 1rem;
}

/* =========================
   Tablet
========================= */

@media (max-width: 1024px) {
  main {
    grid-template-columns: repeat(4, 1fr);
  }

  .projects,
  .about {
    grid-column: 1 / -1;
  }

  .areas,
  .resources {
    grid-column: span 2;
  }
}

/* =========================
   Mobile
========================= */

@media (max-width: 600px) {
  main {
    grid-template-columns: 1fr;
  }

  .projects,
  .areas,
  .resources,
  .about {
    grid-column: span 1;
  }

  nav {
    flex-direction: column;
  }
}

/* =========================
   Reduced Motion Support
========================= */

@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
}
</style>
</head>

<body>

<a class="skip-link" href="#main-content">Skip to main content</a>

<div class="wrapper">

<header>
  <h1>Studio De Stijl</h1>
  <nav aria-label="Primary navigation">
    <a href="#">Home</a>
    <a href="#">Projects</a>
    <a href="#">Areas</a>
    <a href="#">Resources</a>
    <a href="#">About</a>
  </nav>
</header>

<main id="main-content">
  <section class="block red projects">
    <div>
      <h2>Projects</h2>
      <p>Explore structured and minimalist work.</p>
    </div>
  </section>

  <section class="block blue areas">
    <div>
      <h2>Areas</h2>
      <p>Key domains of interest and focus.</p>
    </div>
  </section>

  <section class="block yellow resources">
    <div>
      <h2>Resources</h2>
      <p>Documentation and shared materials.</p>
    </div>
  </section>

  <section class="block white about">
    <div>
      <h2>About</h2>
      <p>A modern interpretation of De Stijl design principles.</p>
    </div>
  </section>
</main>

<footer>
  <p>&copy; 2026 Studio De Stijl</p>
</footer>

</div>

</body>
</html>
```

------

# How to Test This Version

1. Press `Tab` repeatedly.
2. Watch the strong magenta outline.
3. Confirm you always know where focus is.
4. Try navigating without using a mouse.

------

This now supports:

- Skip navigation
- Visible keyboard focus
- WCAG AA color compliance
- Motion sensitivity
- Better tap targets

------

Next we can implement Step 3: Color contrast refinement and semantic improvements.

Would you like to refine color contrast next, or improve structural semantics?