# ZOLTAN GERO BRAND DESIGN GUIDE

Version 2.0, 2026-08-29. The human-readable brand guide.

**Canonical: `git@github.com:YogiZoli/design-system.git`, file `BRAND-GUIDE.md`.**
The Google Doc version is a read-only mirror; edit the repo, then re-push.

This document is the narrative front door to the brand. The **machine source of
truth** is `tokens.css`:

```
C:\Users\gdp\projects\design-system\tokens.css
```

Every value below comes from there. If this doc and `tokens.css` ever disagree,
`tokens.css` wins and this doc is wrong. Say so, do not fork it.

Every AI agent and every design task reads this before producing visual output.

---

## SECTION 1. BRAND ESSENCE

**Mission.** Help course creators turn education businesses into evergreen
income: Purposeful, Peaceful, Profitable, Abundant.

**Archetype.** The Mentor-Futurist. Visionary but grounded. Strategic but warm.

**Positioning.** The AI-powered educator who makes the complex simple and the
complex profitable. YouTube-driven free traffic that converts viewers into
subscribers, and subscribers into customers.

**Design stance (the LeadGenJay language).** Function first. One accent colour,
used sparingly. Small deliberate designer touches: a slow pulse on the main
button, a faint background wash. Calm lines, calm type. Nothing flashy, nothing
luxury. High quality through restraint: few values, used consistently.

---

## SECTION 2. COLOUR

Two poles of blue-green on a blue-biased neutral. Azure is the brand, green is
the action, and about 90 percent of every surface is neutral.

### 2.1 The two brand colours

| Role | Name | Hex | Use for |
|---|---|---|---|
| Brand | Azure | `#1E7CE8` | Links, header, logo mark, dark-section headings, focus ring, secondary button |
| Action | Green | `#0E8542` | The primary CTA only. Solid fill, white text, slow green pulse. |

The primary CTA is **green `#0E8542` with white text** (contrast about 4.7:1).
The secondary button is **azure `#1663C6` with white text** (about 5.8:1). Both
are solid fills. This is the one rule that never bends: **every button is a
solid colour with white text at 4.5:1 or better.** No dark text on a mid-tone
fill, no dark on dark.

### 2.2 Full scales

**Brand (azure).** Identity, links, dark sections.

```
50  #EBF3FE   200 #B0CEFB   400 #4F8DF0   600 #1663C6   800 #163F7B   950 #0E2038
100 #D6E6FD   300 #82B0F7   500 #1E7CE8   700 #144F9F   900 #15355F
```

**Accent (green).** The action colour. Anchored on `#12A150`; the CTA sits at
600 so white text stays readable.

```
50  #E4F5EA   200 #8DD5A6   400 #24A957   600 #0E8542   800 #0C5430
100 #BFE8CC   300 #56BE7B   500 #12A150   700 #0C6A36   900 #0A4228
```

**Neutral (blue-biased grey).** 90 percent of every surface. Never pure black,
never pure white.

```
0   #FFFFFF   200 #E0E6F0   400 #97A3B8   600 #4C5768   800 #1E2733
50  #F6F8FC   300 #CAD3E1   500 #6A7688   700 #333D4C   900 #131A24
100 #EDF1F7
```

**Semantic.** Status only, kept separate from the accent.

```
Success  #0B7A3E on #E3F3E8
Warning  #E5A400 on #FBF2DD
Danger   #E5484D on #FCECED
Info     is brand azure #1663C6
```

### 2.3 Role tokens (what components actually use)

Components read **role tokens**, never a raw scale value, never a literal hex.

```
--background  #F6F8FC      --primary        #0E8542 green    --border  #E0E6F0
--surface     #FFFFFF      --primary-fg     #FFFFFF          --ring    #0E8542
--foreground  #1E2733      --secondary      #1663C6 azure    --link    #1663C6
--muted-fg    #6A7688      --secondary-fg   #FFFFFF
```

### 2.4 Per-touchpoint

