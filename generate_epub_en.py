#!/usr/bin/env python3
"""EPUB generator for the English edition."""
import re, uuid, markdown
from pathlib import Path
from ebooklib import epub

INPUT = Path(__file__).resolve().parent / "BOOK_CLAW_CODE_ARCHITECTURE.md"
OUTPUT = Path(__file__).resolve().parent / "Claw_Code_Architecture_of_an_AI_Agent_Harness.epub"

CSS = open(Path(__file__).resolve().parent / "generate_epub.py").read()
# Extract CSS from German generator
import importlib.util
spec = importlib.util.spec_from_file_location("gen", Path(__file__).resolve().parent / "generate_epub.py")
mod = importlib.util.module_from_spec(spec)
# Just reuse the CSS string directly
BOOK_CSS = """
body{font-family:Georgia,"Times New Roman",serif;font-size:1em;line-height:1.6;color:#1a1a1a;margin:1em;text-align:justify}
h1{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:1.8em;font-weight:700;color:#111;margin-top:2em;margin-bottom:.8em;page-break-before:always;border-bottom:2px solid #333;padding-bottom:.3em}
h2{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:1.4em;font-weight:600;color:#222;margin-top:1.5em;margin-bottom:.5em}
h3{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:1.15em;font-weight:600;color:#333;margin-top:1.2em;margin-bottom:.4em}
p{margin-top:.4em;margin-bottom:.6em}
blockquote{margin:1em 1.5em;padding:.5em 1em;border-left:3px solid #888;background:#f9f9f9;font-style:italic;color:#555}
code{font-family:"Source Code Pro","Courier New",monospace;font-size:.85em;background:#f4f4f4;padding:.1em .3em;border-radius:3px}
pre{font-family:"Source Code Pro","Courier New",monospace;font-size:.7em;background:#f4f4f4;padding:.8em 1em;border:1px solid #ddd;border-radius:4px;overflow-x:auto;white-space:pre;line-height:1.3;margin:1em 0}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.85em;page-break-inside:avoid}
th,td{border:1px solid #bbb;padding:.5em .7em;text-align:left;vertical-align:top}
th{background:#e8e8e8;font-weight:700}
tr:nth-child(even){background:#f7f7f7}
strong{font-weight:700}
em{font-style:italic}
ul,ol{margin:.5em 0 .5em 1.5em}
li{margin-bottom:.3em}
hr{border:none;border-top:1px solid #ccc;margin:2em 0}
"""

def md_to_html(text):
    return markdown.markdown(text, extensions=["fenced_code", "tables", "toc"])

def split_chapters(text):
    pattern = r'^(# Chapter \d+.*)$'
    parts = re.split(pattern, text, flags=re.MULTILINE)
    chapters = []
    i = 1
    while i < len(parts):
        title = parts[i].strip().lstrip("# ").strip()
        body = parts[i+1] if i+1 < len(parts) else ""
        chapters.append((title, body.strip()))
        i += 2
    return chapters

