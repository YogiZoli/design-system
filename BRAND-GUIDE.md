# ZOLTAN GERO BRAND DESIGN GUIDE

Version 3.0 "Shine", 2026-09-26. The human-readable brand guide.

**Canonical: `git@github.com:YogiZoli/design-system.git`, file `BRAND-GUIDE.md`.**
The Google Doc version is a read-only mirror; edit the repo, then re-push.

This document is the narrative front door to the brand. The **machine source of
truth** is `tokens.css`:

```
C:/Users/gdp/projects/design-system/tokens.css
```

Every value below comes from there. If this doc and `tokens.css` ever disagree,
`tokens.css` wins and this doc is wrong. Say so, do not fork it.

The reference design is `shine/VidRev App v3.dc.html` (open it in a browser;
`support.js` must stay next to it). It has a screen switcher at the top and
Tweaks for palette, mobile and states. The previous green/azure guide is
archived as `BRAND-GUIDE.v1.md` and its tokens as `tokens.v1.css`.

Every AI agent and every design task reads this before producing visual output.

---

## SECTION 1. BRAND ESSENCE

**Mission.** Help course creators turn education businesses into evergreen
income: Purposeful, Peaceful, Profitable, Abundant.

**Archetype.** The Mentor-Futurist. Visionary but grounded. Strategic but warm.

**Positioning.** The AI-powered educator who makes the complex simple and the
complex profitable. YouTube-driven free traffic that converts viewers into
subscribers, and subscribers into customers.

**Design stance (Shine).** Function first, with a bright, confident finish. One
primary action per screen, in fuchsia, that visibly lives: a slow halo pulse and
a light sheen. A blue-green live accent shows that the system is working (status
dots, progress, the header hairline). Warm coral and freesia glow faintly behind
hero cards. Everything else is calm cool neutral. The micro-interactions are part
of the brand, not decoration.

---

## SECTION 2. COLOUR

Fuchsia is the action, blue-green is the live signal, ink is the text, and about
90 percent of every surface is cool neutral.

### 2.1 The brand colours

| Role | Name | Hex | Use for |
|---|---|---|---|
| Action | Fuchsia | `#D91E50` | The primary CTA only. Solid fill, white text (about 5:1), pulsing halo, sheen, 1px hover lift. Hover `#B3163F`. Also money figures (`#B3163F` as text). |
| Live | Blue-green | `#00B1B0` | Status dots, progress bars, the 2px header hairline (fuchsia to blue-green). **Never text.** |
| Link | Deep blue-green | `#00807F` | Links (4.6:1 on white), set in Geist Mono. Hover `#006564`. |
| Secondary | Ink | `#0E1330` | Second filled button, white text. Also body text. |
| Glow | Coral / Freesia | `#FF8370` / `#FEC84D` | Faint background glow behind hero cards only. Never text, never fills. |

The rule that never bends: **every filled button is a solid colour with white
text at 4.5:1 or better.** One primary (fuchsia) action per screen; everything
else is outline or ghost.

### 2.2 Full scales

**Primary (fuchsia).** `50 #FFE9EF  100 #FFD0DD  200 #F9A3B8  300 #F2708F
400 #EB4A74  500 #E42256  600 #D91E50  700 #B3163F  800 #A3143A  900 #7F0F2D`.
500 is the pure brand fuchsia, accents only (4.5:1 is borderline). 600 is the
CTA fill, 700 the hover and money text, 800 the text on a 50 tint.

**Live (blue-green).** `50 #E3F7F6  100 #C4EEEC  200 #92DEDC  300 #55CAC8
400 #1FBDBC  500 #00B1B0  600 #009897  700 #00807F  800 #006564  900 #0B4D4C`.
500 for motion only; 700 and 800 are the only shades used as text (links).

**Neutral (cool).** `white #FFFFFF  ground #F7F8FB  surface-alt #F0F1F6
border #E6E8F0  border-strong #D5D8E3  placeholder #9A9FB3  muted text #666C84
label #4A5068  ink-2 #2A3048  ink #0E1330`.

