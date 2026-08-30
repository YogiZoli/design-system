"""
Lead magnet, CHECKLIST style, Zoltan Gero design system v2
=========================================================
Use for: a concrete to-do list, a step-by-step setup, a launch sequence.

  python checklist.py                -> samples/<output_filename>
  python checklist.py content.json   -> render from your own JSON
"""

from brand import esc, document, build

CONTENT = {
    "title_plain":  "The GHL Setup",
    "title_accent": "Checklist",
    "subtitle":     "Everything you need to launch your first funnel, in order.",
    "tagline":      "Your Step-by-Step Launch Checklist for Knowledge Entrepreneurs",

    "intro": "Most course creators waste weeks setting up the wrong things in the "
             "wrong order. This checklist gives you the exact sequence, so you "
             "launch fast and build it right.",

    "sections": [
        {"title": "Phase 1, Foundation (Day 1 to 2)", "items": [
            {"key": "Domain & Hosting", "desc": "Connect your custom domain to GHL. Use Cloudflare for DNS."},
            {"key": "Brand Settings",   "desc": "Upload logo, set brand colours, configure email sender name."},
            {"key": "Calendar Setup",   "desc": "Create your booking calendar. Set availability and buffer time."},
            {"key": "Pipeline",         "desc": "Build your first sales pipeline (Lead, Call, Closed)."},
        ]},
        {"title": "Phase 2, Lead Magnet & Opt-in (Day 3 to 5)", "items": [
            {"key": "Lead Magnet PDF", "desc": "Create your lead magnet using the Playbook template."},
            {"key": "Landing Page",    "desc": "Build the opt-in page. Headline, bullet benefits, form, CTA."},
            {"key": "Thank You Page",  "desc": "Redirect after opt-in. Deliver the PDF and set expectations."},
            {"key": "Automation",      "desc": "Set the trigger: form submitted, tag, deliver PDF email."},
            {"key": "Email Sequence",  "desc": "Write a 5-email welcome sequence. Schedule Day 0 to Day 7."},
        ]},
        {"title": "Phase 3, Traffic & Launch (Day 6 to 7)", "items": [
            {"key": "YouTube CTA",    "desc": "Add the opt-in URL to every video description and pinned comment."},
            {"key": "Test Full Flow", "desc": "Opt in as a test contact. Verify email delivery and tags."},
            {"key": "Analytics",      "desc": "Set up conversion tracking. Know your opt-in rate from day one."},
        ]},
    ],

    "callout_label": "Pro tip",
    "callout_text":  "Do not wait until everything is perfect. A working funnel beats "
                     "a perfect funnel that is not live. Launch on Day 7, then optimise.",

    "cta_label": "Ready to build the whole system in 30 days?",
    "cta_text":  "Start Your Free GHL Trial Now",
    "cta_url":   "https://www.gohighlevel.com/?fp_ref=ownership-67",

    "footer_name":     "Zoltan Gero",
    "footer_doc_name": "The GHL Setup Checklist",
    "footer_url":      "https://www.youtube.com/@ZoltanGero?sub_confirmation=1",
    "footer_year":     "2026",

    "output_filename": "The_GHL_Setup_Checklist.pdf",
}


def build_html(c: dict) -> str:
    blocks = ""
    for sec in c["sections"]:
        items = "".join(
            f'<li><span class="box"></span>'
            f'<span><span class="ck">{esc(it["key"])}</span> &#8212; {esc(it["desc"])}</span></li>'
            for it in sec["items"])
        blocks += f'<h3>{esc(sec["title"])}</h3><ul class="checkbox-list">{items}</ul>'

    callout = ""
    if c.get("callout_text"):
        callout = (f'<div class="tip"><span class="tlabel">{esc(c["callout_label"])}</span>'
                   f'{esc(c["callout_text"])}</div>')

    body = f"""
  <h2>Before You Start</h2>
  <div class="note">{esc(c['intro'])}</div>

  <h2>The Launch Sequence</h2>
  <div class="card">{blocks}</div>
  {callout}
"""
    return document(c, body)


if __name__ == "__main__":
    build(CONTENT, build_html, CONTENT)
