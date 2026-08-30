"""
Zoltan Gero brand v2  PowerPoint template generator.

Canon: git@github.com:YogiZoli/design-system.git (tokens.css + BRAND-GUIDE.md).
Colours and type below are copied from the canon. Do not invent values here.

Outputs (run: python deck.py):
  master.pptx                        one slide per layout, labelled. Duplicate the
                                     one you need in PowerPoint or Google Slides.
  samples/C2C_Lead_Magnet_Promo.pptx a filled 10-slide example, promoting a C2C
                                     lead magnet, ending on "Comment TRIGGER below".

Font: "Open Sans" is named on every run. Google Slides has Open Sans built in, so
the deck renders correctly there with no embedding. For offline PowerPoint on a
machine without Open Sans, install it once (the .ttf files are in
../lead-magnet-pdf/fonts/) or let Office substitute a humanist sans.
"""
from __future__ import annotations
import pathlib
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.lang import MSO_LANGUAGE_ID
from pptx.oxml.ns import qn

HERE = pathlib.Path(__file__).parent
SAMPLES = HERE / "samples"
SAMPLES.mkdir(exist_ok=True)

FONT = "Open Sans"

# --- canon colours (BRAND-GUIDE.md section 2) ---
NAVY        = RGBColor(0x0E, 0x20, 0x38)
NAVY_2      = RGBColor(0x15, 0x35, 0x5F)
PAGE        = RGBColor(0xF6, 0xF8, 0xFC)
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
BODY        = RGBColor(0x1E, 0x27, 0x33)
MUTED       = RGBColor(0x6A, 0x76, 0x88)
MUTED_LIGHT = RGBColor(0x9D, 0xB0, 0xC7)
BODY_ON_DARK= RGBColor(0xC6, 0xD3, 0xE4)
H1_BLUE     = RGBColor(0x14, 0x4F, 0x9F)
AZURE       = RGBColor(0x1E, 0x7C, 0xE8)
AZURE_LIGHT = RGBColor(0x82, 0xB0, 0xF7)
GREEN_CTA   = RGBColor(0x0E, 0x85, 0x42)
GREEN_POP   = RGBColor(0x24, 0xA9, 0x57)
BORDER      = RGBColor(0xE0, 0xE6, 0xF0)
CARD_DARK   = RGBColor(0x17, 0x32, 0x4F)

EMU_W, EMU_H = Inches(13.333), Inches(7.5)
MARGIN = Inches(0.9)


def _new():
    prs = Presentation()
    prs.slide_width = EMU_W
    prs.slide_height = EMU_H
    return prs


def _blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def _bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _text(slide, x, y, w, h, runs, *, size, color, bold=False, align=PP_ALIGN.LEFT,
          anchor=MSO_ANCHOR.TOP, line=1.15, space_after=0, tracking=None):
    """runs: str, or list of (text, color_or_None, bold_or_None) tuples."""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = align
    if line:
        p.line_spacing = line
    if space_after:
        p.space_after = Pt(space_after)
    if isinstance(runs, str):
        runs = [(runs, None, None)]
    for txt, rc, rb in runs:
        r = p.add_run()
        r.text = txt
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = rb if rb is not None else bold
        r.font.color.rgb = rc if rc is not None else color
        r.font.language_id = MSO_LANGUAGE_ID.ENGLISH_US
        if tracking:
            _set_tracking(r, tracking)
    return tb


def _set_tracking(run, pts):
    rPr = run._r.get_or_add_rPr()
    rPr.set("spc", str(int(pts * 100)))


def _ring(slide, corner, color):
    """Thin outline circle bleeding off a corner. The one repeated motif."""
    d = Inches(4.2)
    pos = {
        "tr": (EMU_W - d + Inches(1.4), -Inches(1.4)),
        "br": (EMU_W - d + Inches(1.4), EMU_H - d + Inches(1.4)),
        "bl": (-Inches(1.4), EMU_H - d + Inches(1.4)),
    }[corner]
    sh = slide.shapes.add_shape(MSO_SHAPE.OVAL, pos[0], pos[1], d, d)
    sh.fill.background()
    sh.line.color.rgb = color
    sh.line.width = Pt(2)
    sh.shadow.inherit = False