**Semantic.** Success `#0B7A3E` on `#E3F3E8`. Warning text `#6B4E00`, dot
`#E5A400`, surface `#FBF2DD`. Danger is warm orange-red so an error never reads
as the CTA: text `#A33A00`, dot `#F2651B`, surface `#FFF1E8`, border
`rgba(242,101,27,.4)`.

**Old names still work.** `--brand-*` (was azure) now points at the blue-green
scale with 900/950 on ink, `--accent-*` (was green) points at the fuchsia scale,
`--neutral-*` points at the cool neutrals. New work uses the role tokens below.

### 2.3 Role tokens (what components actually use)

Components read **role tokens**, never a raw scale value, never a literal hex.

```
--background  #F7F8FB      --primary        #D91E50 fuchsia  --border  #E6E8F0
--surface     #FFFFFF      --primary-fg     #FFFFFF          --ring    rgba(217,30,80,.2)
--foreground  #0E1330      --secondary      #0E1330 ink      --link    #00807F
--muted-fg    #666C84      --secondary-fg   #FFFFFF          --live    #00B1B0
--primary-surface #FFE9EF  --primary-surface-fg #A3143A     --ring-solid #D91E50
```

### 2.4 Per-touchpoint

**No dark backgrounds anywhere.** Every surface is light: page `#F7F8FB` with a
faint 20px dot grid, cards and panels `#FFFFFF`. Depth comes from borders and
soft ink-tinted shadows, not from dark fills.

| Touchpoint | Background | Headline and body | Accent and CTA |
|---|---|---|---|
| Web apps, landing pages | `#F7F8FB` + dot grid | `#0E1330` body, `#00807F` links | fuchsia `#D91E50` button, blue-green hairline |
| PDF lead magnets | `#FFFFFF` page, `#FFE9EF` tint boxes | `#0E1330` body and H1 | fuchsia `#D91E50` button in a light panel, blue-green rule lines |
| Slide decks and PLCs | `#F7F8FB` or `#FFFFFF` | `#0E1330` | fuchsia `#D91E50`, keyword in a fuchsia-tint pill |
| YouTube thumbnails | `#FFFFFF` or `#F7F8FB`, optional coral glow | `#0E1330`, one word fuchsia `#D91E50` | fuchsia pop, max 5 words |
| Shorts and Reels | light `#F7F8FB` | `#0E1330` | fuchsia pop |
| Email (GHL, campaigns) | stays black and white | n/a | n/a (see 2.6) |
| Community posts | light `#F7F8FB`, white card | `#0E1330` heading, `#4A5068` body | fuchsia `#D91E50` button |

### 2.5 Accessibility

- All text meets WCAG AA. Buttons meet AA for normal text (4.5:1 or better) via
  the white on solid rule above.
- Blue-green `#00B1B0`, coral and freesia are never text. Links use `#00807F`.
- Never use colour alone to carry meaning: pair with an icon, a shape, or a
  label.
- Focus is always visible: primary border plus a 3px `--ring` glow on inputs, a
  2px `--ring-solid` outline on buttons. Never removed.
- Shadows are ink-tinted (`rgba(14,19,48,...)`), never pure black.
- Every animation stops under `prefers-reduced-motion: reduce`.

### 2.6 Email is deliberately excluded

Campaign and GHL email stays black text on white. Brand colour in bulk email
raises spam-filter risk for no real gain. Brand shows in email through voice and
structure, not colour.

### 2.7 What changed, and why

v1 was "Zoltan Blue" `#00C4FF` with Wise-inspired greens and Inter. v2
(2026-08-29, now archived as `BRAND-GUIDE.v1.md` / `tokens.v1.css`) was azure
`#1E7CE8` plus a green `#0E8542` CTA. Shine (v3, 2026-09-26) replaces it: the
CTA becomes fuchsia `#D91E50`, the secondary becomes ink, the live signal is
blue-green, danger moves to warm orange-red so it never competes with the CTA,
and the dark theme tokens are gone. Anything still on `#1E7CE8`, `#1663C6`,
`#0E8542`, `#12A150` or `#E5484D` as a literal hex is stale and moves to Shine.

