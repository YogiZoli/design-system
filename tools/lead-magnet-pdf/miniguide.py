"""
Lead magnet, MINI-GUIDE style, Zoltan Gero design system v2
==========================================================
Use for: a deeper explanation, teaching content, a "how it works" guide.

  python miniguide.py               -> samples/<output_filename>
  python miniguide.py content.json  -> render from your own JSON
"""

from brand import esc, document, build

CONTENT = {
    "title_plain":  "The YouTube",
    "title_accent": "Fast Start Guide",
    "subtitle":     "Your first 7 days on YouTube, done right.",
    "tagline":      "A No-Fluff Mini-Guide for Knowledge Entrepreneurs",

    "overview_label": "In this guide you will learn how to:",
    "overview_items": [
        "Set up your channel for trust and discoverability from day one",
        "Create your first video without expensive gear or editing skills",
        "Turn views into email subscribers using one simple CTA",
    ],

    "sections": [
        {"number": "01", "title": "Set Up Your Channel for Authority",
         "body": "Your channel page is your storefront. Before you upload a single "
                 "video, complete your About section with a clear one-sentence "
                 "promise: who you help and what they get. Upload a professional "
                 "banner that shows your name and your niche, not a logo. Add your "
                 "lead magnet link in the top 3 featured links so every visitor sees "
                 "the opt-in.",
         "tip_label": "Key action",
         "tip_text": "Write your channel description with this formula: \"I help "
                     "[audience] achieve [outcome] using [method], new videos every "
                     "[frequency].\""},
        {"number": "02", "title": "Create Your First Video Without Overthinking It",
         "body": "Your first video does not need to be perfect, it needs to be "
                 "published. Pick one specific question your ideal viewer is already "
                 "searching for. Answer it in 8 to 12 minutes using the Ownership "
                 "Framework: open with the problem, teach the solution, own by "
                 "directing to your lead magnet. Record with your phone, natural "
                 "light, and a free teleprompter app.",
         "tip_label": "Key action",
         "tip_text": "Use this title formula: \"[Number] Ways to [Achieve Outcome] "
                     "Without [Common Obstacle],\" it ranks and converts."},
        {"number": "03", "title": "Turn Views into Email Subscribers",
         "body": "Views without conversions are vanity. Every video needs one clear "
                 "CTA that sends viewers to your lead magnet. Place it at 30 seconds, "
                 "again at the end, and in the first line of your description. Use a "
                 "direct link, not \"check the description\" but \"go to [URL] right "
                 "now.\" Your email list is the only audience you own.",
         "tip_label": "Key action",
         "tip_text": "Pin a comment with your lead magnet link on every video. Pinned "
                     "comments are seen by 60 percent or more of viewers who scroll "
                     "to comments."},
    ],

    "takeaway_label": "Your 7-Day Launch Plan",
    "takeaway_items": [
        "Day 1 to 2: channel setup, brand, lead magnet live",
        "Day 3 to 4: keyword research and script for video 1",
        "Day 5 to 6: record, edit, upload with full SEO",
        "Day 7: publish, pin the CTA comment, share once",
    ],

    "cta_label": "Want the full system built for you?",
    "cta_text":  "Start Your Free 30-Day GHL Trial Now",
    "cta_url":   "https://www.gohighlevel.com/?fp_ref=ownership-67",

    "footer_name":     "Zoltan Gero",
    "footer_doc_name": "The YouTube Fast Start Guide",
    "footer_url":      "https://www.youtube.com/@ZoltanGero?sub_confirmation=1",
    "footer_year":     "2026",

    "output_filename": "The_YouTube_Fast_Start_Guide.pdf",
}


def build_html(c: dict) -> str:
    overview = "".join(
        f'<li><span class="d">&#8594;</span><span>{esc(i)}</span></li>'
        for i in c["overview_items"])

    sections = ""
    for s in c["sections"]:
        sections += f"""<div class="numcard">
  <div class="num">{esc(s['number'])}</div>
  <div class="nbody">
    <h3>{esc(s['title'])}</h3>
    <p>{esc(s['body'])}</p>
    <div class="tip"><span class="tlabel">{esc(s['tip_label'])}</span>{esc(s['tip_text'])}</div>
  </div>
</div>"""

    takeaway = "".join(
        f'<li><span class="d">&#8594;</span><span>{esc(i)}</span></li>'
        for i in c["takeaway_items"])

    body = f"""
  <div class="darkbox">
    <div class="dlabel">{esc(c['overview_label'])}</div>
    <ul>{overview}</ul>
  </div>

  <h2>The 3 Moves</h2>
  {sections}

  <h2>{esc(c['takeaway_label'])}</h2>
  <div class="panel"><ul class="arrowlist">{takeaway}</ul></div>
"""
    return document(c, body)


if __name__ == "__main__":
    build(CONTENT, build_html, CONTENT)
