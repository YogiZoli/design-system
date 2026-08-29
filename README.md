# Zoltan Gero brand system

**Canonical: `git@github.com:YogiZoli/design-system.git`.** Everything else is a
mirror. The Google Doc "Zoltan Gero Brand Design Guide v2.0"
(`docs.google.com/document/d/1YIn0u0TKb8pzgE7GtH7QwiMFfLq5whYseItPgk_2lwY`) is a
read-only mirror of `BRAND-GUIDE.md`; when they differ, this repo wins. Edit here,
then re-push the doc.

One source of truth for the visual identity across every surface: web apps,
landing pages, HyperFrames video tokens, documents, decks.

Inspired by the LeadGenJay design language (functional-first, restrained accent,
tiny designer touches, calm lines) rebuilt on a **blue** base instead of pink.

## The idea

Azure brand, green action. **Readability rule: every button is a solid fill
with white text, contrast >= 4.5:1.** No dark-text-on-mid-colour, no dark-on-dark.

- **Brand  azure `#1E7CE8`.** Identity, links, header, dark sections.
- **Primary CTA  deep green `#0E8542`, white text (~4.7:1), green pulsing
  halo.** Plain green, pushed to the shade where white text is cleanly readable.
  Literal greenback `#85BB65` rejected (yellow-green, clashes with azure).
- **Secondary button  deep azure `#1663C6`, white text (~5.8:1).** Used
  sparingly for the non-primary action.
- **Semantic success** text/badge = `#0B7A3E`.
- **Neutral bridge  blue-biased grey.** ~90% of every surface. Never pure
  black or pure white.

Base text is **18px** (`--text-base: 1.125rem`), line-height 1.55.

## Files

| File | Purpose |
|---|---|
| `tokens.css` | The canon. All CSS custom properties + portable component patterns. Light active, dark defined but not toggled. |
| `tailwind-preset.js` | For future Tailwind / shadcn projects. Maps the same tokens to Tailwind theme keys. |
| `FONTS.md` | Type choice and rationale. |

## Type

- **Open Sans** (Google Fonts), one family, weight-driven hierarchy. LOCKED.
  Humanist, calm, very legible at small sizes on mobile. Full Hungarian coverage
  (á é í ó ö ő ú ü ű). Chosen over Manrope (too geometric for Zoltan).
- **Geist Mono** for data / code / character counters.

## Per-platform rollout

| Platform | Output used |
|---|---|
| Web apps, landing pages (PDT first) | `tokens.css` linked directly. No build. |
| Future Tailwind / shadcn projects | `tailwind-preset.js` + the `:root` block from `tokens.css` as `globals.css`. |
| HyperFrames video | Retune `_frames/zoltan-gero/FRAME.md` and `_frames/voxflow/FRAME.md` to this palette. Pulsing already at 2%. |
| Docs, decks | Theme built from these hex values. |
| Email (GHL, campaigns) | **Excluded by decision.** Stays black and white (spam-filter risk). |
| Figma | Not now. Wire in later via token JSON when real Figma UI work starts. |

## Applying to a new app (do this in a fresh session, one per app)

The expensive part  choosing the palette, type, spacing  is done. Each app
rollout is cheap and self-contained. Do NOT reopen the long design chat.

Start a new `claude` session in the app's repo and say:
"Apply the Zoltan Gero design system to this app. Canon:
C:\Users\gdp\projects\design-system\tokens.css + README.md."

The agent then:
1. Reads `tokens.css` and this file (2 small files, ~2 min).
2. Copies `tokens.css` into the app (e.g. `static/theme.css`, or a Tailwind
   `globals.css` + the preset) and loads Open Sans.
3. Migrates the app's styles to `var(--...)` role tokens. No raw hex in
   components.
4. Runs the app, checks light theme on mobile width, screenshots.
5. Opens one PR per app. Never commits to main.

Claude Code has no "fork from here". The shared state is these files, not a
chat. That is the point: 5 or 10 apps = 5 or 10 short independent sessions, each
pointed at the same canon.

## Rules

1. Components read **role tokens only** (`--primary`, `--border`, `--foreground`),
   never the raw scales (`--brand-500`) and never a literal hex.
2. Every infinite animation stops under `prefers-reduced-motion: reduce`.
3. Focus ring (`--ring`, turquoise) is always visible, never removed.
4. Shadows are navy-tinted, never pure black.
5. If a token or a doc contradicts this file, fix the doc  do not silently fork
   the canon.

## Spacing

Mobile-first and deliberately tighter than LeadGenJay's desktop rhythm (Zoltan
works on a small screen and optimizes for mobile). `--section-y` is 40px on
mobile, 64px from 768px up. Body line-height is 1.5. Card padding 20px.

## Status

- 2026-08-28  System defined and iterated with Zoltan. LOCKED:
  azure brand `#1E7CE8`; primary CTA green `#12A150` navy text + green pulse;
  secondary button azure fill white text; Open Sans; base 17px; light theme
  ships (dark tokens exist, not used); spacing mobile-first.
- 2026-08-28  First rollout: Publishing Dream Team, all 5 templates, via
  `app/static/theme.css`. PR: github.com/YogiZoli/publishing-dreamteam/pull/4
  (branch `feat/brand-system`). Visual-only, awaiting Zoltan's review.
- 2026-08-29  Second rollout: CommentClient (C2C). `tokens.css` copied verbatim
  to `app/static/css/theme.css`, linked globally in `base.html`, Inter to Open
  Sans. All CSS, template inline styles, landing + legal pages, `dashboard.py`
  colour tuples and JS-injected UI colours migrated to role tokens; canon
  green/azure split enforced. Branch `feat/brand-system`, visual-only,
  awaiting Zoltan's review.