---

## SECTION 3. TYPOGRAPHY

### 3.1 Font: Open Sans

One family, weight-driven hierarchy. Free (Google Fonts, Apache 2.0). Humanist,
calm, very legible at small sizes on a phone. Full Hungarian coverage: á é í ó ö
ő ú ü ű and the capitals.

```
Fallback: "Open Sans", "Segoe UI", system-ui, -apple-system, Roboto, sans-serif
Load:     https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700;800&display=swap
Mono:     Geist Mono for eyebrows, keywords, links, ids, DNS, code, counters
```

For a PDF that cannot use a web font, embed the Open Sans .ttf files. Only if
embedding is impossible, fall back to a system humanist sans (Segoe UI, then
Liberation Sans).

### 3.2 Type scale

Marketing and content keep the 18px base scale below. The app UI (Shine
reference design) uses the compact scale that follows it.

| Level | Size | Weight | Line height | Tracking | Use for |
|---|---|---|---|---|---|
| Display | 62px | 800 | 1.0 | -0.022em | Thumbnails, hero headlines, splash |
| H1 | 40px | 700 | 1.14 | -0.02em | Page and video titles, PLC opening |
| H2 | 32px | 700 | 1.2 | -0.016em | Section titles, slide headings |
| H3 | 22px | 700 | 1.3 | -0.006em | Subsections, card headings |
| Body Large | 20px | 400 | 1.5 | 0 | Lead paragraphs, intros |
| Body | 18px | 400 | 1.55 | 0 | Standard copy |
| Small | 15px | 400 | 1.5 | 0 | Secondary text, meta, captions |
| Label | 13px | 500 | 1.4 | 0.03em | Max 3 words, uppercase allowed here only |

**App UI scale (Shine).** Display money 56/800/-0.035em. Page title 28 to 30,
700 to 800. Card title 18/700. Body 16. Meta 15. Small 13. Eyebrow 12/700
uppercase +0.08em in Geist Mono, with a 6px dot.

### 3.3 Rules

**Do:** default to Open Sans everywhere. Left-align body. Centre only short
headlines and CTAs (max 6 words). Line length 50 to 68 characters. Bold for
genuine emphasis, one or two words per sentence. Keep the heading hierarchy (H1
to H2 to H3, never skip). Tabular figures for aligned numbers.

**Don't:** ALL CAPS beyond a 3-word label or an eyebrow. More than two weights
in one design unit. Italic and bold in the same phrase. Justified text. Anything
below 13px (the 11px intent tag in the app is the only exception). A headline
set entirely in caps.

---

## SECTION 4. SPACING, SHAPE, DEPTH, MOTION

### 4.1 Spacing

4px base. Mobile-first and deliberately tighter than a desktop marketing site.
Section padding 40px on mobile, 64px from 768px up. Card padding 20px. Gap
between blocks 20px. Content max width about 1040px, running text about 720px.
Public app pages centre one card, max 440 to 600px.

### 4.2 Radius

```
6px badge, tag, keyword chip    10px button or input    12px card    18px hero or focus card, modal    24px hero media
```

### 4.3 Depth

Borders carry structure, not drop shadows. Default border `1px #E6E8F0`.
Shadows are ink-tinted and soft:

```
xs  0 1px 2px rgba(14,19,48,.06)
sm  0 1px 3px rgba(14,19,48,.08)
md  0 4px 12px rgba(14,19,48,.08)
lg  0 12px 28px rgba(14,19,48,.12)
cta 0 6px 20px rgba(255,131,112,.35)   coral glow under the primary CTA
```

A focus card is a 1px primary border plus shadow-md.

