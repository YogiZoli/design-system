# Type choice

## Decision: Open Sans

Zoltan rejected Manrope and was lukewarm on Space Grotesk / Unbounded. The
families he liked (Open Sans, Google Sans, Lato, Roboto, Raleway) share one
through-line: humanist, open, calm, highly legible, not geometric-techy.

**"Google Sans" is not on Google Fonts** and cannot be self-hosted legally.
Open Sans is the closest freely licensed match to what Zoltan likes about it:
neutral, friendly, Google-era humanist sans.

- **Free.** Google Fonts, Apache License 2.0.
- **One family.** Weights 400 / 500 / 600 / 700 / 800. Hierarchy from weight
  and size, not from mixing families.
- **Mobile.** Large x-height and open apertures keep it readable at 14 16px on
  a phone, which is the primary target.
- **Hungarian.** Full Latin Extended-A: á é í ó ö ő ú ü ű and capitals, correctly
  shaped. Verified U+0150 U+0151 U+0170 U+0171.

## Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700;800&display=swap">
```

Fallback stack (already in `--font-sans`):
`"Open Sans", "Segoe UI", system-ui, -apple-system, Roboto, sans-serif`

## Optional: Raleway for headings only

If headings want more personality, set `--font-display: "Raleway", ...` and load
`Raleway:wght@600;700`. Raleway is a light-by-nature display sans, so only use
600 and 700; never body text.

## Candidates still on the table

The v2 sample lets Zoltan switch live between Open Sans, Lato, Roboto, and
Raleway. Whichever he confirms becomes `--font-sans`; the rest of the system
does not change.

## Mono: Geist Mono

For the live tag character budget, timestamps, and code snippets. Free.