def _icon_circle(slide, x, y, glyph, circle_color, glyph_color, d=Inches(0.9)):
    c = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, d, d)
    c.fill.solid()
    c.fill.fore_color.rgb = circle_color
    c.line.fill.background()
    c.shadow.inherit = False
    tf = c.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = glyph
    r.font.name = FONT
    r.font.size = Pt(20)
    r.font.bold = True
    r.font.color.rgb = glyph_color


def _footer(slide, dark):
    col = MUTED_LIGHT if dark else MUTED
    _text(slide, MARGIN, EMU_H - Inches(0.62), Inches(11.5), Inches(0.4),
          "commentclient.com    |    youtube.com/@ZoltanGero",
          size=11, color=col, bold=True)


def _card(slide, x, y, w, h, fill_color, border_color=None):
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    sh.adjustments[0] = 0.06
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill_color
    if border_color is not None:
        sh.line.color.rgb = border_color
        sh.line.width = Pt(1)
    else:
        sh.line.fill.background()
    sh.shadow.inherit = False
    return sh


# ----------------------------------------------------------------------------
# LAYOUTS
# ----------------------------------------------------------------------------

def layout_title(prs, eyebrow, title, subtitle, tag="LAYOUT: TITLE (navy)"):
    s = _blank(prs)
    _bg(s, NAVY)
    _ring(s, "br", GREEN_POP)
    _text(s, MARGIN, Inches(1.7), Inches(9.6), Inches(0.5), eyebrow.upper(),
          size=15, color=AZURE_LIGHT, bold=True, tracking=1.6)
    _text(s, MARGIN, Inches(2.35), Inches(10.4), Inches(2.6), title,
          size=44, color=WHITE, bold=True, line=1.05)
    _text(s, MARGIN, Inches(4.9), Inches(9.4), Inches(1.4), subtitle,
          size=18, color=MUTED_LIGHT, line=1.4)
    _footer(s, dark=True)
    _tag(s, tag, True)
    return s


def layout_section(prs, number, title, tag="LAYOUT: SECTION DIVIDER (navy)"):
    s = _blank(prs)
    _bg(s, NAVY)
    _ring(s, "tr", AZURE)
    _text(s, MARGIN, Inches(1.9), Inches(4), Inches(2.2), str(number),
          size=120, color=GREEN_POP, bold=True, line=1.0)
    _text(s, MARGIN, Inches(4.2), Inches(10.6), Inches(1.8), title,
          size=40, color=WHITE, bold=True, line=1.1)
    _footer(s, dark=True)
    _tag(s, tag, True)
    return s


def layout_content_light(prs, title, body, *, bullets=None, right=None,
                         tag="LAYOUT: CONTENT LIGHT"):
    s = _blank(prs)
    _bg(s, PAGE)
    _ring(s, "br", RGBColor(0xD6, 0xE6, 0xFD))
    _text(s, MARGIN, Inches(0.9), Inches(11.5), Inches(1.1), title,
          size=32, color=H1_BLUE, bold=True, line=1.1)
    col_w = Inches(5.6) if right else Inches(11.3)
    y = Inches(2.35)
    if body:
        tb = _text(s, MARGIN, y, col_w, Inches(2.2), body,
                   size=19, color=BODY, line=1.45)
        y += Inches(1.8)
    if bullets:
        _bullets(s, MARGIN, y, col_w, bullets, BODY, GREEN_CTA)
    if right:
        right(s, MARGIN + col_w + Inches(0.5), Inches(2.2))
    _footer(s, dark=False)
    _tag(s, tag, False)
    return s


def layout_content_dark(prs, title, body, *, emphasis=None, callout=None,
                        tag="LAYOUT: CONTENT DARK (navy)"):
    s = _blank(prs)
    _bg(s, NAVY)
    _ring(s, "bl", GREEN_POP)
    if emphasis and emphasis in title:
        before, after = title.split(emphasis, 1)
        runs = [(before, WHITE, True), (emphasis, AZURE_LIGHT, True), (after, WHITE, True)]
        _text(s, MARGIN, Inches(0.9), Inches(11.5), Inches(1.2), runs,
              size=32, color=WHITE, bold=True, line=1.1)
    else:
        _text(s, MARGIN, Inches(0.9), Inches(11.5), Inches(1.2), title,
              size=32, color=WHITE, bold=True, line=1.1)
    _text(s, MARGIN, Inches(2.4), Inches(9.6), Inches(2.4), body,
          size=19, color=BODY_ON_DARK, line=1.45)
    if callout:
        _card(s, MARGIN, Inches(4.9), Inches(10.8), Inches(1.5), CARD_DARK)
        _text(s, MARGIN + Inches(0.45), Inches(5.05), Inches(10), Inches(1.2),
              callout, size=17, color=WHITE, bold=True, line=1.35,
              anchor=MSO_ANCHOR.MIDDLE)
    _footer(s, dark=True)
    _tag(s, tag, True)
    return s