### 4.4 Motion

Purposeful and a little joyful. The signature move is the **CTA pulse**: a
fuchsia halo ring expanding from the button over 2.4s (`cta-halo`), infinite,
over a steady coral glow, plus a light sheen sweep. It does not shift layout. In
HyperFrames video the equivalent stays the plus or minus 2 percent breathe.

```
duration  fast 120ms   base 180ms   slow 280ms
easing    standard cubic-bezier(.4,0,.2,1)   out cubic-bezier(0,0,.2,1)
keyframes cta-halo  sheen  num-pop  ping  bar-grow  card-in  row-in  toast-in  shimmer
```

Micro-interactions (keep them, they are the brand):

- Count-up on every revenue or metric figure (ease-out cubic, 1.1 to 1.8s), then
  `num-pop` once when it lands.
- Approve: the card slides out, the next slides in (`card-in`), a toast says
  "Approved. Sending your reply.", the quota number bumps, the bar grows.
- Copy buttons flip to "Copied" for 1.6s.
- Live activity: a new event slides in every few seconds (`row-in`), with a ping
  dot on the label.
- Empty queue: radar ping plus "No drafts waiting. New keyword comments appear
  here."
- First report: shimmer skeleton plus an info notice.
- Buttons: primary hover darkens one step and lifts 1px; active scales to 0.98;
  a CTA arrow slides 3px right on hover; cards lift 2px on hover.

### 4.5 Theme

Light only. No dark backgrounds on any surface: no dark UI, no dark slides, no
dark PDF panels, no dark thumbnails. The dark-mode tokens were removed from
`tokens.css` in Shine, so a dark OS setting no longer changes anything.

### 4.6 App components (Shine)

- **Card:** white, 1px `#E6E8F0`, radius 12 (hero and focus cards 18),
  shadow-xs.
- **Badge or chip:** pill, 12/700, surface tint plus the deep text of the same
  hue. Keyword chip: mono 13 on `#F0F1F6`, radius 6. Intent tag: outline, 11/700.
- **Input:** min-height 44 (48 on public pages), radius 10, focus = primary
  border plus 3px ring `rgba(217,30,80,.2)`.
- **Notice:** radius 12; info uses the success surface; error uses the danger
  surface and border.
- **App shell:** sticky translucent white header (blur 10px), 2px gradient
  hairline on top, logo plus email plus Sign out, underline tabs (active = 2px
  primary). The Queue tab shows a count pill. Mobile: 5-item bottom tab bar
  (Home, Queue, Keywords, Reports, Connect).
- **Public shell** (/login, /audit, /audit/[id], /connect/crm): logo plus a Sign
  in outline button; one centred card, max 440 to 600px.

---

## SECTION 5. TONE OF VOICE

The verbal identity. Unchanged by Shine, aligned with the global writing rules
in `C:/Users/gdp/CLAUDE.md`.

### 5.1 Personality

Mentor-Futurist. Radical optimist. Strategic teacher. Calm authority. An
entrepreneur teaching from the journey, sharing the process and not only the
destination.

### 5.2 Voice pillars

- **Clear.** No jargon without explanation. Every sentence earns its place.
  Yes: "AI agents can run your whole content system, automatically."
  No: "Leverage multi-modal agentic workflows to optimise throughput."
- **Concise.** Say it once, say it well. "One tool. Infinite content."
- **Empowering.** The reader leaves feeling capable. "You can build this. Here
  is exactly how."
- **Forward-thinking.** "The creators winning in 2026 build systems, not just
  videos."
- **Warm but direct.** Human warmth without hollow enthusiasm. "Let us build
  something that works while you sleep."

### 5.3 Copy rules

| Element | Rule |
|---|---|
| Sentence length | 12 to 18 words average, varied on purpose |
| Paragraph | Max 3 sentences, one idea each |
| CTA copy | Max 8 words, active verb first: "Build your free funnel now." |
| Questions | Rhetorical questions open sections and videos |
| Voice | Active always, especially headlines and CTAs |
| Hungarian | Re-voice, never machine-translate. Same voice: tömör, szakértői, lelkesítő |

