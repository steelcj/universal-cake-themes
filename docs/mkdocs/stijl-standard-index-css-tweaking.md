# stijl-standard-index-css-tweaking

# If you want the grid to shrink further

You must reduce **typographic scale and spacing**, not the grid math.

Example:

```css
.block {
  padding: 0.6rem;
}

.block h2 {
  font-size: 1rem;
}

.block p {
  font-size: 0.9rem;
}

.block a {
  margin-top: 0.3rem;
}
```

New integrated

```css
/* ===== Blocks ===== */

.block {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  padding: 0.6rem;

  min-height: 0;
}

/* Typography polish */

.block h2 {
  margin: 0 0 0.2rem 0;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: .02em;
}

.block p {
  margin: 0;
  font-size: 0.9rem;
}

.block a {
  margin-top: 0.3rem;
  font-weight: bold;
  text-decoration: underline;
  color: inherit;
}

.block a:focus-visible {
  outline: 4px solid #fff;
  outline-offset: 4px;
}
```



Currently we have:

```css
/* ===== Blocks =====
.block { outline: 2px solid lime; } */

.block {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  padding: 0.9rem;

  min-height: 0;
}


/* Typography polish */

.block h2 {
  margin-top: 0;
  font-weight: 600;
  letter-spacing: .02em;
}

.block a {
  margin-top: 0.6rem;
  font-weight: bold;
  text-decoration: underline;
  color: inherit;
}


.block a:focus-visible {
  outline: 4px solid #fff;
  outline-offset: 4px;
}
```

## line

```css
--line: calc(var(--block-unit) * 0.15);
```

f you'd like, I can also show you a **very elegant trick used in De Stijl-inspired landing pages** where the entire Mondrian composition scales perfectly with viewport height while keeping the typography readable.

**very nice trick that makes Mondrian grids like this feel dramatically more “correct” visually** by scaling the line thickness and block padding together.

## Revision

old

```css
:root {

  --black: #000000;
  --white: #ffffff;
  --red:   #c00018;
  --blue:  #003f8c;
  --yellow:#e0b800;

  --line: calc(var(--block-unit) * 0.15);

  /* Mondrian block sizing system */

  /* --block-unit: 60px; */
  --block-unit: clamp(40px, 7vh, 70px);

  --block-sm: calc(var(--block-unit) * 1);
  --block-md: calc(var(--block-unit) * 1.67);
  --block-lg: calc(var(--block-unit) * 2.5);
  --block-xl: calc(var(--block-unit) * 3.33);

}
```

new

```css
:root {

  --block-unit: clamp(40px, 7vh, 70px);

  --block-sm: calc(var(--block-unit) * 1);
  --block-md: calc(var(--block-unit) * 1.67);
  --block-lg: calc(var(--block-unit) * 2.5);
  --block-xl: calc(var(--block-unit) * 3.33);

  --line: calc(var(--block-unit) * 0.15);

  --black: #000000;
  --white: #ffffff;
  --red:   #c00018;
  --blue:  #003f8c;
  --yellow:#e0b800;

}
```

## Adjustments

Good question — the key thing to understand is that with `clamp()` you are **not setting a fixed size**, you are defining a **range**.

Your current rule:

```
--block-unit: clamp(40px, 7vh, 70px);
```

means:

```
minimum size   preferred scaling    maximum size
     |              |                   |
    40px        7% viewport height     70px
```

So the block unit **will never exceed 70px**, even if the viewport gets large.

------

# If you want it to scale up to 90px

You only need to change the **maximum value**:

```
--block-unit: clamp(40px, 7vh, 90px);
```

Now the system behaves like this:

| viewport height | block-unit     |
| --------------- | -------------- |
| small screen    | ~40px          |
| medium screen   | ~55–70px       |
| large screen    | up to **90px** |

Everything tied to `--block-unit` will scale accordingly.

------

# If you want the *normal* size to be closer to 90px

Then adjust the **middle value** instead:

```
--block-unit: clamp(60px, 10vh, 90px);
```

That shifts the scale upward.

------

# Practical presets you might like

### Compact site

```
--block-unit: clamp(35px, 6vh, 60px);
```

### Balanced (what you have)

```
--block-unit: clamp(40px, 7vh, 70px);
```

### Larger / more dramatic Mondrian

```
--block-unit: clamp(50px, 9vh, 90px);
```

------

# One tip

If you later find the layout **growing too large on very tall monitors**, you can also cap it with something like:

```
--block-unit: clamp(40px, 7vh, 85px);
```

This keeps the composition visually controlled.

------

If you'd like, I can also show you **one small improvement that makes the Mondrian grid lines look dramatically better** by matching their thickness to the block scale more precisely (a trick used in design museum sites).