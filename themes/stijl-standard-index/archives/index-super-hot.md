---
hide:
  - toc
  - navigation
  - title
---
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Inclusive Gym — De Stijl Composition</title>

<style>
:root {
  --black: #000000;
  --white: #ffffff;
  --red:   #c00018;
  --blue:  #003f8c;
  --yellow:#e0b800;

  /* Responsive Mondrian line thickness */
  --line: clamp(6px, 1vw, 10px);
}

* { box-sizing: border-box; }

/* Remove MkDocs spacing around content */

.md-grid {
  max-width: 100% !important;
  margin: 0 !important;
}

.md-main__inner {
  margin: 0 !important;
}

.md-content {
  margin: 0 !important;
}

.md-content__inner {
  padding: 0 !important;
}

/* -----------------------------------------
   Hides auto page title
   ----------------------------------------- */
.md-content__inner > h1:first-child {
  display: none;
}


/* ===== Grid Canvas ===== */

.grid {
  display: grid;

  /* Let MkDocs control page height */
  height: 100%;

  gap: var(--line);
  padding: var(--line);

  grid-template-columns: repeat(4, 1fr);

  /* Slightly taller Mondrian rhythm */
  grid-auto-rows: minmax(180px, 1fr);

  background: var(--black);
}

/* ===== Blocks ===== */

.block {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  padding: 1.75rem;

  min-height: 0;
}

/* Typography polish */

.block h2 {
  margin-top: 0;
  font-weight: 600;
  letter-spacing: .02em;
}

.block a {
  margin-top: 1.5rem;
  font-weight: bold;
  text-decoration: underline;
  color: inherit;
}

.block a:focus-visible {
  outline: 4px solid #fff;
  outline-offset: 4px;
}
/* ===== Mondrian Height Utilities ===== */

.h-sm  { min-height: 140px; }
.h-md  { min-height: 220px; }
.h-lg  { min-height: 320px; }
.h-xl  { min-height: 420px; }

/* ===== Colors ===== */

.red    { background: var(--white); color: #000; }
.yellow { background: var(--red); color: #fff; }
.white  { background: var(--yellow); color: #000; }
.blue   { background: var(--blue); color: #fff; }

/* ===== Desktop Mondrian Layout ===== */

.projects {
  grid-column: span 3;
  grid-row: span 1;

  /* Mondrian composition anchor */
  align-items: flex-start;
}

.areas {
  grid-column: span 1;
  grid-row: span 2;
}

.resources {
  grid-column: span 2;
  grid-row: span 2;
}

.archives {
  grid-column: span 1;
}

.contact {
  grid-column: span 2;
}

/* ===== Tablet ===== */

@media (max-width: 1024px) {

  .grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .block {
    grid-column: span 1;
    grid-row: auto;
  }

  .projects {
    grid-column: span 2;
    min-height: 220px;
  }

}

/* ===== Mobile ===== */

@media (max-width: 768px) {

  .grid {
    grid-template-columns: 1fr;
    gap: 6px;
    padding: 6px;
  }

  .block {
    grid-column: span 1 !important;
    grid-row: auto !important;
    padding: 1.25rem;
  }

}
</style>
</head>

<body>

<main class="grid">

<section class="block red projects h-lg">
<h2>Projects</h2>
<p>Current projects we are working on.</p>
<a href="#">Join Us</a>
</section>

<section class="block blue areas h-md">
<h2>Areas</h2>
<p>Areas of ongoing responsibility and attention.</p>
<a href="#">Explore</a>
</section>

<section class="block yellow resources h-lg">
<h2>Resources</h2>
<p>Reference materials, research, and useful information.</p>
<a href="#">Learn More</a>
</section>

<section class="block white archives h-sm">
<h2>Archives</h2>
<p>Completed or inactive work kept for reference.</p>
<a href="#">Our Philosophy</a>
</section>

<section class="block red contact h-md">
<h2>About Us</h2>
<p>Information about who we are and what we do.</p>
<a href="#">Get in Touch</a>
</section>

</main>

</body>
</html>