| Touchpoint | Background | Headline and body | Accent and CTA |
|---|---|---|---|
| Web apps, landing pages | `#F6F8FC` | `#1E2733` body, `#1663C6` links | green `#0E8542` button |
| PDF lead magnets | `#FFFFFF` | `#1E2733` body, `#144F9F` H1 | green `#0E8542` CTA block, azure rule lines |
| YouTube thumbnails | `#0E2038` or `#15355F` dark | `#FFFFFF` or `#82B0F7` | green `#24A957` pop, max 5 words |
| Slide decks and PLCs | `#FFFFFF` | `#1E2733` body, `#144F9F` H1 | green `#0E8542` |
| Shorts and Reels | dark `#0E2038` | high contrast white or `#82B0F7` | green pop |
| Email (GHL, campaigns) | stays black and white | n/a | n/a (see 2.6) |
| Community posts | platform native | platform native | azure or green in graphics only |

### 2.5 Accessibility

- All text meets WCAG AA. Buttons meet AA for normal text (4.5:1 or better) via
  the white on solid rule above.
- Never use colour alone to carry meaning: pair with an icon, a shape, or a
  label.
- The focus ring (green, `--ring`) is always visible and never removed.
- Shadows are navy-tinted (`rgba(14,32,56,...)`), never pure black.

### 2.6 Email is deliberately excluded

Campaign and GHL email stays black text on white. Brand colour in bulk email
raises spam-filter risk for no real gain. Brand shows in email through voice and
structure, not colour.

### 2.7 What changed from v1, and why

v1 was "Zoltan Blue" `#00C4FF` (cyan) with Wise-inspired greens and Inter. It
was replaced wholesale: the cyan fails contrast on white for anything but large
text, the palette had five competing colours, and it never shipped
consistently. v2 is one azure, one green, a disciplined neutral scale, and a
hard readability rule. Anything still on `#00C4FF`, `#9FE870`, `#163300`,
`#A0E1E1` or Inter is stale and moves to v2.

---

## SECTION 3. TYPOGRAPHY

### 3.1 Font: Open Sans

One family, weight-driven hierarchy. Free (Google Fonts, Apache 2.0). Humanist,
calm, very legible at small sizes on a phone. Full Hungarian coverage: á é í ó ö
ő ú ü ű and the capitals. Chosen over Inter (too plain) and Manrope (too
geometric).

```
Fallback: "Open Sans", "Segoe UI", system-ui, -apple-system, Roboto, sans-serif
Load:     https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700;800&display=swap
Data, code, counters: Geist Mono
```

For a PDF that cannot use a web font, embed the Open Sans .ttf files. Only if
embedding is impossible, fall back to a system humanist sans (Segoe UI, then
Liberation Sans).

### 3.2 Type scale, base 18px

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

### 3.3 Rules

**Do:** default to Open Sans everywhere. Left-align body. Centre only short
headlines and CTAs (max 6 words). Line length 50 to 68 characters. Bold for
genuine emphasis, one or two words per sentence. Keep the heading hierarchy (H1
to H2 to H3, never skip). Tabular figures for aligned numbers.

**Don't:** ALL CAPS beyond a 3-word label. More than two weights in one design
unit. Italic and bold in the same phrase. Justified text. Anything below 13px.
A headline set entirely in caps (loses warmth).

---

## SECTION 4. SPACING, SHAPE, DEPTH, MOTION

### 4.1 Spacing

4px base. Mobile-first and deliberately tighter than a desktop marketing site,
because Zoltan works on a small screen. Section padding 40px on mobile, 64px
from 768px up. Card padding 20px. Gap between blocks 20px. Content max width
about 1040px, running text about 720px.

### 4.2 Radius

```
6px badge or tag    10px button or input    12px card    16px panel or modal    24px hero media
```

### 4.3 Depth

Borders carry structure, not drop shadows. Default border `1px #E0E6F0`.
Shadows are navy-tinted and soft:

