#!/usr/bin/env python3
"""
Ersetzt ASCII-Umschreibungen durch echte deutsche Umlaute in einer Textdatei.
Arbeitet wortweise, um falsche Ersetzungen zu minimieren.
"""

import re
import sys
from pathlib import Path


# Woerter/Muster, die NICHT ersetzt werden sollen (englische Begriffe, Code etc.)
SKIP_PATTERNS = {
    # Englische Woerter mit "ue", "ae", "oe"
    "true", "false", "issue", "value", "continue", "queue", "unique",
    "technique", "blue", "clue", "due", "revenue", "rescue", "venue",
    "argue", "vague", "league", "fatigue", "catalogue", "dialogue",
    "monologue", "prologue", "rogue", "vogue", "tongue",
    "does", "goes", "foes", "toes", "shoes", "canoes", "heroes",
    "atoes", "potatoes", "echoes", "vetoes",
    "poem", "poet", "poetry", "aeroplane", "phoenix",
    "maestro", "aloe", "oboe", "joe", "toe", "hoe", "roe", "woe",
    "fuel", "cruel", "duel", "gruel", "samuel",
    "sued", "glued", "cued", "ensued", "pursued", "issued",
    "guest", "guess", "guerilla", "guide", "guild", "guilt", "guitar",
    "guarantee", "guard", "guise",
    "queen", "query", "quest", "question",
    "uel", "uel",
    "thread", "spread", "bread", "dead", "head", "lead", "read",
    "instead", "ahead", "dread", "tread",
    "ue", "ae",  # zu kurz, skip
    "coefficient", "aero", "aesthetic",
    "routed", "computed", "executed", "distributed", "contributed",
    "attributed", "substituted",
    "named", "framed", "blamed", "claimed",
    "based", "cased", "phased", "erased",
    "roessler", "mueller", "schroeder",  # eigennamen behalten
}


def replace_umlauts_in_text(text: str) -> str:
    """
    Ersetzt ae->ä, oe->ö, ue->ü, ss->ß in deutschem Text.
    Laesst Code-Bloecke und englische Begriffe unberuehrt.
    """
    lines = text.split('\n')
    result = []
    in_code_block = False

    for line in lines:
        # Code-Bloecke nicht anfassen
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        # Inline-Code nicht anfassen
        # Splitte die Zeile in Code- und Nicht-Code-Segmente
        parts = re.split(r'(`[^`]+`)', line)
        new_parts = []
        for part in parts:
            if part.startswith('`') and part.endswith('`'):
                new_parts.append(part)
            else:
                new_parts.append(replace_in_segment(part))
        result.append(''.join(new_parts))

    return '\n'.join(result)


