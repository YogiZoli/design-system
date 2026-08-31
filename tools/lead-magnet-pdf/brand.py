"""
Zoltan Gero lead magnet PDF, shared brand layer (design system v2)
=================================================================
Canon: git@github.com:YogiZoli/design-system.git  (tokens.css + BRAND-GUIDE.md)

This module owns everything that is the same across the three lead magnet
styles: the v2 colour tokens, the embedded Open Sans font faces, the shared
print CSS (type scale from BRAND-GUIDE 3.2, 18px body, 12px cards, navy
shadows, azure rules, green CTA block) and the HTML to PDF renderer.

Rendering uses headless Chrome (canon: we do not write our own render engine).
WeasyPrint needs a GTK stack that is not present on this machine; Chrome is.

Output is a real multi page A4 document: a cover page, then content that
flows naturally across as many pages as the content needs. No more one page
cram.
"""

from __future__ import annotations

import base64
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# ── paths ──────────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent
FONT_DIR = ROOT / "fonts"

# ── v2 colour tokens (from design-system/tokens.css, do not invent) ─────────

T = {
    "background":   "#F6F8FC",
    "surface":      "#FFFFFF",
    "foreground":   "#1E2733",   # body text
    "muted":        "#6A7688",
    "border":       "#E0E6F0",
    "primary":      "#0E8542",   # green, CTA fill only
    "primary_fg":   "#FFFFFF",
    "secondary":    "#1663C6",   # azure button
    "brand":        "#1E7CE8",   # azure, rules + marks
    "h1":           "#144F9F",   # azure 700, PDF headline per touchpoint table
    "link":         "#1663C6",
    "dark":         "#0E2038",   # dark section / footer
    "dark_fg":      "#82B0F7",
    "azure_50":     "#EBF3FE",
    "azure_100":    "#D6E6FD",
    "green_50":     "#E4F5EA",
    "green_100":    "#BFE8CC",
    "neutral_50":   "#F6F8FC",
    "neutral_100":  "#EDF1F7",
}

# ── Open Sans, embedded as base64 so the HTML is portable and the PDF
#    always ends up with the font embedded ─────────────────────────────────

_WEIGHTS = {400: "OpenSans-400.ttf", 500: "OpenSans-500.ttf",
            600: "OpenSans-600.ttf", 700: "OpenSans-700.ttf",
            800: "OpenSans-800.ttf"}


def _font_faces() -> str:
    faces = []
    for weight, name in _WEIGHTS.items():
        data = base64.b64encode((FONT_DIR / name).read_bytes()).decode("ascii")
        faces.append(
            "@font-face{font-family:'Open Sans';font-style:normal;"
            f"font-weight:{weight};font-display:swap;"
            f"src:url(data:font/ttf;base64,{data}) format('truetype');}}"
        )
    return "\n".join(faces)


FONT_STACK = '"Open Sans","Segoe UI",system-ui,-apple-system,Roboto,sans-serif'

# ── shared print CSS ───────────────────────────────────────────────────────