### 5.4 Writing mechanics (from CLAUDE.md, applies everywhere)

- **No emoji.** Anywhere, including check marks. Status is a word: "done",
  "running", "0 errors".
- **No horizontal dash between words** (no em dash, no spaced hyphen). Use a
  comma, a colon, brackets, or a new sentence. A hyphen inside a compound, a
  suffix, a filename or a technical id stays.

### 5.5 Words we use and avoid

**Use:** AI agents, AI system, evergreen income, free traffic, email list,
flywheel, build, create, automate, grow, scale, launch, system, machine, course
creator, educator, entrepreneur, Purposeful, Peaceful, Profitable, Abundant.

**Avoid:** hack, trick, secret; revolutionary, game-changing, disruptive; easy,
simple, just; hustle, grind, 24/7; very, really, basically, actually.

**In the VidRev app UI:** the funnel is Comment, Subscriber, Buyer, Revenue.
Never "lead" or "client".

---

## SECTION 6. AI AGENT QUICK REFERENCE

### 6.1 Colour cheat sheet

```
Primary CTA          fuchsia  #D91E50  fill, white text, halo pulse + sheen (hover #B3163F)
Secondary button     ink      #0E1330  fill, white text
Links                #00807F  Geist Mono, hover #006564
Live accent          #00B1B0  dots, progress, hairline. Never text.
Glow (bg only)       coral #FF8370   freesia #FEC84D
Page background      #F7F8FB + 20px dot grid     Surface or card  #FFFFFF
Body text            #0E1330           Muted text       #666C84
Border               #E6E8F0           Tint panel (callout)  #FFE9EF
Fuchsia pop (a highlighted word)  #D91E50
No dark backgrounds anywhere.
Success  #0B7A3E   Warning  #E5A400 (text #6B4E00)   Danger  #F2651B (text #A33A00)
```

### 6.2 Font cheat sheet

```
Thumbnail headline   Open Sans 800   62px   max 5 words
Video title (H1)     Open Sans 700   40px
Section head (H2)    Open Sans 700   32px
Body                 Open Sans 400   18px (app UI 16px)
Eyebrow              Geist Mono 700  12px   uppercase +0.08em
Links, keywords, ids Geist Mono      #00807F links
CTA button label     Open Sans 600   16 to 18px, white on solid
```

### 6.3 CTA formula

`[action verb] plus [outcome] plus [ease or time]`, max 8 words.
"Build your free funnel today." or "Get your AI content system now."

### 6.4 Absolute don't list, every agent

- Never dark text on a mid-tone button. Every button is white text on a solid
  fill at 4.5:1 or better.
- Never more than one fuchsia primary action per screen.
- Never blue-green `#00B1B0`, coral or freesia as text.
- Never a dark background. Every surface is light.
- Never more than three brand colours in one design unit.
- Never a paragraph longer than 3 sentences.
- Never ALL CAPS beyond a 3-word label or an eyebrow.
- Never a font other than Open Sans (and Geist Mono for mono) without an
  explicit request.
- Never passive voice in a headline or CTA.
- Never machine-translate Hungarian, re-voice it.
- Never an emoji. Never a horizontal dash between words.
- Never invent a colour. Use the tokens.

### 6.5 Where the machine values live

`C:/Users/gdp/projects/design-system/tokens.css` (CSS custom properties plus
button, card and input patterns) and `tailwind-preset.js` for Tailwind or
shadcn projects. `README.md` in the same folder has the per-platform rollout
notes. The Shine reference design and its original handoff files live in
`C:/Users/gdp/projects/design-system/shine/`.

---

Version 3.0 "Shine", 2026-09-26. Supersedes v2.0 (2026-08-29, green/azure,
archived as `BRAND-GUIDE.v1.md`).