def build():
    print("Reading English markdown...")
    md = INPUT.read_text(encoding="utf-8")

    book = epub.EpubBook()
    book.set_identifier(str(uuid.uuid4()))
    book.set_title("Claw Code — Architecture of an AI Agent Harness")
    book.set_language("en")
    book.add_author("Belkis Aslani")
    book.add_metadata("DC", "publisher", "Belkis Aslani, Self-published")
    book.add_metadata("DC", "rights", "Copyright 2026 Belkis Aslani. All rights reserved.")
    book.add_metadata("DC", "description", "The complete technical documentation of the Python reimplementation of the Claude Code agent harness architecture.")

    css = epub.EpubItem(uid="style", file_name="style/book.css", media_type="text/css", content=BOOK_CSS.encode("utf-8"))
    book.add_item(css)

    spine = ["nav"]
    toc = []

    # Title page
    title_html = """
    <div style="text-align:center;padding-top:30%">
        <h1 style="font-size:2.2em;border:none;page-break-before:auto">Claw Code</h1>
        <h2 style="font-size:1.2em;font-weight:400;color:#555">Architecture of an AI Agent Harness</h2>
        <p style="margin-top:1em;font-size:.95em;color:#666">The complete technical documentation of the<br/>Python reimplementation of the Claude Code<br/>agent harness architecture</p>
        <p style="font-size:1.3em;margin-top:3em;color:#333">Belkis Aslani</p>
        <p style="font-size:.9em;margin-top:2em;color:#777">1st Edition — 2026<br/>Self-published</p>
    </div>"""
    tp = epub.EpubHtml(title="Title Page", file_name="title.xhtml", lang="en")
    tp.content = title_html.encode("utf-8")
    tp.add_item(css)
    book.add_item(tp)
    spine.append(tp)

    # Impressum
    impr_html = """
    <div style="font-size:.85em;line-height:1.5;color:#444">
    <h2 style="border:none;font-size:1.1em;margin-top:2em">Legal Notice</h2>
    <p><strong>Claw Code — Architecture of an AI Agent Harness</strong></p>
    <p style="margin-top:1.5em"><strong>Author:</strong> Belkis Aslani</p>
    <p><strong>Contact:</strong><br/>Vogelsangstr. 32, 71691 Freiberg am Neckar, Germany<br/>Email: Belkis.aslani@gmail.com</p>
    <p style="margin-top:1.5em"><strong>Edition:</strong> 1st Edition, April 2026</p>
    <p style="margin-top:1.5em"><strong>Copyright:</strong><br/>&copy; 2026 Belkis Aslani. All rights reserved.</p>
    <p>This work, including all its parts, is protected by copyright. Any use beyond the limits of copyright law without the written consent of the author is prohibited and punishable by law. This applies in particular to reproductions, translations, microfilming, and storage and processing in electronic systems.</p>
    <p style="margin-top:1.5em"><strong>Disclaimer:</strong><br/>This book describes the architecture of an open-source project. It makes no claim of ownership over the original Claude Code source material. The described project is not affiliated with, endorsed by, or maintained by Anthropic.</p>
    <p style="margin-top:1.5em"><strong>Trademarks:</strong><br/>"Claude" and "Claude Code" are trademarks of Anthropic, PBC. Use of these names does not imply affiliation or endorsement.</p>
    </div>"""
    im = epub.EpubHtml(title="Legal Notice", file_name="impressum.xhtml", lang="en")
    im.content = impr_html.encode("utf-8")
    im.add_item(css)
    book.add_item(im)
    spine.append(im)
    toc.append(epub.Link("impressum.xhtml", "Legal Notice", "impressum"))

    # Dedication
    ded_html = '<div style="text-align:center;padding-top:30%;font-style:italic;color:#555"><p>"For all who want to understand<br/>how the machines think —<br/>and have the courage to write it down."</p></div>'
    dd = epub.EpubHtml(title="Dedication", file_name="dedication.xhtml", lang="en")
    dd.content = ded_html.encode("utf-8")
    dd.add_item(css)
    book.add_item(dd)
    spine.append(dd)

    # Chapters
    print("Splitting chapters...")
    chapters = split_chapters(md)
    print(f"  {len(chapters)} chapters found")

    toc_page_lines = ["<h1>Table of Contents</h1>", "<ol>"]
    for idx, (title, body) in enumerate(chapters, start=1):
        fname = f"chapter_{idx:02d}.xhtml"
        toc_page_lines.append(f'<li><a href="{fname}">{title}</a></li>')
        html = md_to_html(f"# {title}\n\n{body}")
        ch = epub.EpubHtml(title=title, file_name=fname, lang="en")
        ch.content = html.encode("utf-8")
        ch.add_item(css)
        book.add_item(ch)
        spine.append(ch)
        toc.append(epub.Link(fname, title, f"ch{idx:02d}"))
        print(f"  Chapter {idx:2d}: {title[:60]}")
    toc_page_lines.append("</ol>")

    toc_page = epub.EpubHtml(title="Table of Contents", file_name="toc.xhtml", lang="en")
    toc_page.content = "\n".join(toc_page_lines).encode("utf-8")
    toc_page.add_item(css)
    book.add_item(toc_page)
    spine.insert(spine.index(dd)+1, toc_page)
    toc.insert(0, epub.Link("toc.xhtml", "Table of Contents", "toc_page"))

    book.toc = toc
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = spine

    print(f"\nWriting EPUB: {OUTPUT}")
    epub.write_epub(str(OUTPUT), book, {})
    print(f"Done! Size: {OUTPUT.stat().st_size/1024:.0f} KB")

if __name__ == "__main__":
    build()