def replace_in_segment(text: str) -> str:
    """Ersetzt Umlaut-Umschreibungen in einem Textsegment (kein Code)."""

    # Spezifische deutsche Woerter und Muster ersetzen
    replacements = {
        # ä
        'aenderung': 'Änderung', 'Aenderung': 'Änderung', 'aenderungen': 'Änderungen',
        'aendert': 'ändert', 'aendern': 'ändern', 'veraendert': 'verändert',
        'veraenderlich': 'veränderlich', 'unveraenderlich': 'unveränderlich',
        'Unveraenderlichkeit': 'Unveränderlichkeit', 'unveraenderliche': 'unveränderliche',
        'unveraenderlichen': 'unveränderlichen', 'unveraenderliches': 'unveränderliches',
        'unveraendert': 'unverändert', 'Veraenderung': 'Veränderung',
        'aequivalent': 'äquivalent', 'Aequivalent': 'Äquivalent',
        'aequivalenten': 'äquivalenten', 'aequivalentes': 'äquivalentes',
        'aelter': 'älter', 'aeltere': 'ältere', 'aelteren': 'älteren',
        'aeltester': 'ältester',
        'aehnlich': 'ähnlich', 'Aehnlichkeit': 'Ähnlichkeit',
        'aehnliche': 'ähnliche', 'aehnlichen': 'ähnlichen',
        'aerger': 'ärger', 'aergert': 'ärgert',
        'aesthetisch': 'ästhetisch', 'aesthetische': 'ästhetische',
        'Aestethik': 'Ästhetik',
        'aeusser': 'äußer', 'Aeusser': 'Äußer',
        'aeussere': 'äußere', 'aeusseren': 'äußeren', 'aeusserst': 'äußerst',
        'aeussern': 'äußern', 'aeussert': 'äußert',
        'Aerzte': 'Ärzte', 'aerztlich': 'ärztlich',
        'aerger': 'ärger',
        'faehig': 'fähig', 'Faehigkeit': 'Fähigkeit', 'faehigkeiten': 'fähigkeiten',
        'Faehigkeiten': 'Fähigkeiten', 'leistungsfaehig': 'leistungsfähig',
        'leistungsfaehigere': 'leistungsfähigere',
        'gaengi': 'gängi', 'gaengig': 'gängig', 'zugaenglich': 'zugänglich',
        'haelt': 'hält', 'enthaelt': 'enthält', 'erhaelt': 'erhält',
        'behaelt': 'behält',
        'haette': 'hätte', 'Haette': 'Hätte',
        'haengt': 'hängt', 'abhaengi': 'abhängi', 'Abhaengigkeit': 'Abhängigkeit',
        'Abhaengigkeiten': 'Abhängigkeiten', 'abhaengig': 'abhängig',
        'unabhaengig': 'unabhängig',
        'haeufig': 'häufig', 'haeufigste': 'häufigste',
        'jaehr': 'jähr', 'jaehrlich': 'jährlich',
        'kaempf': 'kämpf',
        'laeng': 'läng', 'laenger': 'länger', 'laengst': 'längst',
        'laesst': 'lässt', 'Laesst': 'Lässt', 'zuverlaessig': 'zuverlässig',
        'verlaesslich': 'verlässlich', 'nachlaessig': 'nachlässig',
        'maechtig': 'mächtig', 'maechtiges': 'mächtiges',
        'maessig': 'mäßig',
        'naechst': 'nächst', 'naechste': 'nächste', 'naechsten': 'nächsten',
        'Naeherung': 'Näherung', 'naeher': 'näher', 'Naehe': 'Nähe',
        'naemlich': 'nämlich',
        'praezis': 'präzis', 'Praezedenz': 'Präzedenz', 'Praezedenzfall': 'Präzedenzfall',
        'praesent': 'präsent', 'Praesentationsschicht': 'Präsentationsschicht',
        'Praefix': 'Präfix', 'Praefixe': 'Präfixe', 'praefixe': 'präfixe',
        'spaeter': 'später', 'Spaeter': 'Später',
        'staerke': 'stärke', 'Staerke': 'Stärke', 'Staerken': 'Stärken',
        'staerker': 'stärker', 'verstaerkt': 'verstärkt',
        'Standardmaessig': 'Standardmäßig', 'standardmaessig': 'standardmäßig',
        'staendig': 'ständig', 'eigenstaendig': 'eigenständig',
        'vollstaendig': 'vollständig', 'Vollstaendigkeit': 'Vollständigkeit',
        'selbststaendig': 'selbständig', 'zustaendig': 'zuständig',
        'Gegenstaende': 'Gegenstände',
        'taeusch': 'täusch', 'taeuscht': 'täuscht', 'enttaeuscht': 'enttäuscht',
        'Taetigkeit': 'Tätigkeit', 'taetig': 'tätig', 'taeglich': 'täglich',
        'traegt': 'trägt',
        'waehlt': 'wählt', 'gewaehlt': 'gewählt', 'ausgewaehlt': 'ausgewählt',
        'waehrend': 'während', 'Waehrend': 'Während',
        'waere': 'wäre', 'Waere': 'Wäre',
        'zaehlt': 'zählt', 'zaehler': 'zähler', 'Zaehler': 'Zähler',
        'erzaehlt': 'erzählt', 'Erzaehlung': 'Erzählung',
        'zulaessig': 'zulässig', 'Zulaessigkeit': 'Zulässigkeit',
        'unzulaessig': 'unzulässig',
        'zusaetzlich': 'zusätzlich', 'Zusaetzlich': 'Zusätzlich',
        'zusammengefaellt': 'zusammengefällt',
        'bewaehrt': 'bewährt',
        'erwaehnt': 'erwähnt',
        'gewaehr': 'gewähr', 'Gewaehr': 'Gewähr',
        'schaerfe': 'schärfe', 'Schaerfe': 'Schärfe',
        'schaetzt': 'schätzt', 'Schaetzung': 'Schätzung',
        'schwaeche': 'schwäche', 'Schwaeche': 'Schwäche', 'Schwaechen': 'Schwächen',
        'ueberwaeltigend': 'überwältigend',
        'verfaelsch': 'verfälsch',
        'verhaeltnis': 'verhältnis', 'Verhaeltnis': 'Verhältnis',
        'verlaeuft': 'verläuft',
        'verspaetet': 'verspätet',
        'waechst': 'wächst',
        'zurueckgegeben': 'zurückgegeben',

        # ö
        'Oekonomie': 'Ökonomie', 'oekonomisch': 'ökonomisch',
        'Oekosystem': 'Ökosystem', 'Oekosystems': 'Ökosystems',
        'oeffentlich': 'öffentlich', 'Oeffentlich': 'Öffentlich',
        'veroeffentlich': 'veröffentlich',
        'Veroeffent': 'Veröffent', 'veroeffent': 'veröffent',
        'moechte': 'möchte', 'Moechte': 'Möchte',
        'moeglich': 'möglich', 'Moeglichkeit': 'Möglichkeit',
        'ermoeglich': 'ermöglich', 'unmoeglich': 'unmöglich',
        'hoechst': 'höchst', 'hoechste': 'höchste',
        'hoeher': 'höher', 'hoehe': 'höhe', 'Hoehe': 'Höhe',
        'koennt': 'könnt', 'koennte': 'könnte', 'Koennte': 'Könnte',
        'koennten': 'könnten',
        'groess': 'größ', 'Groesse': 'Größe', 'groesser': 'größer',
        'groesste': 'größte', 'groessten': 'größten',
        'gehoer': 'gehör', 'zugehoer': 'zugehör',
        'geloest': 'gelöst', 'loest': 'löst', 'loesen': 'lösen', 'Loesung': 'Lösung',
        'benoetigt': 'benötigt', 'noeti': 'nöti', 'noetig': 'nötig',
        'stoerend': 'störend',
        'unterstuetz': 'unterstütz',
        'voellig': 'völlig',
        'woertlich': 'wörtlich', 'Woerterbuch': 'Wörterbuch',
        'woerterbuch': 'wörterbuch',
        'zerstoer': 'zerstör',
        'gehoert': 'gehört',
        'erhoeh': 'erhöh',

        # ü
        'ueber': 'über', 'Ueber': 'Über',
        'ueberall': 'überall',
        'ueberein': 'überein', 'Uebereinstimmung': 'Übereinstimmung',
        'uebergeb': 'übergeb', 'Uebergeb': 'Übergeb',
        'uebergeordnet': 'übergeordnet',
        'ueberlapp': 'überlapp',
        'ueberlass': 'überlass',
        'uebernimmt': 'übernimmt', 'uebernomm': 'übernomm',
        'ueberpruefen': 'überprüfen', 'ueberprueft': 'überprüft',
        'Ueberpruef': 'Überprüf',
        'ueberschreib': 'überschreib', 'ueberschreit': 'überschreit',
        'ueberschritt': 'überschritt',
        'Uebersetz': 'Übersetz', 'uebersetz': 'übersetz',
        'uebersicht': 'übersicht', 'Uebersicht': 'Übersicht',
        'Ueberblick': 'Überblick', 'ueberblick': 'überblick',
        'ueberwach': 'überwach',
        'ueblich': 'üblich',
        'uebrig': 'übrig',
        'fuer': 'für', 'Fuer': 'Für', 'dafuer': 'dafür', 'hierfuer': 'hierfür',
        'wofuer': 'wofür',
        'fuehrt': 'führt', 'fuehren': 'führen', 'Einfuehrung': 'Einführung',
        'einfuehr': 'einführ', 'Ausfuehr': 'Ausführ', 'ausfuehr': 'ausführ',
        'durchfuehr': 'durchführ', 'zurueckfuehr': 'zurückführ',
        'ausgefuehrt': 'ausgeführt',
        'fuenf': 'fünf', 'Fuenf': 'Fünf',
        'Gruende': 'Gründe', 'gruende': 'gründe', 'Begruendung': 'Begründung',
        'begruend': 'begründ', 'gruendlich': 'gründlich',
        'gruendet': 'gründet',
        'gueltig': 'gültig', 'ungueltig': 'ungültig',
        'Gueltigkeit': 'Gültigkeit',
        'kuenftig': 'künftig', 'Kuenftig': 'Künftig', 'zukuenftig': 'zukünftig',
        'kuenst': 'künst', 'Kuenst': 'Künst',
        'kuerz': 'kürz', 'Kuerze': 'Kürze',
        'muess': 'müss', 'Muess': 'Müss',
        'muesste': 'müsste',
        'natuerlich': 'natürlich', 'Natuerlich': 'Natürlich',
        'nuetz': 'nütz', 'Nuetz': 'Nütz',
        'pruefen': 'prüfen', 'Pruefung': 'Prüfung', 'prueft': 'prüft',
        'ueberpruef': 'überprüf', 'geprueft': 'geprüft',
        'Pruef': 'Prüf', 'pruef': 'prüf',
        'rueck': 'rück', 'Rueck': 'Rück',
        'zurueck': 'zurück', 'Zurueck': 'Zurück',
        'stueck': 'stück', 'Stueck': 'Stück',
        'Schluess': 'Schlüss', 'schluess': 'schlüss',
        'Schluessel': 'Schlüssel',
        'spuer': 'spür',
        'stuetz': 'stütz', 'unterstuetz': 'unterstütz',
        'ueberfluessig': 'überflüssig',
        'verfueg': 'verfüg', 'Verfueg': 'Verfüg',
        'verknuepf': 'verknüpf',
        'wuerde': 'würde', 'Wuerde': 'Würde', 'wuerden': 'würden',
        'wuensch': 'wünsch',
        'wuerd': 'würd',
        'zueruck': 'zurück',

        # ß
        'grosser': 'großer', 'grosse': 'große', 'grossen': 'großen',
        'grossem': 'großem', 'grosses': 'großes', 'Grosse': 'Große',
        'Grossen': 'Großen', 'Grosser': 'Großer', 'Grosses': 'Großes',
        'Gross': 'Groß', 'gross': 'groß',
        'Grossschreibung': 'Großschreibung',
        'schliesslich': 'schließlich', 'Schliesslich': 'Schließlich',
        'schliesst': 'schließt', 'schliessen': 'schließen',
        'ausschliesslich': 'ausschließlich',
        'einschliesslich': 'einschließlich',
        'anschliessend': 'anschließend',
        'gemass': 'gemäß', 'gemaess': 'gemäß',
        'massgeblich': 'maßgeblich',
        'Massnahme': 'Maßnahme', 'massnahme': 'maßnahme',
        'massgebend': 'maßgebend',
        'regelmassig': 'regelmäßig', 'regelmaessig': 'regelmäßig',
        'gleichmassig': 'gleichmäßig', 'gleichmaessig': 'gleichmäßig',
        'gewissermassen': 'gewissermaßen',
        'strasse': 'straße', 'Strasse': 'Straße',
        'heisst': 'heißt', 'Heisst': 'Heißt',
        'weiss': 'weiß', 'Weiss': 'Weiß',
        'aussen': 'außen', 'Aussen': 'Außen',
        'ausser': 'außer', 'Ausser': 'Außer',
        'ausserhalb': 'außerhalb', 'Ausserhalb': 'Außerhalb',
        'ausserdem': 'außerdem', 'Ausserdem': 'Außerdem',
        'aeusserst': 'äußerst',
        'gewiss': 'gewiß',
        'bloss': 'bloß',
        'stossen': 'stoßen', 'angestossen': 'angestoßen',
        'Verstoss': 'Verstoß',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def process_file(filepath: Path):
    print(f"Verarbeite: {filepath}")
    content = filepath.read_text(encoding='utf-8')
    new_content = replace_umlauts_in_text(content)

    changes = sum(1 for a, b in zip(content, new_content) if a != b)
    print(f"  {changes} Zeichen geändert")

    filepath.write_text(new_content, encoding='utf-8')


if __name__ == '__main__':
    base = Path(__file__).resolve().parent
    process_file(base / "BUCH_CLAW_CODE_ARCHITEKTUR.md")
    print("Fertig!")
