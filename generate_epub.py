#!/usr/bin/env python3
"""
EPUB-Generator fuer das Buch 'Claw Code — Architektur eines KI-Agent-Harness'
Erzeugt eine verkaufsfertige EPUB-Datei aus der Markdown-Quelle.
"""

import re
import uuid
from pathlib import Path

from ebooklib import epub
import markdown


# ============================================================
# KONFIGURATION
# ============================================================

BOOK_TITLE = "Claw Code — Architektur eines KI-Agent-Harness"
BOOK_SUBTITLE = "Die vollständige technische Dokumentation der Python-Reimplementierung der Claude-Code-Agent-Harness-Architektur"
BOOK_AUTHOR = "Belkis Aslani"
BOOK_LANGUAGE = "de"
BOOK_ISBN = ""  # Kann spaeter ergaenzt werden
BOOK_IDENTIFIER = str(uuid.uuid4())
BOOK_PUBLISHER = "Eigenverlag Belkis Aslani"
BOOK_YEAR = "2026"
BOOK_EDITION = "1. Auflage"

INPUT_FILE = Path(__file__).resolve().parent / "BUCH_CLAW_CODE_ARCHITEKTUR.md"
OUTPUT_FILE = Path(__file__).resolve().parent / "Claw_Code_Architektur_eines_KI-Agent-Harness.epub"


# ============================================================
# CSS-STYLESHEET (professionelles Buchlayout)
# ============================================================

BOOK_CSS = """
@charset "UTF-8";

body {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1em;
    line-height: 1.6;
    color: #1a1a1a;
    margin: 1em;
    text-align: justify;
    hyphens: auto;
    -webkit-hyphens: auto;
}

h1 {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 1.8em;
    font-weight: 700;
    color: #111;
    margin-top: 2em;
    margin-bottom: 0.8em;
    page-break-before: always;
    border-bottom: 2px solid #333;
    padding-bottom: 0.3em;
}

h2 {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 1.4em;
    font-weight: 600;
    color: #222;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}

h3 {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 1.15em;
    font-weight: 600;
    color: #333;
    margin-top: 1.2em;
    margin-bottom: 0.4em;
}

h4 {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 1em;
    font-weight: 600;
    color: #444;
    margin-top: 1em;
    margin-bottom: 0.3em;
}

p {
    margin-top: 0.4em;
    margin-bottom: 0.6em;
    text-indent: 0;
}

blockquote {
    margin: 1em 1.5em;
    padding: 0.5em 1em;
    border-left: 3px solid #888;
    background: #f9f9f9;
    font-style: italic;
    color: #555;
}

code {
    font-family: "Source Code Pro", "Courier New", Courier, monospace;
    font-size: 0.85em;
    background: #f4f4f4;
    padding: 0.1em 0.3em;
    border-radius: 3px;
}

pre {
    font-family: "Source Code Pro", "Courier New", Courier, monospace;
    font-size: 0.7em;
    background: #f4f4f4;
    padding: 0.8em 1em;
    border: 1px solid #ddd;
    border-radius: 4px;
    overflow-x: auto;
    white-space: pre;
    word-wrap: normal;
    overflow-wrap: normal;
    line-height: 1.3;
    margin: 1em 0;
    -webkit-overflow-scrolling: touch;
}

pre code {
    background: none;
    padding: 0;
    border-radius: 0;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    font-size: 0.85em;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #bbb;
    padding: 0.5em 0.7em;
    text-align: left;
    vertical-align: top;
}

th {
    background: #e8e8e8;
    font-weight: 700;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 0.95em;
}

tr:nth-child(even) {
    background: #f7f7f7;
}

td code {
    font-size: 0.9em;
    background: #eee;
}

strong {
    font-weight: 700;
}

em {
    font-style: italic;
}

ul, ol {
    margin: 0.5em 0 0.5em 1.5em;
    padding: 0;
}

li {
    margin-bottom: 0.3em;
}

hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 2em 0;
}

.impressum {
    font-size: 0.85em;
    line-height: 1.5;
    color: #444;
}

.impressum p {
    text-indent: 0;
    margin: 0.3em 0;
}

.titel-seite {
    text-align: center;
    padding-top: 30%;
}

.titel-seite h1 {
    font-size: 2.2em;
    border: none;
    page-break-before: auto;
}

.titel-seite h2 {
    font-size: 1.2em;
    font-weight: 400;
    color: #555;
    margin-top: 0.5em;
}

.titel-seite .autor {
    font-size: 1.3em;
    margin-top: 3em;
    color: #333;
}

.titel-seite .verlag {
    font-size: 0.9em;
    margin-top: 2em;
    color: #777;
}

.widmung {
    text-align: center;
    padding-top: 30%;
    font-style: italic;
    color: #555;
}
"""