```
xs  0 1px 2px rgba(14,32,56,.06)
sm  0 1px 3px rgba(14,32,56,.08)
md  0 4px 12px rgba(14,32,56,.08)
lg  0 12px 28px rgba(14,32,56,.12)
```

### 4.4 Motion

Slow, small, purposeful. The only signature move is the **CTA pulse**: a green
halo ring expanding from the button over 2.4s, infinite, that does not shift
layout. In HyperFrames video the equivalent is the plus or minus 2 percent
breathe. Every infinite animation stops under `prefers-reduced-motion: reduce`.

```
duration  fast 120ms   base 180ms   slow 280ms
easing    standard cubic-bezier(.4,0,.2,1)   out cubic-bezier(0,0,.2,1)
```

Micro-interactions: button hover darkens one step and lifts the shadow; button
active scales to 0.98; a CTA arrow slides 3px right on hover; cards lift 2px on
hover; inputs get a 3px green focus glow.

### 4.5 Theme

Light is the only theme that ships. Dark-mode tokens exist in `tokens.css` for
later; there is no toggle. Do not build a dark UI unless asked.

---

## SECTION 5. TONE OF VOICE

The verbal identity. Unchanged in spirit from v1, aligned with the global
writing rules in `C:\Users\gdp\CLAUDE.md`.

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

- **No emoji.** Anywhere. Status is a word: "done", "running", "0 errors".
- **No horizontal dash between words** (no em dash, no spaced hyphen). Use a
  comma, a colon, brackets, or a new sentence. A hyphen inside a compound, a
  suffix, a filename or a technical id stays.

### 5.5 Words we use and avoid

**Use:** AI agents, AI system, evergreen income, free traffic, email list,
flywheel, build, create, automate, grow, scale, launch, system, machine, course
creator, educator, entrepreneur, Purposeful, Peaceful, Profitable, Abundant.

**Avoid:** hack, trick, secret; revolutionary, game-changing, disruptive; easy,
simple, just; hustle, grind, 24/7; very, really, basically, actually.

---

## SECTION 6. AI AGENT QUICK REFERENCE

### 6.1 Colour cheat sheet

```
Primary CTA          green  #0E8542  fill, white text, green pulse
Secondary button     azure  #1663C6  fill, white text
Brand and links      azure  #1E7CE8
Page background       #F6F8FC        Surface or card  #FFFFFF
Body text             #1E2733        Muted text       #6A7688
Border                #E0E6F0
Dark section, footer  #0E2038        text on it  #FFFFFF or #82B0F7
Success  #0B7A3E   Warning  #E5A400   Danger  #E5484D
```

### 6.2 Font cheat sheet

```
Thumbnail headline   Open Sans 800   62px   max 5 words
Video title (H1)     Open Sans 700   40px
Section head (H2)    Open Sans 700   32px
Body                 Open Sans 400   18px
CTA button label     Open Sans 600   16 to 18px, white on solid
```

### 6.3 CTA formula

`[action verb] plus [outcome] plus [ease or time]`, max 8 words.
"Build your free funnel today." or "Get your AI content system now."

### 6.4 Absolute don't list, every agent

- Never dark text on a mid-tone button. Every button is white text on a solid
  fill at 4.5:1 or better.
- Never more than three brand colours in one design unit.
- Never a paragraph longer than 3 sentences.
- Never ALL CAPS beyond a 3-word label.
- Never a font other than Open Sans without an explicit request.
- Never passive voice in a headline or CTA.
- Never machine-translate Hungarian, re-voice it.
- Never an emoji. Never a horizontal dash between words.
- Never invent a colour. Use the tokens.

### 6.5 Where the machine values live

`C:\Users\gdp\projects\design-system\tokens.css` (CSS custom properties plus
button, card and input patterns) and `tailwind-preset.js` for Tailwind or
shadcn projects. `README.md` in the same folder has the per-platform rollout
notes.

---

Version 2.0, 2026-08-29. Supersedes v1.0 (May 2026, "Zoltan Blue" `#00C4FF`).