def base_css() -> str:
    return _font_faces() + f"""
*{{margin:0;padding:0;box-sizing:border-box;}}

@page{{
  size:A4;
  margin:18mm 16mm 18mm 16mm;
}}

html{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}

body{{
  font-family:{FONT_STACK};
  font-size:11pt;                 /* ~18px body, BRAND-GUIDE 3.2 Body */
  line-height:1.55;
  color:{T['foreground']};
  background:{T['surface']};
}}

a{{color:{T['link']};text-decoration:none;}}

/* fixed page footer, repeats on every page (cover included) */
.docfoot{{
  position:fixed;left:0;right:0;bottom:6mm;
  display:flex;justify-content:space-between;align-items:center;
  font-size:8pt;color:{T['muted']};letter-spacing:0.01em;
}}
.docfoot .rf-name{{font-weight:700;color:{T['foreground']};}}
.docfoot .yt-link{{display:inline-flex;align-items:center;gap:2mm;font-weight:600;color:{T['brand']};}}
.docfoot .yt-link .yt{{width:15px;height:11px;flex:none;}}

/* ---------- cover ---------- */
.cover{{
  break-after:page;
  min-height:210mm;               /* leaves room for the fixed page footer */
  display:flex;flex-direction:column;
  padding-top:8mm;
}}
.cover .brandline{{
  display:flex;align-items:center;gap:2.5mm;
  font-size:9pt;font-weight:700;color:{T['brand']};
  letter-spacing:0.02em;
}}
.cover .brandline .yt{{width:16px;height:11px;flex:none;}}
.cover .rule{{
  height:3px;width:64mm;background:{T['brand']};
  margin:6mm 0 0 0;border-radius:2px;
}}
.cover .cover-mid{{flex:1;display:flex;flex-direction:column;justify-content:center;}}
.cover h1{{
  font-size:34pt;font-weight:800;line-height:1.08;
  letter-spacing:-0.02em;color:{T['h1']};
}}
.cover h1 .accent{{color:{T['brand']};}}
.cover .subtitle{{
  margin-top:6mm;font-size:15pt;font-weight:400;line-height:1.4;
  color:{T['foreground']};max-width:150mm;
}}
.cover .tagline{{
  margin-top:9mm;font-size:9pt;font-weight:600;letter-spacing:0.06em;
  text-transform:uppercase;color:{T['muted']};
}}
.cover .cover-foot{{
  padding-top:5mm;
  display:flex;justify-content:space-between;align-items:baseline;
}}
.cover .cover-foot .who{{font-size:12pt;font-weight:700;color:{T['foreground']};}}
.cover .cover-foot .role{{
  font-size:8.5pt;font-weight:600;letter-spacing:0.06em;
  text-transform:uppercase;color:{T['brand']};
}}

/* ---------- content typography ---------- */
.content h2{{
  font-size:19pt;font-weight:700;line-height:1.2;letter-spacing:-0.014em;
  color:{T['h1']};margin:9mm 0 3mm 0;
  padding-bottom:2.5mm;border-bottom:2px solid {T['brand']};
}}
.content h2:first-child{{margin-top:0;}}
.content h3{{
  font-size:13pt;font-weight:700;line-height:1.3;
  color:{T['foreground']};margin:5mm 0 2mm 0;
}}
.content{{padding-bottom:6mm;}}
.content p{{margin:0 0 3mm 0;max-width:165mm;}}
.content p:last-child{{margin-bottom:0;}}
.lead{{font-size:12pt;line-height:1.5;color:{T['foreground']};}}
.muted{{color:{T['muted']};}}
strong,b{{font-weight:700;}}

/* ---------- reusable blocks ---------- */
.card{{
  background:{T['surface']};
  border:1px solid {T['border']};
  border-radius:12px;
  padding:6mm 7mm;
  margin:4mm 0;
  box-shadow:0 4px 12px rgba(14,32,56,.08);
  break-inside:avoid;
}}

.pillar-row{{display:flex;gap:5mm;margin:5mm 0;}}
.pillar{{
  flex:1;background:{T['surface']};border:1px solid {T['border']};
  border-radius:12px;padding:6mm 5mm;text-align:center;
  box-shadow:0 4px 12px rgba(14,32,56,.08);break-inside:avoid;
}}
.pillar .dot{{
  width:12mm;height:12mm;border-radius:50%;background:{T['azure_50']};
  border:1.5px solid {T['brand']};
  margin:0 auto 3mm auto;display:flex;align-items:center;justify-content:center;
}}
.pillar .p-title{{
  font-size:10.5pt;font-weight:700;letter-spacing:0.04em;text-transform:uppercase;
  color:{T['h1']};margin-bottom:1.5mm;
}}
.pillar .p-desc{{font-size:10pt;line-height:1.4;color:{T['foreground']};}}

.steps{{list-style:none;}}
.steps li{{
  display:flex;gap:3mm;padding:2.5mm 0;font-size:11pt;line-height:1.45;
  border-bottom:1px solid {T['border']};break-inside:avoid;
}}
.steps li:last-child{{border-bottom:none;}}
.steps .k{{
  flex:none;min-width:34mm;font-weight:700;color:{T['brand']};
}}

.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;}}
.feat{{display:flex;gap:2.5mm;font-size:10.5pt;line-height:1.45;break-inside:avoid;}}
.feat .arrow{{flex:none;color:{T['primary']};font-weight:700;}}
.feat .fl{{font-weight:700;color:{T['foreground']};}}

.checkbox-list{{list-style:none;}}
.checkbox-list li{{
  display:flex;gap:3mm;padding:2mm 0;font-size:10.5pt;line-height:1.45;
  break-inside:avoid;
}}
.checkbox-list .box{{
  flex:none;width:4.2mm;height:4.2mm;margin-top:0.6mm;border-radius:3px;
  border:1.6px solid {T['brand']};
}}
.checkbox-list .ck{{font-weight:700;color:{T['h1']};}}

/* left rule "the point" style callout */
.note{{
  border-left:3px solid {T['brand']};
  background:{T['azure_50']};
  padding:3.5mm 5mm;border-radius:0 8px 8px 0;
  margin:4mm 0;font-size:10.5pt;line-height:1.5;break-inside:avoid;
}}
.note .nlabel{{
  display:block;font-size:8pt;font-weight:700;letter-spacing:0.06em;
  text-transform:uppercase;color:{T['h1']};margin-bottom:1mm;
}}

/* green tip / action callout */
.tip{{
  border-left:3px solid {T['primary']};
  background:{T['green_50']};
  padding:3.5mm 5mm;border-radius:0 8px 8px 0;
  margin:3mm 0;font-size:10.5pt;line-height:1.5;break-inside:avoid;
}}
.tip .tlabel{{
  display:block;font-size:8pt;font-weight:700;letter-spacing:0.06em;
  text-transform:uppercase;color:{T['primary']};margin-bottom:1mm;
}}

/* numbered section card (mini-guide) */
.numcard{{
  display:flex;gap:5mm;align-items:flex-start;
  background:{T['surface']};border:1px solid {T['border']};border-radius:12px;
  padding:6mm 6mm;margin:4mm 0;box-shadow:0 4px 12px rgba(14,32,56,.08);
  break-inside:avoid;
}}
.numcard .num{{
  flex:none;font-size:22pt;font-weight:800;line-height:1;color:{T['brand']};
  width:14mm;text-align:center;
}}
.numcard .nbody{{flex:1;}}

/* overview box (light, azure tint  no dark backgrounds anywhere) */
.darkbox{{
  background:{T['azure_50']};color:{T['foreground']};border-radius:12px;
  border:1px solid {T['azure_100']};
  padding:6mm 7mm;margin:4mm 0;break-inside:avoid;
}}
.darkbox .dlabel{{
  font-size:8.5pt;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;
  color:{T['h1']};margin-bottom:3mm;
}}
.darkbox ul{{list-style:none;}}
.darkbox li{{
  display:flex;gap:3mm;padding:1.5mm 0;font-size:10.5pt;line-height:1.45;
}}
.darkbox li .d{{flex:none;color:{T['brand']};font-weight:700;}}

.arrowlist{{list-style:none;}}
.arrowlist li{{
  display:flex;gap:3mm;padding:1.6mm 0;font-size:10.5pt;line-height:1.45;
}}
.arrowlist li .d{{flex:none;color:{T['primary']};font-weight:700;}}

/* checklist / takeaway summary panel */
.panel{{
  border:1px solid {T['border']};background:{T['neutral_50']};
  border-radius:16px;padding:6mm 7mm;margin:5mm 0;break-inside:avoid;
}}
.panel h3{{margin-top:0;color:{T['h1']};}}

/* ---------- CTA block (light panel, green BUTTON  per Zoltan) ---------- */
.cta{{
  background:{T['neutral_50']};border:1px solid {T['border']};
  border-radius:16px;padding:8mm 9mm;margin:9mm 0 4mm 0;
  text-align:center;break-inside:avoid;
}}
.cta .cta-label{{
  font-size:12pt;font-weight:700;line-height:1.4;color:{T['foreground']};
  margin-bottom:4mm;
}}
.cta .cta-btn{{
  display:inline-block;background:{T['primary']};color:{T['primary_fg']};
  font-size:12pt;font-weight:700;letter-spacing:0.01em;
  padding:4mm 12mm;border-radius:10px;
  box-shadow:0 4px 12px rgba(14,32,56,.10);
}}
.cta .cta-url{{
  display:block;margin-top:3mm;font-size:8.5pt;color:{T['muted']};
  word-break:break-all;
}}
"""


