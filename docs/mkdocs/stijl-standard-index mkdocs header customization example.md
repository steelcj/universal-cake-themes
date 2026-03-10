# stijl-standard-index mkdocs header customization example

# 1. White Header (Best for Your Current Theme)

This is usually the **cleanest and most consistent** with De Stijl composition.

### Why it works

- Matches your **white composition background**
- Keeps the **grid artwork dominant**
- Maintains excellent readability
- Feels **museum-like / editorial**

### CSS override

```
.md-header {
  background-color: #ffffff;
  color: #000000;
  border-bottom: 10px solid #000000;
}
```

That **black divider line** makes the header feel like part of the grid structure.

------

# 2. Black Header (Strong Framing Option)

This option frames the artwork like a gallery.

```
.md-header {
  background-color: #000000;
  color: #ffffff;
}
```

Advantages:

- Strong contrast
- Very clear navigation
- Modern aesthetic

But it can compete slightly with the Mondrian layout below.

------

# 3. Light Neutral (Very Elegant)

This is a subtle option used in many editorial designs.

```
.md-header {
  background-color: #f7f7f7;
  color: #000000;
  border-bottom: 10px solid #000000;
}
```

Benefits:

- visually softer than pure white
- still maintains the De Stijl feel

------

# My Recommendation for Your Site

Based on the layout you showed earlier:

**White header + black divider**

```
.md-header {
  background-color: #ffffff;
  color: #000000;
  border-bottom: 10px solid #000000;
}
```

This visually connects the header with the **black grid lines** of the composition.

------

# Optional Enhancement (Very Mondrian)

You can add a **small color accent in the header**:

```
.md-header__title::before {
  content: "";
  display: inline-block;
  width: 12px;
  height: 12px;
  background: #c00018;
  margin-right: 8px;
}
```

This adds a tiny red square next to the title — very subtle but very De Stijl.

------

# Important MkDocs Detail

Material also colors the header via the palette system:

```
theme:
  palette:
    primary: white
```

If you override via CSS, that will take precedence.

------

# If you want

I can also show you a **very clean Material-for-MkDocs override that turns the entire header into a Mondrian bar** (with small color blocks integrated into the header) that looks surprisingly elegant and still stays accessible.