def layout_cta(prs, keyword, line, tag="LAYOUT: CTA (navy)"):
    s = _blank(prs)
    _bg(s, NAVY)
    _ring(s, "tr", GREEN_POP)
    # "Comment  [KEYWORD]  below" centred, keyword in a green pill
    base_y = Inches(2.8)
    _text(s, Inches(1.0), base_y, Inches(4.7), Inches(1.0), "Comment",
          size=44, color=WHITE, bold=True, align=PP_ALIGN.RIGHT,
          anchor=MSO_ANCHOR.MIDDLE)
    pill = slide_pill(s, Inches(5.95), base_y + Inches(0.06), keyword)
    _text(s, Inches(9.05), base_y, Inches(3.3), Inches(1.0), "below",
          size=44, color=WHITE, bold=True, align=PP_ALIGN.LEFT,
          anchor=MSO_ANCHOR.MIDDLE)
    _text(s, Inches(1.5), Inches(4.25), Inches(10.3), Inches(1.3), line,
          size=19, color=MUTED_LIGHT, align=PP_ALIGN.CENTER, line=1.4)
    _footer(s, dark=True)
    _tag(s, tag, True)
    return s


def slide_pill(slide, x, y, keyword):
    w = Inches(0.62 + 0.19 * len(keyword))
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, Inches(0.88))
    sh.adjustments[0] = 0.5
    sh.fill.solid()
    sh.fill.fore_color.rgb = GREEN_CTA
    sh.line.fill.background()
    sh.shadow.inherit = False
    tf = sh.text_frame
    tf.margin_left = tf.margin_right = Inches(0.1)
    tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = keyword
    r.font.name = FONT
    r.font.size = Pt(34)
    r.font.bold = True
    r.font.color.rgb = WHITE
    _set_tracking(r, 1.2)
    return sh


def _bullets(slide, x, y, w, items, text_color, marker_color):
    h = Inches(0.55 * len(items) + 0.4)
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = 1.3
        p.space_after = Pt(10)
        r0 = p.add_run()
        r0.text = "▪  "
        r0.font.name = FONT
        r0.font.size = Pt(18)
        r0.font.color.rgb = marker_color
        r0.font.bold = True
        r1 = p.add_run()
        r1.text = item
        r1.font.name = FONT
        r1.font.size = Pt(18)
        r1.font.color.rgb = text_color
    return tb


def _tag(slide, text, dark):
    """small layout label, master deck only  empty string for the sample."""
    if not text:
        return
    col = MUTED_LIGHT if dark else MUTED
    _text(slide, MARGIN, Inches(0.32), Inches(11.5), Inches(0.35), text,
          size=10, color=col, bold=True, tracking=1.2)


# ----------------------------------------------------------------------------
# MASTER  one slide per layout
# ----------------------------------------------------------------------------

def build_master():
    prs = _new()
    layout_title(prs, "Free playbook",
                 "The headline goes here, in four to nine words",
                 "One sentence. Who it is for and the outcome. Twelve to eighteen words.")
    layout_section(prs, 1, "Section title goes here")

    def demo_right(s, x, y):
        _card(s, x, y, Inches(5.3), Inches(3.4), WHITE, BORDER)
        _icon_circle(s, x + Inches(0.4), y + Inches(0.4), "1", GREEN_CTA, WHITE)
        _text(s, x + Inches(0.4), y + Inches(1.5), Inches(4.5), Inches(1.6),
              "A highlight card. White fill, thin border, an icon in a green circle.",
              size=15, color=BODY, line=1.4)

    layout_content_light(prs, "Content, light background",
                         "Body text is 18 to 19 point, left aligned, colour 1E2733. "
                         "Headings are 32 point bold in 144F9F.",
                         bullets=["First supporting point", "Second supporting point",
                                  "Third supporting point"],
                         right=demo_right)
    layout_content_dark(prs, "Content, dark background with one emphasis word",
                        "On navy the body is C6D3E4. One word in the heading can be "
                        "azure light 82B0F7. Everything else stays white.",
                        emphasis="emphasis",
                        callout="A callout card sits on a 17324F rounded rectangle.")
    layout_cta(prs, "KEYWORD",
               "The CTA slide. Replace KEYWORD with your real trigger word.")
    out = HERE / "master.pptx"
    prs.save(out)
    return out