# ── small shared HTML helpers ──────────────────────────────────────────────

def esc(text) -> str:
    return (str(text)
            .replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("\u2014", "&#8212;").replace("\u2013", "&#8211;")
            .replace("\u2192", "&#8594;")
            .replace("\u201c", "&#8220;").replace("\u201d", "&#8221;")
            .replace("\u2018", "&#8216;").replace("\u2019", "&#8217;"))


YT_SVG = ('<svg class="yt" viewBox="0 0 16 11" xmlns="http://www.w3.org/2000/svg">'
          '<rect width="16" height="11" rx="2.5" fill="#FF0000"/>'
          '<path d="M6.5 3L11.5 5.5L6.5 8Z" fill="white"/></svg>')

ICONS = {
    "book":   '<path d="M4 3h10a1 1 0 0 1 1 1v12l-6-2.2L3 16V4a1 1 0 0 1 1-1z"/>',
    "people": '<circle cx="7" cy="7" r="2.6"/><circle cx="12.5" cy="8" r="2.1"/>'
              '<path d="M2.5 15c0-2.7 2-4.3 4.5-4.3s4.5 1.6 4.5 4.3z"/>'
              '<path d="M12.5 11.4c1.9.1 3.3 1.4 3.3 3.6h-3.3z"/>',
    "target": '<circle cx="9" cy="9" r="6.5" fill="none" stroke-width="1.6"/>'
              '<circle cx="9" cy="9" r="3.2" fill="none" stroke-width="1.6"/>'
              '<circle cx="9" cy="9" r="1.3"/>',
    "star":   '<path d="M9 1.8l2.1 4.6 5 .6-3.7 3.4 1 5L9 12.9 3.6 15.4l1-5L.9 7l5-.6z"/>',
    "check":  '<path d="M3 9.5l4 4 8-9" fill="none" stroke-width="2.2" '
              'stroke-linecap="round" stroke-linejoin="round"/>',
    "bolt":   '<path d="M10 1.5L4 10.5h4l-1 6 7-9.5h-4z"/>',
}