# ============================================================
# TITELSEITE
# ============================================================

TITELSEITE_HTML = f"""
<div class="titel-seite">
    <h1>Claw Code</h1>
    <h2>Architektur eines KI-Agent-Harness</h2>
    <p style="margin-top: 1em; font-size: 0.95em; color: #666;">
        Die vollständige technische Dokumentation der<br/>
        Python-Reimplementierung der Claude-Code-<br/>
        Agent-Harness-Architektur
    </p>
    <p class="autor">{BOOK_AUTHOR}</p>
    <p class="verlag">{BOOK_EDITION} &mdash; {BOOK_YEAR}<br/>{BOOK_PUBLISHER}</p>
</div>
"""


# ============================================================
# IMPRESSUM (professionell, vollstaendig)
# ============================================================

IMPRESSUM_HTML = f"""
<div class="impressum">

<h2 style="border: none; font-size: 1.1em; margin-top: 2em;">Impressum</h2>

<p><strong>{BOOK_TITLE}</strong></p>
<p>{BOOK_SUBTITLE}</p>

<p style="margin-top: 1.5em;"><strong>Autor</strong><br/>
Belkis Aslani</p>

<p><strong>Kontakt</strong><br/>
Vogelsangstr. 32<br/>
71691 Freiberg am Neckar<br/>
Deutschland<br/>
E-Mail: Belkis.aslani@gmail.com</p>

<p style="margin-top: 1.5em;"><strong>Verlag</strong><br/>
{BOOK_PUBLISHER}<br/>
Vogelsangstr. 32, 71691 Freiberg am Neckar</p>

<p style="margin-top: 1.5em;"><strong>Ausgabe</strong><br/>
{BOOK_EDITION}, April {BOOK_YEAR}</p>

<p style="margin-top: 1.5em;"><strong>Copyright</strong><br/>
&copy; {BOOK_YEAR} Belkis Aslani. Alle Rechte vorbehalten.</p>

<p>Das Werk einschließlich aller seiner Teile ist urheberrechtlich
geschützt. Jede Verwertung außerhalb der engen Grenzen des
Urheberrechtsgesetzes ist ohne Zustimmung des Autors unzulässig
und strafbar. Das gilt insbesondere für Vervielfältigungen,
Übersetzungen, Mikroverfilmungen und die Einspeicherung und
Verarbeitung in elektronischen Systemen.</p>

<p style="margin-top: 1.5em;"><strong>Haftungsausschluss</strong><br/>
Die in diesem Buch enthaltenen Informationen wurden mit größter
Sorgfalt recherchiert und zusammengestellt. Dennoch übernimmt der
Autor keine Haftung für die Aktualität, Richtigkeit und
Vollständigkeit der bereitgestellten Inhalte. Die Nutzung der
Inhalte erfolgt auf eigenes Risiko des Lesers.</p>

<p>Dieses Buch beschreibt die Architektur eines Open-Source-Projekts.
Es erhebt keinen Anspruch auf das Eigentum am ursprünglichen
Claude-Code-Quellmaterial. Das beschriebene Projekt ist nicht mit
Anthropic verbunden, wird nicht von Anthropic unterstützt und nicht
von Anthropic gepflegt.</p>

<p style="margin-top: 1.5em;"><strong>Markenrechte</strong><br/>
Alle in diesem Buch verwendeten Marken- und Produktnamen sind
Warenzeichen oder eingetragene Warenzeichen ihrer jeweiligen Inhaber.
Die Verwendung dieser Namen in diesem Buch impliziert keine
Zugehörigkeit zu oder Billigung durch die jeweiligen Markeninhaber.
Insbesondere sind &laquo;Claude&raquo; und &laquo;Claude Code&raquo;
Marken von Anthropic, PBC.</p>

<p style="margin-top: 1.5em;"><strong>Quellenhinweis</strong><br/>
Dieses Buch basiert auf der Analyse des Open-Source-Projekts
&laquo;Claw Code&raquo; (github.com/instructkr/claw-code) sowie des
Essays &laquo;Is Legal the Same as Legitimate: AI Reimplementation
and the Erosion of Copyleft&raquo; von Hong Minhee (9. März 2026).
Alle referenzierten Quellen sind im Text kenntlich gemacht.</p>

<p style="margin-top: 1.5em;"><strong>Technische Hinweise</strong><br/>
Dieses E-Book wurde im EPUB-3-Format erstellt. Codebeispiele sind
für die Darstellung auf E-Book-Readern optimiert. Für die beste
Lesbarkeit der Diagramme und Codelistings wird ein Gerät mit
mindestens 6 Zoll Bildschirmdiagonale empfohlen.</p>

<p style="margin-top: 1.5em;"><strong>Satz und Gestaltung</strong><br/>
Automatisiert erstellt mit Python und ebooklib.</p>

</div>
"""


