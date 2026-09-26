# VidRev Brand & UI Guide: Shine (v3)

Supersedes the green/azure guide. Reference design: `VidRev App v3.dc.html` (open in a browser; screen switcher at the top, Tweaks for palette/mobile/states). Tokens: `tokens.css`.

## Principles
1. Light theme only. Ground `#F7F8FB` with a faint 20px dot grid. No dark page backgrounds.
2. One primary action per screen: solid fuchsia `#D91E50`, white text, pulsing halo (`cta-halo 2.4s`), a light sheen sweep, hover lifts 1px. Everything else is outline or ghost.
3. Every filled button is solid with white text, at least 4.5:1. Secondary filled = ink `#0E1330`.
4. Blue-green `#00B1B0` is the live accent: status dots, progress bars, the 2px header hairline (fuchsia→blue-green). Never text. Links use `#00807F`.
5. Coral `#FF8370` and Freesia `#FEC84D` only as faint background glow behind hero cards.
6. Danger is warm orange-red (`#A33A00` text, `#F2651B` dot, `#FFF1E8` surface) so errors never read as the CTA.
7. Open Sans for everything; Geist Mono for eyebrows, keywords, links, ids, DNS, code.
8. Vocabulary: Comment → Subscriber → Buyer → Revenue. Never "lead" or "client".

## Type scale
Display money 56/800/-0.035em · Page title 28–30/700–800 · Card title 18/700 · Body 16 · Meta 15 · Small 13 · Eyebrow 12/700 uppercase +0.08em with a 6px dot.

## Components
- Card: white, 1px `#E6E8F0`, radius 12 (hero/focus cards 18), shadow-xs; focus card = 1px primary border + shadow-md.
- Badge/chip: pill, 12/700, surface tint + deep text of the same hue. Keyword chip: mono 13 on `#F0F1F6`, radius 6. Intent tag: outline, 11/700.
- Input: min-height 44 (48 on public pages), radius 10, focus = primary border + 3px ring `rgba(217,30,80,.2)`.
- Notice: radius 12; info = success surface; error = danger surface/border.
- App shell: sticky translucent white header (blur 10px), 2px gradient hairline on top, logo + email + Sign out, underline tabs (active = 2px primary). Queue tab shows a count pill. Mobile: 5-item bottom tab bar (Home, Queue, Keywords, Reports, Connect).
- Public shell (/login, /audit, /audit/[id], /connect/crm): logo + Sign in outline button; centered card, max 440–600px.

## Micro-interactions (keep them, they are the brand)
- Count-up on every revenue/metric figure (ease-out cubic, 1.1–1.8s), then `num-pop` once when it lands.
- Approve → card slides out, next slides in (`card-in`), toast "Approved. Sending your reply.", quota number bumps, bar grows.
- Copy buttons flip to "Copied ✓" for 1.6s.
- Live activity: a new event slides in every few seconds (`row-in`), ping dot on the label.
- Empty queue: radar ping + "No drafts waiting. New keyword comments appear here."
- First report: shimmer skeleton + info notice.
- Respect `prefers-reduced-motion`.