def icon_svg(name: str, colour: str) -> str:
    body = ICONS.get(name, ICONS["book"])
    return (f'<svg width="16" height="16" viewBox="0 0 18 18" '
            f'fill="{colour}" stroke="{colour}">{body}</svg>')


def doc_footer(c: dict) -> str:
    year = esc(c.get("footer_year", "2026"))
    name = esc(c.get("footer_name", "Zoltan Gero"))
    doc = esc(c.get("footer_doc_name", ""))
    handle = esc(c.get("footer_handle", "youtube.com/@ZoltanGero"))
    return (f'<div class="docfoot"><span>&#169; {year} '
            f'<span class="rf-name">{name}</span>{" &#183; " + doc if doc else ""}</span>'
            f'<span class="yt-link">{YT_SVG}{handle}</span></div>')


def cover_html(c: dict) -> str:
    return f"""<section class="cover">
  <div class="brandline">{YT_SVG}<span>{esc(c.get('footer_name','Zoltan Gero'))}</span></div>
  <div class="rule"></div>
  <div class="cover-mid">
    <h1>{esc(c['title_plain'])} <span class="accent">{esc(c['title_accent'])}</span></h1>
    <div class="subtitle">{esc(c['subtitle'])}</div>
    <div class="tagline">{esc(c['tagline'])}</div>
  </div>
  <div class="cover-foot">
    <span class="who">{esc(c.get('footer_name','Zoltan Gero'))}</span>
    <span class="role">AI &nbsp;&#183;&nbsp; Business &nbsp;&#183;&nbsp; Freedom</span>
  </div>
</section>"""


def cta_html(c: dict) -> str:
    return f"""<div class="cta">
  <div class="cta-label">{esc(c['cta_label'])}</div>
  <a class="cta-btn" href="{esc(c['cta_url'])}">{esc(c['cta_text'])}</a>
  <span class="cta-url">{esc(c['cta_url'])}</span>
</div>"""


def document(c: dict, body_inner: str, extra_css: str = "") -> str:
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<style>{base_css()}{extra_css}</style></head><body>
{doc_footer(c)}
{cover_html(c)}
<main class="content">
{body_inner}
{cta_html(c)}
</main>
</body></html>"""


# ── renderer ───────────────────────────────────────────────────────────────

_CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "google-chrome", "chromium", "chrome",
]


def _find_chrome() -> str:
    for cand in _CHROME_CANDIDATES:
        if Path(cand).exists() or shutil.which(cand):
            return cand
    raise RuntimeError("No Chrome/Chromium/Edge binary found for PDF rendering.")


def render_pdf(html: str, out_path: str | Path, keep_html: bool = False) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    chrome = _find_chrome()

    tmp_dir = Path(tempfile.mkdtemp(prefix="zg_lm_"))
    html_file = tmp_dir / "doc.html"
    html_file.write_text(html, encoding="utf-8")

    profile = tmp_dir / "profile"
    cmd = [
        chrome, "--headless", "--disable-gpu", "--no-sandbox",
        f"--user-data-dir={profile}",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={out_path}",
        html_file.as_uri(),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if not out_path.exists():
        raise RuntimeError(
            f"Chrome did not produce a PDF.\nstdout: {res.stdout}\nstderr: {res.stderr}")

    if keep_html:
        kept = out_path.with_suffix(".html")
        kept.write_text(html, encoding="utf-8")
    shutil.rmtree(tmp_dir, ignore_errors=True)
    print(f"PDF kesz: {out_path}  ({out_path.stat().st_size // 1024} KB)")
    return out_path


def build(content: dict, build_fn, default_content: dict) -> None:
    """Shared CLI entry: optional JSON path arg, else the module default."""
    import json
    if len(sys.argv) > 1:
        content = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = Path(content.get("output_dir", ROOT / "samples")) / content["output_filename"]
    render_pdf(build_fn(content), out, keep_html=content.get("keep_html", False))
