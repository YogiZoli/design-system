# Lead Magnet PDF generators, v2

Zoltan Gero lead magnet PDFs, rebuilt on design system v2.
Canon: `git@github.com:YogiZoli/design-system.git` (`tokens.css` + `BRAND-GUIDE.md`).

## What changed from v1

| v1 | v2 |
|---|---|
| `#00C4FF` cyan, `#163300`, `#9FE870` | blue-green `#00B1B0` rules, H1 ink `#0E1330`, fuchsia `#D91E50` CTA block, body `#0E1330` on white |
| Liberation Sans | Open Sans, embedded from `fonts/` as base64 (real font embed in the PDF) |
| everything crammed onto one A4 page | cover page, then content flows across as many pages as it needs |
| WeasyPrint | headless Chrome (`--print-to-pdf`); WeasyPrint needs a GTK stack this machine does not have |
| `10pt` body | `11pt` (about 18px), BRAND-GUIDE 3.2 type scale, 12px cards, ink-tinted shadows |

## The 3 styles

| File | Style | Use for |
|---|---|---|
| `playbook.py`  | Playbook   | a framework, a strategy, an "X step" process. Pillars, step framework, tool grid, first moves. |
| `checklist.py` | Checklist  | a concrete to-do list, a step-by-step setup. Intro, phase sections with checkboxes, pro tip. |
| `miniguide.py` | Mini-Guide | a deeper explanation, teaching content. Dark overview box, numbered section cards, action plan. |

## Run

```
cd C:/Users/gdp/projects/freedomOS/tools/lead-magnet-pdf
python playbook.py
python checklist.py
python miniguide.py
```

Each writes to `samples/<output_filename>`. The `CONTENT` dict at the top of each
file is the copy. Edit it in place, or pass a JSON file with the same keys:

```
python playbook.py my_content.json
```

Add `"keep_html": true` to a JSON payload to also drop the intermediate `.html`
next to the PDF for debugging.

## Files

```
brand.py     shared: Shine v3 tokens, embedded Open Sans, print CSS, Chrome renderer
playbook.py  Playbook generator + default content
checklist.py Checklist generator + default content
miniguide.py Mini-Guide generator + default content
fonts/       Open Sans 400 to 800 (Apache 2.0, LICENSE included)
samples/     generated output
```

## Dependencies

Python 3, and Google Chrome (or Edge / Chromium) on the machine. No pip packages.
