"""
Lead magnet, PLAYBOOK style, Zoltan Gero design system v2
========================================================
Use for: a framework, a strategy, an "X step" process.

  python playbook.py                 -> samples/<output_filename>
  python playbook.py content.json    -> render from your own JSON

Layout: cover page, then Pillars, the step framework, the tool section,
your first moves, and the CTA block. Flows across as many pages as needed.
"""

from brand import T, esc, icon_svg, document, build, ROOT

CONTENT = {
    "title_plain":  "The AI Content",
    "title_accent": "Machine",
    "subtitle":     "Turn your content into a system that works while you sleep.",
    "tagline":      "The Complete Blueprint for AI-Powered Creators",

    "intro": "Most creators are stuck making content by hand, one video at a time. "
             "This playbook shows the shift: from manual work to a system where AI "
             "does the heavy lifting and your email list compounds while you sleep.",

    "pillars": [
        {"icon": "bolt",   "title": "Automate", "desc": "Set it up once. AI does the rest."},
        {"icon": "book",   "title": "Create",   "desc": "Scripts, thumbnails, emails, all AI-generated."},
        {"icon": "target", "title": "Convert",  "desc": "Views to subscribers to revenue, on autopilot."},
    ],

    "steps_title": "The 5-Step AI Content Shift",
    "steps": [
        {"k": "1. Mindset",   "v": "Stop creating manually. Start building systems."},
        {"k": "2. Tools",     "v": "Pick one AI stack. Master it. Ignore the rest."},
        {"k": "3. Workflow",  "v": "Map your process. Then automate each step."},
        {"k": "4. Audience",  "v": "Build the list. Email is the only asset you own."},
        {"k": "5. Evergreen", "v": "Publish once. Distribute forever. Trust, list, revenue."},
    ],

    "tool_title_plain":  "The System That Does It All: ",
    "tool_title_accent": "Claude + GHL",
    "tool_intro": "Two tools carry the whole machine. One writes, one delivers.",
    "tool_items": [
        {"label": "Automated Scripts", "desc": "AI writes your videos. You just record."},
        {"label": "Email Sequences",   "desc": "Nurture on autopilot. No manual sending."},
        {"label": "Thumbnails",        "desc": "AI-generated, A/B tested, always improving."},
        {"label": "SEO Titles",        "desc": "Data-driven. Searchable from day one."},
        {"label": "Lead Magnets",      "desc": "Built in hours, not weeks."},
        {"label": "Analytics",         "desc": "Weekly AI review. Always optimising."},
    ],

    "checklist_title": "Your 2 First Moves",
    "checklist_items": [
        {"label": "WHO",  "text": "Define your niche viewer. Broad means ignored. Specific means subscribed."},
        {"label": "WHAT", "text": 'Write your channel promise: "I help [who] do [what] using [how]."'},
    ],

    "cta_label": "Ready to build your AI content system?",
    "cta_text":  "Start Your Free 30-Day GHL Trial Now",
    "cta_url":   "https://www.gohighlevel.com/?fp_ref=ownership-67",

    "footer_name":     "Zoltan Gero",
    "footer_doc_name": "The AI Content Machine",
    "footer_url":      "https://www.youtube.com/@ZoltanGero?sub_confirmation=1",
    "footer_year":     "2026",

    "output_filename": "The_AI_Content_Machine.pdf",
}


def build_html(c: dict) -> str:
    pillars = "".join(
        f'<div class="pillar"><div class="dot">{icon_svg(p["icon"], T["brand"])}</div>'
        f'<div class="p-title">{esc(p["title"])}</div>'
        f'<div class="p-desc">{esc(p["desc"])}</div></div>'
        for p in c["pillars"])

    steps = "".join(
        f'<li><span class="k">{esc(s["k"])}</span><span>{esc(s["v"])}</span></li>'
        for s in c["steps"])

    feats = "".join(
        f'<div class="feat"><span class="arrow">&#8594;</span>'
        f'<span><span class="fl">{esc(i["label"])}</span> &#8212; {esc(i["desc"])}</span></div>'
        for i in c["tool_items"])

    checks = "".join(
        f'<li><span class="box"></span>'
        f'<span><span class="ck">{esc(i["label"])}:</span> {esc(i["text"])}</span></li>'
        for i in c["checklist_items"])

    body = f"""
  <h2>Start Here</h2>
  <p class="lead">{esc(c['intro'])}</p>

  <h2>The 3 Pillars</h2>
  <div class="pillar-row">{pillars}</div>

  <h2>{esc(c['steps_title'])}</h2>
  <div class="card"><ul class="steps">{steps}</ul></div>

  <h2>{esc(c['tool_title_plain'])}<span style="color:{T['brand']}">{esc(c['tool_title_accent'])}</span></h2>
  <p>{esc(c['tool_intro'])}</p>
  <div class="grid2">{feats}</div>

  <h2>{esc(c['checklist_title'])}</h2>
  <div class="note"><span class="nlabel">Do this before anything else</span>
    <ul class="checkbox-list">{checks}</ul>
  </div>
"""
    return document(c, body)


if __name__ == "__main__":
    build(CONTENT, build_html, CONTENT)