# ============================================================
# WIDMUNG
# ============================================================

WIDMUNG_HTML = """
<div class="widmung">
    <p>&laquo;Für alle, die verstehen wollen,<br/>
    wie die Maschinen denken &mdash;<br/>
    und den Mut haben, es aufzuschreiben.&raquo;</p>
</div>
"""


# ============================================================
# MARKDOWN -> HTML KONVERTIERUNG
# ============================================================

def md_to_html(md_text: str) -> str:
    """Konvertiert Markdown zu HTML mit Unterstützung für Tabellen und Code."""
    # fenced_code muss VOR codehilite stehen; nl2br weglassen (bricht <pre>-Blöcke)
    extensions = ["fenced_code", "tables", "toc"]
    extension_configs = {
        "fenced_code": {},  # Standard-Fenced-Code ohne Syntax-Highlighting
    }
    html = markdown.markdown(
        md_text,
        extensions=extensions,
        extension_configs=extension_configs,
    )
    # Nachbearbeitung: <pre><code> sicherstellen
    html = html.replace("<code>```", "<pre><code>").replace("```</code>", "</code></pre>")
    # HTML-Entities in <pre> schützen (Pipes, Sonderzeichen)
    return html


def split_chapters(md_text: str) -> list[tuple[str, str]]:
    """Splittet den Markdown-Text in Kapitel anhand von '# Kapitel N:' Ueberschriften."""
    # Finde alle Kapitel-Ueberschriften
    pattern = r'^(# Kapitel \d+.*)$'
    parts = re.split(pattern, md_text, flags=re.MULTILINE)

    chapters = []
    i = 1  # parts[0] ist der Text vor dem ersten Kapitel (Inhaltsverzeichnis etc.)
    while i < len(parts):
        title = parts[i].strip().lstrip("# ").strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        chapters.append((title, body.strip()))
        i += 2

    return chapters


# ============================================================
# EPUB AUFBAU
# ============================================================