# ----------------------------------------------------------------------------
# SAMPLE  C2C lead magnet promo, voice mirrors the C2C flow deck
# ----------------------------------------------------------------------------

def build_sample():
    prs = _new()

    layout_title(prs, "Free playbook",
                 "The Comment To Client Playbook",
                 "How a single YouTube comment becomes an email subscriber, then a "
                 "paying client. Without leaving GoHighLevel.", tag="")

    def for_you(s, x, y):
        _card(s, x, y, Inches(5.3), Inches(4.6), WHITE, BORDER)
        _icon_circle(s, x + Inches(0.4), y + Inches(0.4), "✓", GREEN_CTA, WHITE)
        _text(s, x + Inches(1.45), y + Inches(0.52), Inches(3.6), Inches(0.7),
              "YES, THIS IS FOR YOU", size=13, color=GREEN_CTA, bold=True, tracking=0.6)
        _bullets(s, x + Inches(0.4), y + Inches(1.55), Inches(4.55),
                 ["You run your business on GoHighLevel",
                  "You publish on YouTube, or you are about to",
                  "You want every lead traced to the exact video and comment"],
                 BODY, GREEN_CTA)

    s2 = layout_content_light(prs, "Is this for you?",
                              "This works when two things are already true. If they are "
                              "not, it is not for you yet.",
                              right=for_you, tag="")
    _card(s2, MARGIN, Inches(4.55), Inches(5.6), Inches(2.1), WHITE, BORDER)
    _text(s2, MARGIN + Inches(0.4), Inches(4.8), Inches(4.9), Inches(1.7),
          [("NOT YET:  ", MUTED, True),
           ("you do not publish on YouTube, you do not use GoHighLevel, or you "
            "want fully automatic replies with no review.", MUTED, False)],
          size=13, color=MUTED, line=1.35)

    layout_section(prs, 1, "How it works, end to end", tag="")

    layout_content_light(prs, "You say the keyword in the video",
                         "You say it on camera: “Comment GUIDE below.” That "
                         "one line starts the whole flow.",
                         bullets=["Step 1 of 5"], tag="")

    layout_content_light(prs, "The viewer comments it",
                         "They leave your keyword under the video. Just the word: "
                         "GUIDE. Nothing else is needed from them.",
                         bullets=["Step 2 of 5"], tag="")

    layout_content_dark(prs, "It lands in GoHighLevel",
                        "The comment shows up where you already reply to your "
                        "messages. You never open YouTube.",
                        callout="Step 3 of 5    |    same inbox you use every day", tag="")

    layout_content_light(prs, "AI drafts the reply, you approve it",
                         "Every draft carries a branded tracking link, pulled live "
                         "from your GHL funnel. You edit it, then you hit send. "
                         "Nothing posts automatically.",
                         bullets=["Every reply is written for that one comment, never a template",
                                  "You approve every reply, so it stays 100 percent YouTube safe",
                                  "Step 4 of 5"], tag="")

    layout_content_dark(prs, "They opt in",
                        "They click the link, your landing page opens, they enter "
                        "their email. Now they are a real lead in your GoHighLevel.",
                        emphasis="opt in",
                        callout="Step 5 of 5    |    a real lead, not an anonymous view", tag="")

    layout_content_dark(prs, "Know where your money comes from",
                        "Every lead is traced back to the exact video and the exact "
                        "comment that created it. Later, to the paying client it "
                        "became. One source of attribution truth, inside GoHighLevel.",
                        callout="This is the 9th view inside GoHighLevel, your single "
                                "source of attribution truth.",
                        tag="")

    layout_cta(prs, "TRIGGER",
               "Comment the word below and I will send you the free playbook, plus a "
               "walkthrough of the whole system.", tag="")

    out = SAMPLES / "C2C_Lead_Magnet_Promo.pptx"
    prs.save(out)
    return out


if __name__ == "__main__":
    m = build_master()
    print("wrote", m)
    s = build_sample()
    print("wrote", s)
