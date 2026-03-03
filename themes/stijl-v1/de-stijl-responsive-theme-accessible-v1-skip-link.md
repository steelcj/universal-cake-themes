# de-stijl-responsive-theme-accessible-v1-skip-link

updated file with **Step 1 (Skip Link)** properly integrated.

I’ve given it a descriptive, versioned name so you can evolve it incrementally.

------

# Suggested File Name

```
de-stijl-responsive-theme-accessible-v1-skip-link.html
```

------

# Full Updated File

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>De Stijl Responsive Theme – Accessible v1</title>

<style>
:root {
  --black: #000;
  --white: #ffffff;
  --red: #d00000;
  --blue: #0033cc;
  --yellow: #f2c200;
  --line: 10px;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  background: var(--white);
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

# How to Test

1. Open the file.
2. Press `Tab`.
3. A yellow “Skip to main content” should appear in the top-left.
4. Press `Enter`.
5. Focus jumps to `<main>`.

------

If that works correctly, next we’ll implement **Step 2: Visible keyboard focus styling**, which is the most impactful improvement for real-world usability.