def build_epub():
    print("Lese Markdown-Quelle...")
    md_text = INPUT_FILE.read_text(encoding="utf-8")

    print("Erstelle EPUB-Struktur...")
    book = epub.EpubBook()

    # Metadaten
    book.set_identifier(BOOK_IDENTIFIER)
    book.set_title(BOOK_TITLE)
    book.set_language(BOOK_LANGUAGE)
    book.add_author(BOOK_AUTHOR)
    book.add_metadata("DC", "publisher", BOOK_PUBLISHER)
    book.add_metadata("DC", "date", f"{BOOK_YEAR}-04-01")
    book.add_metadata("DC", "description", BOOK_SUBTITLE)
    book.add_metadata("DC", "subject", "Software-Architektur")
    book.add_metadata("DC", "subject", "KI-Agenten")
    book.add_metadata("DC", "subject", "Python")
    book.add_metadata("DC", "subject", "Harness-Engineering")
    book.add_metadata("DC", "rights", f"Copyright {BOOK_YEAR} {BOOK_AUTHOR}. Alle Rechte vorbehalten.")

    # CSS
    css_item = epub.EpubItem(
        uid="style",
        file_name="style/book.css",
        media_type="text/css",
        content=BOOK_CSS.encode("utf-8"),
    )
    book.add_item(css_item)

    # Spine und TOC aufbauen
    spine_items = ["nav"]
    toc_items = []

    # --- Titelseite ---
    titel = epub.EpubHtml(title="Titelseite", file_name="titel.xhtml", lang="de")
    titel.content = TITELSEITE_HTML.encode("utf-8")
    titel.add_item(css_item)
    book.add_item(titel)
    spine_items.append(titel)

    # --- Impressum ---
    impressum = epub.EpubHtml(title="Impressum", file_name="impressum.xhtml", lang="de")
    impressum.content = IMPRESSUM_HTML.encode("utf-8")
    impressum.add_item(css_item)
    book.add_item(impressum)
    spine_items.append(impressum)
    toc_items.append(epub.Link("impressum.xhtml", "Impressum", "impressum"))

    # --- Widmung ---
    widmung = epub.EpubHtml(title="Widmung", file_name="widmung.xhtml", lang="de")
    widmung.content = WIDMUNG_HTML.encode("utf-8")
    widmung.add_item(css_item)
    book.add_item(widmung)
    spine_items.append(widmung)

    # --- Inhaltsverzeichnis-Seite ---
    toc_page_lines = [
        "<h1>Inhaltsverzeichnis</h1>",
        "<ol>",
    ]

    # Kapitel aufsplitten
    print("Splitte Kapitel...")
    chapters = split_chapters(md_text)
    print(f"  {len(chapters)} Kapitel gefunden.")

    # Kapitel-Dateien erzeugen
    for idx, (title, body) in enumerate(chapters, start=1):
        fname = f"kapitel_{idx:02d}.xhtml"
        short_title = title

        # TOC-Seite ergaenzen
        toc_page_lines.append(f'<li><a href="{fname}">{title}</a></li>')

        # Kapitel-HTML
        chapter_html = md_to_html(f"# {title}\n\n{body}")
        chapter_item = epub.EpubHtml(title=title, file_name=fname, lang="de")
        chapter_item.content = chapter_html.encode("utf-8")
        chapter_item.add_item(css_item)
        book.add_item(chapter_item)

        spine_items.append(chapter_item)
        toc_items.append(epub.Link(fname, short_title, f"kap{idx:02d}"))

        print(f"  Kapitel {idx:2d}: {short_title}")

    toc_page_lines.append("</ol>")

    toc_page = epub.EpubHtml(title="Inhaltsverzeichnis", file_name="inhaltsverzeichnis.xhtml", lang="de")
    toc_page.content = "\n".join(toc_page_lines).encode("utf-8")
    toc_page.add_item(css_item)
    book.add_item(toc_page)
    # Inhaltsverzeichnis nach Widmung einfuegen
    spine_items.insert(spine_items.index(widmung) + 1, toc_page)
    toc_items.insert(0, epub.Link("inhaltsverzeichnis.xhtml", "Inhaltsverzeichnis", "toc_page"))

    # --- EPUB-Navigation ---
    book.toc = toc_items
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = spine_items

    # --- Schreiben ---
    print(f"\nSchreibe EPUB: {OUTPUT_FILE}")
    epub.write_epub(str(OUTPUT_FILE), book, {})
    size_kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"Fertig! Dateigroesse: {size_kb:.0f} KB")
    print(f"Ausgabedatei: {OUTPUT_FILE}")


if __name__ == "__main__":
    build_epub()
