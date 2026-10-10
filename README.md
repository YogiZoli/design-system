# Zoltan Gero brand system

**Canonical: `git@github.com:YogiZoli/design-system.git`.** Everything else is a
mirror. Current version: **v3 "Shine" (2026-09-26)**. The previous green/azure
canon is archived as `tokens.v1.css` and `BRAND-GUIDE.v1.md`. The Google Doc
"Zoltan Gero Brand Design Guide v2.0"
(`docs.google.com/document/d/1YIn0u0TKb8pzgE7GtH7QwiMFfLq5whYseItPgk_2lwY`) is a
read-only mirror of `BRAND-GUIDE.md`; when they differ, this repo wins. Edit here,
then re-push the doc.

One source of truth for the visual identity across every surface: web apps,
landing pages, HyperFrames video tokens, documents, decks.

Inspired by the LeadGenJay design language (functional-first, restrained accent,
tiny designer touches, calm lines).

## The idea

Fuchsia is the action, blue-green is the live signal, ink is the text, and about
90% of every surface is cool neutral. **Readability rule: every filled button is
a solid fill with white text, contrast >= 4.5:1.** Light theme only, no dark
backgrounds anywhere.

- **Primary CTA: fuchsia `#D91E50`, white text (~5:1), pulsing halo and a light
  sheen.** One primary action per screen. Hover `#B3163F`, which is also the
  colour of money figures.
- **Secondary button: ink `#0E1330`, white text.** Used sparingly for the
  non-primary action. Everything else is outline or ghost.
- **Live accent: blue-green `#00B1B0`.** Status dots, progress bars, the 2px
  header hairline (fuchsia to blue-green). Never text.
- **Links: deep blue-green `#00807F`** (4.6:1 on white), set in Geist Mono.
  Hover `#006564`.
- **Glow: coral `#FF8370` and freesia `#FEC84D`.** Faint background light behind
  hero cards only. Never text, never fills.
- **Semantic.** Success `#0B7A3E`. Danger is warm orange-red (`#A33A00` text,
  `#F2651B` dot) so an error never reads as the CTA.
- **Neutrals: cool and crisp.** Ground `#F7F8FB` with a faint 20px dot grid,
  cards `#FFFFFF`, border `#E6E8F0`, body text ink `#0E1330`.

The old scale names still resolve, so older pages keep working: `--brand-*`
(was azure) points at the blue-green scale, `--accent-*` (was green) points at
the fuchsia scale. New work uses the role tokens.

Base text is **18px** (`--text-base: 1.125rem`), line-height 1.55.

## Files

| File | Purpose |
|---|---|
| `tokens.css` | The canon (v3 Shine). All CSS custom properties + portable component patterns. Light only, the dark overrides were removed. |
| `BRAND-GUIDE.md` | The human-readable guide (v3 Shine). If it and `tokens.css` disagree, `tokens.css` wins. |
| `shine/` | Reference design `VidRev App v3.dc.html`, plus the short Shine UI guide. |
| `tokens.v1.css`, `BRAND-GUIDE.v1.md` | Archive of the green/azure canon. Do not use for new work. |
| `tailwind-preset.js` | For future Tailwind / shadcn projects. Maps the same tokens to Tailwind theme keys. |
| `FONTS.md` | Type choice and rationale. |

## Type

- **Open Sans** (Google Fonts), one family, weight-driven hierarchy. LOCKED.
  Humanist, calm, very legible at small sizes on mobile. Full Hungarian coverage
  (á é í ó ö ő ú ü ű). Chosen over Manrope (too geometric for Zoltan).
- **Geist Mono** for eyebrows, keywords, links, ids, DNS and code.

## Per-platform rollout

| Platform | Output used |
|---|---|
| Web apps, landing pages (PDT first) | `tokens.css` linked directly. No build. |
| Future Tailwind / shadcn projects | `tailwind-preset.js` + the `:root` block from `tokens.css` as `globals.css`. |
| HyperFrames video | **Not migrated to Shine yet.** `_frames/zoltan-gero/` (FRAME.md, tokens.css, zg.css, every block) still renders the v1 azure/green palette. Moving it is a video rebrand, decided separately. Pulsing already at 2%. |
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
3. Focus ring (`--ring` glow or `--ring-solid` outline, fuchsia) is always
   visible, never removed.
4. Shadows are navy-tinted, never pure black.
5. If a token or a doc contradicts this file, fix the doc  do not silently fork
   the canon.

## Spacing

Mobile-first and deliberately tighter than LeadGenJay's desktop rhythm (Zoltan
works on a small screen and optimizes for mobile). `--section-y` is 40px on
mobile, 64px from 768px up. Body line-height is 1.55. Card padding 20px.

## Status

- 2026-10-10  README brought in line with Shine. Until now it still described
  the v1 azure/green palette while `tokens.css` and the live apps (vidrev, PDT,
  IdeaToVideo) were already on Shine.
- 2026-09-26  **v3 "Shine" replaces the green/azure canon.** Primary fuchsia
  `#D91E50`, live blue-green `#00B1B0`, ink `#0E1330`, light only. The entries
  below are history and describe v1.
- 2026-08-29  (v1, superseded) System LOCKED after iterating with Zoltan: azure brand `#1E7CE8`;
  primary CTA deep green `#0E8542` WHITE text (~4.7:1) + green pulse; secondary
  button deep azure `#1663C6` white text; every button white on solid at 4.5:1+;
  Open Sans, base 18px; light theme ships (dark tokens exist, not used);
  spacing mobile-first. Human guide: `BRAND-GUIDE.md`.
- 2026-08-28  First rollout: Publishing Dream Team, all 5 templates, via
  `app/static/theme.css`. PR: github.com/YogiZoli/publishing-dreamteam/pull/4
  (branch `feat/brand-system`). Visual-only, awaiting Zoltan's review.
- 2026-08-29  Second rollout: CommentClient (C2C). `tokens.css` copied verbatim
  to `app/static/css/theme.css`, linked globally in `base.html`, Inter to Open
  Sans. All CSS, template inline styles, landing + legal pages, `dashboard.py`
  colour tuples and JS-injected UI colours migrated to role tokens; canon
  green/azure split enforced. Branch `feat/brand-system`, visual-only,
  awaiting Zoltan's review.
