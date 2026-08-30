# PowerPoint template, brand v2

`python deck.py` writes two files:

| File | What it is |
|---|---|
| `master.pptx` | One slide per layout, each labelled. Duplicate the one you need. |
| `samples/C2C_Lead_Magnet_Promo.pptx` | A filled 10-slide example promoting a C2C lead magnet, ending on "Comment TRIGGER below". Voice mirrors the C2C flow deck. |

## Layouts in the master

1. Title (navy)
2. Section divider (navy) with a large number
3. Content, light background (`#F6F8FC`, H1 `#144F9F`, body `#1E2733`)
4. Content, dark background (navy, white heading, one word optionally `#82B0F7`)
5. CTA (navy) with "Comment [KEYWORD] below", KEYWORD in a green `#0E8542` pill

Motif: one thin outline circle bleeds off a corner, alternating green and azure.
Every colour comes from `../../tokens.css` / `../../BRAND-GUIDE.md`. Do not add
values here.

## Font

Every run is named "Open Sans". Google Slides has Open Sans built in, so the deck
renders correctly there with no embedding. For offline PowerPoint on a machine
without Open Sans, install it once (the `.ttf` files are in
`../lead-magnet-pdf/fonts/`) or let Office substitute a humanist sans.

## Make your own deck

Import the layout helpers from `deck.py` and compose:

```python
from deck import _new, layout_title, layout_section, layout_content_light, \
    layout_content_dark, layout_cta

prs = _new()
layout_title(prs, "Free playbook", "Your title", "Your one-line promise.", tag="")
layout_content_light(prs, "A point", "Body text.", bullets=["one", "two"], tag="")
layout_cta(prs, "GUIDE", "and I will send you the link.", tag="")
prs.save("my_deck.pptx")
```

Pass `tag=""` on every call for a real deck (the tag is the master's layout label).

## Dependency

`python-pptx` (`pip install python-pptx`). No LibreOffice needed to generate;
LibreOffice or PowerPoint is only needed to render to images for visual QA.
