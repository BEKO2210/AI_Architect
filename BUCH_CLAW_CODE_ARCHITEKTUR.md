# Claw Code — Architektur eines KI-Agent-Harness

**Ein technisches Buch über die Python-Reimplementierung der Claude-Code-Agent-Harness-Architektur**

---

## Inhaltsverzeichnis

1. [Einführung & Hintergrundgeschichte](#kapitel-1-einführung-und-hintergrundgeschichte)
2. [Ethik & Recht der KI-Reimplementierung](#kapitel-2-ethik-und-recht-der-ki-reimplementierung)
3. [High-Level-Architektur](#kapitel-3-high-level-architektur)
4. [Der CLI-Einstiegspunkt](#kapitel-4-der-cli-einstiegspunkt)
5. [Datenmodelle & Typsystem](#kapitel-5-datenmodelle--typsystem)
6. [Der Befehls- und Tool-Katalog](#kapitel-6-der-befehls--und-tool-katalog)
7. [Die Laufzeitumgebung (Runtime)](#kapitel-7-die-laufzeitumgebung-runtime)
8. [Die Query Engine](#kapitel-8-die-query-engine)
9. [Session-Management & Persistenz](#kapitel-9-session-management--persistenz)
10. [Setup, Bootstrap & Initialisierung](#kapitel-10-setup-bootstrap--initialisierung)
11. [Ausführungsschicht & Laufzeitmodi](#kapitel-11-ausführungsschicht--laufzeitmodi)
12. [Die Subsystem-Architektur](#kapitel-12-die-subsystem-architektur)
13. [Paritaetsprüfung & Qualitaetssicherung](#kapitel-13-paritaetsprüfung--qualitaetssicherung)
14. [Zusammenfassung & Ausblick](#kapitel-14-zusammenfassung-und-ausblick)

---


# Kapitel 1: Einführung und Hintergrundgeschichte

## 1.1 Was ist Claw Code?

Claw Code ist eine eigenständige Python-Reimplementierung der Agent-Harness-Architektur von Claude Code -- dem Kommandozeilen-Agentensystem von Anthropic. Das Projekt entstand nicht als akademische Übung, nicht als Prototyp und nicht als langsam gewachsenes Hobby. Es entstand in einer einzigen Nacht, unter Druck, mit dem Ziel, die Kernarchitektur eines der fortschrittlichsten KI-Agentensysteme der Welt in Python nachzubilden, bevor der Morgen anbrach.

Um den Kontext zu verstehen, muss man zunächst begreifen, was Claude Code überhaupt ist. Claude Code ist Anthropics offizielle Kommandozeilenschnittstelle für das Claude-Sprachmodell. Es handelt sich dabei nicht um ein einfaches Chat-Interface, sondern um ein vollständiges Agentensystem: eine sogenannte *Harness*, die Werkzeuge verdrahtet, Aufgaben orchestriert, Laufzeitkontext verwaltet, Berechtigungen prüft, Sessions persistiert und Prompts intelligent an die richtigen Befehle und Tools weiterleitet. Die Originalimplementierung ist in TypeScript geschrieben und umfasst ein komplexes Geflecht aus Subsystemen -- von der Bootstrap-Phase über die Tool-Ausführung bis hin zur Session-Verwaltung.

Claw Code bildet genau diese Architekturmuster nach. Es ist kein Fork, kein Copy-Paste, kein Wrapper um bestehenden Code. Es ist eine vollständige Neuimplementierung in Python, die die gleichen Designentscheidungen, die gleichen Schichtungen und die gleichen Orchestrierungsmuster verwendet -- aber auf einer völlig anderen Codebasis aufbaut. Das Projekt verwendet ausschließlich die Python-Standardbibliothek und hat null externe Abhängigkeiten.

In Zahlen ausgedruckt umfasst Claw Code zum Zeitpunkt der Veröffentlichung:

- **66 Python-Dateien** im Quellverzeichnis `src/`
- **207 gespiegelte Befehle** aus dem archivierten TypeScript-Original
- **184 gespiegelte Tools** aus dem archivierten TypeScript-Original
- **30 Subsystem-Pakete**, die die Verzeichnisstruktur des Originals widerspiegeln
- **24 CLI-Befehle**, die über `python3 -m src.main` aufrufbar sind
- **0 externe Abhängigkeiten** -- alles lauft mit der Python-Standardbibliothek

Diese Zahlen sind nicht willkürlich. Sie spiegeln eine bewusste Entscheidung wider: Das Ziel war nicht, ein minimales Proof-of-Concept zu bauen, sondern die volle Oberfläche des Originalsystems in Python abzubilden -- jeden Befehl, jedes Tool, jedes Subsystem. Die 207 Befehle und 184 Tools sind als JSON-Snapshots in `src/reference_data/` gespeichert und werden zur Laufzeit geladen, katalogisiert und für Routing-Entscheidungen herangezogen.

## 1.2 Die Nacht, in der alles begann

Am 31. März 2026, um 4 Uhr morgens, würde Sigrid Jin -- der Autor dieses Projekts -- von einer Flut an Benachrichtigungen auf dem Handy geweckt. Der Claude-Code-Quellcode war offengelegt worden. Nicht durch eine offizielle Veröffentlichung, nicht durch ein geplantes Open-Source-Release, sondern durch ein Leak. Die gesamte Entwickler-Community war in Aufruhr.

Die Situation war zweischneidig. Einerseits lag nun erstmals die vollständige Architektur eines der leistungsfähigsten KI-Agentensysteme offen. Für jeden, der sich für Harness-Engineering interessiert -- also für die Frage, wie Agentensysteme Werkzeuge verdrahten, Aufgaben steuern und ihren Laufzeitkontext verwalten --, war dies ein beispielloser Einblick. Andererseits war der Code proprietar. Ihn einfach zu besitzen, geschweige denn zu verwenden oder weiterzuverbreiten, warf sofort rechtliche Fragen auf.

Jins Freundin in Korea machte sich ernsthaft Sorgen. Die bloße Tatsache, dass der Code auf seinem Rechner lag, könnte rechtliche Schritte von Anthropic nach sich ziehen. Also traf Jin eine Entscheidung, die viele Ingenieure unter Druck treffen würden, wenn sie zugleich fasziniert und beunruhigt sind: Er setzte sich hin, studierte die Architektur -- nicht den Code selbst, sondern die Muster, die Schichten, die Verdrahtung --, und begann, das Ganze von Grund auf in Python nachzubauen.

Die Portierungssitzung dauerte die gesamte Nacht. Vom ersten Lesen der Harness-Struktur über das Entwerfen des Python-Verzeichnisbaums bis hin zum Schreiben der ersten Tests würde alles in einem einzigen, durchgehenden Sprint erledigt. Bevor die Sonne aufging, war der erste funktionsfähige Python-Rewrite auf GitHub gepusht.

Dieses Tempo ware ohne ein entscheidendes Werkzeug nicht möglich gewesen: oh-my-codex.

## 1.3 Die Rolle von oh-my-codex (OmX)

oh-my-codex -- kurz OmX -- ist eine Workflow-Orchestrierungsschicht, die von Yeachan Heo (bekannt als `@bellman_ych` auf X) entwickelt würde. OmX baut auf OpenAIs Codex auf und bietet eine Infrastruktur für koordinierte, parallele und persistente KI-gestutzte Entwicklungsworkflows. Für die Claw-Code-Portierung war OmX nicht nur ein nützliches Hilfsmittel -- es war das Rückgrat des gesamten Prozesses.

Zwei OmX-Modi waren dabei entscheidend:

### Der `$team`-Modus: Paralleles Code-Review

Der `$team`-Modus erlaubt es, mehrere KI-Agenten gleichzeitig auf denselben Code anzusetzen -- für paralleles Review, architektonisches Feedback und Qualitätskontrolle. Wahrend der Portierungsnacht bedeutete dies, dass Jin nicht allein gegen die Uhr arbeitete. Mehrere Agenten könnten gleichzeitig die entstehende Python-Struktur auf Konsistenz, Vollständigkeit und architektonische Korrektheit prüfen.

Stellen Sie sich vor: Ein Agent uberprüft, ob die Befehlskatalog-Spiegelung vollständig ist. Ein zweiter Agent verifiziert, ob die Tool-Registrierung korrekt funktioniert. Ein dritter Agent prüft, ob die Session-Persistenz den gleichen Lebenszyklus wie das Original abbildet. All dies geschieht parallel, koordiniert durch OmX, wahrend der Hauptentwickler die nächste Komponente schreibt.

### Der `$ralph`-Modus: Persistente Ausführungsschleifen

Der `$ralph`-Modus geht noch einen Schritt weiter. Er bietet persistente Ausführungsschleifen mit Architektur-Level-Verifikation. Das bedeutet: Ein Agent lauft nicht einmal und gibt ein Ergebnis zuruck, sondern bleibt aktiv, fuhrt wiederholt Tests aus, uberprüft die Ergebnisse und meldet Abweichungen. Für die Claw-Code-Portierung war dies unerlasslich. Der `$ralph`-Modus stellte sicher, dass jede neu geschriebene Python-Datei nicht nur syntaktisch korrekt war, sondern architektonisch in das Gesamtbild passte.

Die gesamte Portierungssitzung -- vom Lesen der ursprünglichen Harness-Struktur bis zur Erstellung eines funktionierenden Python-Verzeichnisbaums mit Tests -- würde durch OmX-Orchestrierung gesteuert. Jin arbeitet heute aktiv mit Yeachan Heo zusammen, dem Schopfer von OmX, um das Projekt weiterzuentwickeln.

## 1.4 Sigrid Jin und die 25 Milliarden Token

Wer ist die Person hinter Claw Code? Um das zu verstehen, lohnt sich ein Blick auf einen Artikel, der am 21. März 2026 im Wall Street Journal erschien -- zehn Tage vor der Portierungsnacht. Der Artikel trug den Titel *"The Trillion Dollar Race to Automate Our Entire Lives"* und beschaftigte sich mit der wachsenden Gemeinschaft von Power-Usern, die KI-Agentensysteme wie Claude Code an ihre Grenzen treiben.

Sigrid Jin würde darin als eine der aktivsten Nutzerinnen und Nutzer hervorgehoben:

> Die KI-Startup-Mitarbeiterin Sigrid Jin, die am Dinner in Seoul teilnahm, hat im vergangenen Jahr im Alleingang 25 Milliarden Claude-Code-Token verbraucht. Damals waren die Nutzungsgrenzen lockerer, sodass fruhe Enthusiasten bei sehr niedrigen Kosten Dutzende von Milliarden Token erreichen könnten.

25 Milliarden Token. Diese Zahl ist nicht nur beeindruckend in ihrer Große -- sie ist ein Indikator für die Tiefe der Auseinandersetzung mit dem System. Wer so viele Token verbraucht, experimentiert nicht gelegentlich. Er oder sie lebt in dem System, versteht seine Grenzen, kennt seine Schwachen und weiß, wo die Architektur unter Belastung nachgibt.

Der Artikel machte auch deutlich, dass Jin kein dogmatischer Anhanger eines einzelnen KI-Labors ist. Die verschiedenen verfügbaren Werkzeuge -- Claude Code, Codex und andere -- haben unterschiedliche Starken und Schwachen. Codex sei besser im logischen Denken, wahrend Claude Code saubereren, besser teilbaren Code generiere. Diese pragmatische Haltung -- das beste Werkzeug für die jeweilige Aufgabe wahlen, anstatt einem einzigen Anbieter treu zu bleiben -- spiegelt sich auch in der Architektur von Claw Code wider, das zwar Claude Codes Strukturen nachbildet, aber bewusst als unabhängiges, anbieterungebundenes Python-Projekt konzipiert ist.

Im Februar 2026 flog Jin nach San Francisco zur ersten Geburtstagsfeier von Claude Code, wo die Teilnehmer Schlange standen, um sich mit dem Entwicklerteam auszutauschen. Unter den Gasten waren ein praktizierender Kardiologe aus Belgien, der eine App zur Patientennavigation entwickelt hatte, und ein kalifornischer Anwalt, der Baugenehmigungen automatisierte. Jin beschrieb die Veranstaltung als eine "Sharing-Party": Anwalte, Arzte, Zahnarzte -- Menschen ohne Software-Engineering-Hintergrund, die KI-Agenten als Werkzeug für ihre eigenen Fachgebiete nutzten.

Diese Erfahrung -- die Beobachtung, dass KI-Agentensysteme längst über die Grenzen der traditionellen Softwareentwicklung hinausgewachsen sind -- ist ein wesentlicher Antrieb hinter Claw Code. Das Projekt zielt nicht nur darauf ab, eine technische Referenzimplementierung zu schaffen, sondern auch darauf, die zugrundeliegenden Architekturmuster für eine breitere Gemeinschaft zuganglich zu machen.

## 1.5 Der Clean-Room-Ansatz

Ein zentrales Prinzip von Claw Code ist der sogenannte Clean-Room-Ansatz. Dieser Begriff stammt ursprünglich aus der Halbleiterindustrie und bezeichnet ein Verfahren, bei dem ein Produkt nachgebaut wird, ohne den Originalquellcode direkt zu verwenden. Stattdessen studiert man die Architektur, die Schnittstellen und das Verhalten des Originals und implementiert dann alles von Grund auf neu.

Für Claw Code bedeutet dies konkret:

1. **Architekturmuster nachbilden, nicht Code kopieren.** Die Python-Implementierung spiegelt die Schichtung des Originals wider -- Bootstrap-Phase, Tool-Verdrahtung, Prompt-Routing, Session-Management --, aber der eigentliche Quellcode ist vollständig neu geschrieben.

2. **JSON-Snapshots als Referenzdaten.** Die 207 Befehle und 184 Tools des Originals sind als JSON-Dateien in `src/reference_data/` erfasst. Diese Snapshots enthalten Name, Quellhinweis und Verantwortlichkeit jedes Befehls und Tools, aber keinen ausführbaren Code aus dem Original. Sie dienen als Metadaten-Katalog, nicht als Code-Duplizierung.

3. **Eigenständige Datenmodelle.** Die Datenklassen in `models.py` -- `Subsystem`, `PortingModule`, `PortingBacklog`, `UsageSummary`, `PermissionDenial` -- sind eigenständige Python-Definitionen, die auf `dataclasses` aufbauen. Sie modellieren die gleichen Konzepte wie das Original, aber mit einer idiomatischen Python-API.

4. **Keine externen Abhängigkeiten.** Das gesamte Projekt lauft ausschließlich mit der Python-Standardbibliothek. Es werden `json`, `argparse`, `dataclasses`, `pathlib`, `uuid`, `platform`, `sys`, `functools` und `collections` verwendet -- alles Module, die in jeder Standard-Python-Installation verfügbar sind. Keine `pip install`-Schritte, keine Drittanbieter-Bibliotheken, keine versteckten Abhängigkeiten.

5. **Rechtliche und ethische Sauberkeit.** Jin hat sich intensiv mit den rechtlichen und ethischen Fragen rund um die Nutzung des offengelegten Codes beschaftigt. Das Repository enthalt sogar einen ausführlichen Essay mit dem Titel *"Is Legal the Same as Legitimate? AI Reimplementation and the Erosion of Copyleft"*, der diese Fragen aus verschiedenen Perspektiven beleuchtet. Der offengelegte Snapshot ist nicht mehr Teil des nachverfolgten Repository-Zustands. Das Projekt konzentriert sich ausschließlich auf die Python-Portierungsarbeit.

Dieser Clean-Room-Ansatz ist nicht nur eine juristische Absicherung. Er zwingt den Entwickler dazu, jede Architekturentscheidung bewusst zu treffen, anstatt sie blind aus dem Original zu ubernehmen. Das Ergebnis ist ein Projekt, das die gleichen Muster verwendet, aber aus eigenem Verstandnis heraus gebaut würde -- und dadurch oft klarer und lesbarer ist als das Original.

## 1.6 Zusammenfassung

Claw Code ist mehr als eine Portierung. Es ist eine Fallstudie in Harness-Engineering: die Kunst, KI-Agenten nicht nur zu bauen, sondern sie richtig zu verdrahten. Es zeigt, wie ein erfahrener Praktiker -- gewappnet mit 25 Milliarden Token Erfahrung, einem OmX-Orchestrierungssystem und einer einzigen Nacht -- die Kernarchitektur eines der fortschrittlichsten KI-Agentensysteme der Welt in Python nachbilden kann, ohne eine einzige Zeile proprietaren Codes zu kopieren.

In den folgenden Kapiteln werden wir jede Schicht dieser Architektur im Detail untersuchen: die Spiegelungsschicht mit ihren JSON-Snapshots, die Orchestrierungsschicht mit Prompt-Routing und Session-Management, die Infrastrukturschicht mit Setup, Permissions und Persistenz, und schließlich die 30 Subsysteme, die das Gesamtbild abrunden.



# Kapitel 2: Ethik und Recht der KI-Reimplementierung

## 2.1 Einleitung: Wenn Maschinen den Code neu schreiben

Am 9. Maerz 2026 veröffentlichte der suedkoreanische Softwareentwickler und Open-Source-Aktivist Hong Minhee einen Essay, der in der Entwicklergemeinde sofort für heftige Diskussionen sorgte. Der Titel -- *Is Legal the Same as Legitimate: AI Reimplementation and the Erosion of Copyleft* -- stellte eine Frage, die weit über den konkreten Anlass hinausreicht: Ist das, was rechtlich zulässig ist, auch das, was sozial und ethisch vertretbar ist? Hong Minhees Text nimmt einen einzelnen Vorfall zum Ausgangspunkt -- die KI-gestützte Neuimplementierung einer weit verbreiteten Python-Bibliothek -- und entfaltet daraus eine grundsaetzliche Kritik an der Art und Weise, wie die Open-Source-Welt mit dem Aufkommen generativer KI-Systeme umgeht.

Für das vorliegende Buch ist dieser Essay von besonderer Bedeutung, weil das Claw-Code-Projekt selbst exakt in dem Spannungsfeld operiert, das Hong Minhee beschreibt. Claw Code ist eine Reimplementierung der Claude-Code-Agent-Harness-Architektur -- zunächst in Python, später in Rust -- die entstand, nachdem der Claude-Code-Quellcode am 31. Maerz 2026 offengelegt würde. Die Frage, ob eine solche Reimplementierung rechtlich zulässig, ethisch vertretbar und sozial legitim ist, betrifft dieses Projekt unmittelbar. Dieses Kapitel unternimmt daher den Versuch, Hong Minhees Argumentation ausführlich darzustellen, kritisch zu würdigen und auf die spezifische Situation von Claw Code anzuwenden.

## 2.2 Der Fall chardet: Anatomie eines Lizenzwechsels

### 2.2.1 Was geschah

Dan Blanchard, der Maintainer von chardet -- einer Python-Bibliothek zur Erkennung von Textcodierungen, die von rund 130 Millionen Projekten pro Monat heruntergeladen wird -- veröffentlichte Anfang Maerz 2026 die Version 7.0 seiner Bibliothek. Diese Version war 48-mal schneller als ihr Vorgaenger, unterstützte Mehrkernverarbeitung und würde von Grund auf neu entworfen. In der Liste der Mitwirkenden tauchte ein ungewoehnlicher Name auf: Anthropics Claude. Die Lizenz hatte sich von der LGPL (GNU Lesser General Public License) zur MIT-Lizenz geändert.

Blanchards Darstellung: Er habe den bestehenden Quellcode nicht direkt eingesehen. Stattdessen habe er nur die API-Spezifikation und die Testsuite an Claude übergeben und das KI-System gebeten, die Bibliothek von Grund auf neu zu implementieren. Der resultierende Code weise laut einer JPlag-Analyse weniger als 1,3 Prozent Ähnlichkeit mit jeder frueheren Version auf. Sein Schluss: Es handele sich um ein eigenständiges neues Werk, und er sei nicht verpflichtet, die LGPL weiterzuführen.

Mark Pilgrim, der urspruengliche Autor der Bibliothek, widersprach öffentlich über ein GitHub-Issue. Die LGPL verlange, dass Modifikationen unter derselben Lizenz verteilt werden. Eine Reimplementierung, die mit umfassender Kenntnis der bestehenden Codebasis erstellt würde, koenne nach Pilgrims Auffassung nicht als Clean-Room-Implementierung gelten.

### 2.2.2 Warum dieser Fall paradigmatisch ist

Der chardet-Fall verdichtet mehrere Entwicklungen, die einzeln betrachtet schon bedeutsam wären, in ihrer Kombination aber eine qualitätiv neue Situation schaffen:

Erstens die *Geschwindigkeit*: Was frueher Monate oder Jahre manueller Programmierarbeit erfordert hätte, geschah innerhalb von Stunden oder Tagen. Die Reimplementierung einer Bibliothek mit 130 Millionen monatlichen Downloads ist kein theoretisches Szenario mehr, sondern ein praktisch demonstrierter Vorgang.

Zweitens die *Skalierbarkeit*: Wenn eine einzelne Person mit Hilfe eines KI-Systems eine so weit verbreitete Bibliothek reimplementieren kann, dann ist dies grundsaetzlich für jede Copyleft-geschuetzte Software möglich. Die Kosten der Reimplementierung, die bisher ein praktisches Hindernis für die Umgehung von Copyleft darstellten, sind dramatisch gesunken.

Drittens die *rechtliche Grauzone*: Die Frage, ob eine KI-gestützte Reimplementierung als abgeleitetes Werk im Sinne des Urheberrechts gilt, ist juristisch ungeklaert. Die niedrige JPlag-Ähnlichkeit liefert ein quantitatives Argument für die Eigenständigkeit des neuen Werks, aber quantitative Ähnlichkeitsmasse erfassen nicht notwendigerweise die Übernahme von Architekturentscheidungen, algorithmischen Strategien oder Testlogik.

Viertens die *Lizenzrichtung*: Der Wechsel von LGPL zu MIT bedeutet, dass nachfolgende abgeleitete Werke nicht mehr verpflichtet sind, ihren Quellcode offenzulegen. Eine Verpflichtung, die für eine Bibliothek mit 130 Millionen monatlichen Downloads galt, ist mit einem Schlag entfallen.

## 2.3 Die GNU-Analogie und warum sie in die falsche Richtung zeigt

### 2.3.1 Das Argument von Antirez

Salvatore Sanfilippo, besser bekannt als Antirez und Schoepfer von Redis, veröffentlichte eine ausführliche Verteidigung der KI-Reimplementierung. Sein zentrales Argument stützt sich auf historische Präzedenz: Als das GNU-Projekt den UNIX-Userspace reimplementierte, war dies rechtmäßig. Ebenso Linux. Das Urheberrecht schuetze konkrete Ausdrücke -- den tatsaechlichen Code, seine Struktur, seine spezifischen Mechanismen --, nicht aber Ideen oder Verhaltensweisen. KI-gestützte Reimplementierung bewege sich auf demselben rechtlichen Boden. Folglich sei sie rechtmäßig.

### 2.3.2 Hong Minhees Gegenargument: Die Richtung des Vektors

Hong Minhee bestreitet die juristische Analyse nicht. Was er bestreitet, ist der Sprung von der juristischen zur sozialen Schlussfolgerung -- und er tut dies mit einem eleganten argumentativen Maneuver: Er nimmt die GNU-Analogie ernst und zeigt, dass sie das Gegenteil dessen belegt, was Antirez beabsichtigt.

Als GNU den UNIX-Userspace reimplementierte, verlief der Vektor von proprietary zu frei. Stallman nutzte die Grenzen des Urheberrechts, um proprietaere Software in freie Software zu verwandeln. Die ethische Kraft dieses Projekts kam nicht aus seiner rechtlichen Zulässigkeit -- sie kam aus der Richtung, in die es sich bewegte: Es erweiterte die Allmende (Commons).

Im chardet-Fall verläuft der Vektor in die entgegengesetzte Richtung. Software, die durch eine Copyleft-Lizenz geschuetzt war -- eine Lizenz, die Nutzern das Recht garantiert, abgeleitete Werke unter denselben Bedingungen zu studieren, zu modifizieren und weiterzugeben --, würde unter einer permissiven Lizenz reimplementiert, die keine solche Garantie enthält. Dies ist keine Reimplementierung, die die Allmende erweitert. Es ist eine, die den Zaun entfernt, der die Allmende schuetzte.

Hong Minhees Formulierung ist präzise: Antirez beruft sich auf den GNU-Präzedenzfall, aber dieser Präzedenzfall ist ein Gegenbeispiel zu seiner Schlussfolgerung, kein stützendes.

### 2.3.3 Bewertung der Vektorargumentation

Die Stärke von Hong Minhees Argument liegt in seiner strukturellen Klarheit. Er bestreitet nicht die formale Analogie -- ja, beides sind Reimplementierungen -- sondern zeigt, dass die formale Analogie den entscheidenden Unterschied verdeckt: die Richtung des ethischen Transfers.

Man könnte einwenden, dass die Richtung des Vektors eine Frage des Standpunkts ist. Aus der Perspektive eines Entwicklers, der chardet in einem MIT-lizenzierten Projekt verwenden möchte, verläuft der Vektor ebenfalls von restriktiv zu frei. Aber dieses Argument verwechselt individuelle Bequemlichkeit mit kollektiver Freiheit. Die LGPL schuetzt nicht die Freiheit des einzelnen Entwicklers, mit Code zu tun, was er will, sondern die Freiheit aller Nutzer, den Code und seine Ableitungen inspizieren und modifizieren zu koennen. Wenn diese Garantie entfaellt, sind es langfristig gerade die Nutzer ohne eigene Entwicklungsressourcen, die den Schaden tragen.

## 2.4 Die Illusion der "freundlicheren" permissiven Lizenz

### 2.4.1 Ronachers Position

Armin Ronacher, der Schoepfer von Flask, begruesste die Relizenzierung ausdrücklich. Er legte offen, dass er ein persoenliches Interesse am Ergebnis hat: Er habe selbst seit Jahren gewünscht, dass chardet unter einer Nicht-GPL-Lizenz stehe. Er betrachte die GPL als einen Widerspruch zum Geist des Teilens, weil sie einschraenke, was mit Code getan werden koenne.

### 2.4.2 Was die GPL tatsaechlich verbietet -- und was nicht

Hong Minhee weist darauf hin, dass Ronachers Behauptung auf einem grundlegenden Missverstaendnis der GPL beruht.

Die GPL verbietet nicht, Quellcode privat zu halten. Sie erlegt keinerlei Beschraenkungen für die private Modifikation und Nutzung von GPL-Software auf. Die Bedingungen der GPL werden erst durch die Distribution ausgelöst. Wer modifizierten Code verteilt oder als Netzwerkdienst anbietet, muss den Quellcode unter denselben Bedingungen zur Verfügung stellen.

Dies ist keine Einschraenkung des Teilens. Es ist eine Bedingung, die an das Teilen geknuepft wird: Wenn du teilst, musst du gleichartig teilen. Die Anforderung, Verbesserungen an die Allmende zurückzugeben, ist kein Mechanismus, der das Teilen unterdrückt -- es ist ein Mechanismus, der das Teilen rekursiv und selbstverstärkend macht.

Der Kontrast mit der MIT-Lizenz verdeutlicht den Punkt: Unter MIT darf jeder Code nehmen, verbessern und in ein proprietaeres Produkt einschließen. Man kann von der Allmende empfangen, ohne etwas zurückzugeben. Wenn Ronacher diese Struktur als "teilfreundlicher" bezeichnet, verwendet er einen Begriff des Teilens mit einer eingebauten Richtung: Teilen fliesst in Richtung derjenigen, die über mehr Kapital und mehr Ingenieure verfügen, um davon zu profitieren.

### 2.4.3 Das historische Zeugnis

Hong Minhee stützt seine Argumentation mit einem historischen Verweis: In den 1990er Jahren absorbierten Unternehmen routinemäßig GPL-Code in proprietaere Produkte -- nicht weil sie permissive Lizenzen gewählt hatten, sondern weil die Copyleft-Durchsetzung lasch war. Die Staerkung der Copyleft-Mechanismen schloss diese Luecke. Für einzelne Entwickler und kleine Projekte ohne die Ressourcen, auf etwas anderem als Reziprozitaet zu konkurrieren, war Copyleft das, was den Austausch annähernd fair machte.

Dieser historische Punkt ist für die Bewertung des chardet-Falls wesentlich. Die LGPL war nicht ein willkuerlich gewahltes Detail, sondern der Mechanismus, der sicherstellte, dass Beitraege zur Bibliothek nicht in proprietaeren Produkten verschwanden, ohne dass die Nutzer Zugang zum verbesserten Code erhielten.

### 2.4.4 Das sich selbst widerlegende Beispiel

Das vielleicht scharfsinnigste Stück in Hong Minhees Essay ist seine Analyse eines Details, das Ronacher beilaeufig erwähnt: Vercel reimplementierte GNU Bash mit Hilfe von KI und veröffentlichte das Ergebnis. Anschließend reagierte Vercel sichtbar verärgert, als Cloudflare Next.js auf dieselbe Weise reimplementierte.

Next.js steht unter der MIT-Lizenz. Cloudflares vinext verletzte keine Lizenz -- es tat genau das, was Ronacher als Beitrag zur Kultur der Offenheit bezeichnet, angewandt auf eine permissiv lizenzierte Codebasis. Vercels Reaktion hatte nichts mit Lizenzverletzung zu tun; sie war rein kompetitiv und territorial.

Die implizite Position lautet: Die Reimplementierung von GPL-Software als MIT ist ein Sieg für das Teilen, aber die Reimplementierung der eigenen MIT-Software durch einen Wettbewerber ist ein Grund für Empoerung. So sieht die Behauptung, permissive Lizenzierung sei "teilfreundlicher" als Copyleft, in der Praxis aus. Der Geist des Teilens fliesst, wie sich herausstellt, nur in eine Richtung: von einem selbst nach außen.

Hong Minhees Beobachtung dazu ist schneidend: Wenn man Belege prasentiert, die gegen die eigene Position sprechen, sie anerkennt und dann unverändert zur urspruenglichen Schlussfolgerung übergeht, dann ist das ein Signal, dass die Schlussfolgerung dem Argument vorausging.

## 2.5 Rechtliche Zulässigkeit versus soziale Legitimitaet

### 2.5.1 Die zentrale Unterscheidung

Hong Minhees Essay kulminiert in einer Unterscheidung, die für die gesamte Debatte um KI-Reimplementierung grundlegend ist: Recht setzt eine Untergrenze. Diese Untergrenze zu überschreiten, bedeutet nicht, dass das Verhalten richtig ist.

Beide -- Antirez und Ronacher -- behandeln die rechtliche Zulässigkeit als Stellvertreter für soziale Legitimitaet. Antirez schließt seine sorgfaeltige juristische Analyse ab, als ob sie die Angelegenheit erledige. Ronacher raeumt ein, dass "hier eine offensichtliche moralische Frage steht, die mich aber nicht notwendigerweise interessiert". Beide behandeln die juristische Zulässigkeit als ausreichende Bedingung. Aber das Recht sagt nur, welches Verhalten es nicht verhindern wird -- es zertifiziert dieses Verhalten nicht als richtig.

Hong Minhee zieht Parallelen: Aggressive Steuerminimierung, die nie in die Illegalitaet abgleitet, kann dennoch weithin als unsozial betrachtet werden. Ein Pharmaunternehmen, das legal ein Patent auf ein längst generisches Medikament erwirbt und den Preis verhundertfacht, hat etwas Legales getan, aber das macht es nicht in Ordnung. Legalitaet ist eine notwendige Bedingung; sie ist keine hinreichende.

### 2.5.2 Der Bruch des sozialen Pakts

Im chardet-Fall ist die Unterscheidung noch schärfer. Was die LGPL schuetzte, war nicht allein Blanchards Arbeit. Es war ein sozialer Pakt, dem alle zugestimmt hatten, die über zwoelf Jahre zur Bibliothek beigetragen haben. Die Bedingungen dieses Pakts lauteten: Wenn du dies nimmst und darauf aufbaust, teilst du unter denselben Bedingungen zurück.

Dieser Pakt funktionierte als rechtliches Instrument, aber er war auch die Vertrauensgrundlage, die Beitraege rational machte. Die Tatsache, dass eine Reimplementierung rechtlich als neues Werk gelten könnte, und die Tatsache, dass sie den Vertrauensbruch gegenüber den urspruenglichen Mitwirkenden darstellt, sind getrennte Fragen. Wenn ein Gericht schließlich zugunsten von Blanchard entscheidet, sagt dieses Urteil uns, was das Recht erlaubt. Es sagt uns nicht, dass die Handlung richtig war.

Zoe Kooyman, Geschaeftsfuehrerin der Free Software Foundation, brachte es auf den Punkt: "Sich zu weigern, anderen die Rechte zu gewähren, die man selbst als Nutzer erhalten hat, ist hochgradig unsozial, unabhängig davon, welche Methode man dafür verwendet."

### 2.5.3 Das Positionsproblem

Hong Minhee stellt eine Frage, die in technischen Debatten selten gestellt wird: Von welcher Position aus argumentieren die Beteiligten?

Antirez schuf Redis. Ronacher schuf Flask. Beide sind Figuren im Zentrum des Open-Source-Ökosystems, mit großen Publikum und etabliertem Ruf. Für sie bedeuten sinkende Kosten der KI-Reimplementierung etwas Bestimmtes: Es wird einfacher, Dinge in einer anderen Form zu reimplementieren, die ihnen besser passt. Ronacher sagt ausdrücklich, er habe begonnen, GNU Readline gerade wegen seiner Copyleft-Bedingungen zu reimplementieren.

Für die Menschen, die jahrelang zu einer Bibliothek wie chardet beigetragen haben, bedeutet dieselbe Kostenverschiebung etwas völlig anderes: Der Copyleft-Schutz um ihre Beitraege kann entfernt werden.

Wenn positionelle Asymmetrie dieser Art ignoriert wird und das Argument als universelle Analyse präsentiert wird, erhält man nicht Analyse, sondern Rationalisierung. Beide Autoren gelangen zu Schlussfolgerungen, die präzise mit ihren eigenen Interessen übereinstimmen. Hong Minhee bittet die Leser, diesen Umstand im Hinterkopf zu behalten.

## 2.6 Was die Debatte für die Zukunft des Copyleft bedeutet

### 2.6.1 Bruce Perens und das Ende der alten Ökonomie

Bruce Perens, der die urspruengliche Open Source Definition schrieb, sagte gegenüber The Register: "Die gesamte Ökonomie der Softwareentwicklung ist tot, vorbei, erledigt, kaputt!" Er meinte es als Alarm. Antirez zieht aus einer ähnlichen Einschaetzung der Lage die Schlussfolgerung: Anpassen. Ronacher sagt, er finde die Richtung aufregend.

Hong Minhee stellt fest, dass keine der drei Reaktionen die zentrale Frage beantwortet: Wenn Copyleft technisch leichter zu umgehen wird, macht es das weniger notwendig -- oder notwendiger?

Seine Antwort: notwendiger. Was die GPL schuetzte, war nicht die Knappheit von Code, sondern die Freiheit der Nutzer. Die Tatsache, dass die Produktion von Code billiger geworden ist, macht es nicht akzeptabel, diesen Code als Vehikel für die Erosion von Freiheit zu verwenden. Wenn die Reibung der Reimplementierung verschwindet, verschwindet auch die Reibung des Abstreifens von Copyleft von allem, was exponiert bleibt.

### 2.6.2 Von der Trainings-Copyleft zur Spezifikations-Copyleft

Hong Minhee hatte in frueheren Schriften eine Trainings-Copyleft (TGPL) als nächsten Schritt in dieser Entwicklungslinie vorgeschlagen. Die chardet-Situation legt nahe, dass das Argument noch weiter gehen muss: zu einer Spezifikations-Copyleft, die die Ebene unterhalb des Quellcodes abdeckt.

Wenn Quellcode jetzt aus einer Spezifikation generiert werden kann, dann ist die Spezifikation der Ort, an dem der wesentliche intellektuelle Gehalt eines GPL-Projekts residiert. Blanchards eigene Behauptung -- dass er nur von der Testsuite und der API aus gearbeitet hat, ohne den Quellcode zu lesen -- ist, paradoxerweise, ein Argument dafür, diese Testsuite und API-Spezifikation unter Copyleft-Bedingungen zu schuetzen.

Die Geschichte der GPL ist die Geschichte von Lizenzwerkzeugen, die sich als Reaktion auf neue Formen der Ausbeutung weiterentwickeln: GPLv2 zu GPLv3, dann AGPL. Was jede Evolution antrieb, war nicht ein Gerichtsurteil, sondern eine Gemeinschaft, die zuerst ein Werturteil faellte und dann nach rechtlichen Instrumenten suchte, um es auszudrücken. Dieselbe Sequenz ist jetzt verfügbar.

## 2.7 Claw Code im Spiegel der Debatte

### 2.7.1 Die Parallele

Nun wenden wir den Blick auf das Projekt, das dieses Buch dokumentiert. Claw Code entstand, nachdem der Claude-Code-Quellcode am 31. Maerz 2026 offengelegt würde. Die Projektbeschreibung im README ist ausdrücklich: Der Schoepfer, Sigrid Jin, setzte sich hin, portierte die Kernfunktionen von Grund auf nach Python und pushte alles, bevor die Sonne aufging. Die Arbeit würde mit oh-my-codex (OmX) orchestriert, einer Workflow-Schicht auf Basis von OpenAIs Codex. Das Ergebnis wird als "sauberer Python-Rewrite, der die Architekturmuster von Claude Codes Agent-Harness erfasst, ohne proprietaeren Quellcode zu kopieren" beschrieben.

Die strukturelle Parallele zum chardet-Fall ist offensichtlich: Ein bestehendes Softwaresystem wird mit KI-Unterstützung reimplementiert. Die Hintergrundgeschichte des Projekts erwähnt ausdrücklich die Sorge vor rechtlichen Schritten seitens Anthropic. Die Lösung bestand darin, eine eigenständige Implementierung zu schaffen, die sich auf Architekturmuster stützt, nicht auf kopierten Code.

### 2.7.2 Die Unterschiede

Es gibt jedoch wesentliche Unterschiede zum chardet-Fall, und sie verdienen eine ehrliche Analyse:

*Die Ausgangssituation*: chardet war eine Open-Source-Bibliothek unter einer Copyleft-Lizenz. Claude Code war proprietaere Software, deren Quellcode unbeabsichtigt offengelegt würde. Der ethische Vektor ist hier ein anderer: Die Reimplementierung eines proprietaeren Systems als Open-Source-Projekt verläuft -- in Hong Minhees Terminologie -- von proprietary zu frei. Das ist strukturell näher an der GNU-Analogie als am chardet-Fall.

*Die Lizenzfrage*: Bei chardet ging es um den Wechsel von Copyleft zu permissiv innerhalb des Open-Source-Ökosystems. Bei Claw Code geht es um die Frage, ob die Reimplementierung proprietaerer Architekturmuster überhaupt zulässig ist. Das ist eine andere rechtliche und ethische Frage.

*Die Motivation*: Blanchard reimplementierte eine bestehende Open-Source-Bibliothek, die er selbst betreute, und änderte deren Lizenz. Claw Code entstand als Reaktion auf eine unbeabsichtigte Offenlegung, mit dem erklaeerten Ziel, die Architekturmuster zu verstehen und nachzubauen, nicht aber den proprietaeren Code zu kopieren.

### 2.7.3 Die bleibenden Fragen

Trotz der Unterschiede wirft die Existenz von Claw Code Fragen auf, die Hong Minhees Analyse direkt betreffen:

*Wo verläuft die Grenze zwischen Architekturmuster und geschuetztem Ausdruck?* Das Claw-Code-Projekt betont wiederholt, dass es Architekturmuster nachbildet, nicht Code kopiert. Aber Architekturmuster -- die Organisation in Subsysteme, die Bootstrap-Phasen, die Tool-Verdrahtung, das Trust-Gating-Modell -- sind das Ergebnis erheblicher intellektueller Arbeit. Hong Minhees Argument für eine Spezifikations-Copyleft legt nahe, dass genau diese Ebene -- die Architektur, die API, die Testsuite -- der Ort ist, an dem der wesentliche intellektuelle Gehalt residiert.

*Ist die Verwendung von KI-Systemen für die Reimplementierung eine relevante Tatsache?* Blanchards Verteidigung beruhte darauf, dass er den Code nicht direkt eingesehen habe, sondern nur die API und die Testsuite an Claude übergeben habe. Die Claw-Code-Hintergrundgeschichte beschreibt einen ähnlichen Prozess: Lesen der urspruenglichen Harness-Struktur, dann Erstellung eines Python-Verzeichnisbaums mit Tests, gesteuert durch KI-Orchestrierung. Die Frage, ob ein KI-System als Filter zwischen dem Original und der Reimplementierung fungieren kann, der die rechtliche Verantwortung des Entwicklers mindert, ist dieselbe Frage, die im chardet-Fall gestellt wird.

*Wem gehört die Architektur?* Das Claw-Code-README enthält einen ausdrücklichen Haftungsausschluss: "Dieses Repository erhebt keinen Anspruch auf das Eigentum am urspruenglichen Claude-Code-Quellmaterial." Aber es stellt auch fest, dass es eine Python-Nachbildung der Architekturmuster ist, die einen Befehls- und Tool-Katalog mit rund 150 Befehlen und 100 Tools spiegelt. Die Frage, wie viel Architektur man nachbilden kann, bevor die Nachbildung selbst zu einem abgeleiteten Werk wird, ist genau die Frage, die Hong Minhee als zentral identifiziert.

### 2.7.4 Das Verhältnis zur Allmende

Es gibt einen Aspekt, in dem Claw Code sich positiv von chardet 7.0 unterscheidet: Es fuegt der Allmende hinzu. Wo Blanchard eine Copyleft-Lizenz durch eine permissive ersetzte und damit den Schutz der Allmende verringerte, schafft Claw Code ein neues Open-Source-Projekt, das vorher nicht existierte. Das proprietaere Claude Code würde nicht entlizenziert; es würde reimplementiert und als Open Source veröffentlicht.

Allerdings ist auch diese Einschaetzung nicht unkompliziert. Die Reimplementierung stützt sich auf Wissen, das aus der unbeabsichtigten Offenlegung proprietaeren Codes stammt. Der README formuliert das offen: "Ich habe die offengelegte Codebasis urspruenglich studiert, um das Harness, die Tool-Verdrahtung und den Agent-Workflow zu verstehen." Die Tatsache, dass der nachverfolgte Quellbaum jetzt nur die Python-Portierung enthält, ändert nichts daran, dass das Wissen, auf dem die Portierung beruht, aus der Einsicht in proprietaeren Code stammt.

## 2.8 Die tiefere Schicht: Werte, die keinem Urteil beduerfen

### 2.8.1 Gemeinschaftsnormen jenseits des Rechts

Hong Minhee schließt seinen Essay mit einer Beobachtung, die über den konkreten Fall hinausreicht: Recht wird langsam gemacht, im Nachhinein, und spiegelt bestehende Machtverhältnisse wider. Die Normen, die Open-Source-Gemeinschaften über Jahrzehnte aufgebaut haben, warteten nicht auf gerichtliche Genehmigung. Menschen wählten die GPL, als das Recht ihnen keine Garantie für deren Durchsetzung bot, weil sie die Werte der Gemeinschaften ausdrückte, denen sie angehören wollten.

Diese Beobachtung ist für jeden von Bedeutung, der im Bereich der KI-gestützten Softwareentwicklung arbeitet. Gerichte werden irgendwann über die Zulässigkeit von KI-Reimplementierungen entscheiden. Aber die Frage, die zuerst beantwortet werden muss, ist keine juristische, sondern eine soziale: Schulden diejenigen, die von der Allmende nehmen, etwas zurück?

Hong Minhees Antwort ist klar: Ja. Dieses Urteil benötigt keinen Gerichtsentscheid.

### 2.8.2 Was Antirez und Ronacher sichtbar machen

Der letzte Satz von Hong Minhees Essay verdient es, vollständig zitiert zu werden: "Was die Stücke von Antirez und Ronacher lesenswert macht, ist nicht, dass sie recht haben. Es ist, dass sie mit ungewoehnlicher Klarheit sichtbar machen, was sie sich entscheiden, nicht zu sehen. Wenn Legalitaet als Ersatz für ein Werturteil verwendet wird, wird die Frage, die tatsaechlich zählt, in den Fussnoten eines Rechts begraben, das sie bereits entwachsen hat."

Diese Kritik richtet sich nicht gegen die intellektuelle Redlichkeit der beiden Autoren -- Hong Minhee respektiert beide ausdrücklich. Sie richtet sich gegen eine Argumentationsstruktur, die in der Technologiebranche weit verbreitet ist: die Verwendung juristischer Zulässigkeit als Fluchtweg vor ethischer Verantwortung.

## 2.9 Schlussfolgerungen für die Praxis

### 2.9.1 Fünf Leitfragen für KI-Reimplementierungsprojekte

Aus Hong Minhees Analyse lassen sich fünf Fragen ableiten, die jedes KI-Reimplementierungsprojekt -- einschließlich Claw Code -- sich stellen sollte:

1. **Die Richtungsfrage**: In welche Richtung verläuft der Vektor? Von proprietary zu frei (Expansion der Allmende) oder von Copyleft zu permissiv (Erosion der Allmende)?

2. **Die Paktfrage**: Wird ein sozialer Pakt gebrochen, dem urspruengliche Mitwirkende zugestimmt haben? Haben Menschen unter bestimmten Lizenzerwartungen beigetragen, die nun unterlaufen werden?

3. **Die Positionsfrage**: Von welcher Position aus argumentiere ich? Profitiere ich selbst von der Kostenreduktion der Reimplementierung, während andere den Schaden tragen?

4. **Die Spezifikationsfrage**: Wenn ich behaupte, nur die Spezifikation und nicht den Code reimplementiert zu haben -- ist die Spezifikation selbst nicht der Ort, an dem der wesentliche intellektuelle Gehalt liegt?

5. **Die Zukunftsfrage**: Wenn mein Vorgehen zur Norm wird, welche Welt entsteht? Eine, in der Copyleft-geschuetzte Projekte systematisch in permissiv lizenzierte umgewandelt werden?

### 2.9.2 Was Claw Code richtig macht -- und wo Fragen offen bleiben

Claw Code macht einiges richtig im Sinne dieser Analyse: Es operiert in der Richtung proprietary zu frei. Es ist transparent über seine Herkunft. Es hält den urspruenglichen proprietaeren Code aus dem nachverfolgten Repository heraus. Es bietet einen Haftungsausschluss an.

Aber die offenen Fragen bleiben bestehen: Die Grenze zwischen Architekturmuster und geschuetztem Ausdruck ist ungeklaert. Die Rolle der KI als vermittelnde Schicht zwischen proprietaerem Original und Reimplementierung wirft dieselben Fragen auf wie im chardet-Fall. Und die Tatsache, dass das Projekt auf der Einsicht in unbeabsichtigt offengelegten proprietaeren Code beruht, fuegt eine zusätzliche ethische Dimension hinzu, die über Hong Minhees Analyse hinausgeht.

## 2.10 Ausblick

Die Debatte, die Hong Minhee angestoßen hat, wird nicht durch ein einzelnes Gerichtsurteil oder einen einzelnen Blogbeitrag gelöst werden. Sie ist Teil einer umfassenderen Neubewertung der Beziehung zwischen KI-Systemen, geistigem Eigentum und den sozialen Normen der Softwareentwicklung.

Für das Claw-Code-Projekt bedeutet dies, dass die technische Arbeit -- die Portierung, die Rust-Reimplementierung, die Paritaetsprüfungen -- nicht isoliert von diesen Fragen betrachtet werden kann. Jede technische Entscheidung ist auch eine ethische Entscheidung. Die Wahl der Lizenz, der Umgang mit dem offengelegten Quellmaterial, die Transparenz über die Herkunft des Wissens -- all dies sind Antworten auf die Frage, die Hong Minhee stellt.

Die nächsten Kapitel dieses Buches werden die technische Architektur von Claw Code im Detail untersuchen. Aber die Fragen, die in diesem Kapitel aufgeworfen würden, begleiten jede Codezeile. Denn wie Hong Minhee schreibt: Was immer Gerichte letztendlich über KI-Reimplementierung entscheiden, die Frage, die wir zuerst beantworten müssen, ist keine juristische. Es ist eine soziale. Schulden diejenigen, die von der Allmende nehmen, etwas zurück? Ich denke, ja. Dieses Urteil braucht keinen Richterspruch.

---

*Quellen für dieses Kapitel: Hong Minhee, "Is Legal the Same as Legitimate: AI Reimplementation and the Erosion of Copyleft", 9. Maerz 2026; Claw Code Repository (github.com/instructkr/claw-code), README.md und ANLEITUNG.md; die darin referenzierten Beitraege von Salvatore Sanfilippo (antirez) und Armin Ronacher sowie die Stellungnahmen von Zoe Kooyman (FSF) und Bruce Perens.*


# Kapitel 3: High-Level-Architektur

## 3.1 Einleitung und Leitgedanke

Die Architektur von Claw Code folgt einem klaren Gestaltungsprinzip: **Unveränderlichkeit nach außen, Zustandsverwaltung nach innen**. Das gesamte System ist als Drei-Schichten-Modell aufgebaut, bei dem jede Schicht eine eindeutig abgegrenzte Verantwortung tragt. Die unterste Schicht stellt Infrastruktur bereit -- Umgebungserkennung, Dateisystemkontext und Persistenz. Die mittlere Schicht orchestriert den eigentlichen Ablauf: Sie routet Benutzereingaben zu den passenden Befehlen und Werkzeugen, verwaltet Sessions und kontrolliert das Token-Budget. Die oberste Schicht -- die sogenannte Spiegelungsschicht -- ladt die archivierten Referenzdaten aus JSON-Snapshots und stellt sie als unveränderliche Python-Tupel bereit.

Dieses Kapitel beschreibt jede Schicht im Detail, stellt die Abhängigkeiten zwischen den Modulen dar und zeichnet den Datenfluss von der CLI-Eingabe bis zur formatierten Ausgabe nach. Drei ASCII-Diagramme veranschaulichen die Zusammenhange visuell.

## 3.2 Gesamtarchitektur im Überblick

Bevor wir die einzelnen Schichten im Detail betrachten, bietet das folgende Diagramm einen Gesamtüberblick über alle drei Schichten, die Querschnittsmodule und ihre Beziehungen zueinander:

**CLI-Einstiegspunkt: main.py** (argparse) -- `build_parser()` --> `main(argv)` --> Dispatch nach `args.command`

#### Schicht 1 -- Spiegelungsschicht (Mirror Layer)

| Modul | Beschreibung |
|-------|-------------|
| **commands.py** | SNAPSHOT_PATH --> `commands_snapshot.json` |
| | `load_command_snapshot()` mit `@lru_cache(maxsize=1)` |
| | PORTED_COMMANDS: tuple (207 PortingModule) |
| | `get_command(name)`, `get_commands(filter...)`, `find_commands(query)` |
| | `execute_command(name, p)`, `render_command_index()` |
| **tools.py** | SNAPSHOT_PATH --> `tools_snapshot.json` |
| | `load_tool_snapshot()` mit `@lru_cache(maxsize=1)` |
| | PORTED_TOOLS: tuple (184 PortingModule) |
| | `get_tool(name)`, `get_tools(filter...)`, `find_tools(query)` |
| | `execute_tool(name, payload)`, `render_tool_index()` |

#### Schicht 2 -- Orchestrierungsschicht

| Modul | Beschreibung |
|-------|-------------|
| **runtime.py** -- PortRuntime | `.route_prompt(prompt, limit)`, `.bootstrap_session(prompt)` |
| | `.run_turn_loop(prompt, ...)`, `._collect_matches(tokens, ...)` |
| | `._score(tokens, module)`, `._infer_permission_denials()` |
| | RuntimeSession (dataclass), RoutedMatch (dataclass) |
| **execution_registry.py** | ExecutionRegistry, MirroredCommand, MirroredTool |
| | `build_execution_registry()` |
| **query_engine.py** -- QueryEnginePort | `.submit_message(...)`, `.stream_submit_message()` |
| | `.compact_messages_...()`, `.persist_session()`, `.render_summary()` |
| | QueryEngineConfig: max_turns=8, max_budget_tokens=2000, compact_after_turns=12, structured_output=False |
| | TurnResult (dataclass): prompt, output, matched_commands/tools, permission_denials, usage, stop_reason |

#### Schicht 3 -- Infrastrukturschicht

| Modul | Beschreibung |
|-------|-------------|
| **setup.py** | WorkspaceSetup: python_version, implementation, platform_name, test_command, `startup_steps()` |
| | SetupReport: prefetches, deferred_init |
| | `run_setup(cwd, trusted)` |
| **context.py** | PortContext: source_root, tests_root, assets_root, archive_root, python_file_count, archive_available |
| | `build_port_context()`, `render_context()` |
| **session_store.py** | StoredSession: session_id, messages, input_tokens, output_tokens |
| | `save_session()`, `load_session()` -- Speicherort: `.port_sessions/` |
| **transcript.py** | TranscriptStore: `.append(entry)`, `.compact(keep_last)`, `.replay()`, `.flush()` |
| **history.py** | HistoryLog, HistoryEvent: `.add(title, det.)`, `.as_markdown()` |

#### Querschnittsmodule (werden von allen Schichten importiert)

| Modul | Beschreibung |
|-------|-------------|
| **models.py** | PortingModule, PortingBacklog, PermissionDenial, UsageSummary, Subsystem |
| **permissions.py** | ToolPermissionContext: `.blocks(name)`, `.from_iterables()` |
| **parity_audit.py** | ParityAuditResult, `run_parity_audit()` -- Fortschrittsmessung gegen TS-Archiv |

## 3.3 Schicht 1 -- Die Spiegelungsschicht (Mirror Layer)

### 3.3.1 Konzept und Motivation

Die Spiegelungsschicht bildet das Fundament des gesamten Systems. Ihr Name leitet sich von der zentralen Designentscheidung ab: Anstatt die 207 Befehle und 184 Werkzeuge des originalen TypeScript-Projekts von Grund auf neu zu implementieren, werden sie als **JSON-Snapshots** archiviert und zur Laufzeit als unveränderliche Referenzdaten geladen. Diese Snapshots befinden sich im Verzeichnis `src/reference_data/` und enthalten strukturierte Metadaten -- Name, Verantwortlichkeit und Herkunftshinweis -- für jeden einzelnen Befehl und jedes Werkzeug.

Der Begriff "Spiegelung" beschreibt diesen Vorgang treffend: Die Python-Schicht spiegelt die Oberfläche des TypeScript-Originals wider, ohne dessen interne Logik nachzubilden. Das Ergebnis ist ein **schreibgeschuetzter Katalog**, der von der Orchestrierungsschicht durchsucht, gefiltert und geroutet werden kann.

### 3.3.2 commands.py -- Der Befehlskatalog

Das Modul `commands.py` ist für das Laden und Bereitstellen der gespiegelten Befehlseintraege zuständig. Der Kern ist denkbar einfach:

```python
SNAPSHOT_PATH = Path(__file__).resolve().parent / 'reference_data' / 'commands_snapshot.json'

@lru_cache(maxsize=1)
def load_command_snapshot() -> tuple[PortingModule, ...]:
    raw_entries = json.loads(SNAPSHOT_PATH.read_text())
    return tuple(
        PortingModule(
            name=entry['name'],
            responsibility=entry['responsibility'],
            source_hint=entry['source_hint'],
            status='mirrored',
        )
        for entry in raw_entries
    )

PORTED_COMMANDS = load_command_snapshot()
```

Drei Designentscheidungen sind hier bemerkenswert:

1. **`@lru_cache(maxsize=1)`**: Der Snapshot wird beim ersten Zugriff genau einmal geladen und danach im Speicher gehalten. Wiederholte Aufrufe lesen nicht erneut vom Dateisystem. Dies ist ein klassisches Singleton-Muster über den Decorator-Mechanismus von Python.

2. **`tuple` statt `list`**: Das Ergebnis wird als unveränderliches Tupel zurückgegeben. Kein nachgelagerter Code kann die Referenzdaten versehentlich mutieren -- ein zentrales Sicherheitsprinzip in einer Architektur, die auf unveränderliche Referenzen setzt.

3. **Modullevel-Konstante `PORTED_COMMANDS`**: Durch die Zuweisung auf Modulebene wird der Snapshot beim Import des Moduls geladen. Jeder Import von `commands.py` greift auf dasselbe gecachte Tupel zu.

Über dem unveränderlichen Kern bietet `commands.py` eine Reihe von Zugriffsfunktionen:

- `get_command(name)` -- Einzelnen Befehl anhand des Namens finden (case-insensitiv)
- `get_commands(cwd, include_plugin_commands, include_skill_commands)` -- Gefilterte Befehlsliste abrufen
- `find_commands(query, limit)` -- Textsuche über Name und `source_hint`
- `execute_command(name, prompt)` -- Fuehrt einen gespiegelten Befehl aus (erzeugt eine `CommandExecution`-Instanz)
- `render_command_index(limit, query)` -- Formatierte Markdown-Ausgabe der Befehlsliste

Die `execute_command`-Funktion verdient besondere Beachtung: Da die Befehle nur gespiegelt und nicht vollständig portiert sind, erzeugt sie eine **Shim-Ausführung** -- eine Nachricht, die beschreibt, was der Originalbefehl tun würde, ohne die eigentliche Logik auszuführen. Das `CommandExecution`-Datenklassenobjekt enthalt ein `handled`-Flag, das anzeigt, ob der Befehl im Katalog gefunden würde.

### 3.3.3 tools.py -- Der Werkzeugkatalog

`tools.py` folgt exakt demselben Muster wie `commands.py`, jedoch für Werkzeuge (Tools). Die Parallele ist bewusst gewählt und erleichtert das Verstaendnis der Codebasis erheblich:

```python
SNAPSHOT_PATH = Path(__file__).resolve().parent / 'reference_data' / 'tools_snapshot.json'
PORTED_TOOLS = load_tool_snapshot()   # 184 Eintraege, tuple[PortingModule, ...]
```

Eine zusätzliche Schicht an Funktionalitaet ist die Integration mit dem Berechtigungssystem. Die Funktion `get_tools` akzeptiert einen optionalen `ToolPermissionContext`, der bestimmte Werkzeuge anhand ihres Namens oder eines Namenspraefix blockieren kann:

```python
def get_tools(
    simple_mode: bool = False,
    include_mcp: bool = True,
    permission_context: ToolPermissionContext | None = None,
) -> tuple[PortingModule, ...]:
```

Der `simple_mode`-Parameter reduziert die sichtbare Werkzeugoberfläche auf drei Kernwerkzeuge: `BashTool`, `FileReadTool` und `FileEditTool`. Der `include_mcp`-Parameter filtert MCP-basierte Werkzeuge (Model Context Protocol) heraus. Beide Parameter demonstrieren, wie die Spiegelungsschicht **Projektionslogik** bereitstellt -- sie formt die Sicht auf den unveränderlichen Katalog, ohne diesen selbst zu verändern.

### 3.3.4 Symmetrie zwischen Befehlen und Werkzeugen

Die bewusste Symmetrie zwischen `commands.py` und `tools.py` ist ein architektonisches Merkmal, das sich durch das gesamte Projekt zieht. Beide Module:

- laden ihre Daten aus JSON-Snapshots unter `src/reference_data/`
- verwenden `@lru_cache(maxsize=1)` für einmaliges Laden
- exponieren ein modullevel-Tupel (`PORTED_COMMANDS` bzw. `PORTED_TOOLS`)
- bieten identische Zugriffsoperationen: `get_*`, `find_*`, `execute_*`, `render_*_index`
- produzieren ihre jeweilige Execution-Datenklasse (`CommandExecution` bzw. `ToolExecution`)
- erstellen Backlog-Objekte über `build_command_backlog()` und `build_tool_backlog()`

Diese Symmetrie ist kein Zufall, sondern eine bewusste Anwendung des **Uniform-Access-Prinzips**: Die Orchestrierungsschicht kann Befehle und Werkzeuge gleichartig behandeln, da beide dieselbe Schnittstelle (`PortingModule`) und dasselbe Muster der Bereitstellung verwenden.

## 3.4 Schicht 2 -- Die Orchestrierungsschicht

### 3.4.1 runtime.py -- Prompt-Routing und Session-Bootstrapping

`runtime.py` ist das Herzstück der Orchestrierungsschicht. Es enthält zwei Hauptklassen: `PortRuntime` und `RuntimeSession`.

**PortRuntime** ist die zentrale Steuerungsklasse und bietet drei öffentliche Methoden:

1. **`route_prompt(prompt, limit)`** -- Token-basiertes Routing einer Benutzereingabe
2. **`bootstrap_session(prompt, limit)`** -- Vollständiges Session-Bootstrapping
3. **`run_turn_loop(prompt, limit, max_turns, structured_output)`** -- Zustandsbehaftete Turn-Schleife

#### Das Routing-Verfahren

Das Prompt-Routing in `route_prompt` folgt einem einfachen, aber effektiven Token-Scoring-Algorithmus:

```python
def route_prompt(self, prompt: str, limit: int = 5) -> list[RoutedMatch]:
    tokens = {token.lower() for token in prompt.replace('/', ' ').replace('-', ' ').split() if token}
    by_kind = {
        'command': self._collect_matches(tokens, PORTED_COMMANDS, 'command'),
        'tool': self._collect_matches(tokens, PORTED_TOOLS, 'tool'),
    }
```

Der Algorithmus funktioniert in vier Schritten:

1. **Tokenisierung**: Der Prompt wird in Kleinbuchstaben-Tokens aufgespalten. Schraegstriche und Bindestriche werden als Trennzeichen behandelt, sodass z.B. `/file-edit` zu den Tokens `{'file', 'edit'}` wird.

2. **Scoring**: Für jedes Modul im Befehls- und Werkzeugkatalog wird ein Score berechnet. Die `_score`-Methode zählt, wie viele Tokens im Namen, `source_hint` oder in der Verantwortlichkeitsbeschreibung des Moduls vorkommen:

```python
@staticmethod
def _score(tokens: set[str], module: PortingModule) -> int:
    haystacks = [module.name.lower(), module.source_hint.lower(), module.responsibility.lower()]
    score = 0
    for token in tokens:
        if any(token in haystack for haystack in haystacks):
            score += 1
    return score
```

3. **Vorselektion**: Aus jeder Kategorie (Befehle und Werkzeuge) wird der beste Treffer garantiert in die Ergebnisliste aufgenommen. Dies stellt sicher, dass sowohl ein Befehl als auch ein Werkzeug repräsentiert werden, sofern Treffer existieren.

4. **Auffuellung**: Die restlichen Plaetze bis zum `limit` werden mit den nächstbesten Treffern aus beiden Kategorien gefuellt, sortiert nach absteigendem Score.

Das Ergebnis ist eine Liste von `RoutedMatch`-Objekten, die jeweils `kind` (command/tool), `name`, `source_hint` und `score` enthalten.

#### Session-Bootstrapping

Die Methode `bootstrap_session` führt den vollständigen Initialisierungsprozess einer Sitzung durch. Sie orchestriert dabei Komponenten aus allen drei Schichten:

1. **Infrastruktur initialisieren**: `build_port_context()` sammelt Dateisysteminformationen, `run_setup(trusted=True)` erkennt die Laufzeitumgebung
2. **History-Log anlegen**: Ein `HistoryLog` wird erstellt und dokumentiert jeden Schritt
3. **Query Engine erstellen**: `QueryEnginePort.from_workspace()` baut eine frische Engine mit Manifest
4. **Routing ausführen**: `route_prompt(prompt, limit)` findet die besten Treffer
5. **Execution Registry aufbauen**: `build_execution_registry()` erstellt Shim-Wrapper für alle gespiegelten Befehle und Werkzeuge
6. **Befehle und Werkzeuge ausführen**: Die gerouteten Treffer werden über die Registry ausgeführt
7. **Permission Denials prüfen**: `_infer_permission_denials` markiert potenziell gefaehrliche Werkzeuge (z.B. `bash`-haltige Tools)
8. **Stream-Events erzeugen**: `stream_submit_message` generiert einen Event-Strom (message_start, command_match, tool_match, permission_denial, message_delta, message_stop)
9. **Turn ausführen**: `submit_message` verarbeitet den Prompt in der Query Engine
10. **Session persistieren**: `persist_session()` speichert den Zustand auf der Festplatte

Das Ergebnis ist ein `RuntimeSession`-Objekt -- eine umfassende Datenklasse mit 12 Feldern, die den gesamten Zustand der bootstrapped Session enthält. Die Methode `as_markdown()` von `RuntimeSession` kann diesen Zustand als strukturierten Markdown-Bericht ausgeben.

#### Die Turn-Schleife

`run_turn_loop` implementiert eine zustandsbehaftete Iterationsschleife:

```python
def run_turn_loop(self, prompt, limit=5, max_turns=3, structured_output=False):
    engine = QueryEnginePort.from_workspace()
    engine.config = QueryEngineConfig(max_turns=max_turns, structured_output=structured_output)
    matches = self.route_prompt(prompt, limit=limit)
    results: list[TurnResult] = []
    for turn in range(max_turns):
        turn_prompt = prompt if turn == 0 else f'{prompt} [turn {turn + 1}]'
        result = engine.submit_message(turn_prompt, command_names, tool_names, ())
        results.append(result)
        if result.stop_reason != 'completed':
            break
    return results
```

Die Schleife laeuft maximal `max_turns` Iterationen. In jedem Turn wird der Prompt (ab dem zweiten Turn mit Turn-Nummer annotiert) an die Query Engine übergeben. Wenn der `stop_reason` nicht `'completed'` ist -- etwa weil das Token-Budget erreicht würde (`'max_budget_reached'`) oder die maximale Anzahl an Nachrichten überschritten würde (`'max_turns_reached'`) -- bricht die Schleife vorzeitig ab.

### 3.4.2 query_engine.py -- Session-Zustand und Token-Budgetierung

Die `QueryEnginePort`-Klasse ist die zustandsbehaftete Komponente der Orchestrierungsschicht. Während `PortRuntime` selbst zustandslos ist und als Coordinator fungiert, verwaltet `QueryEnginePort` den veränderlichen Sitzungszustand:

- **`session_id`**: Eindeutige UUID für jede Sitzung
- **`mutable_messages`**: Liste der bisherigen Nachrichten (der veränderliche Nachrichtenpuffer)
- **`permission_denials`**: Gesammelte Berechtigungsverweigerungen
- **`total_usage`**: Kumuliertes Token-Verbrauchsobjekt (`UsageSummary`)
- **`transcript_store`**: Transkript-Speicher für Replay und Kompaktierung

#### Konfiguration

Die `QueryEngineConfig`-Datenklasse definiert vier zentrale Steuerungsparameter:

| Parameter | Standardwert | Beschreibung |
|---|---|---|
| `max_turns` | 8 | Maximale Anzahl von Nachrichten pro Sitzung |
| `max_budget_tokens` | 2000 | Token-Obergrenze (Summe aus Input und Output) |
| `compact_after_turns` | 12 | Ab dieser Nachrichtenanzahl wird kompaktiert |
| `structured_output` | False | JSON-Ausgabe statt Klartext |

#### Nachrichtenverarbeitung

Die zentrale Methode `submit_message` verarbeitet einen Prompt in mehreren Schritten:

1. **Turn-Limit prüfen**: Falls `mutable_messages` bereits `max_turns` erreicht hat, wird sofort ein `TurnResult` mit `stop_reason='max_turns_reached'` zurückgegeben.
2. **Zusammenfassung erstellen**: Prompt, gematchte Befehle/Werkzeuge und Permission Denials werden in eine Zusammenfassungszeile formatiert.
3. **Ausgabe formatieren**: Je nach `structured_output`-Flag wird entweder Klartext oder JSON erzeugt.
4. **Token-Budget prüfen**: Über `total_usage.add_turn(prompt, output)` wird der projizierte Verbrauch berechnet. Überschreitet er `max_budget_tokens`, wird `stop_reason='max_budget_reached'` gesetzt.
5. **Zustand aktualisieren**: Nachricht wird dem `mutable_messages`-Puffer und dem `transcript_store` hinzugefuegt.
6. **Kompaktierung prüfen**: `compact_messages_if_needed()` kürzt den Puffer und das Transkript, falls sie zu lang geworden sind.

Die Token-Budgetierung ist bewusst vereinfacht implementiert: `UsageSummary.add_turn` zählt die Woerter (per `split()`) als Näherung für Token-Counts:

```python
def add_turn(self, prompt: str, output: str) -> 'UsageSummary':
    return UsageSummary(
        input_tokens=self.input_tokens + len(prompt.split()),
        output_tokens=self.output_tokens + len(output.split()),
    )
```

Diese Wortbasierte Approximation ist für den aktuellen Portierungsstatus ausreichend und kann später durch einen echten Tokenizer ersetzt werden.

#### Streaming-Schnittstelle

Die Methode `stream_submit_message` liefert einen Generator, der Server-Sent-Events-ähnliche Dictionaries produziert:

```
message_start  -->  command_match  -->  tool_match  -->  permission_denial
                                                              |
                                                              v
                                              message_delta  -->  message_stop
```

Jedes Event ist ein Dictionary mit einem `type`-Feld und zugehorigen Daten. Das `message_stop`-Event enthält das Usage-Summary und die Transkript-Größe. Diese Generator-Architektur ermöglicht spätere Integration mit echten Streaming-Protokollen (SSE, WebSockets) ohne Änderungen an der Kernlogik.

#### Persistenz-Integration

`QueryEnginePort.persist_session()` flusht zunächst das Transkript und speichert dann die Session über `session_store.save_session()`:

```python
def persist_session(self) -> str:
    self.flush_transcript()
    path = save_session(StoredSession(
        session_id=self.session_id,
        messages=tuple(self.mutable_messages),
        input_tokens=self.total_usage.input_tokens,
        output_tokens=self.total_usage.output_tokens,
    ))
    return str(path)
```

Der umgekehrte Weg -- das Laden einer gespeicherten Session -- ist über die Klassenmethode `from_saved_session(session_id)` möglich. Sie stellt den vollständigen Zustand wieder her, einschließlich des Transkripts und der Token-Zähler.

### 3.4.3 execution_registry.py -- Die Ausführungsschicht

Das `ExecutionRegistry`-Modul stellt eine einheitliche Schnittstelle für die Ausführung gespiegelter Befehle und Werkzeuge bereit. Es erzeugt `MirroredCommand`- und `MirroredTool`-Wrapper, die jeweils eine `execute`-Methode bieten:

```python
@dataclass(frozen=True)
class MirroredCommand:
    name: str
    source_hint: str

    def execute(self, prompt: str) -> str:
        return execute_command(self.name, prompt).message
```

Die Funktion `build_execution_registry()` baut die gesamte Registry beim Aufruf auf, indem sie alle `PORTED_COMMANDS` und `PORTED_TOOLS` in ihre jeweiligen Wrapper-Typen verpackt. Dies entkoppelt die Orchestrierungsschicht von den Details der Befehlsausführung und ermöglicht spätere Erweiterungen, etwa das Ersetzen von Shim-Ausführungen durch echte Implementierungen.

## 3.5 Schicht 3 -- Die Infrastrukturschicht

### 3.5.1 setup.py -- Umgebungserkennung und Startup

`setup.py` ist für die Erkennung der Laufzeitumgebung und die Durchfuehrung der Startup-Schritte zuständig. Es liefert zwei Datenklassen:

**`WorkspaceSetup`** hält die statischen Umgebungsinformationen: Python-Version, Implementierung (CPython, PyPy, etc.), Plattformname und Test-Befehl. Die Methode `startup_steps()` liefert die sechs definierten Startup-Schritte als Tupel:

1. Start der Top-Level-Prefetch-Seiteneffekte
2. Aufbau des Workspace-Kontexts
3. Laden des gespiegelten Befehlssnapshots
4. Laden des gespiegelten Werkzeugsnapshots
5. Vorbereitung der Parity-Audit-Hooks
6. Anwendung der Trust-gesteuerten verzogerten Initialisierung

**`SetupReport`** aggregiert das Setup mit den Ergebnissen der Prefetch-Operationen und der verzogerten Initialisierung. Die Funktion `run_setup` koordiniert drei Prefetch-Operationen:

- `start_mdm_raw_read()` -- Liest MDM-Konfigurationsdaten (Mobile Device Management)
- `start_keychain_prefetch()` -- Laedt Schlüsselketten-Daten vor
- `start_project_scan(root)` -- Scannt das Projektverzeichnis

Der `trusted`-Parameter steuert, ob die verzogerte Initialisierung (`deferred_init`) mit erweiterten Rechten ausgeführt wird. Dies ist ein zentraler Sicherheitsmechanismus: Im nicht-vertrauenswürdigen Modus werden bestimmte Initialisierungsschritte übersprungen.

### 3.5.2 context.py -- Workspace-Kontext

`context.py` sammelt Dateisystem-Metadaten über den Workspace. Die `PortContext`-Datenklasse enthält:

- Pfade zu `source_root`, `tests_root`, `assets_root` und `archive_root`
- Zähler für Python-Dateien, Testdateien und Asset-Dateien
- Ein `archive_available`-Flag, das anzeigt, ob das TypeScript-Originalarchiv lokal vorhanden ist

`build_port_context()` traversiert das Dateisystem über `Path.rglob('*.py')` und zählt die Dateien dynamisch. Diese Funktion wird vom Session-Bootstrapping aufgerufen und liefert dem Benutzer einen Überblick über den aktuellen Zustand des Portierungsprojekts.

### 3.5.3 session_store.py -- Persistenz

Das Persistenz-Modul ist bewusst minimal gehalten. Es definiert eine `StoredSession`-Datenklasse mit vier Feldern:

```python
@dataclass(frozen=True)
class StoredSession:
    session_id: str
    messages: tuple[str, ...]
    input_tokens: int
    output_tokens: int
```

`save_session` serialisiert eine Session als JSON-Datei unter `.port_sessions/{session_id}.json`. `load_session` deserialisiert sie zurück. Das Verzeichnis wird bei Bedarf automatisch angelegt (`mkdir(parents=True, exist_ok=True)`).

### 3.5.4 transcript.py und history.py -- Nachverfolgung

**`TranscriptStore`** ist ein leichtgewichtiger Speicher für Nachrichten mit vier Operationen:
- `append(entry)` -- Nachricht hinzufuegen (setzt `flushed=False`)
- `compact(keep_last)` -- Alte Eintraege entfernen, nur die letzten `keep_last` behalten
- `replay()` -- Alle Eintraege als Tupel zurückgeben
- `flush()` -- `flushed`-Flag setzen

**`HistoryLog`** dokumentiert die Schritte einer Session als `HistoryEvent`-Objekte (Titel + Detail). Es wird primaer während des Session-Bootstrapping verwendet, um den Fortschritt der Initialisierung nachzuvollziehen.

## 3.6 Querschnittsmodule

### 3.6.1 models.py -- Gemeinsame Datenklassen

`models.py` definiert die fünf zentralen Datenklassen, die von allen Schichten verwendet werden:

- **`Subsystem`**: Beschreibt ein Python-Modul im Workspace (Name, Pfad, Dateianzahl, Notizen)
- **`PortingModule`**: Die universelle Einheit für gespiegelte Befehle und Werkzeuge (Name, Verantwortlichkeit, Herkunftshinweis, Status)
- **`PermissionDenial`**: Modelliert eine Zugriffsverweigerung (Werkzeugname + Grund)
- **`UsageSummary`**: Token-Verbrauchszähler mit der Methode `add_turn` für inkrementelle Aktualisierung
- **`PortingBacklog`**: Aggregiert eine Liste von `PortingModule`-Objekten unter einem Titel mit formatierten Zusammenfassungszeilen

Alle Datenklassen bis auf `PortingBacklog` und `UsageSummary` sind mit `frozen=True` deklariert, also unveränderlich nach der Erstellung.

### 3.6.2 permissions.py -- Zugriffskontrolle

`ToolPermissionContext` implementiert ein einfaches Deny-List-basiertes Berechtigungssystem:

```python
@dataclass(frozen=True)
class ToolPermissionContext:
    deny_names: frozenset[str] = field(default_factory=frozenset)
    deny_prefixes: tuple[str, ...] = ()

    def blocks(self, tool_name: str) -> bool:
        lowered = tool_name.lower()
        return lowered in self.deny_names or any(lowered.startswith(prefix) for prefix in self.deny_prefixes)
```

Die Klasse unterstützt zwei Blockierungsmechanismen: exakte Namensübereinstimmung und Präfix-Matching. Beides geschieht case-insensitiv. Die Factory-Methode `from_iterables` erstellt einen Kontext aus CLI-Argumenten (z.B. `--deny-tool BashTool --deny-prefix mcp_`).

### 3.6.3 parity_audit.py -- Fortschrittsmessung

Das Parity-Audit-Modul vergleicht den aktuellen Python-Portierungsstand mit dem archivierten TypeScript-Original. Es misst fünf Metriken:

1. **Root File Coverage**: Wie viele der erwarteten Root-Dateien existieren bereits in Python?
2. **Directory Coverage**: Wie viele der erwarteten Verzeichnisse würden angelegt?
3. **Total File Ratio**: Verhältnis der Python-Dateien zu den archivierten TypeScript-Dateien
4. **Command Entry Ratio**: Gespiegelte Befehle vs. erwartete Befehle
5. **Tool Entry Ratio**: Gespiegelte Werkzeuge vs. erwartete Werkzeuge

Die Funktion `run_parity_audit()` produziert ein `ParityAuditResult`, das über `to_markdown()` als formatierter Bericht ausgegeben werden kann. Dieses Modul ist ein reines Diagnose-Werkzeug und hat keinen Einfluss auf den Laufzeitbetrieb.

## 3.7 Abhängigkeitsgraph zwischen Modulen

Das folgende Diagramm zeigt die Import-Beziehungen zwischen allen Modulen. Ein Pfeil von A nach B bedeutet "A importiert B":

**Importgraph -- Oberste Ebene:**

- **main.py** importiert:
  - runtime.py, query_engine.py, setup.py, commands/tools.py (Spiegelungsschicht)

- **runtime.py** und **query_engine.py** importieren:
  - context.py, history.py, transcript.py, prefetch.py, models.py, permissions.py

- **execution_registry.py** importiert:
  - commands.py, tools.py

- **parity_audit.py** importiert:
  - reference_data/*.json, models.py

- **session_store.py** wird importiert von:
  - query_engine.py, main.py

**Detaillierte Import-Beziehungen:**

- **main.py**
  - runtime.py (PortRuntime)
  - query_engine.py (QueryEnginePort)
  - commands.py (execute_command, get_command, get_commands, render_command_index)
  - tools.py (execute_tool, get_tool, get_tools, render_tool_index)
  - setup.py (run_setup)
  - permissions.py (ToolPermissionContext)
  - port_manifest.py (build_port_manifest)
  - session_store.py (load_session)
  - parity_audit.py (run_parity_audit)
  - bootstrap_graph.py, command_graph.py, tool_pool.py
  - direct_modes.py, remote_runtime.py

- **runtime.py**
  - commands.py (PORTED_COMMANDS)
  - tools.py (PORTED_TOOLS)
  - context.py (PortContext, build_port_context, render_context)
  - history.py (HistoryLog)
  - models.py (PermissionDenial, PortingModule)
  - query_engine.py (QueryEngineConfig, QueryEnginePort, TurnResult)
  - setup.py (SetupReport, WorkspaceSetup, run_setup)
  - system_init.py (build_system_init_message)
  - execution_registry.py (build_execution_registry)

- **query_engine.py**
  - commands.py (build_command_backlog)
  - tools.py (build_tool_backlog)
  - models.py (PermissionDenial, UsageSummary)
  - port_manifest.py (PortManifest, build_port_manifest)
  - session_store.py (StoredSession, load_session, save_session)
  - transcript.py (TranscriptStore)

- **commands.py**
  - models.py (PortingBacklog, PortingModule)

- **tools.py**
  - models.py (PortingBacklog, PortingModule)
  - permissions.py (ToolPermissionContext)

Bemerkenswert ist die klare Hierarchie: `main.py` importiert aus allen Schichten, aber die Schichten selbst haben geordnete Abhängigkeiten. `runtime.py` importiert aus der Spiegelungsschicht und der Infrastruktur, aber nie umgekehrt. `models.py` als Querschnittsmodul wird von fast allen anderen Modulen importiert, importiert aber selbst keine anderen Projektmodule.

## 3.8 Datenfluss von CLI-Eingabe bis Ausgabe

Das folgende Diagramm zeichnet den vollständigen Datenfluss für den exemplarischen Befehl `turn-loop` nach -- den komplexesten Pfad durch die Architektur:

**Datenfluss: CLI-Eingabe bis Ausgabe**

**Benutzer-Eingabe:** `$ python -m src.main turn-loop "edit file" --max-turns 3`

1. **main.py :: main(argv)** -- Parser und Argument-Extraktion
   - `parser = build_parser()`
   - `args = parser.parse_args(argv)` ergibt: `args.command = 'turn-loop'`, `args.prompt = 'edit file'`, `args.max_turns = 3`

2. **main.py :: Dispatch-Block**
   - `if args.command == 'turn-loop':` ruft `PortRuntime().run_turn_loop(prompt, limit, max_turns, structured_output)` auf

3. **runtime.py :: PortRuntime.run_turn_loop()**
   1. Engine erstellen: `engine = QueryEnginePort.from_workspace`
      - Ruft `port_manifest.py :: build_port_manifest()` auf: scannt `src/*.py`, zaehlt Dateien, erzeugt `PortManifest`
   2. Konfiguration: `engine.config = QueryEngineConfig(max_turns=3, structured_output=...)`
   3. Routing: `matches = self.route_prompt(prompt)`
      - Tokenisierung: `"edit file"` wird zu `tokens = {'edit', 'file'}`
      - `_collect_matches(tokens, PORTED_COMMANDS, 'command')` -- bewertet jedes der 207 Befehle, sortiert nach Score (absteigend)
      - `_collect_matches(tokens, PORTED_TOOLS, 'tool')` -- bewertet jedes der 184 Tools, sortiert nach Score (absteigend)
      - Vorselektion: je 1 aus command/tool, Auffuellung bis `limit=5`, Ergebnis: `[RoutedMatch, ...]`
   4. **Turn-Schleife** (max 3 Iterationen):
      - **Turn 1:** prompt = `"edit file"` --> `engine.submit_message(...)` --> TurnResult mit `stop_reason='completed'`
      - **Turn 2:** prompt = `"edit file [turn 2]"` --> `engine.submit_message(...)` --> TurnResult mit `stop_reason='completed'`
      - **Turn 3:** prompt = `"edit file [turn 3]"` --> `engine.submit_message(...)` --> TurnResult mit `stop_reason='max_budget_...'` --> Schleife bricht ab
   5. `return [TurnResult, TurnResult, ...]`

4. **query_engine.py :: submit_message()** -- Detailablauf
   1. Pruefen: `len(mutable_messages) >= max_turns?` --> `'max_turns_reached'`
   2. `summary_lines` zusammenstellen: Prompt, gematchte Commands, gematchte Tools, Permission Denials
   3. `output = _format_output(summary_lines)` -- structured: JSON, plain: `'\n'.join(lines)`
   4. `projected_usage = total_usage.add_turn(prompt, output)` -- addiert `input_tokens` und `output_tokens`
   5. Budget pruefen: `in + out > 2000?` --> `'max_budget_...'`
   6. State aktualisieren: `mutable_messages.append(prompt)`, `transcript_store.append(prompt)`, `permission_denials.extend(denied)`, `total_usage = projected_usage`
   7. `compact_messages_if_needed()` -- `len(msgs) > 12?` --> kuerzen
   8. `return TurnResult(...)`

5. **main.py :: Ausgabe-Formatierung**
   - `for idx, result in enumerate(results, 1):` gibt `## Turn {idx}`, `result.output`, `stop_reason=...` aus

**Terminal-Ausgabe (Beispiel):**

| Turn | Prompt | stop_reason |
|------|--------|-------------|
| 1 | edit file | completed |
| 2 | edit file [turn 2] | completed |
| 3 | edit file [turn 3] | max_budget_reached |

## 3.9 Zusammenspiel der Schichten

Die Stärke der Architektur liegt im kontrollierten Zusammenspiel der drei Schichten. Jede Schicht hat eine klare Aufgabe und kommuniziert über wohldefinierte Schnittstellen mit den anderen:

### Datenrichtung: Bottom-Up

Die Daten fliessen grundsaetzlich von unten nach oben:

1. **Infrastruktur** stellt Rohdaten bereit: Dateipfade, Umgebungsinformationen, gespeicherte Sessions
2. **Spiegelung** transformiert JSON-Snapshots in typisierte Python-Objekte
3. **Orchestrierung** kombiniert beides zu Session-Logik, Routing und Turn-Verwaltung

### Kontrollrichtung: Top-Down

Die Steuerung fliesst dagegen von oben nach unten:

1. **CLI** (`main.py`) bestimmt, welcher Modus aktiviert wird
2. **Orchestrierung** entscheidet, welche Befehle/Werkzeuge geroutet werden und wie viele Turns durchlaufen werden
3. **Infrastruktur/Spiegelung** führt die konkreten Operationen aus (Laden, Speichern, Suchen)

### Unveränderlichkeit als Architekturprinzip

Ein durchgängiges Prinzip ist die Unterscheidung zwischen unveränderlichen und veränderlichen Daten:

**Unveränderlich (frozen=True):**
- `PortingModule`, `PortContext`, `WorkspaceSetup`, `SetupReport`
- `StoredSession`, `PermissionDenial`, `RoutedMatch`, `TurnResult`
- `ToolPermissionContext`, `QueryEngineConfig`
- `PORTED_COMMANDS`, `PORTED_TOOLS` (Tupel auf Modulebene)

**Veraenderlich:**
- `QueryEnginePort.mutable_messages` (wachsender Nachrichtenpuffer)
- `QueryEnginePort.permission_denials` (gesammelte Verweigerungen)
- `QueryEnginePort.total_usage` (wird bei jedem Turn ersetzt)
- `TranscriptStore.entries` (wachsendes Transkript)
- `HistoryLog.events` (wachsendes Ereignisprotokoll)
- `PortingBacklog.modules` (veränderliche Modulliste)

Dieses Muster -- unveränderliche Referenzdaten und Konfigurationen, veränderlicher Sitzungszustand -- ist typisch für ereignisgesteuerte Systeme und erleichtert das Nachvollziehen von ZustandsÄnderungen erheblich.

## 3.10 Der Einstiegspunkt: main.py

`main.py` verdient eine gesonderte Betrachtung als Klammer um die gesamte Architektur. Die Funktion `build_parser()` definiert 21 Unterbefehle über `argparse`, die sich in vier Kategorien einteilen lassen:

**Berichtsbefehle** (zustandslos, lesen nur):
- `summary`, `manifest`, `parity-audit`, `setup-report`, `command-graph`, `tool-pool`, `bootstrap-graph`, `subsystems`

**Katalogbefehle** (durchsuchen die Spiegelungsschicht):
- `commands`, `tools`, `show-command`, `show-tool`

**Ausführungsbefehle** (durchlaufen die Orchestrierungsschicht):
- `route`, `bootstrap`, `turn-loop`, `exec-command`, `exec-tool`

**Persistenzbefehle** (nutzen die Infrastrukturschicht):
- `flush-transcript`, `load-session`

**Remote-Befehle** (erweiterter Laufzeitmodus):
- `remote-mode`, `ssh-mode`, `teleport-mode`, `direct-connect-mode`, `deep-link-mode`

Die `main()`-Funktion verwendet eine einfache if-elif-Kaskade für das Dispatching. Jeder Zweig folgt demselben Muster: Objekt erstellen, Methode aufrufen, Ergebnis auf stdout ausgeben, Exitcode 0 zurückgeben. Dieses Muster hält die Einstiegspunktlogik flach und leicht testbar -- jeder CLI-Befehl lässt sich isoliert aufrufen.

## 3.11 Entwurfsmuster und Konventionen

Über die drei Schichten hinweg lassen sich mehrere wiederkehrende Entwurfsmuster identifizieren:

### Factory-Methoden

`QueryEnginePort.from_workspace()` und `QueryEnginePort.from_saved_session(session_id)` sind Klassenmethoden, die als benannte Konstruktoren dienen. Sie kapseln die Erstellungslogik und machen den aufrufenden Code ausdrückstärker als ein direkter `__init__`-Aufruf.

### Builder-Pattern

`build_port_manifest()`, `build_port_context()`, `build_execution_registry()`, `build_system_init_message()` -- alle folgen der Konvention `build_*()`. Diese Funktionen aggregieren Daten aus verschiedenen Quellen und liefern ein fertiges, unveränderliches Objekt zurück.

### Markdown-as-Output

Nahezu jede Datenklasse bietet eine `to_markdown()`- oder `as_markdown()`-Methode. Dies ist eine bewusste Designentscheidung: Die CLI gibt Markdown-formatierte Berichte aus, die sowohl im Terminal lesbar sind als auch in Dokumentation oder Issue-Tracker eingefuegt werden koennen.

### Defensive Konfiguration

Die `QueryEngineConfig`-Datenklasse mit ihren Standardwerten (`max_turns=8`, `max_budget_tokens=2000`) demonstriert das Prinzip der defensiven Konfiguration: Ohne explizite Konfiguration verhält sich das System sicher und vorhersagbar. Der Benutzer kann diese Werte überschreiben, muss es aber nicht.

## 3.12 Zusammenfassung

Die Drei-Schichten-Architektur von Claw Code trennt Verantwortlichkeiten klar und konsequent:

- Die **Spiegelungsschicht** (`commands.py`, `tools.py`) laedt 207 Befehle und 184 Werkzeuge als unveränderliche Referenzdaten aus JSON-Snapshots. Ihre `@lru_cache`-gestützten Ladefunktionen und die symmetrische API für Befehle und Werkzeuge bilden das Fundament.

- Die **Orchestrierungsschicht** (`runtime.py`, `query_engine.py`, `execution_registry.py`) implementiert Token-Scoring-basiertes Prompt-Routing, Session-Bootstrapping mit Umgebungserkennung, zustandsbehaftete Turn-Schleifen mit Token-Budgetierung und eine Streaming-Schnittstelle für ereignisbasierte Ausgabe.

- Die **Infrastrukturschicht** (`setup.py`, `context.py`, `session_store.py`, `transcript.py`, `history.py`) stellt Umgebungserkennung mit Prefetch-Operationen, Dateisystem-Kontexterfassung, JSON-basierte Session-Persistenz und Transkript- sowie History-Nachverfolgung bereit.

Die **Querschnittsmodule** (`models.py`, `permissions.py`, `parity_audit.py`) liefern die gemeinsamen Datenstrukturen, ein Deny-List-basiertes Berechtigungssystem und eine Fortschrittsmessung gegen das TypeScript-Original.

Das Ergebnis ist eine Architektur, die trotz ihrer Komplexitaet überraschend gut navigierbar bleibt: Jedes Modul hat eine klar abgegrenzte Verantwortung, die Datenflussrichtung ist vorhersagbar, und die konsequente Verwendung von unveränderlichen Datenklassen minimiert die Fehlerquellen bei der Zustandsverwaltung.


# Kapitel 4: Der CLI-Einstiegspunkt

## Einleitung

Das Herzstück jeder kommandozeilengesteuerten Anwendung ist ihr Einstiegspunkt — der Ort, an dem Benutzereingaben entgegengenommen, interpretiert und an die jeweils zuständige Verarbeitungslogik weitergeleitet werden. Im Claw-Code-Projekt erfüllt die Datei `src/main.py` genau diese Funktion. Mit 214 Zeilen ist sie bewusst schlank gehalten und folgt einem klaren architektonischen Prinzip: Die CLI-Schicht kennt alle verfügbaren Befehle und deren Argumente, delegiert die eigentliche Arbeit aber vollständig an spezialisierte Module. Diese Trennung von Befehlsparsing und Geschäftslogik ist ein Kennzeichen gut strukturierter Python-Projekte und erleichtert sowohl das Testen als auch die Erweiterbarkeit.

Die Datei gliedert sich in drei klar abgegrenzte Bereiche: einen Importblock (Zeilen 1–18), die Funktion `build_parser()` (Zeilen 21–91) und die Funktion `main()` (Zeilen 94–213). Im Folgenden werden alle drei Bereiche im Detail analysiert.

---

## 4.1 Der Importblock

```python
from __future__ import annotations

import argparse

from .bootstrap_graph import build_bootstrap_graph
from .command_graph import build_command_graph
from .commands import execute_command, get_command, get_commands, render_command_index
from .direct_modes import run_deep_link, run_direct_connect
from .parity_audit import run_parity_audit
from .permissions import ToolPermissionContext
from .port_manifest import build_port_manifest
from .query_engine import QueryEnginePort
from .remote_runtime import run_remote_mode, run_ssh_mode, run_teleport_mode
from .runtime import PortRuntime
from .session_store import load_session
from .setup import run_setup
from .tool_pool import assemble_tool_pool
from .tools import execute_tool, get_tool, get_tools, render_tool_index
```

Die erste Zeile `from __future__ import annotations` aktiviert die sogenannte „postponed evaluation of annotations" (PEP 563). Damit werden Typannotationen als Strings behandelt und erst bei Bedarf aufgelöst. Dies erlaubt die Nutzung moderner Typ-Syntax wie `list[str] | None` auch in älteren Python-Versionen und vermeidet zirkuläre Importprobleme.

Der einzige Standardbibliotheks-Import ist `argparse` — das bewährte Modul der Python-Standardbibliothek zum Parsen von Kommandozeilenargumenten.

Alle weiteren Importe sind relative Importe aus dem eigenen Paket (erkennbar am führenden Punkt). Sie lassen sich thematisch gruppieren:

- **Graphen und Analysen:** `build_bootstrap_graph`, `build_command_graph`, `run_parity_audit`, `assemble_tool_pool`
- **Befehls- und Tool-Verwaltung:** `execute_command`, `get_command`, `get_commands`, `render_command_index`, `execute_tool`, `get_tool`, `get_tools`, `render_tool_index`
- **Laufzeitmodi:** `run_deep_link`, `run_direct_connect`, `run_remote_mode`, `run_ssh_mode`, `run_teleport_mode`
- **Infrastruktur:** `ToolPermissionContext`, `build_port_manifest`, `QueryEnginePort`, `PortRuntime`, `load_session`, `run_setup`

Dieses Importmuster macht auf einen Blick sichtbar, welche Module von der CLI-Schicht abhängen — und umgekehrt, welche Module keinerlei Wissen über die CLI besitzen müssen.

---

## 4.2 Die `build_parser()`-Funktion

```python
def build_parser() -> argparse.ArgumentParser:
```

Diese Funktion erzeugt und konfiguriert den gesamten Argument-Parser. Sie gibt ein `argparse.ArgumentParser`-Objekt zurück, das alle 24 Subcommands kennt. Die Funktion ist eine reine Fabrikfunktion ohne Seiteneffekte — sie liest keine Dateien, greift nicht auf das Netzwerk zu und verändert keinen globalen Zustand.

### 4.2.1 Der Wurzel-Parser und die Subparser-Gruppe

```python
parser = argparse.ArgumentParser(
    description='Python porting workspace for the Claude Code rewrite effort'
)
subparsers = parser.add_subparsers(dest='command', required=True)
```

Der Wurzel-Parser wird mit einer Beschreibung versehen, die beim Aufruf von `--help` angezeigt wird. Entscheidend ist der Aufruf von `add_subparsers()`:

- `dest='command'` legt fest, dass der gewählte Subcommand-Name nach dem Parsen im Attribut `args.command` verfügbar ist. Dies ist der Schlüssel für die gesamte Dispatch-Logik in `main()`.
- `required=True` stellt sicher, dass der Benutzer immer einen Subcommand angeben muss. Ohne Subcommand gibt argparse automatisch eine Fehlermeldung aus.

### 4.2.2 Alle 24 Subcommands im Detail

Im Folgenden werden alle Subcommands in der Reihenfolge ihrer Definition im Quelltext beschrieben und nach funktionalen Kategorien gruppiert.

---

### Kategorie 1: Workspace-Inspektion

Diese vier Befehle dienen der Inspektion des aktuellen Workspace-Zustands. Sie benötigen keine oder nur minimale Argumente und liefern strukturierte Berichte.

#### `summary`

```python
subparsers.add_parser('summary',
    help='render a Markdown summary of the Python porting workspace')
```

Der einfachste aller Subcommands: keine zusätzlichen Argumente. Er erzeugt eine Markdown-Zusammenfassung des gesamten Python-Portierungs-Workspace. In `main()` wird er wie folgt behandelt:

```python
if args.command == 'summary':
    print(QueryEnginePort(manifest).render_summary())
    return 0
```

Es wird ein `QueryEnginePort`-Objekt mit dem zuvor gebauten Manifest instanziiert und dessen `render_summary()`-Methode aufgerufen. Das Ergebnis wird direkt auf die Standardausgabe geschrieben.

#### `manifest`

```python
subparsers.add_parser('manifest',
    help='print the current Python workspace manifest')
```

Ebenfalls ohne Argumente. Er gibt das Workspace-Manifest in Markdown-Form aus:

```python
if args.command == 'manifest':
    print(manifest.to_markdown())
    return 0
```

Das `manifest`-Objekt würde bereits zu Beginn von `main()` durch `build_port_manifest()` erzeugt und steht somit sofort zur Verfügung.

#### `subsystems`

```python
list_parser = subparsers.add_parser('subsystems',
    help='list the current Python modules in the workspace')
list_parser.add_argument('--limit', type=int, default=32)
```

Dieser Befehl listet die Python-Module im Workspace auf. Er besitzt ein optionales Argument `--limit` vom Typ `int` mit dem Standardwert 32, das die Anzahl der angezeigten Module begrenzt. Der Handler:

```python
if args.command == 'subsystems':
    for subsystem in manifest.top_level_modules[: args.limit]:
        for subsystem in manifest.top_level_modules[: args.limit]:
        print(f'{subsystem.name}\t{subsystem.file_count}\t{subsystem.notes}')
    return 0
```

Er iteriert über die im Manifest gespeicherten Top-Level-Module (begrenzt durch das Limit) und gibt für jedes Modul Name, Dateianzahl und Notizen als tabulatorgetrennte Zeilen aus. Dieses Format eignet sich gut für die Weiterverarbeitung in Shell-Pipelines.

#### `setup-report`

```python
subparsers.add_parser('setup-report',
    help='render the startup/prefetch setup report')
```

Keine zusätzlichen Argumente. Der Handler:

```python
if args.command == 'setup-report':
    print(run_setup().as_markdown())
    return 0
```

Hier wird `run_setup()` aus dem Modul `.setup` aufgerufen. Das Ergebnis besitzt eine `as_markdown()`-Methode, die den Bericht als Markdown-Text zurückgibt. Dieser Befehl simuliert den Startup-/Prefetch-Bericht, wie er beim Hochfahren der Laufzeitumgebung erzeugt wird.

---

### Kategorie 2: Befehls- und Tool-Katalog

Diese vier Befehle ermöglichen die Navigation durch den Katalog der gespiegelten Befehle und Tools.

#### `commands`

```python
commands_parser = subparsers.add_parser('commands',
    help='list mirrored command entries from the archived snapshot')
commands_parser.add_argument('--limit', type=int, default=20)
commands_parser.add_argument('--query')
commands_parser.add_argument('--no-plugin-commands', action='store_true')
commands_parser.add_argument('--no-skill-commands', action='store_true')
```

Dies ist einer der komplexesten Subcommands in Bezug auf die Argument-Konfiguration. Er verfügt über vier optionale Argumente:

- `--limit` (int, Standard 20): Maximale Anzahl angezeigter Einträge.
- `--query` (String, optional): Ein Suchbegriff zur Filterung der Befehle.
- `--no-plugin-commands` (Boolean-Flag): Wenn gesetzt, werden Plugin-Befehle ausgeschlossen.
- `--no-skill-commands` (Boolean-Flag): Wenn gesetzt, werden Skill-Befehle ausgeschlossen.

Der Handler implementiert eine Verzweigung je nachdem, ob eine Query angegeben würde:

```python
if args.command == 'commands':
    if args.query:
        print(render_command_index(limit=args.limit, query=args.query))
    else:
        commands = get_commands(
            include_plugin_commands=not args.no_plugin_commands,
            include_skill_commands=not args.no_skill_commands
        )
        output_lines = [f'Command entries: {len(commands)}', '']
        output_lines.extend(
            f'- {module.name} — {module.source_hint}'
            for module in commands[: args.limit]
        )
        print('\n'.join(output_lines))
    return 0
```

Wenn eine Query vorhanden ist, wird `render_command_index()` aufgerufen — eine Funktion, die vermutlich eine durchsuchbare Indexdarstellung liefert. Ohne Query wird `get_commands()` aufgerufen, wobei die beiden Boolean-Flags invertiert übergeben werden (beachte die `not`-Negation: `--no-plugin-commands` setzt `include_plugin_commands` auf `False`). Die Ausgabe besteht aus einer Kopfzeile mit der Gesamtanzahl, gefolgt von einer Aufzählung mit Name und Herkunftshinweis.

#### `tools`

```python
tools_parser = subparsers.add_parser('tools',
    help='list mirrored tool entries from the archived snapshot')
tools_parser.add_argument('--limit', type=int, default=20)
tools_parser.add_argument('--query')
tools_parser.add_argument('--simple-mode', action='store_true')
tools_parser.add_argument('--no-mcp', action='store_true')
tools_parser.add_argument('--deny-tool', action='append', default=[])
tools_parser.add_argument('--deny-prefix', action='append', default=[])
```

Der tool-reichste Subcommand mit sechs optionalen Argumenten:

- `--limit` (int, Standard 20): Begrenzung der Ausgabe.
- `--query` (String, optional): Suchbegriff.
- `--simple-mode` (Boolean-Flag): Aktiviert einen vereinfachten Modus.
- `--no-mcp` (Boolean-Flag): Schließt MCP-Tools (Model Context Protocol) aus.
- `--deny-tool` (Liste, wiederholbar): Explizites Verbot einzelner Tools nach Name. Durch `action='append'` können mehrere `--deny-tool`-Angaben kumuliert werden.
- `--deny-prefix` (Liste, wiederholbar): Verbot ganzer Tool-Familien nach Namenspräfix.

Der Handler:

```python
if args.command == 'tools':
    if args.query:
        print(render_tool_index(limit=args.limit, query=args.query))
    else:
        permission_context = ToolPermissionContext.from_iterables(
            args.deny_tool, args.deny_prefix
        )
        tools = get_tools(
            simple_mode=args.simple_mode,
            include_mcp=not args.no_mcp,
            permission_context=permission_context
        )
        output_lines = [f'Tool entries: {len(tools)}', '']
        output_lines.extend(
            f'- {module.name} — {module.source_hint}'
            for module in tools[: args.limit]
        )
        print('\n'.join(output_lines))
    return 0
```

Besonders bemerkenswert ist die Verwendung von `ToolPermissionContext.from_iterables()`. Hier werden die vom Benutzer spezifizierten Ablehnungslisten in ein strukturiertes Berechtigungsobjekt umgewandelt, das anschließend an `get_tools()` übergeben wird. Dies zeigt eine saubere Trennung zwischen CLI-Parsing und Geschäftslogik: Die CLI sammelt die Rohdaten, die Domänenschicht interpretiert sie.

#### `show-command`

```python
show_command = subparsers.add_parser('show-command',
    help='show one mirrored command entry by exact name')
show_command.add_argument('name')
```

Ein positionelles Argument `name` — der exakte Befehlsname. Der Handler:

```python
if args.command == 'show-command':
    module = get_command(args.name)
    if module is None:
        print(f'Command not found: {args.name}')
        return 1
    print('\n'.join([module.name, module.source_hint, module.responsibility]))
    return 0
```

Dieser Befehl zeigt die Details eines einzelnen gespiegelten Befehls an. Wird der Befehl nicht gefunden, gibt der Handler eine Fehlermeldung aus und liefert den Exit-Code 1 zurück — ein wichtiges Signal für Skripte und Automatisierungen, die den Exit-Code auswerten.

#### `show-tool`

```python
show_tool = subparsers.add_parser('show-tool',
    help='show one mirrored tool entry by exact name')
show_tool.add_argument('name')
```

Strukturell identisch mit `show-command`, aber für Tools. Der Handler:

```python
if args.command == 'show-tool':
    module = get_tool(args.name)
    if module is None:
        print(f'Tool not found: {args.name}')
        return 1
    print('\n'.join([module.name, module.source_hint, module.responsibility]))
    return 0
```

Auch hier wird bei Nichtauffinden des Tools der Exit-Code 1 zurückgegeben.

---

### Kategorie 3: Ausführung

Diese beiden Befehle gehen über die reine Inspektion hinaus und führen tatsächlich Befehls- bzw. Tool-Shims aus.

#### `exec-command`

```python
exec_command_parser = subparsers.add_parser('exec-command',
    help='execute a mirrored command shim by exact name')
exec_command_parser.add_argument('name')
exec_command_parser.add_argument('prompt')
```

Zwei positionelle Argumente: `name` (der exakte Befehlsname) und `prompt` (die Eingabe, die an den Befehl übergeben wird). Der Handler:

```python
if args.command == 'exec-command':
    result = execute_command(args.name, args.prompt)
    print(result.message)
    return 0 if result.handled else 1
```

Die Funktion `execute_command()` liefert ein Ergebnisobjekt zurück, das mindestens die Attribute `message` und `handled` besitzt. Der Exit-Code hängt von `handled` ab: War die Ausführung erfolgreich, wird 0 zurückgegeben, andernfalls 1. Dieses Muster ermöglicht es aufrufenden Skripten, den Erfolg oder Misserfolg programmatisch zu erkennen.

#### `exec-tool`

```python
exec_tool_parser = subparsers.add_parser('exec-tool',
    help='execute a mirrored tool shim by exact name')
exec_tool_parser.add_argument('name')
exec_tool_parser.add_argument('payload')
```

Analog zu `exec-command`, aber mit dem Argument `payload` statt `prompt`. Das Wort „Payload" deutet darauf hin, dass Tools eher strukturierte Eingaben erwarten (z. B. JSON), während Befehle mit natürlichsprachlichen Prompts arbeiten. Der Handler:

```python
if args.command == 'exec-tool':
    result = execute_tool(args.name, args.payload)
    print(result.message)
    return 0 if result.handled else 1
```

Identische Struktur wie bei `exec-command`: Ergebnis ausgeben, Exit-Code basierend auf dem `handled`-Flag setzen.

---

### Kategorie 4: Routing und Sessions

Diese drei Befehle bilden den Kern der Laufzeitinteraktion — vom einfachen Routing über die Session-Initialisierung bis hin zur mehrstufigen Gesprächsschleife.

#### `route`

```python
route_parser = subparsers.add_parser('route',
    help='route a prompt across mirrored command/tool inventories')
route_parser.add_argument('prompt')
route_parser.add_argument('--limit', type=int, default=5)
```

Ein positionelles Argument `prompt` und ein optionales `--limit` (Standard 5). Der Handler:

```python
if args.command == 'route':
    matches = PortRuntime().route_prompt(args.prompt, limit=args.limit)
    if not matches:
        print('No mirrored command/tool matches found.')
        return 0
    for match in matches:
        print(f'{match.kind}\t{match.name}\t{match.score}\t{match.source_hint}')
    return 0
```

Es wird eine neue `PortRuntime`-Instanz erzeugt und deren `route_prompt()`-Methode aufgerufen. Die Ergebnisse werden als tabulatorgetrennte Zeilen ausgegeben, jeweils mit Art (command oder tool), Name, Relevanz-Score und Herkunftshinweis. Werden keine Treffer gefunden, wird eine entsprechende Meldung ausgegeben — der Exit-Code bleibt dennoch 0, da das Fehlen von Treffern kein Fehler ist.

#### `bootstrap`

```python
bootstrap_parser = subparsers.add_parser('bootstrap',
    help='build a runtime-style session report from the mirrored inventories')
bootstrap_parser.add_argument('prompt')
bootstrap_parser.add_argument('--limit', type=int, default=5)
```

Gleiche Argument-Struktur wie `route`. Der Handler:

```python
if args.command == 'bootstrap':
    print(PortRuntime().bootstrap_session(args.prompt, limit=args.limit).as_markdown())
    return 0
```

Hier wird `bootstrap_session()` aufgerufen, das eine vollständige Session-Struktur aufbaut und als Markdown-Bericht ausgibt. Dies entspricht dem Initialisierungsschritt einer Laufzeit-Session, bei dem Befehle und Tools für einen bestimmten Prompt zusammengestellt werden.

#### `turn-loop`

```python
loop_parser = subparsers.add_parser('turn-loop',
    help='run a small stateful turn loop for the mirrored runtime')
loop_parser.add_argument('prompt')
loop_parser.add_argument('--limit', type=int, default=5)
loop_parser.add_argument('--max-turns', type=int, default=3)
loop_parser.add_argument('--structured-output', action='store_true')
```

Der funktionsreichste Befehl in dieser Kategorie mit vier Argumenten:

- `prompt` (positionell): Der initiale Prompt.
- `--limit` (int, Standard 5): Begrenzung der Tool-/Befehlsauswahl.
- `--max-turns` (int, Standard 3): Maximale Anzahl von Gesprächsrunden.
- `--structured-output` (Boolean-Flag): Aktiviert strukturierte Ausgabe.

Der Handler:

```python
if args.command == 'turn-loop':
    results = PortRuntime().run_turn_loop(
        args.prompt,
        limit=args.limit,
        max_turns=args.max_turns,
        structured_output=args.structured_output
    )
    for idx, result in enumerate(results, start=1):
        print(f'## Turn {idx}')
        print(result.output)
        print(f'stop_reason={result.stop_reason}')
    return 0
```

Die `run_turn_loop()`-Methode liefert eine Liste von Ergebnissen zurück — eines pro Gesprächsrunde. Jedes Ergebnis wird mit einer Markdown-Überschrift (`## Turn N`), dem Ausgabetext und dem Abbruchgrund formatiert. Dies ermöglicht die Nachverfolgung des gesamten Gesprächsverlaufs.

---

### Kategorie 5: Session-Verwaltung

Diese beiden Befehle befassen sich mit der Persistierung und dem Laden von Sessions.

#### `flush-transcript`

```python
flush_parser = subparsers.add_parser('flush-transcript',
    help='persist and flush a temporary session transcript')
flush_parser.add_argument('prompt')
```

Ein positionelles Argument `prompt`. Der Handler:

```python
if args.command == 'flush-transcript':
    engine = QueryEnginePort.from_workspace()
    engine.submit_message(args.prompt)
    path = engine.persist_session()
    print(path)
    print(f'flushed={engine.transcript_store.flushed}')
    return 0
```

Hier wird eine `QueryEnginePort`-Instanz über die Klassenmethode `from_workspace()` erzeugt (im Gegensatz zu `summary`, wo das Manifest explizit übergeben wird). Anschließend wird eine Nachricht eingereicht, die Session persistiert, und der Dateipfad sowie der Flush-Status ausgegeben. Die zweite Ausgabezeile dient der Verifikation: `flushed=True` bestätigt, dass das Transkript erfolgreich geschrieben würde.

#### `load-session`

```python
load_session_parser = subparsers.add_parser('load-session',
    help='load a previously persisted session')
load_session_parser.add_argument('session_id')
```

Ein positionelles Argument `session_id`. Der Handler:

```python
if args.command == 'load-session':
    session = load_session(args.session_id)
    print(f'{session.session_id}\n{len(session.messages)} messages\n'
          f'in={session.input_tokens} out={session.output_tokens}')
    return 0
```

Die Funktion `load_session()` aus dem Modul `.session_store` lädt eine zuvor persistierte Session anhand ihrer ID. Die Ausgabe enthält die Session-ID, die Anzahl der Nachrichten und die Token-Statistiken (Eingabe- und Ausgabe-Tokens). Diese kompakte Zusammenfassung eignet sich hervorragend zur schnellen Diagnose.

---

### Kategorie 6: Laufzeitmodi

Fünf Befehle simulieren verschiedene Laufzeit-Verzweigungen. Sie teilen alle dieselbe Argument-Struktur: ein einziges positionelles Argument `target`.

#### `remote-mode`

```python
remote_parser = subparsers.add_parser('remote-mode',
    help='simulate remote-control runtime branching')
remote_parser.add_argument('target')
```

Handler:

```python
if args.command == 'remote-mode':
    print(run_remote_mode(args.target).as_text())
    return 0
```

Simuliert eine Fernsteuerungs-Laufzeitverzweigung. Die Funktion `run_remote_mode()` stammt aus `.remote_runtime`.

#### `ssh-mode`

```python
ssh_parser = subparsers.add_parser('ssh-mode',
    help='simulate SSH runtime branching')
ssh_parser.add_argument('target')
```

Handler:

```python
if args.command == 'ssh-mode':
    print(run_ssh_mode(args.target).as_text())
    return 0
```

Simuliert eine SSH-Laufzeitverzweigung. Auch diese Funktion stammt aus `.remote_runtime`.

#### `teleport-mode`

```python
teleport_parser = subparsers.add_parser('teleport-mode',
    help='simulate teleport runtime branching')
teleport_parser.add_argument('target')
```

Handler:

```python
if args.command == 'teleport-mode':
    print(run_teleport_mode(args.target).as_text())
    return 0
```

Die dritte Variante aus `.remote_runtime`. „Teleport" bezeichnet hier einen spezifischen Verbindungsmodus, bei dem der Kontext direkt an ein entferntes Ziel übertragen wird.

#### `direct-connect-mode`

```python
direct_parser = subparsers.add_parser('direct-connect-mode',
    help='simulate direct-connect runtime branching')
direct_parser.add_argument('target')
```

Handler:

```python
if args.command == 'direct-connect-mode':
    print(run_direct_connect(args.target).as_text())
    return 0
```

Diese und die folgende Funktion stammen aus `.direct_modes` — einem separaten Modul, das sich von `.remote_runtime` unterscheidet. Dies deutet auf eine architektonische Unterscheidung zwischen „entfernten" und „direkten" Verbindungsmodi hin.

#### `deep-link-mode`

```python
deep_link_parser = subparsers.add_parser('deep-link-mode',
    help='simulate deep-link runtime branching')
deep_link_parser.add_argument('target')
```

Handler:

```python
if args.command == 'deep-link-mode':
    print(run_deep_link(args.target).as_text())
    return 0
```

Der fünfte und letzte Laufzeitmodus. Alle fünf Modi folgen demselben Muster: Target entgegennehmen, Handler aufrufen, Ergebnis über `as_text()` formatieren und ausgeben. Diese Konsistenz vereinfacht das Verständnis und die Wartung erheblich.

---

### Kategorie 7: Architekturanalyse

Vier Befehle liefern tiefgreifende Analysen der Projektarchitektur. Keiner benötigt Argumente.

#### `command-graph`

```python
subparsers.add_parser('command-graph',
    help='show command graph segmentation')
```

Handler:

```python
if args.command == 'command-graph':
    print(build_command_graph().as_markdown())
    return 0
```

Erzeugt eine graphbasierte Darstellung der Befehlssegmentierung. Die Funktion `build_command_graph()` aus `.command_graph` liefert ein Objekt mit einer `as_markdown()`-Methode. Dieser Befehl ist besonders nützlich, um die Abhängigkeiten und Gruppierungen innerhalb des Befehlskatalogs zu verstehen.

#### `tool-pool`

```python
subparsers.add_parser('tool-pool',
    help='show assembled tool pool with default settings')
```

Handler:

```python
if args.command == 'tool-pool':
    print(assemble_tool_pool().as_markdown())
    return 0
```

Zeigt den zusammengestellten Tool-Pool mit Standardeinstellungen an. Die Funktion `assemble_tool_pool()` aus `.tool_pool` aggregiert alle verfügbaren Tools und stellt sie in einer strukturierten Übersicht dar.

#### `bootstrap-graph`

```python
subparsers.add_parser('bootstrap-graph',
    help='show the mirrored bootstrap/runtime graph stages')
```

Handler:

```python
if args.command == 'bootstrap-graph':
    print(build_bootstrap_graph().as_markdown())
    return 0
```

Visualisiert die Stufen des Bootstrap-Prozesses — also die Schritte, die beim Hochfahren der Laufzeitumgebung durchlaufen werden.

#### `parity-audit`

```python
subparsers.add_parser('parity-audit',
    help='compare the Python workspace against the local ignored TypeScript archive when available')
```

Handler:

```python
if args.command == 'parity-audit':
    print(run_parity_audit().to_markdown())
    return 0
```

Ein besonders wichtiger Befehl im Kontext des Portierungsprojekts: Er vergleicht den aktuellen Python-Workspace mit dem archivierten TypeScript-Original und identifiziert Abweichungen. Die Methode heißt hier `to_markdown()` (statt `as_markdown()` wie bei den anderen) — eine kleine Inkonsistenz in der Benennung, die aber funktional keinen Unterschied macht.

---

## 4.3 Die `main()`-Funktion

```python
def main(argv: list[str] | None = None) -> int:
```

Die `main()`-Funktion ist der eigentliche Einstiegspunkt der Anwendung. Sie akzeptiert ein optionales `argv`-Argument (eine Liste von Strings), das standardmässig `None` ist. Wenn `None`, verwendet `argparse` automatisch `sys.argv[1:]`. Die Möglichkeit, `argv` explizit zu übergeben, ist entscheidend für die Testbarkeit: In Tests kann die Funktion direkt mit beliebigen Argumentlisten aufgerufen werden, ohne `sys.argv` manipulieren zu müssen.

### 4.3.1 Initialisierung

```python
parser = build_parser()
args = parser.parse_args(argv)
manifest = build_port_manifest()
```

Die ersten drei Zeilen bilden die Initialisierungsphase:

1. Der Parser wird über `build_parser()` erzeugt.
2. Die Kommandozeilenargumente werden geparst. Scheitert dies (z. B. wegen eines unbekannten Subcommands oder fehlender Pflichtargumente), beendet argparse das Programm automatisch mit einer Fehlermeldung.
3. Das Port-Manifest wird gebaut. Dieses Manifest wird von mehreren Befehlen benötigt und wird daher einmalig zu Beginn erzeugt — ein Beispiel für das „Eager Loading"-Muster.

### 4.3.2 Die Dispatch-Logik

Die gesamte Dispatch-Logik besteht aus einer linearen Kette von `if`-Abfragen auf `args.command`. Es wird kein `match`-Statement (Python 3.10+), kein Dictionary-Dispatch und kein anderes Muster verwendet. Die Wahl einer einfachen `if`-Kette hat Vor- und Nachteile:

**Vorteile:**
- Maximale Lesbarkeit: Jeder Befehl ist sofort auffindbar.
- Flexibilität: Jeder Handler kann beliebig komplex sein, ohne in ein einheitliches Schema gepresst zu werden.
- Debuggbarkeit: Breakpoints können einfach an einzelnen Stellen gesetzt werden.

**Nachteile:**
- Skalierbarkeit: Bei deutlich mehr Befehlen würde die Funktion unübersichtlich lang.
- Wiederholung: Das Muster `if args.command == '...': ... return 0` wird 24 Mal wiederholt.

Die Autoren haben sich bewusst für die einfache Variante entschieden, die bei 24 Befehlen noch gut handhabbar ist.

### 4.3.3 Rückgabewerte und Fehlerbehandlung

Jeder Handler gibt explizit einen ganzzahligen Exit-Code zurück:

- **0** signalisiert Erfolg.
- **1** signalisiert einen anwendungsspezifischen Fehler (z. B. „Command not found" bei `show-command` und `show-tool`, oder `handled == False` bei `exec-command` und `exec-tool`).
- **2** wird am Ende der Funktion für unbekannte Befehle zurückgegeben (ein Sicherheitsnetz, das in der Praxis nie erreicht werden sollte, da argparse unbekannte Subcommands bereits abfängt).

```python
parser.error(f'unknown command: {args.command}')
return 2
```

Der Aufruf von `parser.error()` gibt eine formatierte Fehlermeldung aus und beendet das Programm mit Exit-Code 2. Das nachfolgende `return 2` ist technisch unerreichbar, dient aber als Typannotations-Hilfe und Sicherheitsnetz.

### 4.3.4 Der `__main__`-Block

```python
if __name__ == '__main__':
    raise SystemExit(main())
```

Die letzte Zeile der Datei ermöglicht die direkte Ausführung als Skript. `raise SystemExit(main())` wandelt den von `main()` zurückgegebenen Integer in einen Prozess-Exit-Code um. Die Verwendung von `raise SystemExit()` anstelle von `sys.exit()` ist eine bewusste stilistische Wahl: Sie vermeidet den Import von `sys` und macht die Absicht — das Programm mit einem bestimmten Exit-Code zu beenden — expliziter.

---

## 4.4 Architektonische Beobachtungen

### Einheitliche Ausgabemuster

Die Datei zeigt zwei Hauptmuster für die Ausgabeformatierung:

1. **Markdown-Methoden** (`as_markdown()`, `to_markdown()`): Verwendet von `summary`, `manifest`, `setup-report`, `command-graph`, `tool-pool`, `bootstrap-graph`, `bootstrap` und `parity-audit`.
2. **Text-Methoden** (`as_text()`): Verwendet von allen fünf Laufzeitmodi.
3. **Direkte Formatierung**: Verwendet von `subsystems`, `commands`, `tools`, `route`, `turn-loop`, `flush-transcript` und `load-session`.

### Zwei Laufzeit-Objekte

Die Datei verwendet zwei verschiedene Laufzeit-Abstraktionen:

- `QueryEnginePort`: Für Workspace-bezogene Operationen (Summary, Flush).
- `PortRuntime`: Für Routing- und Session-Operationen (Route, Bootstrap, Turn-Loop).

Diese Trennung spiegelt die Architektur des Gesamtsystems wider: Die Query-Engine ist eine Inspektionsschicht, die Runtime eine Ausführungsschicht.

### Testbarkeit durch Design

Die gesamte Datei ist testfreundlich gestaltet: `build_parser()` kann isoliert getestet werden, `main()` akzeptiert ein explizites `argv`, und alle Handler delegieren sofort an importierte Funktionen. Es gibt keinen globalen Zustand und keine Seiteneffekte außerhalb der Handler-Aufrufe.

---

## 4.5 Zusammenfassung

Die Datei `src/main.py` ist der zentrale CLI-Einstiegspunkt des Claw-Code-Projekts. Mit 24 Subcommands, die in sieben funktionale Kategorien fallen, bietet sie einen umfassenden Zugang zu allen Aspekten des Python-Portierungs-Workspace — von der einfachen Inspektion über die Befehlsausführung bis hin zur Architekturanalyse. Die Trennung in `build_parser()` (Konfiguration) und `main()` (Dispatch) ist sauber, die Delegation an spezialisierte Module konsequent, und die Fehlerbehandlung über Exit-Codes folgt Unix-Konventionen. Trotz der Einfachheit der linearen `if`-Kette bleibt der Code übersichtlich und wartbar — ein solides Fundament für die gesamte CLI-Schicht des Projekts.


# Kapitel 5: Datenmodelle & Typsystem

## 5.1 Einführung -- Warum Datenmodelle das Rückgrat jeder Architektur sind

In jeder nicht-trivialen Software stellt sich frueh die Frage: Wie repräsentieren wir die Konzepte unserer Domaene im Code? Claw Code beantwortet diese Frage mit einer kleinen, aber durchdacht geschichteten Sammlung von **Dataclasses**, die in drei Dateien leben:

| Datei | Klassen | Zeilen |
|---|---|---|
| `src/models.py` | `Subsystem`, `PortingModule`, `PermissionDenial`, `UsageSummary`, `PortingBacklog` | 50 |
| `src/query.py` | `QueryRequest`, `QueryResponse` | 14 |
| `src/Tool.py` | `ToolDefinition`, `DEFAULT_TOOLS` | 16 |

Zusammen umfassen diese drei Dateien weniger als 80 Zeilen -- und dennoch definieren sie das gesamte Vokabular, mit dem saemtliche anderen Module kommunizieren. In diesem Kapitel werden wir jede einzelne Klasse, jedes Feld, jede Methode und jede Entwurfsentscheidung im Detail untersuchen.

---

## 5.2 Frozen Dataclasses als Wertobjekte

### 5.2.1 Das Prinzip der Unveränderlichkeit

Sechs der acht Klassen im Datenmodell tragen den Dekorator `@dataclass(frozen=True)`. Was bedeutet das konkret? Python erzeugt für solche Klassen automatisch `__setattr__`- und `__delattr__`-Methoden, die jede nachtraegliche Änderung mit einem `FrozenInstanceError` quittieren:

```python
from src.models import PortingModule

mod = PortingModule(
    name='query_engine',
    responsibility='LLM-Abfragen ausfuehren',
    source_hint='session.ts',
    status='planned',
)

mod.status = 'done'  # -> FrozenInstanceError!
```

Dieses Verhalten ist kein Zufall, sondern eine bewusste Entwurfsentscheidung. In der Terminologie von Domain-Driven Design handelt es sich bei frozen Dataclasses um **Wertobjekte** (Value Objects). Ein Wertobjekt ist vollständig durch seine Attribute definiert -- es besitzt keine eigene Identitaet, die sich unabhängig von seinen Feldern ändern könnte. Zwei `PortingModule`-Instanzen mit denselben Feldern sind *gleich*, und sie bleiben gleich, solange sie existieren.

### 5.2.2 Hashing und Verwendung in Mengen

Frozen Dataclasses sind automatisch **hashbar**. Python generiert eine `__hash__`-Methode auf Basis aller Felder. Das erlaubt Konstrukte wie:

```python
seen = set()
seen.add(PortingModule('a', 'Aufgabe A', 'file_a.ts'))
seen.add(PortingModule('a', 'Aufgabe A', 'file_a.ts'))
assert len(seen) == 1  # Duplikat wird erkannt
```

Oder als Dictionary-Schlüssel:

```python
stats: dict[PortingModule, int] = {
    PortingModule('query_engine', 'Abfragen', 'session.ts'): 42,
}
```

In einem System, das Module entdeckt, klassifiziert und in verschiedenen Phasen verarbeitet, ist die Fähigkeit, sie in `set`- und `dict`-Strukturen zu verwenden, enorm wertvoll. Ohne `frozen=True` wäre dies nicht möglich, da mutable Dataclasses in Python standardmäßig nicht hashbar sind.

### 5.2.3 Thread-Sicherheit und Vorhersagbarkeit

Ein weiterer Vorteil der Unveränderlichkeit: In einem System, in dem Daten durch mehrere Verarbeitungsstufen fliessen -- von der Analyse über die Planung bis zur Ausführung -- koennen frozen Objekte gefahrlos zwischen Funktionen, Modulen und potentiell sogar Threads weitergereicht werden, ohne dass eine defensive Kopie nötig ist. Wenn eine Funktion ein `Subsystem`-Objekt empfaengt, kann sie sicher sein, dass niemand es nachtraeglich verändert.

---

## 5.3 Mutable vs. Immutable -- Zwei Strategien, eine Architektur

Von den fünf Klassen in `models.py` ist genau **eine** mutable: `PortingBacklog`. Dies ist kein Versehen, sondern folgt einer klaren Logik.

### Immutable (frozen=True):

- `Subsystem` -- ein entdecktes Teilsystem ändert sich nicht; es wird *einmal analysiert, dann festgehalten*
- `PortingModule` -- ein geplantes Modul ist eine Spezifikation; Änderungen erzeugen ein neues Objekt
- `PermissionDenial` -- eine Verweigerung ist ein Fakt, der protokolliert wird
- `UsageSummary` -- Token-Zähler; Aktualisierung erzeugt ein *neues* Summary (funktionaler Stil)

### Mutable:

- `PortingBacklog` -- eine wachsende Sammlung von Modulen, die sich während der Laufzeit verändert

Die Entscheidung ist pragmatisch: Ein Backlog ist seinem Wesen nach eine **veränderliche Liste**. Module werden hinzugefuegt, umpriorisiert, entfernt. Eine frozen-Variante würde bei jeder Änderung eine vollständige Kopie erfordern -- das wäre in Python unnötig umstaendlich und würde keinen echten Sicherheitsgewinn bringen, da das Backlog typischerweise an einer zentralen Stelle verwaltet wird.

`UsageSummary` hingegen wählt den entgegengesetzten Weg: Obwohl sie konzeptuell einen sich ändernden Zähler darstellt, ist sie `frozen=True` und realisiert Änderungen durch die Erzeugung neuer Instanzen. Dies folgt dem funktionalen Paradigma und ermöglicht es, die Historie von Token-Nutzungen als Kette unveränderlicher Snapshots zu modellieren.

---

## 5.4 Die Klassen im Detail

### 5.4.1 `Subsystem`

```python
@dataclass(frozen=True)
class Subsystem:
    name: str
    path: str
    file_count: int
    notes: str
```

**Zweck:** Repräsentiert ein entdecktes Teilsystem im analysierten Quellcode. Wird von `port_manifest.py` erzeugt und importiert:

```python
# src/port_manifest.py
from .models import Subsystem
```

**Felder:**

| Feld | Typ | Beschreibung |
|---|---|---|
| `name` | `str` | Menschenlesbarer Name des Subsystems, z.B. `"CLI-Kern"` |
| `path` | `str` | Dateipfad oder Verzeichnis, in dem das Subsystem lebt |
| `file_count` | `int` | Anzahl der zum Subsystem gehörenden Dateien |
| `notes` | `str` | Freitextnotizen, z.B. Hinweise auf Abhängigkeiten |

Alle vier Felder sind Pflichtfelder (keine Defaults). Das ist sinnvoll: Ein Subsystem ohne Pfad oder ohne Dateianzahl wäre unvollständig und darf gar nicht erst erzeugt werden.

**Typische Verwendung:**

```python
sub = Subsystem(
    name='Session-Management',
    path='src/session/',
    file_count=12,
    notes='Abhaengigkeit zu auth-Modul',
)
```

### 5.4.2 `PortingModule`

```python
@dataclass(frozen=True)
class PortingModule:
    name: str
    responsibility: str
    source_hint: str
    status: str = 'planned'
```

**Zweck:** Die zentrale und vielseitigste Datenklasse des gesamten Projekts. Ein `PortingModule` repräsentiert eine **geplante oder bereits umgesetzte Arbeitseinheit** -- das kann ein CLI-Befehl sein, ein Tool, ein Dienstprogramm oder jede andere funktionale Einheit, die im Rahmen der Portierung erstellt werden soll.

**Felder:**

| Feld | Typ | Default | Beschreibung |
|---|---|---|---|
| `name` | `str` | -- | Bezeichner des Moduls, z.B. `"query_engine"` oder `"port_manifest"` |
| `responsibility` | `str` | -- | Kurzbeschreibung der Aufgabe, z.B. `"LLM-Abfragen ausfuehren"` |
| `source_hint` | `str` | -- | Hinweis auf die Ursprungsdatei im Referenzprojekt, z.B. `"session.ts"` |
| `status` | `str` | `'planned'` | Aktueller Zustand: `'planned'`, `'in_progress'`, `'done'` etc. |

Das Feld `status` besitzt den Default-Wert `'planned'`, was die häufigste Entstehungssituation widerspiegelt: Neue Module werden zuerst geplant und später umgesetzt. Durch den Default-Wert genuegt es, beim Erzeugen nur die drei Pflichtfelder anzugeben:

```python
mod = PortingModule('tool_pool', 'Werkzeugverwaltung', 'tools.ts')
assert mod.status == 'planned'
```

**Universelle Repräsentation -- Befehle UND Tools:**

Ein besonders eleganter Aspekt dieser Klasse ist ihre Doppelrolle. In Claw Code gibt es keine separate `Command`- oder `Tool`-Modellklasse auf Domaenenebene. Stattdessen wird `PortingModule` sowohl für CLI-Befehle als auch für registrierte Tools verwendet. Die Unterscheidung erfolgt rein über den Kontext, in dem das Objekt verwendet wird:

```python
# Als CLI-Befehl (in commands.py / command_graph.py)
from .models import PortingModule
cmd = PortingModule('plan', 'Porting-Plan erstellen', 'commands.ts')

# Als Tool (in tools.py / tool_pool.py)
from .models import PortingModule
tool = PortingModule('port_manifest', 'Workspace zusammenfassen', 'tools.ts')
```

Diese Vereinheitlichung reduziert die Anzahl der Klassen, vermeidet Redundanz und drückt eine wichtige architektonische Erkenntnis aus: Aus Sicht des Porting-Systems sind Befehle und Tools strukturell identisch -- sie haben einen Namen, eine Verantwortlichkeit, einen Ursprung und einen Status. Erst zur Laufzeit unterscheidet das System, wie sie ausgeführt werden.

Die Import-Statistik belegt diese zentrale Rolle: `PortingModule` wird von fünf verschiedenen Modulen importiert -- `commands.py`, `command_graph.py`, `tools.py`, `tool_pool.py` und `runtime.py`. Keine andere Datenklasse ist so breit vernetzt.

### 5.4.3 `PermissionDenial`

```python
@dataclass(frozen=True)
class PermissionDenial:
    tool_name: str
    reason: str
```

**Zweck:** Protokolliert einen Fall, in dem ein Tool-Zugriff verweigert würde. Dies ist für die Sicherheitsarchitektur relevant: Wenn ein Benutzer oder eine automatisierte Aktion versucht, ein Tool auszuführen, für das keine Berechtigung besteht, wird ein `PermissionDenial`-Objekt erzeugt und kann später ausgewertet werden.

**Felder:**

| Feld | Typ | Beschreibung |
|---|---|---|
| `tool_name` | `str` | Name des verweigerten Tools, z.B. `"file_write"` |
| `reason` | `str` | Menschenlesbare Begründung, z.B. `"Schreibzugriff nicht erlaubt"` |

Importiert von:

```python
# src/query_engine.py
from .models import PermissionDenial
# src/runtime.py
from .models import PermissionDenial
```

Die Klasse ist absichtlich minimalistisch. Sie speichert keine Zeitstempel, keine Benutzer-IDs, keine Stack-Traces -- nur den nackten Fakt: *welches* Tool würde verweigert und *warum*. Erweiterte Kontextinformationen koennen bei Bedarf im aufrufenden Code ergaenzt werden.

### 5.4.4 `UsageSummary` -- Funktionale Token-Buchhaltung

```python
@dataclass(frozen=True)
class UsageSummary:
    input_tokens: int = 0
    output_tokens: int = 0

    def add_turn(self, prompt: str, output: str) -> 'UsageSummary':
        return UsageSummary(
            input_tokens=self.input_tokens + len(prompt.split()),
            output_tokens=self.output_tokens + len(output.split()),
        )
```

**Zweck:** Verfolgt den kumulativen Token-Verbrauch über mehrere Gespraechsrunden hinweg. Trotz der `frozen=True`-Deklaration bietet die Klasse eine Methode zur "Aktualisierung" -- allerdings im funktionalen Stil.

**Felder:**

| Feld | Typ | Default | Beschreibung |
|---|---|---|---|
| `input_tokens` | `int` | `0` | Geschätzte Anzahl eingegebener Tokens |
| `output_tokens` | `int` | `0` | Geschätzte Anzahl ausgegebener Tokens |

Beide Felder haben den Default `0`, was das Erzeugen eines leeren Summaries erlaubt:

```python
summary = UsageSummary()  # input_tokens=0, output_tokens=0
```

**Die Methode `add_turn()` im Detail:**

```python
def add_turn(self, prompt: str, output: str) -> 'UsageSummary':
    return UsageSummary(
        input_tokens=self.input_tokens + len(prompt.split()),
        output_tokens=self.output_tokens + len(output.split()),
    )
```

Diese Methode ist das Herzpunkt des funktionalen Musters. Sie verändert die bestehende Instanz *nicht* (das wäre aufgrund von `frozen=True` ohnehin unmöglich), sondern erzeugt eine **neue** `UsageSummary` mit aktualisierten Zählerstaenden.

**Token-Schätzung per Wortanzahl:**

Die Token-Schätzung erfolgt über `len(prompt.split())` bzw. `len(output.split())`. Das ist eine bewusste Vereinfachung: Echte Tokenizer (wie der von OpenAI oder Anthropic) zerlegen Text in Subword-Einheiten, die nicht mit Wortgrenzen übereinstimmen. Ein Wort wie "Unveränderlichkeit" könnte je nach Tokenizer in 3--5 Tokens zerlegt werden, `split()` zählt es als ein Wort.

Warum diese Vereinfachung? Drei Gründe:

1. **Keine Abhängigkeit:** Ein echter Tokenizer würde eine externe Bibliothek erfordern (z.B. `tiktoken`), was die Abhängigkeitskette vergrößert.
2. **Ausreichende Genauigkeit:** Für die Zwecke einer Verbrauchsübersicht -- nicht einer exakten Abrechnung -- ist die Wortanzahl ein brauchbarer Näherungswert. Typischerweise liegt das Verhältnis bei ca. 1,3 Tokens pro Wort im Englischen.
3. **Geschwindigkeit:** `str.split()` ist eine der schnellsten String-Operationen in Python und verursacht keine nennenswerte Latenz.

**Typischer Einsatz als Kette:**

```python
summary = UsageSummary()
summary = summary.add_turn("Analysiere das Projekt", "Das Projekt hat 5 Module.")
summary = summary.add_turn("Zeige Details", "Modul A ist fuer X zustaendig.")

print(summary.input_tokens)   # 5 (3 + 2)
print(summary.output_tokens)  # 12 (6 + 6)
```

Jede Zuweisung an `summary` überschreibt die Referenz, nicht das Objekt. Die alten Instanzen werden vom Garbage Collector eingesammelt. Dieses Muster ist identisch mit dem Umgang mit unveränderlichen Strings in Python (`s = s + "x"`) und für Python-Entwickler intuitiv verstaendlich.

### 5.4.5 `PortingBacklog` -- Die mutable Ausnahme

```python
@dataclass
class PortingBacklog:
    title: str
    modules: list[PortingModule] = field(default_factory=list)

    def summary_lines(self) -> list[str]:
        return [
            f'- {module.name} [{module.status}] — {module.responsibility} (from {module.source_hint})'
            for module in self.modules
        ]
```

**Zweck:** Verwaltet eine benannte Sammlung von `PortingModule`-Eintraegen. Dies ist die einzige mutable Datenklasse in `models.py`, erkennbar am fehlenden `frozen=True`.

**Felder:**

| Feld | Typ | Default | Beschreibung |
|---|---|---|---|
| `title` | `str` | -- | Titel des Backlogs, z.B. `"Claw Code Porting-Plan"` |
| `modules` | `list[PortingModule]` | `[]` (via `field(default_factory=list)`) | Liste der geplanten Module |

Beachtenswert ist die Verwendung von `field(default_factory=list)` statt eines einfachen `= []`. Dies ist ein beruehmt-beruechtigtes Python-Muster: Würde man `modules: list = []` schreiben, würden *alle* Instanzen dieselbe Liste teilen -- ein klassischer und heimtueckischer Bug. `default_factory=list` stellt sicher, dass jede Instanz ihre eigene, leere Liste erhält.

**Die Methode `summary_lines()` im Detail:**

```python
def summary_lines(self) -> list[str]:
    return [
        f'- {module.name} [{module.status}] — {module.responsibility} (from {module.source_hint})'
        for module in self.modules
    ]
```

Diese Methode erzeugt eine Markdown-kompatible Darstellung aller Module im Backlog. Jede Zeile folgt dem Schema:

```
- <name> [<status>] — <responsibility> (from <source_hint>)
```

**Beispiel:**

```python
backlog = PortingBacklog(title='Claw Code Hauptplan')
backlog.modules.append(
    PortingModule('query_engine', 'LLM-Abfragen', 'session.ts', 'in_progress')
)
backlog.modules.append(
    PortingModule('tool_pool', 'Werkzeugverwaltung', 'tools.ts')
)

for line in backlog.summary_lines():
    print(line)
```

Ausgabe:

```
- query_engine [in_progress] — LLM-Abfragen (from session.ts)
- tool_pool [planned] — Werkzeugverwaltung (from tools.ts)
```

Das Markdown-Format ist bewusst gewählt: Die Ausgabe kann direkt in Berichts-Dateien, Terminal-Ausgaben oder Chat-Antworten eingefuegt werden. Der em-Dash (`---`) und die eckigen Klammern um den Status erzeugen ein visuell klares, scanfreundliches Layout.

Die Methode ist als **reine Lesemethode** implementiert -- sie verändert die Liste nicht, sondern projiziert sie in eine neue Liste von Strings. Dies ist ein gutes Beispiel für das Zusammenspiel von Mutabilitaet und Reinheit: Die Klasse selbst ist mutable (Module koennen hinzugefuegt werden), aber ihre Abfragemethoden erzeugen keine Seiteneffekte.

---

## 5.5 Query-Datenmodelle (`src/query.py`)

```python
@dataclass(frozen=True)
class QueryRequest:
    prompt: str

@dataclass(frozen=True)
class QueryResponse:
    text: str
```

Diese beiden Klassen bilden ein klassisches **Request/Response-Paar**. Ihre extreme Schlichtheit -- je ein einziges Feld -- ist kein Zeichen von Unreife, sondern eine bewusste Entscheidung.

### 5.5.1 `QueryRequest`

| Feld | Typ | Beschreibung |
|---|---|---|
| `prompt` | `str` | Der Abfragetext, der an die Query-Engine gesendet wird |

Warum nicht einfach einen `str` übergeben? Weil eine eigene Klasse mehrere Vorteile bietet:

1. **Typsicherheit:** Eine Funktion `def execute(request: QueryRequest)` ist präziser als `def execute(prompt: str)`. Der Typ kommuniziert die *Absicht*.
2. **Erweiterbarkeit:** Später koennen Felder wie `temperature`, `max_tokens` oder `system_prompt` hinzugefuegt werden, ohne bestehende Signaturen zu ändern.
3. **Einheitlichkeit:** Alle Daten im System fliessen als typisierte Objekte, nicht als lose Strings.

### 5.5.2 `QueryResponse`

| Feld | Typ | Beschreibung |
|---|---|---|
| `text` | `str` | Der Antworttext der Query-Engine |

Auch hier gilt: Die Klasse ist ein Erweiterungspunkt. Künftige Felder wie `token_count`, `model_id` oder `finish_reason` könnten das Response-Objekt anreichern.

Beide Klassen sind `frozen=True`, da weder eine Anfrage noch eine Antwort nach ihrer Erzeugung verändert werden sollte. Sie sind Fakten, keine Zustaende.

---

## 5.6 Tool-Definitionen (`src/Tool.py`)

```python
@dataclass(frozen=True)
class ToolDefinition:
    name: str
    purpose: str

DEFAULT_TOOLS = (
    ToolDefinition('port_manifest', 'Summarize the active Python workspace'),
    ToolDefinition('query_engine', 'Render a Python-first porting summary'),
)
```

### 5.6.1 `ToolDefinition`

| Feld | Typ | Beschreibung |
|---|---|---|
| `name` | `str` | Maschinenlesbarer Bezeichner des Tools |
| `purpose` | `str` | Menschenlesbare Beschreibung des Verwendungszwecks |

Die Klasse beschreibt ein verfügbares Werkzeug im System. Sie ist `frozen=True`, da Tool-Definitionen zur Laufzeit nicht verändert werden -- ein Tool hat einen festen Namen und einen festen Zweck.

### 5.6.2 `DEFAULT_TOOLS`

```python
DEFAULT_TOOLS = (
    ToolDefinition('port_manifest', 'Summarize the active Python workspace'),
    ToolDefinition('query_engine', 'Render a Python-first porting summary'),
)
```

Bemerkenswert: `DEFAULT_TOOLS` ist ein **Tupel**, kein Liste. Dies verstärkt die Unveränderlichkeits-Philosophie auf Sammlungsebene. Während `ToolDefinition`-Instanzen per `frozen=True` geschuetzt sind, würde eine `list` es erlauben, Elemente hinzuzufuegen oder zu entfernen. Ein `tuple` schließt auch das aus.

Die beiden Standard-Tools -- `port_manifest` und `query_engine` -- spiegeln die Kernfunktionalitaet wider: Analyse des Workspaces und Erzeugung von Porting-Zusammenfassungen.

### 5.6.3 Abgrenzung zu `PortingModule`

Man könnte fragen: Warum gibt es neben `PortingModule` auch `ToolDefinition`? Der Unterschied liegt in der Abstraktionsebene:

- `PortingModule` beschreibt ein geplantes oder implementiertes Modul *im Kontext der Portierung* -- mit Status, Verantwortlichkeit und Quellhinweis.
- `ToolDefinition` beschreibt ein *registriertes Werkzeug* im laufenden System -- mit Name und Zweck, aber ohne Portierungskontext.

`PortingModule` ist ein Planungsobjekt; `ToolDefinition` ist ein Laufzeitobjekt. Beide koennen dasselbe reale Modul repräsentieren, aber aus unterschiedlichen Perspektiven.

---

## 5.7 `models.py` als gemeinsames Fundament

Die Datei `src/models.py` bildet das **gemeinsame Fundament** des gesamten Projekts. Jedes nennenswerte Modul importiert mindestens eine Klasse daraus:

| Importierendes Modul | Importierte Klassen |
|---|---|
| `src/commands.py` | `PortingBacklog`, `PortingModule` |
| `src/command_graph.py` | `PortingModule` |
| `src/tools.py` | `PortingBacklog`, `PortingModule` |
| `src/tool_pool.py` | `PortingModule` |
| `src/runtime.py` | `PermissionDenial`, `PortingModule` |
| `src/query_engine.py` | `PermissionDenial`, `UsageSummary` |
| `src/port_manifest.py` | `Subsystem` |

Dieses Importmuster zeigt eine sternfoermige Abhängigkeitsstruktur: `models.py` steht im Zentrum und hat selbst *keine* Abhängigkeiten zu anderen Projektmodulen (es importiert nur `dataclass` und `field` aus der Standardbibliothek). Das ist eine bewusste und wichtige Eigenschaft:

1. **Zyklenfreiheit:** Da `models.py` nichts aus dem Projekt importiert, koennen keine zirkulaeren Abhängigkeiten entstehen.
2. **Stabiliaet:** Änderungen an der Geschäftslogik in `commands.py` oder `runtime.py` beruehren die Datenmodelle nicht.
3. **Testbarkeit:** Die Modellklassen koennen isoliert getestet werden, ohne Mocking oder Setup.

Das `from __future__ import annotations` am Anfang jeder Datei ermöglicht die Verwendung von Forward-References in Typ-Annotationen. In `UsageSummary.add_turn()` wird der Rückgabetyp als String `'UsageSummary'` annotiert -- mit dem Future-Import wird dies auch ohne Anfuehrungszeichen möglich (in älteren Python-Versionen vor 3.10 war dies noch notwendig).

---

## 5.8 Entwurfsmuster und Zusammenfassung

Die Datenmodelle von Claw Code folgen mehreren bewährten Entwurfsprinzipien:

**Value Object Pattern:** Frozen Dataclasses sind klassische Wertobjekte -- unveränderlich, gleichheitsbasiert, hashbar. Sie repräsentieren Konzepte wie "ein Subsystem" oder "eine Berechtigungsverweigerung" als reine Daten ohne Verhalten (abgesehen von `add_turn` und `summary_lines`).

**Immutable-by-Default, Mutable-by-Exception:** Die überwältigende Mehrheit der Klassen ist `frozen`. Nur dort, wo Mutabilitaet dem natürlichen Lebenszyklus des Objekts entspricht (wie beim wachsenden Backlog), wird auf `frozen` verzichtet.

**Functional Update Pattern:** `UsageSummary.add_turn()` demonstriert, wie man unveränderliche Objekte "aktualisieren" kann, indem man neue Instanzen mit veränderten Werten erzeugt. Dieses Muster ist aus funktionalen Sprachen bekannt und führt zu vorhersagbarem, gut testbarem Code.

**Shared Kernel:** `models.py` dient als geteilter Kern (Shared Kernel), der die gemeinsame Sprache aller Module definiert. Es ist die einzige Datei, die von allen anderen abhängt, und es hängt selbst von nichts ab.

**Separation of Concerns:** Abfrage-Datenmodelle (`query.py`) und Tool-Definitionen (`Tool.py`) leben in eigenen Dateien, obwohl sie nur je zwei Definitionen enthalten. Dies hält die thematische Trennung aufrecht: Domaenenobjekte, Abfrage-Protokoll und Werkzeugregistrierung sind drei verschiedene Belange.

Mit weniger als 80 Zeilen Code etabliert das Typsystem von Claw Code ein vollständiges Vokabular, das Klarheit, Sicherheit und Erweiterbarkeit in Balance hält. Die Datenmodelle sind klein genug, um auf einen Blick verstanden zu werden, und präzise genug, um als zuverlässiges Fundament für die gesamte darüberliegende Architektur zu dienen.


# Kapitel 6: Der Befehls- und Tool-Katalog

## 6.1 Einleitung

Ein CLI-Agent wie Claude Code lebt von zwei Achsen der Interaktion: **Befehle** (Commands), die der Benutzer explizit aufruft, und **Tools**, die das Sprachmodell während einer Konversation selbstständig einsetzt. In der Originalimplementierung von Claude Code sind diese beiden Kataloge über Hunderte von TypeScript-Dateien verteilt -- React-Komponenten für die Darstellung, Handler für die Logik, Validierungsdateien für die Eingabe. Claw Code wählt einen grundlegend anderen Ansatz: Statt jedes einzelne Modul funktional nachzubauen, werden saemtliche Befehle und Tools als **Referenzdaten** in JSON-Snapshots erfasst und über eine schmale Python-API zugänglich gemacht.

Dieses Kapitel beschreibt die gesamte Pipeline -- von der JSON-Datei auf der Festplatte über das LRU-Cache-gestützte Laden bis hin zur gefilterten Zusammenstellung eines konkreten Tool-Pools für eine Sitzung. Wir betrachten dabei vier Quellcode-Dateien (`commands.py`, `tools.py`, `permissions.py`, `tool_pool.py`), zwei JSON-Snapshots und die zugrundeliegenden Datenmodelle.

## 6.2 Die JSON-Snapshot-Struktur

### 6.2.1 Aufbau eines Eintrags

Beide Snapshots -- `commands_snapshot.json` und `tools_snapshot.json` -- liegen im Verzeichnis `src/reference_data/` und folgen exakt demselben Schema. Jede Datei enthält ein JSON-Array aus Objekten mit drei Feldern:

```json
{
  "name": "add-dir",
  "source_hint": "commands/add-dir/add-dir.tsx",
  "responsibility": "Command module mirrored from archived TypeScript path commands/add-dir/add-dir.tsx"
}
```

Die drei Felder im Detail:

- **`name`**: Der kanonische Bezeichner des Befehls oder Tools. Bei Commands sind dies kebab-case-Namen wie `add-dir`, `branch`, `autofix-pr` oder `backfill-sessions`. Bei Tools dominiert PascalCase: `AgentTool`, `BashTool`, `FileReadTool`. Der Name ist der primaere Suchschlüssel für alle Lookup-Operationen.

- **`source_hint`**: Der relative Pfad innerhalb der archivierten TypeScript-Codebasis, aus der dieses Modul stammt. Beispiele sind `commands/add-dir/add-dir.tsx` oder `tools/AgentTool/AgentTool.tsx`. Dieser Pfad dient nicht der Ausführung -- er ist ein reiner Rückverweis, der Entwicklern zeigt, wo die urspruengliche Implementierung zu finden wäre. Der `source_hint` spielt außerdem eine zentrale Rolle bei der Filterung: Ob ein Command als Plugin- oder Skill-Befehl gilt, wird anhand von Teilstrings in diesem Feld entschieden.

- **`responsibility`**: Ein beschreibender Satz, der die Aufgabe des Moduls zusammenfasst. In der aktuellen Fassung ist dies ein generierter Text nach dem Muster `"Command module mirrored from archived TypeScript path ..."` bzw. `"Tool module mirrored from archived TypeScript path ..."`. Er dokumentiert den Spiegelungsstatus und bietet einen menschenlesbaren Kontext.

### 6.2.2 Struktur der Command-Snapshots

Die Datei `commands_snapshot.json` umfasst 1036 Zeilen und enthält **207 Eintraege**. Ein Ausschnitt vom Anfang der Datei zeigt die typische Struktur:

```json
[
  {
    "name": "add-dir",
    "source_hint": "commands/add-dir/add-dir.tsx",
    "responsibility": "Command module mirrored from archived TypeScript path commands/add-dir/add-dir.tsx"
  },
  {
    "name": "add-dir",
    "source_hint": "commands/add-dir/index.ts",
    "responsibility": "Command module mirrored from archived TypeScript path commands/add-dir/index.ts"
  },
  {
    "name": "validation",
    "source_hint": "commands/add-dir/validation.ts",
    "responsibility": "Command module mirrored from archived TypeScript path commands/add-dir/validation.ts"
  },
  {
    "name": "advisor",
    "source_hint": "commands/advisor.ts",
    "responsibility": "Command module mirrored from archived TypeScript path commands/advisor.ts"
  }
]
```

Man beachte: Derselbe `name` kann mehrfach auftreten, wenn das urspruengliche Command aus mehreren Dateien bestand (etwa `add-dir.tsx` und `index.ts`). Jede Datei der Originalquelle wird als separater Eintrag erfasst. Dadurch bleibt die Granularitaet der TypeScript-Codebasis erhalten -- ein einzelnes Command wie `add-dir` bringt seine React-Komponente, seinen Index-Export und seine Validierungslogik als drei getrennte `PortingModule`-Eintraege mit.

### 6.2.3 Struktur der Tool-Snapshots

Die Datei `tools_snapshot.json` ist mit 921 Zeilen und **184 Eintraegen** etwas kompakter. Die Tool-Namen folgen den TypeScript-Konventionen:

```json
[
  {
    "name": "AgentTool",
    "source_hint": "tools/AgentTool/AgentTool.tsx",
    "responsibility": "Tool module mirrored from archived TypeScript path tools/AgentTool/AgentTool.tsx"
  },
  {
    "name": "UI",
    "source_hint": "tools/AgentTool/UI.tsx",
    "responsibility": "Tool module mirrored from archived TypeScript path tools/AgentTool/UI.tsx"
  },
  {
    "name": "agentColorManager",
    "source_hint": "tools/AgentTool/agentColorManager.ts",
    "responsibility": "Tool module mirrored from archived TypeScript path tools/AgentTool/agentColorManager.ts"
  }
]
```

Auch hier bilden die Eintraege die Verzeichnisstruktur des Originals ab: Das `AgentTool`-Verzeichnis enthielt neben der Hauptkomponente auch Hilfsdateien wie `agentMemory.ts`, `agentDisplay.ts` und eingebaute Agenten (`claudeCodeGuideAgent.ts`, `exploreAgent.ts`, `generalPurposeAgent.ts`). Jede dieser Dateien wird als eigener Tool-Eintrag geführt.

## 6.3 Das PortingModule-Datenmodell

Beide Snapshot-Loader konvertieren die JSON-Eintraege in Instanzen der Klasse `PortingModule`, definiert in `src/models.py`:

```python
@dataclass(frozen=True)
class PortingModule:
    name: str
    responsibility: str
    source_hint: str
    status: str = 'planned'
```

Die Klasse ist als `frozen=True` Dataclass deklariert -- das macht sie immutabel und hashbar. Die vier Felder korrespondieren direkt mit den drei JSON-Feldern plus einem vierten Feld `status`, das beim Laden aus dem Snapshot stets auf `'mirrored'` gesetzt wird (der Default `'planned'` greift nur, wenn Module programmatisch erzeugt werden, ohne dass der Status explizit angegeben wird).

Die Immutabilitaet ist hier kein Zufall: Da die geladenen Module in globalen Tupeln gespeichert und über LRU-Caches verwaltet werden, wäre Mutabilitaet eine Fehlerquelle. Ein versehentliches Aendern eines Moduls würde den Cache korrumpieren, ohne dass dies auffiele.

## 6.4 LRU-Caching: `load_command_snapshot()` und `load_tool_snapshot()`

### 6.4.1 Die Ladefunktionen

Beide Module -- `commands.py` und `tools.py` -- definieren je eine Ladefunktion, die den JSON-Snapshot von der Festplatte liest und in ein Tupel aus `PortingModule`-Instanzen konvertiert:

```python
SNAPSHOT_PATH = Path(__file__).resolve().parent / 'reference_data' / 'commands_snapshot.json'

@lru_cache(maxsize=1)
def load_command_snapshot() -> tuple[PortingModule, ...]:
    raw_entries = json.loads(SNAPSHOT_PATH.read_text())
    return tuple(
        PortingModule(
            name=entry['name'],
            responsibility=entry['responsibility'],
            source_hint=entry['source_hint'],
            status='mirrored',
        )
        for entry in raw_entries
    )
```

Die Funktion `load_tool_snapshot()` in `tools.py` ist identisch aufgebaut, lediglich der Pfad verweist auf `tools_snapshot.json`.

### 6.4.2 Warum `@lru_cache(maxsize=1)`?

Der Decorator `@lru_cache(maxsize=1)` aus `functools` bewirkt, dass das Ergebnis der Funktion nach dem ersten Aufruf im Speicher gehalten wird. Bei jedem weiteren Aufruf wird nicht erneut die JSON-Datei gelesen und geparst, sondern das bereits berechnete Tupel direkt zurückgegeben.

Die Wahl von `maxsize=1` ist dabei präzise und begründet:

1. **Parameterlose Funktion**: Beide Ladefunktionen nehmen keine Argumente entgegen. Es gibt also genau einen möglichen Cache-Schlüssel -- den leeren Argumenttupel `()`. Ein größerer Cache wäre sinnlos, da es nie mehr als einen Eintrag geben kann.

2. **Vermeidung redundanter I/O**: Die JSON-Dateien umfassen zusammen fast 2000 Zeilen. Das Lesen und Parsen kostet Zeit, insbesondere wenn es bei jedem Zugriff auf einen Befehlsnamen erneut geschehen würde. Der Cache reduziert dies auf einen einzigen Lesevorgang pro Prozesslebensdauer.

3. **Implizite Initialisierung**: Die globalen Konstanten `PORTED_COMMANDS` und `PORTED_TOOLS` werden auf Modulebene zugewiesen. Beim Import des Moduls wird die Ladefunktion einmalig aufgerufen, und ab diesem Zeitpunkt liefert der Cache das Ergebnis.

4. **Thread-Sicherheit**: `lru_cache` in CPython ist durch die GIL (Global Interpreter Lock) ausreichend geschuetzt. Da die Funktion nur beim ersten Aufruf tatsaechlich I/O durchführt und danach stets den Cache bedient, gibt es kein Race-Condition-Risiko im Normalbetrieb.

Ein wichtiger Nebeneffekt: Da `lru_cache` sein Ergebnis als starke Referenz hält, bleibt das gesamte Tupel aus `PortingModule`-Instanzen für die Lebensdauer des Prozesses im Speicher. Bei 207 bzw. 184 Eintraegen ist der Speicherverbrauch vernachlässigbar -- ein Tupel aus einigen hundert kleinen Dataclass-Instanzen belegt wenige Kilobyte.

## 6.5 Globale Konstanten: `PORTED_COMMANDS` und `PORTED_TOOLS`

Unmittelbar nach der Definition der Ladefunktionen werden die globalen Konstanten gesetzt:

```python
PORTED_COMMANDS = load_command_snapshot()   # 207 Eintraege
```

```python
PORTED_TOOLS = load_tool_snapshot()         # 184 Eintraege
```

Diese Tupel bilden das Rückgrat des gesamten Katalog-Subsystems. Alle nachfolgenden Funktionen -- Lookup, Filterung, Suche, Ausführung -- arbeiten auf diesen globalen Konstanten. Da es sich um immutable Tupel aus immutablen Dataclasses handelt, sind sie inherent thread-sicher und koennen ohne Kopie an beliebige Stellen weitergereicht werden.

Die Zahl der Eintraege -- 207 Commands und 184 Tools -- reflektiert die betraechtliche Oberflaeche des Originalprojekts. Nicht jeder Eintrag entspricht dabei einem eigenständigen Befehl oder Tool; wie in Abschnitt 6.2 beschrieben, werden auch Hilfsmodule (Validierung, UI-Komponenten, Utilities) einzeln erfasst.

Zusätzlich existiert in `commands.py` eine gecachte Hilfsfunktion:

```python
@lru_cache(maxsize=1)
def built_in_command_names() -> frozenset[str]:
    return frozenset(module.name for module in PORTED_COMMANDS)
```

Diese liefert ein `frozenset` aller Command-Namen und ermöglicht O(1)-Mitgliedschaftstests. Auch hier ist `maxsize=1` die korrekte Wahl, da die Funktion parameterlos ist und das Ergebnis sich zur Laufzeit nicht ändert.

## 6.6 Lookup-Funktionen: `get_command()` und `get_tool()`

### 6.6.1 Case-insensitive lineare Suche

Beide Module stellen eine `get_*`-Funktion bereit, die ein einzelnes `PortingModule` anhand seines Namens nachschlaegt:

```python
def get_command(name: str) -> PortingModule | None:
    needle = name.lower()
    for module in PORTED_COMMANDS:
        if module.name.lower() == needle:
            return module
    return None
```

```python
def get_tool(name: str) -> PortingModule | None:
    needle = name.lower()
    for module in PORTED_TOOLS:
        if module.name.lower() == needle:
            return module
    return None
```

Beide Funktionen sind **case-insensitive**: Der Suchbegriff und der gespeicherte Name werden jeweils mit `.lower()` normalisiert, bevor sie verglichen werden. Dadurch findet `get_tool("bashtool")` das Modul mit dem Namen `"BashTool"`, und `get_command("Add-Dir")` findet `"add-dir"`.

Die Suche ist linear -- O(n) über das gesamte Tupel. Bei 207 bzw. 184 Eintraegen ist das völlig unproblematisch. Eine Hashtabelle wäre hier Über-Engineering: Die Funktion wird typischerweise einmal pro Benutzerinteraktion aufgerufen, und selbst auf langsamer Hardware benötigt ein linearer Scan über 200 kurze Strings weniger als eine Mikrosekunde.

Wichtig: Bei Duplikaten (wie dem mehrfach vorhandenen `add-dir`) liefert `get_command()` den **ersten Treffer**. Dies ist das Modul mit dem niedrigsten Index im Tupel -- also das, welches in der JSON-Datei zuerst steht.

## 6.7 Filterung: `get_commands()` und `get_tools()`

### 6.7.1 Command-Filterung

Die Funktion `get_commands()` liefert eine gefilterte Sicht auf den Command-Katalog:

```python
def get_commands(
    cwd: str | None = None,
    include_plugin_commands: bool = True,
    include_skill_commands: bool = True,
) -> tuple[PortingModule, ...]:
    commands = list(PORTED_COMMANDS)
    if not include_plugin_commands:
        commands = [module for module in commands
                    if 'plugin' not in module.source_hint.lower()]
    if not include_skill_commands:
        commands = [module for module in commands
                    if 'skills' not in module.source_hint.lower()]
    return tuple(commands)
```

Die Filterlogik ist elegant in ihrer Einfachheit: Statt eine formale Taxonomie zu pflegen, nutzt sie **Substring-Matching auf dem `source_hint`**. Ein Command gilt als Plugin-Command, wenn sein `source_hint` den Teilstring `"plugin"` enthält (case-insensitive). Analog gilt ein Command als Skill-Command, wenn `"skills"` im `source_hint` vorkommt.

Dieser Ansatz hat Vor- und Nachteile. Der Vorteil: Es muss kein zusätzliches Klassifikationsfeld in der JSON-Datei gepflegt werden. Die Verzeichnisstruktur des Originals -- `commands/plugin-*`, `commands/skills/*` -- kodiert die Kategorie bereits implizit. Der Nachteil: Sollte ein Command zuufaellig `"plugin"` im Pfad tragen, ohne ein Plugin zu sein, würde es falsch gefiltert. In der Praxis ist dies bei der vorliegenden Codebasis kein Problem.

Der Parameter `cwd` wird entgegengenommen, aber aktuell nicht ausgewertet. Er dient als Platzhalter für künftige Erweiterungen, bei denen die Command-Liste vom aktuellen Arbeitsverzeichnis abhaengen könnte (z. B. projektspezifische Commands).

### 6.7.2 Tool-Filterung

Die Funktion `get_tools()` bietet eine reichhaltigere Filterung:

```python
def get_tools(
    simple_mode: bool = False,
    include_mcp: bool = True,
    permission_context: ToolPermissionContext | None = None,
) -> tuple[PortingModule, ...]:
    tools = list(PORTED_TOOLS)
    if simple_mode:
        tools = [module for module in tools
                 if module.name in {'BashTool', 'FileReadTool', 'FileEditTool'}]
    if not include_mcp:
        tools = [module for module in tools
                 if 'mcp' not in module.name.lower()
                 and 'mcp' not in module.source_hint.lower()]
    return filter_tools_by_permission_context(tuple(tools), permission_context)
```

Drei Filter sind hier gestaffelt:

1. **Simple Mode**: Wenn aktiviert, wird der gesamte Katalog auf exakt drei Tools reduziert: `BashTool`, `FileReadTool` und `FileEditTool`. Dies sind die minimalen Werkzeuge, die ein Agent benötigt, um überhaupt arbeiten zu koennen -- Dateien lesen, Dateien bearbeiten und Shell-Befehle ausführen. Der Simple Mode ist besonders nützlich in eingeschraenkten Umgebungen oder beim Debugging, wo die volle Tool-Palette störend wäre.

2. **MCP-Filter**: Das Model Context Protocol (MCP) erlaubt die Integration externer Tool-Server. Wenn `include_mcp=False` gesetzt wird, werden alle Tools entfernt, deren Name oder `source_hint` den Teilstring `"mcp"` enthält. Dies ermöglicht einen rein lokalen Betrieb ohne Abhängigkeit von externen Diensten.

3. **Permission-Filter**: Als letzter Schritt wird `filter_tools_by_permission_context()` aufgerufen, das über den `ToolPermissionContext` (siehe Abschnitt 6.8) weitere Tools ausschließt.

Die Reihenfolge der Filter ist signifikant: Zuerst wird die Grundmenge eingeschraenkt (Simple Mode), dann werden MCP-Tools entfernt, und zuletzt greift das Berechtigungssystem. Dadurch ist sichergestellt, dass die Permission-Prüfung nur noch auf den relevanten Restbestand angewandt wird.

## 6.8 Suchfunktionen: `find_commands()` und `find_tools()`

Für interaktive Szenarien -- etwa wenn ein Benutzer einen Index der verfügbaren Befehle anzeigen lassen möchte -- stehen Suchfunktionen bereit:

```python
def find_commands(query: str, limit: int = 20) -> list[PortingModule]:
    needle = query.lower()
    matches = [module for module in PORTED_COMMANDS
               if needle in module.name.lower()
               or needle in module.source_hint.lower()]
    return matches[:limit]
```

Die Suche ist eine **Substring-Suche**: Der `query`-String wird in Kleinbuchstaben konvertiert und dann gegen sowohl den `name` als auch den `source_hint` jedes Moduls geprüft. Eine Anfrage wie `find_commands("agent")` würde alle Commands zurückgeben, in deren Name oder Herkunftspfad `"agent"` vorkommt.

Der Parameter `limit` begrenzt die Ergebnismenge auf standardmäßig 20 Treffer. Dies ist eine pragmatische Wahl für die Darstellung -- ein Terminal kann schließlich nur eine begrenzte Anzahl Zeilen gleichzeitig anzeigen.

Die Funktion `find_tools()` in `tools.py` ist identisch aufgebaut. Beide liefern eine `list` (nicht ein `tuple`), was semantisch korrekt ist: Das Ergebnis ist eine frische, veraenderbare Kollektion, die der Aufrufer nach Belieben weiterverarbeiten kann.

Für die Anzeige existieren zudem `render_command_index()` und `render_tool_index()`, die eine formatierte Textausgabe erzeugen:

```python
def render_command_index(limit: int = 20, query: str | None = None) -> str:
    modules = find_commands(query, limit) if query else list(PORTED_COMMANDS[:limit])
    lines = [f'Command entries: {len(PORTED_COMMANDS)}', '']
    if query:
        lines.append(f'Filtered by: {query}')
        lines.append('')
    lines.extend(f'- {module.name} — {module.source_hint}' for module in modules)
    return '\n'.join(lines)
```

Diese Funktion zeigt zuerst die Gesamtzahl der Eintraege an und listet dann die (ggf. gefilterten) Module mit Name und Herkunft auf.

## 6.9 CommandExecution und ToolExecution: Shim-Ausführung

### 6.9.1 Die Dataclasses

Beide Module definieren je eine Ausführungs-Dataclass:

```python
@dataclass(frozen=True)
class CommandExecution:
    name: str
    source_hint: str
    prompt: str
    handled: bool
    message: str
```

```python
@dataclass(frozen=True)
class ToolExecution:
    name: str
    source_hint: str
    payload: str
    handled: bool
    message: str
```

Der Unterschied liegt im dritten Feld: Commands erhalten einen `prompt` (den Benutzerbefehl), Tools einen `payload` (die Eingabedaten für das Tool). Beide sind `frozen=True` -- das Ergebnis einer Ausführung ist unveränderlich.

### 6.9.2 Die Ausführungsfunktionen

```python
def execute_command(name: str, prompt: str = '') -> CommandExecution:
    module = get_command(name)
    if module is None:
        return CommandExecution(
            name=name, source_hint='', prompt=prompt,
            handled=False,
            message=f'Unknown mirrored command: {name}',
        )
    action = f"Mirrored command '{module.name}' from {module.source_hint} would handle prompt {prompt!r}."
    return CommandExecution(
        name=module.name, source_hint=module.source_hint,
        prompt=prompt, handled=True, message=action,
    )
```

Die Funktion führt den Befehl nicht wirklich aus -- sie ist ein **Shim**. Ein Shim (wörtlich: Unterlegscheibe) ist ein Platzhalter, der die Schnittstelle der echten Implementierung nachbildet, ohne deren Funktionalitaet zu besitzen. Stattdessen erzeugt er eine beschreibende Nachricht, die dokumentiert, was die echte Implementierung tun würde.

Das Feld `handled` gibt Auskunft darüber, ob der Befehl bekannt war: `True`, wenn ein entsprechendes `PortingModule` gefunden würde, `False` bei einem unbekannten Namen. Aufrufer koennen anhand dieses Feldes entscheiden, wie sie weiter verfahren -- etwa eine Fehlermeldung anzeigen oder einen Fallback auslösen.

Die Funktion `execute_tool()` in `tools.py` folgt demselben Muster mit `payload` statt `prompt`.

Dieses Shim-Design passt zur Gesamtphilosophie von Claw Code: Die vollständige, funktionale Nachimplementierung aller 391 Module wäre ein enormer Aufwand. Der Shim-Ansatz erlaubt es, die **Oberflaeche** des Systems vollständig abzubilden, während die eigentliche Logik schrittweise portiert werden kann.

## 6.10 ToolPermissionContext: Das Berechtigungssystem

### 6.10.1 Die Datenstruktur

Die Datei `src/permissions.py` definiert mit nur 21 Zeilen ein kompaktes, aber maaechtiges Berechtigungssystem:

```python
@dataclass(frozen=True)
class ToolPermissionContext:
    deny_names: frozenset[str] = field(default_factory=frozenset)
    deny_prefixes: tuple[str, ...] = ()

    @classmethod
    def from_iterables(
        cls,
        deny_names: list[str] | None = None,
        deny_prefixes: list[str] | None = None,
    ) -> 'ToolPermissionContext':
        return cls(
            deny_names=frozenset(name.lower() for name in (deny_names or [])),
            deny_prefixes=tuple(prefix.lower() for prefix in (deny_prefixes or [])),
        )

    def blocks(self, tool_name: str) -> bool:
        lowered = tool_name.lower()
        return (lowered in self.deny_names
                or any(lowered.startswith(prefix)
                       for prefix in self.deny_prefixes))
```

### 6.10.2 Zwei Blockierungsmechanismen

Der `ToolPermissionContext` arbeitet nach dem **Deny-List-Prinzip**: Alles ist erlaubt, es sei denn, es wird explizit blockiert. Dabei stehen zwei komplementaere Mechanismen zur Verfügung:

1. **`deny_names`**: Ein `frozenset` von exakten Tool-Namen (in Kleinbuchstaben). Wenn ein Tool-Name in dieser Menge enthalten ist, wird es blockiert. Beispiel: `frozenset({'bashtool', 'filewritetool'})` würde genau diese beiden Tools sperren.

2. **`deny_prefixes`**: Ein Tuple von Präfix-Strings (in Kleinbuchstaben). Ein Tool wird blockiert, wenn sein Name mit einem dieser Präfixe beginnt. Beispiel: `('mcp_',)` würde alle Tools blockieren, deren Name mit `mcp_` anfaengt -- also saemtliche MCP-Tools auf einen Schlag.

Die Wahl der Datentypen ist bewusst: `frozenset` für `deny_names` bietet O(1)-Mitgliedschaftstests und ist immutabel. `tuple` für `deny_prefixes` ist immutabel und sequentiell durchsuchbar -- bei typischerweise wenigen Präfixen (ein bis drei) ist die lineare Suche mit `any()` völlig ausreichend.

### 6.10.3 Die `blocks()`-Methode

Die zentrale Methode `blocks()` kombiniert beide Prüfungen:

```python
def blocks(self, tool_name: str) -> bool:
    lowered = tool_name.lower()
    return (lowered in self.deny_names
            or any(lowered.startswith(prefix)
                   for prefix in self.deny_prefixes))
```

Auch hier ist die Prüfung case-insensitive. Der Name wird einmal in Kleinbuchstaben konvertiert und dann gegen beide Listen geprüft. Die Kurzschlussauswertung von `or` sorgt dafür, dass die Präfix-Prüfung übersprungen wird, wenn der Name bereits in `deny_names` gefunden würde.

### 6.10.4 Der Factory-Klassenmethode `from_iterables()`

Die Klassenmethode `from_iterables()` bietet eine bequeme Konstruktionsschnittstelle:

```python
ToolPermissionContext.from_iterables(
    deny_names=['BashTool', 'FileWriteTool'],
    deny_prefixes=['mcp_'],
)
```

Sie akzeptiert regulaere Listen und kuemmert sich intern um die Normalisierung (Kleinschreibung) und Konvertierung in die richtigen Containertypen. Dadurch müssen Aufrufer nicht selbst `frozenset`-Literale konstruieren.

### 6.10.5 Zusammenspiel mit der Tool-Filterung

Die Funktion `filter_tools_by_permission_context()` in `tools.py` wendet den Kontext auf eine Tool-Sammlung an:

```python
def filter_tools_by_permission_context(
    tools: tuple[PortingModule, ...],
    permission_context: ToolPermissionContext | None = None,
) -> tuple[PortingModule, ...]:
    if permission_context is None:
        return tools
    return tuple(
        module for module in tools
        if not permission_context.blocks(module.name)
    )
```

Wenn kein Permission-Kontext angegeben ist (`None`), werden alle Tools durchgelassen -- ein sinnvoller Default. Andernfalls wird jedes Tool einzeln gegen `blocks()` geprüft und nur die nicht blockierten Tools in das Ergebnis-Tupel aufgenommen.

## 6.11 ToolPool: Die Zusammenstellung des Tool-Pools

### 6.11.1 Die `ToolPool`-Dataclass

Die Datei `src/tool_pool.py` definiert die zentrale Abstrahierung für eine konkrete Sitzungs-Tool-Menge:

```python
@dataclass(frozen=True)
class ToolPool:
    tools: tuple[PortingModule, ...]
    simple_mode: bool
    include_mcp: bool

    def as_markdown(self) -> str:
        lines = [
            '# Tool Pool',
            '',
            f'Simple mode: {self.simple_mode}',
            f'Include MCP: {self.include_mcp}',
            f'Tool count: {len(self.tools)}',
        ]
        lines.extend(
            f'- {tool.name} — {tool.source_hint}'
            for tool in self.tools[:15]
        )
        return '\n'.join(lines)
```

Die Klasse buendelt das Ergebnis der Filterung mit den Parametern, die zu dieser Filterung geführt haben. Dies ist ein Beispiel für das **Result-with-Context-Muster**: Der Aufrufer erhält nicht nur die gefilterten Tools, sondern auch die Metadaten `simple_mode` und `include_mcp`, die dokumentieren, unter welchen Bedingungen der Pool erstellt würde.

Die Methode `as_markdown()` erzeugt eine kompakte Darstellung, die maximal 15 Tools auflistet -- genuegend für eine schnelle Übersicht, ohne die Ausgabe zu überfluten.

### 6.11.2 Die Assemblierungsfunktion

```python
def assemble_tool_pool(
    simple_mode: bool = False,
    include_mcp: bool = True,
    permission_context: ToolPermissionContext | None = None,
) -> ToolPool:
    return ToolPool(
        tools=get_tools(
            simple_mode=simple_mode,
            include_mcp=include_mcp,
            permission_context=permission_context,
        ),
        simple_mode=simple_mode,
        include_mcp=include_mcp,
    )
```

Die Funktion `assemble_tool_pool()` ist der zentrale Einstiegspunkt für die Erstellung eines Tool-Pools. Sie delegiert die eigentliche Filterung an `get_tools()` und verpackt das Ergebnis in eine `ToolPool`-Instanz. Alle drei Filterdimensionen -- Simple Mode, MCP-Einschluss und Permission-Kontext -- werden weitergereicht.

Ein typischer Aufruf könnte so aussehen:

```python
# Eingeschraenkte Umgebung: nur Basis-Tools, kein MCP, BashTool gesperrt
ctx = ToolPermissionContext.from_iterables(deny_names=['BashTool'])
pool = assemble_tool_pool(simple_mode=True, include_mcp=False, permission_context=ctx)
```

In diesem Beispiel würde der Simple Mode die 184 Tools auf drei reduzieren (`BashTool`, `FileReadTool`, `FileEditTool`), dann würde der Permission-Kontext `BashTool` entfernen -- übrig blieben nur `FileReadTool` und `FileEditTool`.

## 6.12 Simple Mode: Das Minimalprinzip

Der Simple Mode verdient besondere Beachtung, da er eine fundamentale Design-Entscheidung widerspiegelt. Die drei Tools, die im Simple Mode verbleiben, bilden die **irreduzible Kernfähigkeit** eines Code-Agenten:

| Tool | Fähigkeit |
|------|-----------|
| `BashTool` | Shell-Befehle ausführen |
| `FileReadTool` | Dateien lesen |
| `FileEditTool` | Dateien bearbeiten |

Mit diesen drei Werkzeugen kann ein Agent prinzipiell jede Aufgabe erledigen -- wenn auch umstaendlicher als mit spezialisierten Tools. `FileReadTool` ersetzt `Grep`, `Glob` und jedes andere Lese-Tool; `FileEditTool` ersetzt `Write` und jedes andere Schreib-Tool; `BashTool` ersetzt alles andere.

Der Simple Mode ist bewusst als **Whitelist** implementiert -- er prüft `module.name in {'BashTool', 'FileReadTool', 'FileEditTool'}`. Dies ist robust gegenüber Änderungen am Gesamtkatalog: Neue Tools werden automatisch ausgeschlossen, ohne dass die Simple-Mode-Logik angepasst werden muss.

## 6.13 Architektonische Zusammenfassung

Die vier Dateien bilden zusammen eine dreischichtige Architektur:

| Schicht | Modul(e) | Aufgabe |
|---------|----------|---------|
| **Orchestrierung** | **tool_pool.py** -- `assemble_tool_pool()` liefert `ToolPool` | Zusammenstellung eines konkreten Tool-Pools fuer eine Sitzung |
| **Katalog + Filterung** | **commands.py** -- `get_commands`, `find_commands`, `execute_cmd`; **tools.py** -- `get_tools`, `find_tools`, `execute_tool` | Lookup, Filterung, Suche, Shim-Ausfuehrung |
| **Zugriffskontrolle** | **permissions.py** -- `ToolPermissionContext.blocks()` | Deny-List-Mechanismus |
| **Datenbasis** | `commands_snapshot.json`, `tools_snapshot.json` | Statische, versionierte Daten |

Die unterste Schicht sind die JSON-Snapshots -- statische, versionierte Daten. Darüber liegt die Zugriffskontrolle mit ihrem Deny-List-Mechanismus. Die mittlere Schicht stellt Katalogdienste bereit (Lookup, Filterung, Suche, Shim-Ausführung). Ganz oben orchestriert `tool_pool.py` die Zusammenstellung eines konkreten Tool-Pools für eine Sitzung.

Diese Schichtung sorgt für klare Verantwortlichkeiten: `permissions.py` weiß nichts über JSON-Dateien, `tool_pool.py` weiß nichts über Substring-Matching in `source_hint`-Feldern, und die Snapshots wissen gar nichts -- sie sind reine Daten.

Die Entscheidung, 391 Module als Referenzdaten statt als lauffähigen Code zu modellieren, ist das pragende Merkmal dieses Subsystems. Sie erlaubt es Claw Code, die vollständige Oberflaeche von Claude Code abzubilden, ohne den enormen Implementierungsaufwand einer 1:1-Portierung zu tragen. Der Shim-Mechanismus in `execute_command()` und `execute_tool()` macht diese Strategie transparent: Jeder Aufruf wird dokumentiert, und das `handled`-Feld signalisiert dem System, dass der Befehl zwar erkannt, aber nur simuliert würde.


# Kapitel 7: Die Laufzeitumgebung (Runtime)

## 7.1 Einleitung

Die Datei `src/runtime.py` bildet das Herzstück von Claw Code. Sie ist mit 193 Zeilen bewusst kompakt gehalten, vereint aber sämtliche Phasen einer Benutzerinteraktion: vom Parsen des eingegebenen Prompts über das Routing zu passenden Befehlen und Werkzeugen, die Ausführung dieser Module, das Streaming der Ergebnisse bis hin zur Persistierung der gesamten Sitzung. Man kann `runtime.py` als den Dirigenten eines Orchesters betrachten -- die einzelnen Musiker (Kontextaufbau, Setup, Query-Engine, Execution-Registry) spielen ihre Stimmen, doch erst die Runtime bringt sie in die richtige Reihenfolge und sorgt dafür, dass aus den Einzelteilen ein zusammenhängendes Ganzes wird.

In diesem Kapitel analysieren wir jede Komponente der Runtime im Detail: die Datenstrukturen `RoutedMatch` und `RuntimeSession`, die Routing-Logik der Klasse `PortRuntime`, den vollständigen Session-Lebenszyklus in `bootstrap_session()` sowie die Multi-Turn-Schleife `run_turn_loop()`. Am Ende steht ein Flussdiagramm, das den Routing-Algorithmus visuell zusammenfasst.

---

## 7.2 Die Datenstruktur `RoutedMatch`

```python
@dataclass(frozen=True)
class RoutedMatch:
    kind: str
    name: str
    source_hint: str
    score: int
```

`RoutedMatch` ist eine eingefrorene (immutable) Dataclass, die ein einzelnes Routing-Ergebnis repräsentiert. Jedes Mal, wenn die Runtime einen Prompt analysiert und dabei feststellt, dass ein bestimmter Befehl oder ein bestimmtes Werkzeug relevant sein könnte, wird ein `RoutedMatch`-Objekt erzeugt. Die vier Felder tragen folgende Bedeutung:

### 7.2.1 Das Feld `kind`

Das Feld `kind` ist ein einfacher String, der exakt einen von zwei Werten annehmen kann: `'command'` oder `'tool'`. Diese Unterscheidung ist fundamental für die Architektur von Claw Code. Befehle (Commands) sind eigenständige Aktionen, die der Benutzer auslöst -- etwa das Starten eines Tests, das Anzeigen einer Zusammenfassung oder das Navigieren in der Projektstruktur. Werkzeuge (Tools) hingegen sind Hilfsmittel, die das System intern verwendet -- beispielsweise ein Dateileser, ein Bash-Executor oder ein Grep-Werkzeug. Der `kind`-Wert entscheidet später darüber, in welchem Register das Modul nachgeschlagen und ausgeführt wird: Befehle werden über `registry.command()` aufgelöst, Werkzeuge über `registry.tool()`.

### 7.2.2 Das Feld `name`

Der Name des gematchten Moduls, also der eindeutige Bezeichner, unter dem der Befehl oder das Werkzeug im System registriert ist. Dieser Name stammt direkt aus dem zugehörigen `PortingModule`-Objekt und wird verwendet, um das Modul in der `ExecutionRegistry` wiederzufinden. Beispiele wären `'grep'`, `'bash'`, `'read_file'` oder `'run_tests'`.

### 7.2.3 Das Feld `source_hint`

Der `source_hint` gibt an, aus welchem Teil des ursprünglichen TypeScript-Quellcodes dieses Modul portiert würde. Er dient primär der Dokumentation und der Nachvollziehbarkeit: Wenn ein Entwickler wissen möchte, welche Originalquelle einem bestimmten Python-Modul zugrunde liegt, kann er den `source_hint` konsultieren. In der Markdown-Ausgabe von `RuntimeSession.as_markdown()` wird dieses Feld mit einem Gedankenstrich an den Modulnamen angehängt, sodass jeder Routed Match seine Herkunft transparent macht.

### 7.2.4 Das Feld `score`

Der Score ist eine ganzzahlige Bewertung, die angibt, wie viele der aus dem Prompt extrahierten Token in den Metadaten des Moduls gefunden würden. Ein Score von 3 bedeutet, dass drei verschiedene Prompt-Token im Namen, im Source-Hint oder in der Responsibility-Beschreibung des Moduls vorkommen. Je höher der Score, desto relevanter wird das Modul für den gegebenen Prompt eingeschätzt. Der Score-Mechanismus ist bewusst einfach gehalten -- es handelt sich um ein Token-Overlap-Verfahren ohne Gewichtung, TF-IDF oder semantische Ähnlichkeit. Diese Einfachheit ist gewollt: Sie macht das Routing deterministisch, leicht nachvollziehbar und schnell.

### 7.2.5 Warum `frozen=True`?

Die Entscheidung, `RoutedMatch` als eingefrorene Dataclass zu deklarieren, ist eine bewusste Designentscheidung. Routing-Ergebnisse sollen nach ihrer Erzeugung nicht mehr verändert werden. Sie werden in Listen gesammelt, sortiert, gefiltert und an verschiedene Stellen weitergereicht -- von der `bootstrap_session()`-Methode an die `ExecutionRegistry`, an die `QueryEnginePort` und schließlich in die `RuntimeSession`. Unveränderlichkeit garantiert, dass ein einmal berechnetes Routing-Ergebnis konsistent bleibt, unabhängig davon, wie viele Konsumenten es lesen.

---

## 7.3 Die Klasse `PortRuntime`

`PortRuntime` ist die zentrale Klasse der Laufzeitumgebung. Sie hat keinen Konstruktor und keinen internen Zustand -- sie ist eine reine Sammlung von Methoden, die den gesamten Lebenszyklus einer Sitzung orchestrieren. Man könnte sie als zustandslose Service-Klasse bezeichnen.

### 7.3.1 `route_prompt(prompt, limit=5)` -- Der Routing-Algorithmus

Die Methode `route_prompt` ist das Herzstück des Prompt-Routings. Sie nimmt einen natürlichsprachlichen Prompt entgegen und gibt eine Liste von `RoutedMatch`-Objekten zurück, die die relevantesten Befehle und Werkzeuge für diesen Prompt darstellen.

#### Schritt 1: Tokenisierung

```python
tokens = {token.lower() for token in prompt.replace('/', ' ').replace('-', ' ').split() if token}
```

Der Prompt wird zunächst normalisiert: Schrägstriche (`/`) und Bindestriche (`-`) werden durch Leerzeichen ersetzt. Anschließend wird der resultierende String auf Leerzeichen gesplittet. Jedes Token wird in Kleinbuchstaben konvertiert, und leere Strings werden herausgefiltert. Das Ergebnis ist ein `set` -- also eine Menge ohne Duplikate. Diese Entscheidung hat zwei Konsequenzen: Erstens wird jedes Token nur einmal gezählt, auch wenn es im Prompt mehrfach vorkommt. Zweitens ist die Reihenfolge der Token irrelevant.

Warum werden gerade `/` und `-` als Trennzeichen behandelt? Weil in einem CLI-Kontext Pfadangaben wie `src/runtime` oder zusammengesetzte Begriffe wie `query-engine` häufig vorkommen. Durch das Aufbrechen an diesen Zeichen werden die einzelnen Bestandteile (`src`, `runtime`, `query`, `engine`) als eigenständige Token verfügbar und können gegen die Modulnamen gematcht werden.

#### Schritt 2: Scoring pro Art

```python
by_kind = {
    'command': self._collect_matches(tokens, PORTED_COMMANDS, 'command'),
    'tool': self._collect_matches(tokens, PORTED_TOOLS, 'tool'),
}
```

Die tokenisierten Prompt-Bestandteile werden gegen zwei Modulsammlungen gescort: `PORTED_COMMANDS` und `PORTED_TOOLS`. Beide sind Tupel von `PortingModule`-Objekten, die beim Import aus JSON-Snapshot-Dateien geladen und per `@lru_cache` gecacht werden. Die Methode `_collect_matches()` (siehe Abschnitt 7.3.4) erzeugt für jede Sammlung eine nach Score absteigend sortierte Liste von `RoutedMatch`-Objekten.

#### Schritt 3: Auswahl der besten Treffer

```python
selected: list[RoutedMatch] = []
for kind in ('command', 'tool'):
    if by_kind[kind]:
        selected.append(by_kind[kind].pop(0))
```

Dieser Schritt ist entscheidend und implementiert eine Art "Fair-Share-Strategie": Aus jeder Kategorie wird zunächst der beste Treffer (derjenige mit dem höchsten Score) ausgewählt und aus der Originalliste entfernt. Dadurch ist garantiert, dass das Ergebnis mindestens einen Befehl und mindestens ein Werkzeug enthält -- sofern überhaupt Treffer in der jeweiligen Kategorie existieren. Diese Strategie verhindert, dass eine Kategorie die andere vollständig verdrängt. Wenn beispielsweise fünf Werkzeuge hohe Scores haben, aber nur ein Befehl, würde ohne diese Logik der Befehl möglicherweise aus der finalen Liste fallen.

#### Schritt 4: Auffüllen mit Resttreffer

```python
leftovers = sorted(
    [match for matches in by_kind.values() for match in matches],
    key=lambda item: (-item.score, item.kind, item.name),
)
selected.extend(leftovers[: max(0, limit - len(selected))])
return selected[:limit]
```

Alle noch nicht ausgewählten Treffer beider Kategorien werden in einer einzigen Liste zusammengeführt und nach drei Kriterien sortiert: primär nach Score (absteigend, daher das Minuszeichen), sekundär nach `kind` (alphabetisch, wobei `'command'` vor `'tool'` kommt) und tertiär nach `name` (alphabetisch, für deterministische Reihenfolge bei Gleichstand). Von dieser sortierten Restliste werden so viele Treffer entnommen, wie noch Platz im Limit ist. Die abschließende Begrenzung `selected[:limit]` stellt sicher, dass niemals mehr als `limit` Ergebnisse zurückgegeben werden.

### 7.3.2 `_score(tokens, module)` -- Die Bewertungsfunktion

```python
@staticmethod
def _score(tokens: set[str], module: PortingModule) -> int:
    haystacks = [module.name.lower(), module.source_hint.lower(), module.responsibility.lower()]
    score = 0
    for token in tokens:
        if any(token in haystack for haystack in haystacks):
            score += 1
    return score
```

Die statische Methode `_score` berechnet die Relevanz eines einzelnen Moduls für eine gegebene Menge von Prompt-Token. Sie konstruiert eine Liste von drei "Heuhaufen" (haystacks): den Namen des Moduls, den Source-Hint und die Responsibility-Beschreibung, jeweils in Kleinbuchstaben. Dann iteriert sie über alle Token und prüft für jedes Token, ob es als Teilstring in mindestens einem der drei Heuhaufen vorkommt. Wenn ja, wird der Score um 1 erhöht.

Einige wichtige Details:

- **Teilstring-Matching, nicht exaktes Matching:** Das Token `'run'` matcht sowohl `'runtime'` als auch `'run_tests'`. Dies erhöht die Trefferquote, kann aber auch zu falsch-positiven Ergebnissen führen. In der Praxis ist dieses Verhalten erwünscht, da Benutzer oft nur Teile von Modulnamen eingeben.
- **Keine Gewichtung:** Ein Treffer im `name`-Feld zählt genauso viel wie ein Treffer in `responsibility`. Man könnte argumentieren, dass Namens-Treffer relevanter sein sollten, doch die Einfachheit des Algorithmus würde hier bewusst bevorzugt.
- **Set-basierte Token:** Da `tokens` ein `set` ist, wird jedes Token höchstens einmal gezählt, selbst wenn es in allen drei Heuhaufen vorkommt. Der maximale Score eines Moduls entspricht daher der Anzahl der eindeutigen Prompt-Token.

### 7.3.3 `_collect_matches(tokens, modules, kind)` -- Sammlung aller Treffer

```python
def _collect_matches(self, tokens: set[str], modules: tuple[PortingModule, ...], kind: str) -> list[RoutedMatch]:
    matches: list[RoutedMatch] = []
    for module in modules:
        score = self._score(tokens, module)
        if score > 0:
            matches.append(RoutedMatch(kind=kind, name=module.name, source_hint=module.source_hint, score=score))
    matches.sort(key=lambda item: (-item.score, item.name))
    return matches
```

Diese Methode iteriert über alle Module einer Kategorie, berechnet für jedes den Score und sammelt diejenigen mit positivem Score in einer Liste. Module mit Score 0 -- also solche, bei denen kein einziges Prompt-Token gefunden würde -- werden sofort verworfen. Die resultierende Liste wird nach Score (absteigend) und bei Gleichstand nach Name (alphabetisch aufsteigend) sortiert. Diese Sortierung ist deterministisch: Bei identischem Eingabeprompt liefert `_collect_matches` immer dieselbe Reihenfolge.

### 7.3.4 `_infer_permission_denials(matches)` -- Automatische Berechtigungsverweigerungen

```python
def _infer_permission_denials(self, matches: list[RoutedMatch]) -> list[PermissionDenial]:
    denials: list[PermissionDenial] = []
    for match in matches:
        if match.kind == 'tool' and 'bash' in match.name.lower():
            denials.append(PermissionDenial(
                tool_name=match.name,
                reason='destructive shell execution remains gated in the Python port'
            ))
    return denials
```

Diese Methode implementiert eine einfache, aber wichtige Sicherheitsregel: Jedes Werkzeug, dessen Name den Teilstring `'bash'` enthält, wird automatisch mit einer `PermissionDenial` versehen. Die Begründung lautet, dass destruktive Shell-Ausführungen im Python-Port weiterhin eingeschränkt bleiben sollen.

Die `PermissionDenial`-Dataclass (definiert in `src/models.py`) besteht aus zwei Feldern: `tool_name` und `reason`. Diese Verweigerungen werden an die `QueryEnginePort` weitergeleitet, die sie in ihrem Stream als `permission_denial`-Events ausgibt und im `TurnResult` als Teil der `permission_denials`-Tupel zurückgibt.

Bemerkenswert ist, dass die aktuelle Implementierung ausschließlich auf den Modulnamen schaut. Es gibt keine Konfigurationsdatei oder Datenbank für Berechtigungsregeln -- die Logik ist hart kodiert. Dies mag für den aktuellen Stand des Projekts ausreichen, deutet aber auf einen zukünftigen Erweiterungspunkt hin: Eine regelbasierte oder konfigurierbare Berechtigungsschicht wäre eine natürliche Weiterentwicklung.

---

## 7.4 `bootstrap_session(prompt, limit=5)` -- Der vollständige Session-Lebenszyklus

Die Methode `bootstrap_session` ist die umfangreichste Methode in `runtime.py`. Sie orchestriert den gesamten Lebenszyklus einer Sitzung in zehn klar abgegrenzten Schritten. Betrachten wir jeden einzelnen Schritt im Detail:

### Schritt 1: `build_port_context()` -- Kontextaufbau

```python
context = build_port_context()
```

Zu Beginn wird der Projekt-Kontext aufgebaut. Die Funktion `build_port_context()` aus `src/context.py` analysiert den Workspace und erzeugt ein `PortContext`-Objekt mit Informationen wie der Anzahl der Python-Dateien, der Verfügbarkeit von Archiven und weiteren Metadaten. Dieser Kontext wird später in der `RuntimeSession` gespeichert und kann über `render_context()` als Markdown ausgegeben werden.

### Schritt 2: `run_setup(trusted=True)` -- Setup-Ausführung

```python
setup_report = run_setup(trusted=True)
setup = setup_report.setup
```

Der Setup-Schritt führt die Workspace-Initialisierung durch. Das Flag `trusted=True` signalisiert, dass die Umgebung als vertrauenswürdig eingestuft wird -- es werden also keine zusätzlichen Sicherheitsprüfungen durchgeführt. Das `SetupReport` enthält ein `WorkspaceSetup`-Objekt mit Informationen zur Python-Version, zur Plattform und zum konfigurierten Test-Befehl. Außerdem stellt `WorkspaceSetup` eine Methode `startup_steps()` bereit, die die durchgeführten Initialisierungsschritte als Liste zurückgibt.

### Schritt 3: `QueryEnginePort.from_workspace()` -- Engine-Initialisierung

```python
engine = QueryEnginePort.from_workspace()
```

Die Query-Engine wird über die Klassenmethode `from_workspace()` erzeugt. Intern wird dazu `build_port_manifest()` aufgerufen, das ein `PortManifest`-Objekt erstellt. Die Engine erhält eine automatisch generierte Session-ID (UUID-Hex), eine leere Nachrichtenliste, eine frische `UsageSummary` und einen leeren `TranscriptStore`.

### Schritt 4: History-Logging und `route_prompt()`

```python
history = HistoryLog()
history.add('context', f'python_files={context.python_file_count}, archive_available={context.archive_available}')
history.add('registry', f'commands={len(PORTED_COMMANDS)}, tools={len(PORTED_TOOLS)}')
matches = self.route_prompt(prompt, limit=limit)
```

Ein `HistoryLog` wird angelegt und mit den ersten Einträgen befüllt: der Anzahl der Python-Dateien und der Archiv-Verfügbarkeit aus dem Kontext sowie der Anzahl der registrierten Befehle und Werkzeuge. Dann wird `route_prompt()` aufgerufen, um die relevantesten Module für den gegebenen Prompt zu ermitteln. Das Ergebnis ist eine Liste von `RoutedMatch`-Objekten.

### Schritt 5: `build_execution_registry()` -- Registry-Aufbau

```python
registry = build_execution_registry()
```

Die `ExecutionRegistry` wird aufgebaut. Sie enthält für jeden `PortingModule`-Eintrag in `PORTED_COMMANDS` ein `MirroredCommand`-Objekt und für jeden Eintrag in `PORTED_TOOLS` ein `MirroredTool`-Objekt. Diese Wrapper-Objekte bieten jeweils eine `execute()`-Methode, die den eigentlichen Befehl bzw. das Werkzeug ausführt und eine Nachricht als String zurückgibt.

### Schritt 6: Ausführung aller gematchten Module

```python
command_execs = tuple(
    registry.command(match.name).execute(prompt)
    for match in matches if match.kind == 'command' and registry.command(match.name)
)
tool_execs = tuple(
    registry.tool(match.name).execute(prompt)
    for match in matches if match.kind == 'tool' and registry.tool(match.name)
)
```

Für jeden `RoutedMatch` mit `kind == 'command'` wird der entsprechende Befehl in der Registry nachgeschlagen und ausgeführt. Analog geschieht dies für Werkzeuge mit `kind == 'tool'`. Die Ergebnisse -- Nachrichten-Strings -- werden als Tupel gesammelt. Bemerkenswert ist die doppelte Prüfung: `registry.command(match.name)` wird sowohl als Guard in der `if`-Bedingung als auch als Aufrufziel in `.execute()` verwendet. Würde ein Modul in der Registry nicht gefunden, würde es stillschweigend übersprungen.

### Schritt 7: Berechtigungsverweigerungen und `stream_submit_message()`

```python
denials = tuple(self._infer_permission_denials(matches))
stream_events = tuple(engine.stream_submit_message(
    prompt,
    matched_commands=tuple(match.name for match in matches if match.kind == 'command'),
    matched_tools=tuple(match.name for match in matches if match.kind == 'tool'),
    denied_tools=denials,
))
```

Die automatischen Berechtigungsverweigerungen werden berechnet (siehe Abschnitt 7.3.4). Dann wird `stream_submit_message()` auf der Query-Engine aufgerufen. Diese Generator-Methode gibt eine Folge von Events aus: `message_start` (mit Session-ID und Prompt), optional `command_match` und `tool_match` (mit den Namen der gematchten Module), optional `permission_denial` (mit den Namen der verweigerten Werkzeuge), `message_delta` (mit dem formatierten Ausgabetext) und schließlich `message_stop` (mit Nutzungsstatistiken und dem Stop-Grund). Alle Events werden als Tupel materialisiert und in der Session gespeichert.

### Schritt 8: `submit_message()` -- Synchrone Nachrichtenverarbeitung

```python
turn_result = engine.submit_message(
    prompt,
    matched_commands=tuple(match.name for match in matches if match.kind == 'command'),
    matched_tools=tuple(match.name for match in matches if match.kind == 'tool'),
    denied_tools=denials,
)
```

Zusätzlich zum Stream wird `submit_message()` aufgerufen, das ein `TurnResult` zurückgibt. Dieses enthält den Prompt, die formatierte Ausgabe, die gematchten Befehle und Werkzeuge, die Berechtigungsverweigerungen, die kumulierte Token-Nutzung und den Stop-Grund. Es ist wichtig zu bemerken, dass `stream_submit_message()` intern ebenfalls `submit_message()` aufruft -- der Prompt wird also effektiv zweimal verarbeitet. Dies ist ein Designaspekt, der möglicherweise auf eine geplante Entkopplung von Stream- und Synchron-Pfad hindeutet.

### Schritt 9: `persist_session()` -- Sitzungspersistierung

```python
persisted_session_path = engine.persist_session()
```

Die Engine flusht ihren Transkript-Store und speichert die gesamte Sitzung als `StoredSession` über den Session-Store ab. Der zurückgegebene Pfad wird als String in der `RuntimeSession` abgelegt, sodass die Sitzung später über `QueryEnginePort.from_saved_session()` wiederhergestellt werden kann.

### Schritt 10: `RuntimeSession` zusammenbauen

```python
return RuntimeSession(
    prompt=prompt,
    context=context,
    setup=setup,
    setup_report=setup_report,
    system_init_message=build_system_init_message(trusted=True),
    history=history,
    routed_matches=matches,
    turn_result=turn_result,
    command_execution_messages=command_execs,
    tool_execution_messages=tool_execs,
    stream_events=stream_events,
    persisted_session_path=persisted_session_path,
)
```

Abschließend werden sämtliche gesammelten Informationen in einem `RuntimeSession`-Objekt zusammengeführt und zurückgegeben. Zusätzlich werden noch History-Einträge für das Routing, die Ausführung und das Turn-Ergebnis hinzugefügt. Die System-Init-Nachricht wird ebenfalls mit `trusted=True` erzeugt und als Feld in der Session abgelegt.

---

## 7.5 Die Datenstruktur `RuntimeSession`

`RuntimeSession` ist eine nicht-eingefrorene Dataclass mit zwölf Feldern, die den vollständigen Zustand einer abgeschlossenen Sitzung repräsentiert:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `prompt` | `str` | Der ursprüngliche Benutzer-Prompt |
| `context` | `PortContext` | Der Workspace-Kontext |
| `setup` | `WorkspaceSetup` | Die Workspace-Konfiguration |
| `setup_report` | `SetupReport` | Der vollständige Setup-Bericht |
| `system_init_message` | `str` | Die System-Initialisierungsnachricht |
| `history` | `HistoryLog` | Das chronologische Ablaufprotokoll |
| `routed_matches` | `list[RoutedMatch]` | Die Routing-Ergebnisse |
| `turn_result` | `TurnResult` | Das Ergebnis der Nachrichtenverarbeitung |
| `command_execution_messages` | `tuple[str, ...]` | Die Ausgaben der Befehlsausführungen |
| `tool_execution_messages` | `tuple[str, ...]` | Die Ausgaben der Werkzeugausführungen |
| `stream_events` | `tuple[dict[str, object], ...]` | Die Stream-Events |
| `persisted_session_path` | `str` | Der Speicherpfad der persistierten Sitzung |

### 7.5.1 `as_markdown()` -- Menschenlesbare Ausgabe

Die Methode `as_markdown()` transformiert die gesamte Session in einen gut lesbaren Markdown-String. Sie beginnt mit einer Überschrift und dem Prompt, gefolgt vom gerenderten Kontext. Dann folgen die Setup-Informationen (Python-Version, Implementierung, Plattform, Test-Befehl), die Startup-Schritte, die System-Init-Nachricht und die Routing-Ergebnisse.

Für jeden `RoutedMatch` wird eine Zeile im Format `- [kind] name (score) -- source_hint` erzeugt. Wenn keine Matches vorhanden sind, wird stattdessen `- none` ausgegeben. Es folgen die Befehlsausführungen, die Werkzeugausführungen, die Stream-Events (jeweils mit Typ-Prefix), das Turn-Ergebnis (als Textausgabe), der persistierte Sitzungspfad und schließlich die History als Markdown.

Diese Methode ist besonders nützlich für Debugging, Protokollierung und Transparenz: Ein Entwickler kann sich jederzeit den vollständigen Ablauf einer Sitzung als Markdown-Dokument ausgeben lassen und so nachvollziehen, welche Module geroutet und ausgeführt würden, welche Events gestreamt würden und wie die Token-Nutzung aussah.

---

## 7.6 `run_turn_loop(prompt, limit, max_turns, structured_output)` -- Die Multi-Turn-Schleife

```python
def run_turn_loop(self, prompt: str, limit: int = 5, max_turns: int = 3,
                  structured_output: bool = False) -> list[TurnResult]:
    engine = QueryEnginePort.from_workspace()
    engine.config = QueryEngineConfig(max_turns=max_turns, structured_output=structured_output)
    matches = self.route_prompt(prompt, limit=limit)
    command_names = tuple(match.name for match in matches if match.kind == 'command')
    tool_names = tuple(match.name for match in matches if match.kind == 'tool')
    results: list[TurnResult] = []
    for turn in range(max_turns):
        turn_prompt = prompt if turn == 0 else f'{prompt} [turn {turn + 1}]'
        result = engine.submit_message(turn_prompt, command_names, tool_names, ())
        results.append(result)
        if result.stop_reason != 'completed':
            break
    return results
```

Während `bootstrap_session()` eine einzelne Runde (einen einzelnen "Turn") durchläuft, ermöglicht `run_turn_loop()` die Ausführung mehrerer aufeinanderfolgender Runden mit demselben Prompt. Dies ist relevant für iterative Aufgaben, bei denen das System mehrere Durchläufe benötigt, um eine Aufgabe abzuschließen.

### 7.6.1 Initialisierung

Eine frische `QueryEnginePort` wird erstellt, und ihre Konfiguration wird durch ein neues `QueryEngineConfig`-Objekt mit den übergebenen `max_turns` und `structured_output`-Parametern überschrieben. Das Routing wird einmalig durchgeführt -- die gematchten Befehle und Werkzeuge bleiben über alle Turns hinweg konstant.

### 7.6.2 Die Schleife

Die Schleife iteriert von `0` bis `max_turns - 1`. Im ersten Turn wird der ursprüngliche Prompt verwendet. Ab dem zweiten Turn wird der Prompt um einen Suffix `[turn N]` erweitert, wobei `N` die 1-basierte Turn-Nummer ist. Jedes Turn-Ergebnis wird der Ergebnisliste hinzugefügt.

### 7.6.3 Stop-Bedingungen

Die Schleife kennt drei Stop-Bedingungen:

1. **`max_turns` erreicht:** Wenn die Schleife alle geplanten Turns durchlaufen hat, endet sie natürlich. Dies ist der implizite Abbruch durch die `range()`-Begrenzung.
2. **Stop-Grund ungleich `'completed'`:** Wenn ein `TurnResult` einen `stop_reason` hat, der nicht `'completed'` ist, wird die Schleife vorzeitig abgebrochen. Mögliche Gründe sind `'max_turns_reached'` (die Engine hat ihr internes Turn-Limit erreicht) oder `'max_budget_reached'` (das Token-Budget würde überschritten).
3. **Implizites Budget-Limit:** Innerhalb der `QueryEnginePort` prüft `submit_message()`, ob die projizierte Token-Nutzung das konfigurierte `max_budget_tokens` überschreitet. Wenn ja, wird der `stop_reason` auf `'max_budget_reached'` gesetzt, was in der nächsten Schleifenrunde zum Abbruch führt.

Bemerkenswert ist, dass `run_turn_loop()` keine Berechtigungsverweigerungen an die Engine weiterreicht (das letzte Argument ist ein leeres Tupel `()`). Dies unterscheidet die Turn-Schleife von `bootstrap_session()`, wo `_infer_permission_denials()` explizit aufgerufen wird. Es handelt sich möglicherweise um eine bewusste Vereinfachung oder um einen Bereich, der in zukünftigen Versionen noch erweitert wird.

### 7.6.4 Rückgabewert

Die Methode gibt eine Liste aller `TurnResult`-Objekte zurück. Der Aufrufer kann daraus ablesen, wie viele Turns tatsächlich ausgeführt würden, was die jeweilige Ausgabe war und warum die Schleife endete.

---

## 7.7 Flussdiagramm des Routing-Algorithmus

Das folgende Diagramm zeigt den vollständigen Ablauf von `route_prompt()` als Textflussdiagramm:

**Ablauf von `route_prompt()`:**

1. **Prompt empfangen**

2. **Tokenisierung:** `/` und `-` werden durch Leerzeichen ersetzt, dann `split()`, `lower()`, dedupliziert -- ergibt ein Set von Tokens

3. **Paralleles Matching** -- zwei unabhaengige Pfade:
   - **`_collect_matches(PORTED_COMMANDS)`:** Fuer jedes Modul wird `_score(tokens, module)` berechnet. Alle Module mit `score > 0` werden als `RoutedMatch` erfasst. Sortierung: absteigend nach Score, dann nach Name.
   - **`_collect_matches(PORTED_TOOLS)`:** Identisches Verfahren fuer die Tool-Liste. Ergebnis: sortierte `tool_matches`.

4. **Fair-Share-Auswahl:** Der beste Command und das beste Tool werden jeweils entnommen und in `selected[]` eingefuegt.

5. **Leftovers sammeln:** Alle verbleibenden Treffer aus beiden Listen werden zusammengefuehrt und nach `-score`, `kind`, `name` sortiert.

6. **Auffuellen:** `selected += leftovers` bis das Limit erreicht ist.

7. **Rueckgabe:** `selected[:limit]` (maximal 5 Treffer)

### Scoring-Detail (`_score`):

**Scoring-Ablauf pro Token:**

Fuer jedes Token aus dem Prompt-Set wird geprueft:

1. Token in `module.name`? -- Ja: `score += 1`
2. Token in `module.source_hint`? -- Ja: (bereits gezaehlt)
3. Token in `module.responsibility`? -- Ja: (bereits gezaehlt)

Die Pruefung verwendet `any()` -- es wird nur einmal pro Token gezaehlt, auch wenn mehrere Felder treffen.

---

## 7.8 Zusammenspiel der Komponenten

Die Runtime fungiert als zentraler Integrationspunkt des gesamten Claw-Code-Systems. Die folgende Übersicht zeigt die Abhängigkeiten:

- **`src/context.py`** liefert den `PortContext` (Workspace-Metadaten)
- **`src/setup.py`** liefert `SetupReport` und `WorkspaceSetup` (Plattform-/Python-Informationen)
- **`src/commands.py`** stellt `PORTED_COMMANDS` bereit (Tupel von `PortingModule` aus JSON-Snapshot)
- **`src/tools.py`** stellt `PORTED_TOOLS` bereit (Tupel von `PortingModule` aus JSON-Snapshot)
- **`src/models.py`** definiert die Kerndatentypen `PortingModule`, `PermissionDenial`, `UsageSummary`
- **`src/query_engine.py`** stellt `QueryEnginePort` bereit (Nachrichten-Engine mit Session-Verwaltung)
- **`src/execution_registry.py`** stellt `ExecutionRegistry` bereit (Lookup und Ausführung von Modulen)
- **`src/system_init.py`** liefert die System-Initialisierungsnachricht
- **`src/history.py`** stellt `HistoryLog` bereit (chronologisches Ablaufprotokoll)

Die Runtime selbst definiert nur zwei Datentypen (`RoutedMatch`, `RuntimeSession`) und eine Klasse (`PortRuntime`) mit fünf Methoden. Ihre Komplexität liegt nicht im eigenen Code, sondern in der Orchestrierung der genannten Subsysteme.

---

## 7.9 Designentscheidungen und Kritische Würdigung

### Zustandslosigkeit von `PortRuntime`

Die Klasse `PortRuntime` hat keinen Konstruktor und keinen internen Zustand. Jede Methode erzeugt bei Bedarf ihre eigenen Abhängigkeiten (z.B. `QueryEnginePort.from_workspace()`). Dies macht die Klasse einfach zu testen und zu verwenden, bedeutet aber auch, dass bei jeder Session-Erstellung alle Abhängigkeiten neu aufgebaut werden.

### Doppelte Nachrichtenverarbeitung in `bootstrap_session()`

Der Prompt wird sowohl durch `stream_submit_message()` als auch durch `submit_message()` verarbeitet. Da `stream_submit_message()` intern `submit_message()` aufruft, wird der Prompt tatsächlich zweimal an die Engine übergeben. Dies führt zu einer doppelten Zustandsmutation (Nachrichten werden zweimal angehängt, Usage wird zweimal aktualisiert). Für einen Produktionseinsatz wäre hier eine Entkopplung sinnvoll.

### Einfachheit des Scoring-Algorithmus

Der Token-Overlap-Ansatz ist bewusst simpel. Er funktioniert gut für kurze, schlagwortartige Prompts, kann aber bei längeren natürlichsprachlichen Eingaben an seine Grenzen stoßen: Ein Prompt wie "Ich möchte die Dateien im Verzeichnis lesen" würde viele Stoppwörter enthalten, die selten in Modulnamen vorkommen. Eine mögliche Erweiterung wäre eine Stoppwort-Liste oder eine Gewichtung basierend auf dem Feld, in dem der Treffer gefunden würde.

### Fehlende Berechtigungsverweigerungen in `run_turn_loop()`

Wie bereits erwähnt, übergibt `run_turn_loop()` ein leeres Tupel für `denied_tools`. Dies bedeutet, dass in der Multi-Turn-Schleife auch Bash-Werkzeuge ohne Verweigerung ausgeführt werden könnten. Je nach Sicherheitsanforderungen könnte dies ein bewusstes Verhalten oder ein offener Punkt sein.

---

## 7.10 Zusammenfassung

Die Datei `src/runtime.py` ist der Knotenpunkt von Claw Code. Mit nur 193 Zeilen orchestriert sie den gesamten Lebenszyklus einer Benutzersitzung: vom Parsen des Prompts über ein einfaches aber effektives Token-basiertes Routing, die Ausführung der gematchten Module, das Streaming der Ergebnisse, die synchrone Nachrichtenverarbeitung bis hin zur Persistierung. Die `RoutedMatch`-Dataclass bildet die Brücke zwischen Routing und Ausführung, die `RuntimeSession`-Dataclass sammelt alle Artefakte einer Sitzung, und die `PortRuntime`-Klasse bindet alles zusammen. Die Multi-Turn-Schleife `run_turn_loop()` erweitert das Grundmodell um iterative Verarbeitung mit konfigurierbaren Abbruchbedingungen. Das Design bevorzugt durchgehend Einfachheit und Transparenz gegenüber Abstraktion -- eine Philosophie, die sich durch das gesamte Claw-Code-Projekt zieht.


# Kapitel 8: Die Query Engine

## 8.1 Einleitung

Die Query Engine bildet das Herzstück der Interaktionsschicht von Claw Code. Sie ist die zentrale Komponente, die eingehende Benutzer-Prompts entgegennimmt, sie gegen registrierte Befehle und Werkzeuge abgleicht, den Token-Verbrauch überwacht, Berechtigungsverweigerungen protokolliert und schließlich ein strukturiertes Ergebnis zurückliefert. Dabei verfolgt sie einen klaren architektonischen Ansatz: Die Engine trennt strikt zwischen der zustandsbehafteten Konversationslogik (dem "Port") und der darüberliegenden Laufzeitschicht (der "Runtime"), die das eigentliche Routing übernimmt.

Dieses Kapitel analysiert drei Quelldateien, die zusammen das gesamte Query-Engine-Subsystem bilden:

- **`src/query_engine.py`** (194 Zeilen) — enthält die Konfiguration, die Datenklasse für Turn-Ergebnisse und die vollständige `QueryEnginePort`-Klasse
- **`src/QueryEngine.py`** (20 Zeilen) — definiert die `QueryEngineRuntime`-Subklasse mit ihrer `route()`-Methode
- **`src/transcript.py`** (24 Zeilen) — implementiert den `TranscriptStore`, der das Gesprächsprotokoll verwaltet

Wir werden jede dieser Komponenten im Detail durchgehen, ihren Zusammenhang erläutern und mit Sequenzdiagrammen veranschaulichen, wie Nachrichten durch das System fliessen.

---

## 8.2 QueryEngineConfig — Die Konfigurationsklasse

Die gesamte Verhaltenssteuerung der Query Engine wird über eine einzige, unveränderliche Datenklasse (`frozen=True`) gesteuert:

```python
@dataclass(frozen=True)
class QueryEngineConfig:
    max_turns: int = 8
    max_budget_tokens: int = 2000
    compact_after_turns: int = 12
    structured_output: bool = False
    structured_retry_limit: int = 2
```

### 8.2.1 Die einzelnen Parameter

**`max_turns = 8`**

Dieser Parameter definiert die maximale Anzahl von Konversationsrunden (Turns), die eine einzelne Session durchlaufen darf. Sobald die Länge von `mutable_messages` diesen Wert erreicht oder überschreitet, wird kein neuer Turn mehr verarbeitet. Stattdessen gibt `submit_message()` sofort ein `TurnResult` mit dem `stop_reason` `'max_turns_reached'` zurück. Der Wert 8 ist bewusst konservativ gewählt: Er erlaubt eine substanzielle Konversation, verhindert aber endlose Schleifen, die bei automatisierten Agenten auftreten können.

**`max_budget_tokens = 2000`**

Dieses Token-Budget begrenzt den kumulativen Verbrauch einer Session. Die Berechnung erfolgt über die Methode `UsageSummary.add_turn()`, die eine vereinfachte Wort-basierte Schätzung verwendet (`len(text.split())`). Wenn die Summe aus `input_tokens` und `output_tokens` nach einem Turn den Wert 2000 übersteigt, wird der `stop_reason` auf `'max_budget_reached'` gesetzt. Wichtig: Der Turn wird trotzdem noch ausgeführt — das Budget fungiert als weiches Limit, nicht als harte Sperre. Erst der nächste Turn würde durch die `max_turns`-Prüfung oder eine explizite Prüfung des Aufrufers verhindert werden.

**`compact_after_turns = 12`**

Dieser Wert steuert die Kompaktierungsstrategie. Wenn die Anzahl gespeicherter Nachrichten `compact_after_turns` übersteigt (also mehr als 12 Einträge vorhanden sind), werden die älteren Einträge verworfen und nur die letzten `compact_after_turns` Nachrichten behalten. Man beachte den scheinbaren Widerspruch: `max_turns` ist 8, aber `compact_after_turns` ist 12. Das ist kein Fehler — eine Session kann durch `from_saved_session()` mit einem bereits gefüllten Nachrichtenverlauf wiederhergestellt werden, und die Kompaktierung soll auch in diesen Fällen greifen. Die Kompaktierung betrifft sowohl `mutable_messages` als auch den `TranscriptStore`.

**`structured_output = False`**

Standardmässig erzeugt die Engine eine einfache Textausgabe (zeilenweise mit Newlines getrennt). Wird `structured_output` auf `True` gesetzt, serialisiert die Engine die Zusammenfassung als JSON-Objekt mit den Schlüsseln `summary` und `session_id`. Diese Option ist besonders nützlich, wenn ein nachgelagertes System die Ausgabe maschinell parsen muss.

**`structured_retry_limit = 2`**

Wenn die JSON-Serialisierung fehlschlägt (etwa durch nicht-serialisierbare Objekte im Payload), versucht die Engine bis zu `structured_retry_limit` Mal, eine bereinigte Fallback-Ausgabe zu erzeugen. Bei jedem Fehlversuch wird der Payload auf einen minimalen Inhalt (`{'summary': ['structured output retry'], 'session_id': ...}`) reduziert. Schlägt auch der letzte Versuch fehl, wird eine `RuntimeError` geworfen.

### 8.2.2 Designentscheidung: Warum `frozen=True`?

Die Konfiguration ist als eingefrorene Datenklasse implementiert. Das bedeutet: Einmal erzeugt, kann kein Attribut mehr geändert werden. Diese Entscheidung hat zwei Vorteile. Erstens: Thread-Sicherheit. Auch wenn das aktuelle System nicht explizit multithreaded ist, garantiert die Unveränderlichkeit, dass eine Konfiguration gefahrlos zwischen mehreren Komponenten geteilt werden kann. Zweitens: Klarheit der Verantwortung. Konfigurationsänderungen erfordern die Erzeugung einer neuen Instanz, was im Code explizit und nachvollziehbar ist.

---

## 8.3 TurnResult — Das Ergebnis eines Turns

Jeder Aufruf von `submit_message()` liefert ein `TurnResult` zurück, das den vollständigen Zustand dieses einen Verarbeitungsschritts kapselt:

```python
@dataclass(frozen=True)
class TurnResult:
    prompt: str
    output: str
    matched_commands: tuple[str, ...]
    matched_tools: tuple[str, ...]
    permission_denials: tuple[PermissionDenial, ...]
    usage: UsageSummary
    stop_reason: str
```

### 8.3.1 Felder im Detail

**`prompt`** speichert den Original-Prompt, der in diesen Turn eingespeist würde. Dies ermöglicht es nachgelagerten Systemen, das Ergebnis dem Auslöser zuzuordnen, ohne den Kontext separat mitführen zu müssen.

**`output`** enthält die formatierte Zusammenfassung des Turns. Je nach `structured_output`-Einstellung ist dies entweder ein mehrzeiliger String oder ein JSON-Dokument.

**`matched_commands`** und **`matched_tools`** sind Tupel von Strings, die angeben, welche registrierten Befehle bzw. Werkzeuge auf den Prompt gepasst haben. Diese werden nicht von der Engine selbst berechnet, sondern vom Aufrufer übergeben — die Engine protokolliert sie lediglich.

**`permission_denials`** ist ein Tupel von `PermissionDenial`-Objekten. Jedes Objekt enthält einen `tool_name` und einen `reason`. Diese Datenstruktur dokumentiert, welche Werkzeuge angefragt, aber aus Berechtigungsgründen verweigert würden — ein zentrales Sicherheitsmerkmal.

**`usage`** ist eine `UsageSummary`-Instanz mit den Feldern `input_tokens` und `output_tokens`, die den kumulativen Token-Verbrauch der gesamten Session bis einschließlich dieses Turns widerspiegelt.

**`stop_reason`** ist ein String mit einem von drei möglichen Werten:

| Wert | Bedeutung |
|------|-----------|
| `'completed'` | Der Turn würde normal abgeschlossen |
| `'max_turns_reached'` | Die maximale Anzahl erlaubter Turns war bereits erreicht |
| `'max_budget_reached'` | Das Token-Budget würde mit diesem Turn überschritten |

Auch `TurnResult` ist `frozen=True` — ein Turn-Ergebnis ist ein unveränderliches Protokoll und soll nachträglich nicht mehr manipuliert werden können.

---

## 8.4 Die QueryEnginePort-Klasse

`QueryEnginePort` ist die zentrale, zustandsbehaftete Klasse der Query Engine. Der Name "Port" folgt dem Ports-and-Adapters-Muster (Hexagonale Architektur): Die Klasse definiert die Schnittstelle zur Außenwelt, ohne selbst die konkreten Routing-Entscheidungen zu treffen.

### 8.4.1 Felder

```python
@dataclass
class QueryEnginePort:
    manifest: PortManifest
    config: QueryEngineConfig = field(default_factory=QueryEngineConfig)
    session_id: str = field(default_factory=lambda: uuid4().hex)
    mutable_messages: list[str] = field(default_factory=list)
    permission_denials: list[PermissionDenial] = field(default_factory=list)
    total_usage: UsageSummary = field(default_factory=UsageSummary)
    transcript_store: TranscriptStore = field(default_factory=TranscriptStore)
```

**`manifest`** ist eine `PortManifest`-Instanz, die den aktuellen Zustand des Arbeitsbereichs beschreibt (welche Module portiert sind, welche offen stehen etc.). Es ist das einzige Feld ohne Default-Wert und muss bei der Erzeugung angegeben werden.

**`config`** ist die oben beschriebene `QueryEngineConfig`. Durch die `default_factory` erhält jede neue Engine-Instanz automatisch die Standardkonfiguration mit `max_turns=8` und `max_budget_tokens=2000`.

**`session_id`** wird über `uuid4().hex` generiert — ein 32-stelliger Hex-String ohne Bindestriche. Jede neue Session erhält eine eindeutige Kennung, die bei der Persistierung und Wiederherstellung als Schlüssel dient.

**`mutable_messages`** ist die zentrale Nachrichtenliste. Im Gegensatz zu den eingefrorenen Datenklassen ist diese Liste bewusst mutabel — sie wächst mit jedem Turn um einen Eintrag und wird bei Bedarf kompaktiert.

**`permission_denials`** sammelt alle Berechtigungsverweigerungen über die gesamte Lebensdauer der Session hinweg.

**`total_usage`** akkumuliert den Token-Verbrauch. Da `UsageSummary` selbst `frozen=True` ist, wird bei jedem Turn ein neues Objekt erzeugt und zugewiesen.

**`transcript_store`** ist eine Instanz von `TranscriptStore`, die parallel zu `mutable_messages` geführt wird, aber zusätzlich einen `flushed`-Status besitzt und über eigene Methoden zur Kompaktierung und Wiedergabe verfügt.

### 8.4.2 Factory-Methode: from_workspace()

```python
@classmethod
def from_workspace(cls) -> 'QueryEnginePort':
    return cls(manifest=build_port_manifest())
```

Diese Methode erzeugt eine völlig neue Session. Sie ruft `build_port_manifest()` auf, um den aktuellen Arbeitsbereichszustand zu erfassen, und überlässt alle anderen Felder ihren Standardwerten. Das Ergebnis ist eine frische Engine mit einer neuen `session_id`, leeren Nachrichtenlisten und einem Null-Verbrauch.

### 8.4.3 Factory-Methode: from_saved_session(session_id)

```python
@classmethod
def from_saved_session(cls, session_id: str) -> 'QueryEnginePort':
    stored = load_session(session_id)
    transcript = TranscriptStore(entries=list(stored.messages), flushed=True)
    return cls(
        manifest=build_port_manifest(),
        session_id=stored.session_id,
        mutable_messages=list(stored.messages),
        total_usage=UsageSummary(stored.input_tokens, stored.output_tokens),
        transcript_store=transcript,
    )
```

Diese Methode stellt eine zuvor gespeicherte Session wieder her. Der Ablauf:

1. `load_session(session_id)` liest ein `StoredSession`-Objekt aus dem Dateisystem (standardmässig aus `.port_sessions/`).
2. Ein `TranscriptStore` wird mit den gespeicherten Nachrichten initialisiert und als bereits `flushed` markiert — schließlich stammen die Daten aus einer bereits persistierten Quelle.
3. Die `mutable_messages` und `total_usage` werden aus der gespeicherten Session rekonstruiert.
4. Ein neues `PortManifest` wird erzeugt, da sich der Arbeitsbereich seit der letzten Speicherung verändert haben könnte.

Ein wichtiges Detail: Die `permission_denials` werden nicht wiederhergestellt. Sie gehen beim Speichern verloren, da `StoredSession` sie nicht enthält. Dies ist eine bewusste Designentscheidung — Berechtigungsverweigerungen sind transient und nur für die aktuelle Sitzung relevant.

### 8.4.4 submit_message() — Die Kernmethode

`submit_message()` ist die wichtigste Methode der gesamten Query Engine. Sie implementiert den vollständigen Verarbeitungszyklus eines einzelnen Turns:

```python
def submit_message(
    self,
    prompt: str,
    matched_commands: tuple[str, ...] = (),
    matched_tools: tuple[str, ...] = (),
    denied_tools: tuple[PermissionDenial, ...] = (),
) -> TurnResult:
```

Der Ablauf gliedert sich in acht klar getrennte Schritte:

**Schritt 1: Max-Turns prüfen**

```python
if len(self.mutable_messages) >= self.config.max_turns:
    output = f'Max turns reached before processing prompt: {prompt}'
    return TurnResult(
        prompt=prompt,
        output=output,
        matched_commands=matched_commands,
        matched_tools=matched_tools,
        permission_denials=denied_tools,
        usage=self.total_usage,
        stop_reason='max_turns_reached',
    )
```

Dieser Schritt fungiert als Schutzschalter. Wenn die Nachrichtenliste bereits `max_turns` Einträge enthält, wird sofort ein `TurnResult` mit `stop_reason='max_turns_reached'` zurückgegeben, ohne dass der Prompt weiter verarbeitet wird. Beachtenswert: Der Prompt wird in das `output`-Feld eingebettet, damit der Aufrufer weiß, welcher Prompt nicht mehr verarbeitet werden könnte.

**Schritt 2: Zusammenfassung formatieren**

```python
summary_lines = [
    f'Prompt: {prompt}',
    f'Matched commands: {", ".join(matched_commands) if matched_commands else "none"}',
    f'Matched tools: {", ".join(matched_tools) if matched_tools else "none"}',
    f'Permission denials: {len(denied_tools)}',
]
output = self._format_output(summary_lines)
```

Hier werden die vier Kernaspekte des Turns — Prompt, Befehle, Werkzeuge und Verweigerungen — in eine menschenlesbare Zusammenfassung überführt. Die `_format_output()`-Methode entscheidet dann basierend auf `self.config.structured_output`, ob die Ausgabe als Plaintext oder als JSON gerendert wird.

**Schritt 3: Token-Verbrauch schätzen**

```python
projected_usage = self.total_usage.add_turn(prompt, output)
```

Die Methode `add_turn()` der `UsageSummary`-Klasse berechnet eine vereinfachte Token-Schätzung auf Basis der Wortanzahl. Die resultierende `projected_usage` enthält den kumulativen Verbrauch inklusive des aktuellen Turns.

**Schritt 4: Budget prüfen**

```python
stop_reason = 'completed'
if projected_usage.input_tokens + projected_usage.output_tokens > self.config.max_budget_tokens:
    stop_reason = 'max_budget_reached'
```

Anders als die `max_turns`-Prüfung blockiert die Budget-Prüfung den Turn nicht. Der Turn wird vollständig ausgeführt, aber der `stop_reason` wird auf `'max_budget_reached'` gesetzt, um dem Aufrufer zu signalisieren, dass keine weiteren Turns eingereicht werden sollten.

**Schritt 5: An mutable_messages anhängen**

```python
self.mutable_messages.append(prompt)
```

Der Prompt wird der internen Nachrichtenliste hinzugefügt. Nur der Prompt wird gespeichert, nicht die Ausgabe — die Nachrichtenliste repräsentiert den Verlauf der Benutzereingaben.

**Schritt 6: An transcript_store anhängen**

```python
self.transcript_store.append(prompt)
self.permission_denials.extend(denied_tools)
self.total_usage = projected_usage
```

Parallel zur Nachrichtenliste wird der Prompt auch im Transkript gespeichert. Berechtigungsverweigerungen werden der kumulativen Liste hinzugefügt, und der Token-Verbrauch wird aktualisiert.

**Schritt 7: compact_messages_if_needed()**

```python
self.compact_messages_if_needed()
```

Nach dem Anfügen wird geprüft, ob eine Kompaktierung nötig ist (Details in Abschnitt 8.4.6).

**Schritt 8: TurnResult zurückgeben**

```python
return TurnResult(
    prompt=prompt,
    output=output,
    matched_commands=matched_commands,
    matched_tools=matched_tools,
    permission_denials=denied_tools,
    usage=self.total_usage,
    stop_reason=stop_reason,
)
```

Das Ergebnis wird als unveränderliches `TurnResult` zurückgegeben.

#### Sequenzdiagramm: submit_message()

```
Aufrufer            QueryEnginePort         TranscriptStore       UsageSummary
   |                      |                       |                    |
   |--- submit_message -->|                       |                    |
   |   (prompt, cmds,     |                       |                    |
   |    tools, denials)   |                       |                    |
   |                      |                       |                    |
   |                      |-- len(messages)       |                    |
   |                      |   >= max_turns?       |                    |
   |                      |   [Ja] -> Return      |                    |
   |                      |   [Nein] -> weiter    |                    |
   |                      |                       |                    |
   |                      |-- _format_output() -->|                    |
   |                      |   (summary_lines)     |                    |
   |                      |<-- output ------------|                    |
   |                      |                       |                    |
   |                      |-- add_turn() -------->|-------------------->|
   |                      |                       |    projected_usage  |
   |                      |<-------------------------------------------+
   |                      |                       |                    |
   |                      |-- Budget prüfen       |                    |
   |                      |   (projected > max?)  |                    |
   |                      |                       |                    |
   |                      |-- messages.append()   |                    |
   |                      |                       |                    |
   |                      |-- append(prompt) ---->|                    |
   |                      |                       |                    |
   |                      |-- compact_messages -->|                    |
   |                      |      _if_needed()     |-- compact() ------>|
   |                      |                       |                    |
   |<-- TurnResult -------|                       |                    |
   |                      |                       |                    |
```

### 8.4.5 stream_submit_message() — Der Streaming-Generator

Neben der synchronen `submit_message()` bietet die Engine einen Generator für die schrittweise Ausgabe:

```python
def stream_submit_message(
    self,
    prompt: str,
    matched_commands: tuple[str, ...] = (),
    matched_tools: tuple[str, ...] = (),
    denied_tools: tuple[PermissionDenial, ...] = (),
):
    yield {'type': 'message_start', 'session_id': self.session_id, 'prompt': prompt}
    if matched_commands:
        yield {'type': 'command_match', 'commands': matched_commands}
    if matched_tools:
        yield {'type': 'tool_match', 'tools': matched_tools}
    if denied_tools:
        yield {'type': 'permission_denial', 'denials': [d.tool_name for d in denied_tools]}
    result = self.submit_message(prompt, matched_commands, matched_tools, denied_tools)
    yield {'type': 'message_delta', 'text': result.output}
    yield {
        'type': 'message_stop',
        'usage': {'input_tokens': result.usage.input_tokens,
                  'output_tokens': result.usage.output_tokens},
        'stop_reason': result.stop_reason,
        'transcript_size': len(self.transcript_store.entries),
    }
```

Der Generator emittiert bis zu sechs Ereignisse in einer festen Reihenfolge:

1. **`message_start`** — Enthält die `session_id` und den Prompt. Wird immer emittiert.
2. **`command_match`** — Enthält die erkannten Befehle. Wird nur emittiert, wenn `matched_commands` nicht leer ist.
3. **`tool_match`** — Enthält die erkannten Werkzeuge. Wird nur emittiert, wenn `matched_tools` nicht leer ist.
4. **`permission_denial`** — Enthält die Namen der verweigerten Werkzeuge (nur die `tool_name`-Felder, nicht die vollständigen `PermissionDenial`-Objekte). Wird nur emittiert, wenn `denied_tools` nicht leer ist.
5. **`message_delta`** — Enthält den formatierten Ausgabetext. Wird immer emittiert.
6. **`message_stop`** — Enthält Token-Verbrauch, Abbruchgrund und Transkriptgrösse. Wird immer emittiert.

Dieses Muster ist an die Server-Sent-Events-Architektur angelehnt, wie sie bei Streaming-APIs üblich ist. Es ermöglicht einem Frontend oder einem nachgelagerten Agenten, inkrementell auf die einzelnen Phasen der Verarbeitung zu reagieren, anstatt auf das vollständige Ergebnis warten zu müssen.

#### Sequenzdiagramm: stream_submit_message()

```
Aufrufer            stream_submit_message()        submit_message()
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- message_start -------|                          |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- command_match --------|  (falls vorhanden)      |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- tool_match -----------|  (falls vorhanden)      |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- permission_denial ----|  (falls vorhanden)      |
   |                          |                          |
   |--- next() ------------->|                          |
   |                          |--- submit_message() --->|
   |                          |<-- TurnResult ----------|
   |<-- message_delta --------|                          |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- message_stop ---------|                          |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- StopIteration -------|                          |
```

Ein bemerkenswertes Detail: Die eigentliche `submit_message()`-Logik wird erst ausgeführt, wenn der Consumer des Generators das fünfte Element (`message_delta`) anfordert. Die ersten drei bis vier Ereignisse werden ohne Seiteneffekte emittiert. Das bedeutet: Wenn ein Consumer den Generator nach `message_start` abbricht, findet keine Zustandsmutation statt — die Session bleibt unverändert.

### 8.4.6 compact_messages_if_needed()

```python
def compact_messages_if_needed(self) -> None:
    if len(self.mutable_messages) > self.config.compact_after_turns:
        self.mutable_messages[:] = self.mutable_messages[-self.config.compact_after_turns:]
    self.transcript_store.compact(self.config.compact_after_turns)
```

Diese Methode implementiert eine Sliding-Window-Strategie. Wenn die Nachrichtenliste mehr als `compact_after_turns` Einträge enthält, werden alle Einträge außer den letzten `compact_after_turns` verworfen. Die Zuweisung `self.mutable_messages[:] = ...` stellt sicher, dass die In-Place-Modifikation der bestehenden Liste erfolgt, anstatt eine neue Liste zu erzeugen. Das ist wichtig, falls andere Teile des Systems eine Referenz auf dieselbe Liste halten.

Anschließend wird auch der `TranscriptStore` kompaktiert, wobei derselbe `compact_after_turns`-Wert als `keep_last`-Parameter übergeben wird. Diese Symmetrie stellt sicher, dass `mutable_messages` und `transcript_store.entries` stets dieselbe Teilmenge der Konversationshistorie enthalten.

### 8.4.7 persist_session()

```python
def persist_session(self) -> str:
    self.flush_transcript()
    path = save_session(
        StoredSession(
            session_id=self.session_id,
            messages=tuple(self.mutable_messages),
            input_tokens=self.total_usage.input_tokens,
            output_tokens=self.total_usage.output_tokens,
        )
    )
    return str(path)
```

Die Persistierung folgt einem Zwei-Schritt-Prozess:

1. **Transkript flushen**: Durch den Aufruf von `self.flush_transcript()` wird `transcript_store.flushed` auf `True` gesetzt. Dies signalisiert, dass alle Einträge gesichert würden.

2. **Session speichern**: Ein `StoredSession`-Objekt wird erzeugt und über `save_session()` im Dateisystem abgelegt. Gespeichert werden: die `session_id`, die Nachrichten als unveränderliches Tupel, sowie die Token-Zähler. Der Rückgabewert ist der Pfad zur erzeugten Datei.

Nicht gespeichert werden: die `QueryEngineConfig`, das `PortManifest`, und die `permission_denials`. Die Konfiguration wird bei der Wiederherstellung neu erzeugt (mit Standardwerten), das Manifest wird frisch aus dem Arbeitsbereich gelesen, und die Berechtigungsverweigerungen sind — wie bereits erläutert — transient.

### 8.4.8 render_summary()

```python
def render_summary(self) -> str:
```

Diese Methode erzeugt einen Markdown-formatierten Überblicksbericht über den aktuellen Zustand der Engine. Der Bericht umfasst:

- Das Manifest des Arbeitsbereichs (via `self.manifest.to_markdown()`)
- Die Grösse der Befehls- und Werkzeug-Backlogs (jeweils maximal 10 Zusammenfassungszeilen)
- Die Session-ID
- Die Anzahl gespeicherter Konversationsrunden
- Die Anzahl protokollierter Berechtigungsverweigerungen
- Die Token-Verbrauchswerte
- Die Konfigurationsparameter `max_turns` und `max_budget_tokens`
- Den Flush-Status des Transkripts

Dieser Bericht ist primär für diagnostische Zwecke gedacht — er gibt Entwicklern und Operatoren einen schnellen Überblick über den Zustand einer laufenden oder wiederhergestellten Session.

### 8.4.9 Private Hilfsmethoden

**`_format_output(summary_lines)`** ist die Weiche zwischen Plaintext- und strukturierter Ausgabe. Bei `structured_output=False` werden die Zeilen einfach mit Newlines verbunden. Bei `structured_output=True` wird ein Dictionary erzeugt und an `_render_structured_output()` übergeben.

**`_render_structured_output(payload)`** versucht bis zu `structured_retry_limit` Mal, den Payload als JSON zu serialisieren. Im Fehlerfall wird der Payload auf ein Minimum reduziert und erneut versucht. Dieses Muster ist defensiv, aber in der Praxis ist `json.dumps()` bei Dictionaries mit Strings und Listen nahezu fehlerresistent. Der defensive Code schützt gegen den Fall, dass durch einen Programmierfehler nicht-serialisierbare Objekte in den Payload gelangen.

---

## 8.5 TranscriptStore — Das Gesprächsprotokoll

```python
@dataclass
class TranscriptStore:
    entries: list[str] = field(default_factory=list)
    flushed: bool = False
```

Der `TranscriptStore` ist eine schlanke, aber konzeptionell wichtige Klasse mit nur vier Methoden:

### 8.5.1 append(entry)

```python
def append(self, entry: str) -> None:
    self.entries.append(entry)
    self.flushed = False
```

Fügt einen Eintrag hinzu und setzt `flushed` auf `False`. Dieses Flag ist das zentrale Koordinationsmerkmal: Es zeigt an, ob seit dem letzten `flush()` neue, noch nicht persistierte Einträge hinzugekommen sind.

### 8.5.2 compact(keep_last=10)

```python
def compact(self, keep_last: int = 10) -> None:
    if len(self.entries) > keep_last:
        self.entries[:] = self.entries[-keep_last:]
```

Behält nur die letzten `keep_last` Einträge. Wie bei `mutable_messages` erfolgt die Zuweisung in-place. Der Standardwert von 10 wird in der Praxis durch den `compact_after_turns`-Wert aus der Konfiguration überschrieben.

### 8.5.3 replay()

```python
def replay(self) -> tuple[str, ...]:
    return tuple(self.entries)
```

Gibt alle Einträge als unveränderliches Tupel zurück. Diese Methode wird von `QueryEnginePort.replay_user_messages()` exponiert und ermöglicht es externen Systemen, den Gesprächsverlauf nachzulesen, ohne die interne Liste zu mutieren.

### 8.5.4 flush()

```python
def flush(self) -> None:
    self.flushed = True
```

Markiert das Transkript als persistiert. Die Methode löscht bewusst keine Einträge — sie setzt lediglich das Flag. Das tatsächliche Schreiben auf die Festplatte erfolgt durch `QueryEnginePort.persist_session()`, das `flush()` als Vorbereitung aufruft.

### 8.5.5 Das flushed-Flag als Zustandsanzeiger

Das `flushed`-Flag implementiert ein minimalistisches Dirty-Tracking: `False` bedeutet "es gibt ungesicherte Änderungen", `True` bedeutet "alles ist persistiert". Dieses Flag wird in `render_summary()` angezeigt und könnte von einer zukünftigen Auto-Save-Logik genutzt werden, um unnötige Schreibvorgänge zu vermeiden.

#### Sequenzdiagramm: Lebenszyklus des TranscriptStore

```
QueryEnginePort              TranscriptStore             Dateisystem
      |                            |                          |
      |-- new TranscriptStore ---->|                          |
      |                     entries=[], flushed=False         |
      |                            |                          |
      |-- submit_message #1 ------>|                          |
      |      append("prompt1")     |                          |
      |                     entries=["p1"], flushed=False      |
      |                            |                          |
      |-- submit_message #2 ------>|                          |
      |      append("prompt2")     |                          |
      |                     entries=["p1","p2"], flushed=False |
      |                            |                          |
      |-- persist_session() ------>|                          |
      |      flush()               |                          |
      |                     entries=["p1","p2"], flushed=True  |
      |                            |                          |
      |-- save_session() -------->|---------------------------->|
      |                            |              session.json  |
      |                            |                          |
      |-- submit_message #3 ------>|                          |
      |      append("prompt3")     |                          |
      |                  entries=["p1","p2","p3"], flushed=False|
      |                            |                          |
```

---

## 8.6 QueryEngineRuntime — Die Routing-Subklasse

Die Datei `src/QueryEngine.py` (beachte die Großschreibung — eine bewusste Konvention, um die "öffentliche" API-Klasse von der internen Port-Klasse zu unterscheiden) definiert die `QueryEngineRuntime`:

```python
class QueryEngineRuntime(QueryEnginePort):
    def route(self, prompt: str, limit: int = 5) -> str:
        matches = PortRuntime().route_prompt(prompt, limit=limit)
        lines = ['# Query Engine Route', '', f'Prompt: {prompt}', '']
        if not matches:
            lines.append('No mirrored command/tool matches found.')
            return '\n'.join(lines)
        lines.append('Matches:')
        lines.extend(
            f'- [{match.kind}] {match.name} ({match.score}) — {match.source_hint}'
            for match in matches
        )
        return '\n'.join(lines)
```

### 8.6.1 Vererbung und Verantwortung

`QueryEngineRuntime` erbt von `QueryEnginePort` und erweitert sie um eine einzige Methode: `route()`. Damit erhält sie automatisch alle Port-Fähigkeiten — Session-Management, Turn-Verarbeitung, Kompaktierung, Persistierung — und fügt darüber hinaus die Fähigkeit hinzu, einen Prompt aktiv gegen die registrierten Befehle und Werkzeuge zu routen.

### 8.6.2 Die route()-Methode

Die Methode nimmt einen Prompt und ein optionales Limit (Standard: 5) entgegen und delegiert die eigentliche Suche an eine `PortRuntime`-Instanz. Das Routing in `PortRuntime.route_prompt()` führt eine Token-basierte Suche durch: Der Prompt wird in Tokens zerlegt (Schrägstriche und Bindestriche werden als Trennzeichen behandelt), und diese Tokens werden gegen die Namen der portierten Befehle und Werkzeuge abgeglichen.

Das Ergebnis ist eine Liste von `RoutedMatch`-Objekten mit den Feldern `kind` (entweder `'command'` oder `'tool'`), `name`, `score` und `source_hint`. Diese werden als Markdown-formatierter String zurückgegeben.

Bemerkenswert ist, dass `PortRuntime()` bei jedem Aufruf von `route()` neu instanziiert wird. Es gibt kein Caching der Runtime-Instanz. Dies ist ein bewusster Kompromiss: Da sich die registrierten Befehle und Werkzeuge zwischen Aufrufen ändern können (etwa durch dynamisches Laden von Modulen), wäre ein Cache potenziell inkonsistent.

### 8.6.3 Architektonische Einordnung

Die Trennung zwischen `QueryEnginePort` und `QueryEngineRuntime` folgt dem Open/Closed-Prinzip: Die Port-Klasse ist abgeschlossen gegenüber Änderungen, aber offen für Erweiterungen durch Subklassen. Eine alternative Runtime könnte beispielsweise eine andere Routing-Strategie implementieren, ohne die Kernlogik der Turn-Verarbeitung anfassen zu müssen.

Die `__all__`-Deklaration in `QueryEngine.py` exportiert beide Klassen:

```python
__all__ = ['QueryEnginePort', 'QueryEngineRuntime']
```

Dies signalisiert, dass Konsumenten des Moduls sowohl den "rohen" Port als auch die vollständige Runtime nutzen können.

---

## 8.7 Zusammenspiel der Komponenten

### 8.7.1 Vollständiger Lebenszyklus einer Session

Das folgende Sequenzdiagramm zeigt den typischen Lebenszyklus einer Query-Engine-Session von der Erzeugung bis zur Persistierung:

```
Aufrufer              QueryEngineRuntime         PortRuntime        TranscriptStore    Dateisystem
   |                        |                       |                    |                |
   |-- from_workspace() --->|                       |                    |                |
   |<-- neue Instanz -------|                       |                    |                |
   |   (session_id=abc123)  |                       |                    |                |
   |                        |                       |                    |                |
   |-- route("bash ls") --->|                       |                    |                |
   |                        |-- route_prompt() ---->|                    |                |
   |                        |<-- [RoutedMatch] -----|                    |                |
   |<-- Markdown-Report ----|                       |                    |                |
   |                        |                       |                    |                |
   |-- submit_message() --->|                       |                    |                |
   |   ("bash ls",          |                       |                    |                |
   |    cmds=("Bash",),     |                       |                    |                |
   |    tools=())           |                       |                    |                |
   |                        |-- append() ---------->|------------------>|                |
   |                        |-- compact() --------->|------------------>|                |
   |<-- TurnResult ---------|                       |                    |                |
   |   (stop_reason=        |                       |                    |                |
   |    'completed')        |                       |                    |                |
   |                        |                       |                    |                |
   |-- [... weitere Turns]  |                       |                    |                |
   |                        |                       |                    |                |
   |-- persist_session() -->|                       |                    |                |
   |                        |-- flush() ----------->|------------------>|                |
   |                        |-- save_session() ---->|------------------->|-- write() --->|
   |<-- Dateipfad ----------|                       |                    |                |
   |                        |                       |                    |                |
```

### 8.7.2 Wiederherstellung und Fortsetzung

```
Aufrufer              QueryEngineRuntime         session_store       TranscriptStore
   |                        |                       |                    |
   |-- from_saved_session ->|                       |                    |
   |   (session_id=abc123)  |                       |                    |
   |                        |-- load_session() ---->|                    |
   |                        |<-- StoredSession -----|                    |
   |                        |                       |                    |
   |                        |-- new TranscriptStore |                    |
   |                        |   (entries=[...],     |------------------->|
   |                        |    flushed=True)      |                    |
   |<-- Instanz (restored) -|                       |                    |
   |                        |                       |                    |
   |-- submit_message() --->|                       |                    |
   |   (neuer Prompt)       |-- append() ---------->|------------------->|
   |                        |              flushed = False               |
   |<-- TurnResult ---------|                       |                    |
```

---

## 8.8 Fehlerbehandlung und Robustheit

### 8.8.1 Verteidigungslinien

Die Query Engine implementiert mehrere Verteidigungslinien gegen fehlerhafte oder übermässige Nutzung:

1. **Turn-Limit**: Verhindert endlose Schleifen durch automatisierte Agenten.
2. **Token-Budget**: Begrenzt den kumulativen Ressourcenverbrauch.
3. **Kompaktierung**: Verhindert unbegrenztes Wachstum des Nachrichtenverlaufs.
4. **Structured-Output-Retries**: Fängt Serialisierungsfehler ab.
5. **Frozen Dataclasses**: Verhindert versehentliche Mutation von Konfiguration und Ergebnissen.

### 8.8.2 Weiche vs. harte Limits

Die Unterscheidung zwischen weichen und harten Limits ist architektonisch bemerkenswert:

- **`max_turns`** ist ein **hartes Limit**: Ist es erreicht, wird der Turn nicht mehr verarbeitet.
- **`max_budget_tokens`** ist ein **weiches Limit**: Der Turn wird noch ausgeführt, aber der `stop_reason` signalisiert die Überschreitung. Die Verantwortung, die Session tatsächlich zu beenden, liegt beim Aufrufer.

Dieses Design gibt dem Aufrufer Flexibilität: Er kann auf ein Budget-Signal reagieren, indem er die Session beendet, oder er kann — bei Bedarf — noch einen abschließenden "Zusammenfassungs-Turn" durchführen, bevor er stoppt.

---

## 8.9 Zusammenfassung

Die Query Engine von Claw Code ist ein durchdachtes Subsystem, das mehrere Verantwortlichkeiten saüber trennt:

| Komponente | Verantwortung | Datei |
|---|---|---|
| `QueryEngineConfig` | Unveränderliche Konfiguration | `query_engine.py` |
| `TurnResult` | Unveränderliches Turn-Ergebnis | `query_engine.py` |
| `QueryEnginePort` | Zustandsbehaftete Session-Verwaltung | `query_engine.py` |
| `TranscriptStore` | Gesprächsprotokoll mit Dirty-Tracking | `transcript.py` |
| `QueryEngineRuntime` | Routing-fähige Erweiterung | `QueryEngine.py` |

Die Architektur folgt klar erkennbaren Prinzipien: Hexagonale Architektur (Port/Adapter-Trennung), Open/Closed (Erweiterbarkeit durch Vererbung), und Defensive Programmierung (Retries, Limits, eingefrorene Datenklassen). Mit lediglich 238 Zeilen Code über drei Dateien verteilt bietet die Query Engine eine erstaunlich vollständige Lösung für das Problem der gesteuerten, budgetierten und protokollierten Konversationsverarbeitung.


# Kapitel 9: Session-Management & Persistenz

## Einleitung

Eines der zentralen Probleme jeder interaktiven Anwendung, die auf Large Language Models (LLMs) aufsetzt, ist die Frage: Wie bewahrt man den Zustand einer Konversation über die Grenzen eines einzelnen Prozesslebenszyklus hinaus? Claw Code löst dieses Problem durch ein dreischichtiges Persistenzmodell, das aus dem **Session Store**, dem **History Log** und dem **Transcript Store** besteht. Jede dieser Schichten erfuellt eine klar abgegrenzte Aufgabe: Der Session Store serialisiert den vollständigen Nachrichtenverlauf samt Token-Verbrauchsstatistiken auf die Festplatte. Der History Log hält strukturierte Meilensteine einer laufenden Sitzung im Arbeitsspeicher fest. Und der Transcript Store fungiert als kompaktierbarer Ringpuffer für die chronologische Abfolge der Benutzer-Eingaben.

Dieses Kapitel führt durch den gesamten Quellcode der drei Module `session_store.py`, `history.py` und `transcript.py`, erklaert jede Klasse und jede Funktion im Detail und zeigt abschließend, wie die drei Schichten im Rahmen des vollständigen Session-Lebenszyklus zusammenspielen.

---

## 9.1 Der Session Store: `session_store.py`

### 9.1.1 Die `StoredSession`-Datenklasse

Das Herzstrück der Persistenzschicht ist die Klasse `StoredSession`, definiert als unveränderliche Datenklasse (`frozen=True`):

```python
@dataclass(frozen=True)
class StoredSession:
    session_id: str
    messages: tuple[str, ...]
    input_tokens: int
    output_tokens: int
```

Die Entscheidung für `frozen=True` ist bewusst und architektonisch bedeutsam. Eine gespeicherte Session repräsentiert einen **abgeschlossenen Snapshot** -- einen Zeitpunkt, zu dem der Zustand der Konversation eingefroren und auf die Festplatte geschrieben würde. Nachdem eine `StoredSession` erzeugt würde, darf kein Attribut mehr verändert werden. Das schuetzt vor einer ganzen Klasse von Fehlern, bei denen ein bereits persistiertes Objekt im Speicher nachtraeglich modifiziert wird und so eine Diskrepanz zwischen dem gespeicherten und dem tatsaechlichen Zustand entsteht.

Die vier Felder im Detail:

**`session_id: str`** -- Ein eindeutiger Bezeichner für die Sitzung. Er wird an anderer Stelle (in `QueryEnginePort`) durch `uuid4().hex` erzeugt, was eine 32 Zeichen lange hexadezimale Zeichenkette ohne Bindestriche ergibt. Dieser Bezeichner dient gleichzeitig als Dateiname auf der Festplatte (ergaenzt um die Endung `.json`), was eine direkte Zuordnung zwischen Session-Objekt und Datei ermöglicht.

**`messages: tuple[str, ...]`** -- Ein unveränderliches Tupel aller Nachrichten, die während der Sitzung ausgetauscht würden. Die Wahl eines Tupels anstelle einer Liste ist konsistent mit der `frozen=True`-Semantik: Da die Datenklasse unveränderlich ist, wäre ein mutables `list`-Feld zwar technisch möglich (Python prüft nur die Zuweisung an das Attribut, nicht die Mutation des Inhalts), aber semantisch irreführend. Ein Tupel signalisiert dem Leser unmissverstaendlich: "Diese Nachrichtensequenz ist abgeschlossen."

**`input_tokens: int`** und **`output_tokens: int`** -- Die kumulierten Token-Zähler für die gesamte Sitzung. Sie werden aus dem `UsageSummary`-Objekt übernommen, das die `QueryEnginePort` während der Nachrichtenverarbeitung pflegt. Diese Werte sind unverzichtbar für Budgetierungsentscheidungen: Beim Wiederherstellen einer Sitzung kann die Engine sofort erkennen, wie viele Tokens bereits verbraucht würden, und ihr verbleibendes Budget entsprechend berechnen.

### 9.1.2 Das Standard-Verzeichnis

```python
DEFAULT_SESSION_DIR = Path('.port_sessions')
```

Alle Sessions werden standardmäßig in einem Verzeichnis namens `.port_sessions` relativ zum aktuellen Arbeitsverzeichnis gespeichert. Der führende Punkt im Namen folgt der Unix-Konvention für versteckte Verzeichnisse und signalisiert, dass es sich um interne Daten handelt, die nicht Teil des eigentlichen Projekts sind. In einer produktiven Umgebung würde man dieses Verzeichnis typischerweise in die `.gitignore`-Datei aufnehmen.

### 9.1.3 Die Funktion `save_session`

```python
def save_session(session: StoredSession, directory: Path | None = None) -> Path:
    target_dir = directory or DEFAULT_SESSION_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / f'{session.session_id}.json'
    path.write_text(json.dumps(asdict(session), indent=2))
    return path
```

Diese Funktion übernimmt die Serialisierung einer `StoredSession` auf die Festplatte. Der Ablauf ist geradlinig, aber in jedem Schritt durchdacht:

1. **Verzeichnis-Bestimmung:** Wird kein explizites Verzeichnis übergeben, greift die Funktion auf `DEFAULT_SESSION_DIR` zurück. Die Verwendung des `or`-Operators statt eines expliziten `if`-Blocks ist idiomatisches Python und deckt sowohl `None` als auch andere falsy-Werte ab.

2. **Verzeichniserstellung:** Der Aufruf `target_dir.mkdir(parents=True, exist_ok=True)` ist defensiv programmiert. `parents=True` stellt sicher, dass auch verschachtelte Verzeichnisstrukturen vollständig angelegt werden koennen -- beispielsweise wenn `directory` als `Path('data/sessions/archive')` übergeben wird und keines dieser Verzeichnisse existiert. `exist_ok=True` verhindert einen `FileExistsError`, falls das Verzeichnis bereits vorhanden ist. Diese Kombination macht den Aufruf idempotent: Er kann beliebig oft ausgeführt werden, ohne Fehler zu produzieren.

3. **Dateipfad-Konstruktion:** Der Pfad wird aus dem Verzeichnis und dem `session_id` zusammengesetzt, wobei die Erweiterung `.json` angehängt wird. Durch die Verwendung der UUID als Dateiname sind Kollisionen praktisch ausgeschlossen.

4. **Serialisierung:** `dataclasses.asdict(session)` wandelt die Datenklasse rekursiv in ein wörterbuchähnliches Objekt um. Das Tupel `messages` wird dabei automatisch in eine JSON-Liste konvertiert. `json.dumps(..., indent=2)` erzeugt formatierten JSON-Text, der auch manuell lesbar ist -- ein wichtiges Merkmal für Debugging-Zwecke.

5. **Rückgabewert:** Die Funktion gibt den vollständigen `Path` der geschriebenen Datei zurück. Das ermöglicht dem Aufrufer, den Pfad zu protokollieren oder weiterzuverarbeiten, ohne ihn selbst rekonstruieren zu müssen.

### 9.1.4 Die Funktion `load_session`

```python
def load_session(session_id: str, directory: Path | None = None) -> StoredSession:
    target_dir = directory or DEFAULT_SESSION_DIR
    data = json.loads((target_dir / f'{session_id}.json').read_text())
    return StoredSession(
        session_id=data['session_id'],
        messages=tuple(data['messages']),
        input_tokens=data['input_tokens'],
        output_tokens=data['output_tokens'],
    )
```

Die Gegenfunktion zu `save_session` liest eine Sitzung anhand ihrer ID von der Festplatte zurück. Bemerkenswert ist hier die **explizite Rekonstruktion** des `StoredSession`-Objekts: Anstatt das Wörterbuch direkt an den Konstruktor zu übergeben (etwa per `StoredSession(**data)`), werden die einzelnen Felder namentlich extrahiert. Das hat drei Vorteile:

Erstens wird `data['messages']` explizit in ein `tuple` konvertiert. JSON kennt nur Arrays, die Python als `list` deserialisiert. Um die Typannotation `tuple[str, ...]` der Datenklasse zu erfuellen und die Unveränderlichkeitssemantik zu wahren, ist diese Konvertierung notwendig.

Zweitens dient die explizite Zuordnung als eine Art "Schema-Validierung zur Laufzeit": Sollte die JSON-Datei ein fehlendes Feld enthalten, wirft Python einen `KeyError` mit dem konkreten Feldnamen -- wesentlich informativer als ein generischer `TypeError` bei `**data`.

Drittens schuetzt die Methode vor unbekannten Feldern in der JSON-Datei. Würde ein zukünftiges Format zusätzliche Felder enthalten, würde `StoredSession(**data)` mit einem `TypeError` ("unexpected keyword argument") fehlschlagen, während die explizite Zuordnung diese Felder einfach ignoriert.

### 9.1.5 Das JSON-Format auf der Festplatte

Eine gespeicherte Session-Datei hat folgendes Format:

```json
{
  "session_id": "a3f8c91b0e4d47f29a1c6e83d5b72f40",
  "messages": [
    "Erklaere mir die Architektur des Projekts",
    "Welche Module gibt es?"
  ],
  "input_tokens": 1247,
  "output_tokens": 583
}
```

Dieses Format ist bewusst flach und einfach gehalten. Es gibt keine Verschachtelung, keine Metadaten-Umschlaege, kein Versionierungsfeld. Das entspricht dem Prinzip der Einfachheit: Solange sich das Schema nicht ändert, ist kein Overhead notwendig. Sollte eine Schema-Migration in Zukunft nötig werden, könnte man ein `"version"`-Feld ergaenzen und die `load_session`-Funktion um Migrationslogik erweitern.

---

## 9.2 Der History Log: `history.py`

### 9.2.1 Die `HistoryEvent`-Datenklasse

```python
@dataclass(frozen=True)
class HistoryEvent:
    title: str
    detail: str
```

Ein `HistoryEvent` repräsentiert einen einzelnen Meilenstein innerhalb einer Sitzung. Es besteht aus einem kurzen Titel und einem ausführlicheren Detail-Text. Auch hier ist `frozen=True` gesetzt: Ein einmal protokolliertes Ereignis ist unveränderlich. Diese Eigenschaft spiegelt die Realitaet wider -- vergangene Ereignisse koennen nicht nachtraeglich modifiziert werden.

Die Einfachheit dieser Klasse ist beabsichtigt. Ein `HistoryEvent` trägt keinen Zeitstempel, keine Prioritaet, keine Kategorisierung. Es ist ein reiner Textbaustein, dessen Semantik sich ausschließlich aus dem Inhalt von `title` und `detail` ergibt. Die Verantwortung für die Einhaltung von Namenskonventionen liegt beim aufrufenden Code.

### 9.2.2 Die `HistoryLog`-Klasse

```python
@dataclass
class HistoryLog:
    events: list[HistoryEvent] = field(default_factory=list)

    def add(self, title: str, detail: str) -> None:
        self.events.append(HistoryEvent(title=title, detail=detail))

    def as_markdown(self) -> str:
        lines = ['# Session History', '']
        lines.extend(f'- {event.title}: {event.detail}' for event in self.events)
        return '\n'.join(lines)
```

Im Gegensatz zu `HistoryEvent` ist `HistoryLog` **mutable** -- sie hat kein `frozen=True`. Das ist notwendig, da das Log während der Sitzung kontinuierlich wächst.

**Die `add`-Methode** ist eine Komfortfunktion, die ein neues `HistoryEvent` erzeugt und an die interne Liste anhängt. Sie nimmt `title` und `detail` als separate Strings entgegen, anstatt ein fertiges `HistoryEvent`-Objekt zu erwarten. Diese Entkopplung hat den Vorteil, dass der aufrufende Code nicht direkt von der `HistoryEvent`-Klasse abhaengen muss.

**Die `as_markdown`-Methode** serialisiert das gesamte Log in ein Markdown-Dokument. Das Format ist bewusst schlicht: Eine Überschrift erster Ordnung (`# Session History`), gefolgt von einer Aufzaehlungsliste, in der jedes Ereignis als `- title: detail` formatiert wird. Diese Markdown-Repräsentation wird in der `as_markdown`-Methode der `RuntimeSession` verwendet, wo sie als Abschnitt in den vollständigen Session-Bericht eingebettet wird.

### 9.2.3 Verwendung in der Praxis

In der `PortRuntime.bootstrap_session`-Methode (Datei `runtime.py`) wird der `HistoryLog` an mehreren Stellen befuellt:

```python
history = HistoryLog()
history.add('context', f'python_files={context.python_file_count}, archive_available={context.archive_available}')
history.add('registry', f'commands={len(PORTED_COMMANDS)}, tools={len(PORTED_TOOLS)}')
history.add('routing', f'matches={len(matches)} for prompt={prompt!r}')
history.add('execution', f'command_execs={len(command_execs)} tool_execs={len(tool_execs)}')
history.add('turn', f'commands=... tools=... denials=... stop={turn_result.stop_reason}')
history.add('session_store', persisted_session_path)
```

Man erkennt die Konvention: Der `title` benennt die Phase des Bootstrapping-Prozesses (`context`, `registry`, `routing`, `execution`, `turn`, `session_store`), während `detail` die konkreten Kennzahlen dieser Phase enthält. Auf diese Weise entsteht ein kompaktes, aber informatives Protokoll, das sich hervorragend für Debugging und Nachvollziehbarkeit eignet. Im Markdown-Export würde dies beispielsweise so aussehen:

```markdown
# Session History

- context: python_files=42, archive_available=True
- registry: commands=7, tools=5
- routing: matches=3 for prompt='Erklaere die Architektur'
- execution: command_execs=1 tool_execs=2
- turn: commands=1 tools=2 denials=0 stop=completed
- session_store: .port_sessions/a3f8c91b0e4d47f29a1c6e83d5b72f40.json
```

---

## 9.3 Der Transcript Store: `transcript.py`

### 9.3.1 Aufbau der Klasse

```python
@dataclass
class TranscriptStore:
    entries: list[str] = field(default_factory=list)
    flushed: bool = False

    def append(self, entry: str) -> None:
        self.entries.append(entry)
        self.flushed = False

    def compact(self, keep_last: int = 10) -> None:
        if len(self.entries) > keep_last:
            self.entries[:] = self.entries[-keep_last:]

    def replay(self) -> tuple[str, ...]:
        return tuple(self.entries)

    def flush(self) -> None:
        self.flushed = True
```

Der `TranscriptStore` ist ein spezialisierter In-Memory-Puffer, der sich von einer einfachen Liste durch drei wesentliche Fähigkeiten unterscheidet: **Kompaktierung**, **Replay** und **Flush-Tracking**.

### 9.3.2 Die `append`-Methode

Jeder neue Eintrag wird am Ende der Liste angehängt. Gleichzeitig wird das `flushed`-Flag auf `False` zurückgesetzt. Diese Semantik ist wichtig: Sie signalisiert, dass seit dem letzten Flush neue Daten hinzugekommen sind und die persistierte Version auf der Festplatte möglicherweise veraltet ist. Im Kontext des Gesamtsystems wird `append` innerhalb von `QueryEnginePort.submit_message` aufgerufen, sodass jede verarbeitete Nachricht automatisch im Transkript landet.

### 9.3.3 Die `compact`-Methode

```python
def compact(self, keep_last: int = 10) -> None:
    if len(self.entries) > keep_last:
        self.entries[:] = self.entries[-keep_last:]
```

Die `compact`-Methode implementiert eine **Sliding-Window-Kompaktierung**. Wenn die Anzahl der Eintraege `keep_last` übersteigt, werden alle Eintraege bis auf die letzten `keep_last` verworfen. Die Verwendung der Slice-Zuweisung `self.entries[:] = ...` anstelle von `self.entries = ...` ist ein subtiles, aber wichtiges Detail: Die Slice-Zuweisung **mutiert die bestehende Liste in-place**, während eine einfache Zuweisung eine **neue Liste** erzeugen und die Referenz ersetzen würde. In diesem Fall macht der Unterschied keinen semantischen Unterschied, da `entries` ohnehin ein privates Feld ist. Aber die In-Place-Mutation ist konsistent mit der Slice-Zuweisung, die auch in `QueryEnginePort.compact_messages_if_needed` für `mutable_messages` verwendet wird, und signalisiert die Absicht: "Wir modifizieren den Inhalt, nicht die Identitaet."

Die Kompaktierung ist eine Antwort auf ein fundamentales Problem von LLM-basierten Systemen: das **Kontextfenster**. Je länger eine Konversation laeuft, desto mehr Tokens werden für die historischen Nachrichten verbraucht, und desto weniger Platz bleibt für neue Eingaben und Ausgaben. Durch das Verwerfen älterer Eintraege wird der Speicherverbrauch begrenzt, wobei die juengsten Eintraege erhalten bleiben, da sie typischerweise die relevantesten sind.

In der `QueryEnginePort` wird die Kompaktierung durch `compact_messages_if_needed` gesteuert:

```python
def compact_messages_if_needed(self) -> None:
    if len(self.mutable_messages) > self.config.compact_after_turns:
        self.mutable_messages[:] = self.mutable_messages[-self.config.compact_after_turns:]
    self.transcript_store.compact(self.config.compact_after_turns)
```

Hier wird sowohl die Nachrichtenliste als auch der `TranscriptStore` mit demselben `compact_after_turns`-Wert (standardmäßig 12) kompaktiert. Das stellt sicher, dass beide Datenstrukturen synchron bleiben.

### 9.3.4 Die `replay`-Methode

```python
def replay(self) -> tuple[str, ...]:
    return tuple(self.entries)
```

`replay` gibt eine unveränderliche Kopie aller aktuellen Eintraege zurück. Die Rückgabe als Tupel -- nicht als Liste -- ist eine bewusste Designentscheidung: Der Aufrufer erhält einen Snapshot, den er nicht versehentlich modifizieren kann. In der `QueryEnginePort` wird diese Methode über `replay_user_messages` exponiert und ermöglicht es, die bisherige Konversation an externe Konsumenten weiterzugeben, ohne die interne Datenstruktur zu gefaehrden.

### 9.3.5 Die `flush`-Methode

```python
def flush(self) -> None:
    self.flushed = True
```

`flush` setzt lediglich ein boolsches Flag. Es loescht **keine** Daten und schreibt **nichts** auf die Festplatte. Seine Funktion ist rein signalisierend: "Die aktuellen Daten würden vom Aufrufer verarbeitet." Im Kontext der `QueryEnginePort` wird `flush` unmittelbar vor der Persistierung aufgerufen:

```python
def persist_session(self) -> str:
    self.flush_transcript()
    path = save_session(
        StoredSession(
            session_id=self.session_id,
            messages=tuple(self.mutable_messages),
            input_tokens=self.total_usage.input_tokens,
            output_tokens=self.total_usage.output_tokens,
        )
    )
    return str(path)
```

Der Flush signalisiert, dass der Transkript-Inhalt in die `StoredSession` überführt und auf die Festplatte geschrieben würde. Nachfolgende `append`-Aufrufe setzen das Flag wieder auf `False`, was anzeigt, dass erneut persistiert werden müsste.

---

## 9.4 Das Zusammenspiel: `QueryEnginePort` als Orchestrator

Die drei vorgestellten Module -- `session_store`, `history` und `transcript` -- werden in der Klasse `QueryEnginePort` (Datei `query_engine.py`) zusammengeführt. Diese Klasse ist der zentrale Orchestrator des Session-Managements.

### 9.4.1 Erzeugung der Session

Bei der Instanziierung einer `QueryEnginePort` wird automatisch eine neue Session-ID generiert:

```python
session_id: str = field(default_factory=lambda: uuid4().hex)
```

Gleichzeitig wird ein leerer `TranscriptStore` angelegt:

```python
transcript_store: TranscriptStore = field(default_factory=TranscriptStore)
```

Der `HistoryLog` wird nicht innerhalb der `QueryEnginePort` verwaltet, sondern in der übergeordneten `RuntimeSession`-Klasse (Datei `runtime.py`), die als Fassade über die gesamte Sitzung dient.

### 9.4.2 Nachrichtenverarbeitung

Innerhalb von `submit_message` werden sowohl die mutable Nachrichtenliste als auch der Transcript Store aktualisiert:

```python
self.mutable_messages.append(prompt)
self.transcript_store.append(prompt)
```

Unmittelbar danach wird geprüft, ob eine Kompaktierung notwendig ist:

```python
self.compact_messages_if_needed()
```

### 9.4.3 Persistierung

Die Methode `persist_session` erzeugt eine `StoredSession` aus dem aktuellen Zustand und schreibt sie auf die Festplatte:

```python
def persist_session(self) -> str:
    self.flush_transcript()
    path = save_session(
        StoredSession(
            session_id=self.session_id,
            messages=tuple(self.mutable_messages),
            input_tokens=self.total_usage.input_tokens,
            output_tokens=self.total_usage.output_tokens,
        )
    )
    return str(path)
```

Der Ablauf: Zuerst wird der Transcript Store geflusht, dann wird eine `StoredSession` konstruiert, deren `messages`-Feld aus den aktuellen `mutable_messages` als Tupel gespeist wird. Anschließend ruft `save_session` die JSON-Serialisierung und den Dateischreibvorgang durch. Der zurückgegebene Pfad wird als String weitergereicht.

### 9.4.4 Wiederherstellung

Die Klassenmethode `from_saved_session` stellt eine vollständige `QueryEnginePort` aus einer gespeicherten Session wieder her:

```python
@classmethod
def from_saved_session(cls, session_id: str) -> 'QueryEnginePort':
    stored = load_session(session_id)
    transcript = TranscriptStore(entries=list(stored.messages), flushed=True)
    return cls(
        manifest=build_port_manifest(),
        session_id=stored.session_id,
        mutable_messages=list(stored.messages),
        total_usage=UsageSummary(stored.input_tokens, stored.output_tokens),
        transcript_store=transcript,
    )
```

Bemerkenswert ist hier die Konvertierung in beide Richtungen: `stored.messages` ist ein Tupel (aus `StoredSession`), wird aber sowohl für `mutable_messages` als auch für `TranscriptStore.entries` in eine `list` konvertiert, da beide Strukturen im laufenden Betrieb mutiert werden müssen. Der `TranscriptStore` wird mit `flushed=True` initialisiert, da seine Daten gerade von der Festplatte geladen würden -- es besteht kein Bedarf für eine erneute Persistierung, solange keine neuen Eintraege hinzukommen.

Das `manifest` wird frisch über `build_port_manifest()` erzeugt, da es den aktuellen Zustand des Workspace widerspiegeln soll, nicht den zum Zeitpunkt der Speicherung.

---

## 9.5 Der vollständige Session-Lebenszyklus

Zusammenfassend lässt sich der Lebenszyklus einer Session in fünf Phasen gliedern:

### Phase 1: Erstellung

Beim Aufruf von `QueryEnginePort.from_workspace()` oder bei der direkten Instanziierung wird eine neue Session-ID durch `uuid4().hex` generiert. Ein leerer `TranscriptStore` und eine leere Nachrichtenliste werden angelegt. Die Session existiert zu diesem Zeitpunkt ausschließlich im Arbeitsspeicher.

In der übergeordneten `PortRuntime.bootstrap_session` wird außerdem ein `HistoryLog` erzeugt und mit initialen Kontextinformationen befuellt.

### Phase 2: Nachrichtenverarbeitung

Jeder Aufruf von `submit_message` fuegt den Prompt sowohl der Nachrichtenliste als auch dem Transcript Store hinzu. Die Engine berechnet den Token-Verbrauch, prüft Budgetgrenzen und erzeugt ein `TurnResult`. Der History Log wird in der umgebenden `bootstrap_session`-Methode mit Informationen über das Routing, die Ausführung und das Ergebnis der Runde befuellt.

### Phase 3: Transkript-Kompaktierung

Nach jeder Nachrichtenverarbeitung prüft `compact_messages_if_needed`, ob die Anzahl der Nachrichten den Schwellenwert `compact_after_turns` (Standard: 12) überschreitet. Falls ja, werden sowohl `mutable_messages` als auch `transcript_store.entries` auf die letzten 12 Eintraege beschnitten. Dieser Mechanismus verhindert ein unbegrenztes Wachstum der Datenstrukturen und begrenzt den Token-Verbrauch bei der nächsten Nachrichtenverarbeitung.

### Phase 4: Persistierung

Die Methode `persist_session` buendelt den aktuellen Zustand -- Session-ID, Nachrichten und Token-Zähler -- in eine unveränderliche `StoredSession` und delegiert die Serialisierung an `save_session`. Das Ergebnis ist eine JSON-Datei im Verzeichnis `.port_sessions/`, die den vollständigen Konversationszustand repräsentiert.

### Phase 5: Wiederherstellung

Durch `QueryEnginePort.from_saved_session(session_id)` wird die JSON-Datei gelesen, zu einer `StoredSession` deserialisiert und als Grundlage für eine neue, voll funktionsfähige `QueryEnginePort` verwendet. Die wiederhergestellte Engine kann sofort neue Nachrichten verarbeiten, wobei sie nahtlos an den gespeicherten Zustand anknuepft -- inklusive der Token-Zähler, die für Budgetentscheidungen relevant sind.

---

## 9.6 Architektonische Bewertung

### Stärken

**Einfachheit:** Das gesamte Persistenzmodell umfasst weniger als 85 Zeilen Code über drei Dateien. Es gibt keine Datenbank, kein ORM, keine Migration -- nur JSON-Dateien und Datenklassen. Diese Einfachheit reduziert die Fehlerwahrscheinlichkeit und macht das System leicht verstaendlich.

**Immutabilitaet an den richtigen Stellen:** `StoredSession` und `HistoryEvent` sind `frozen`, während `HistoryLog`, `TranscriptStore` und `QueryEnginePort` mutable sind. Diese Aufteilung folgt einem klaren Prinzip: Datenstrukturen, die Snapshots repräsentieren, sind unveränderlich; Datenstrukturen, die aktive Prozesse repräsentieren, sind veränderlich.

**Kompaktierung als First-Class-Konzept:** Die Tatsache, dass Kompaktierung direkt im `TranscriptStore` implementiert ist (und nicht als nachgelagerter Hack), zeigt, dass die Autoren die Beschraenkungen von LLM-Kontextfenstern von Anfang an berücksichtigt haben.

**Testbarkeit:** Da `save_session` und `load_session` das Zielverzeichnis als Parameter akzeptieren, koennen Tests problemlos temporaere Verzeichnisse verwenden, ohne das Standard-Verzeichnis zu verschmutzen.

### Moegliche Erweiterungen

**Zeitstempel:** Weder `StoredSession` noch `HistoryEvent` tragen einen Zeitstempel. Für Debugging-Zwecke wäre ein `created_at`-Feld in `StoredSession` und ein `timestamp`-Feld in `HistoryEvent` nützlich.

**Kompaktierungsstrategie:** Die aktuelle Strategie "behalte die letzten N Eintraege" ist einfach und effektiv, aber verlustbehaftet. Eine Erweiterung könnte eine Zusammenfassungsfunktion sein, die ältere Eintraege zu einem komprimierten Überblick verdichtet, anstatt sie vollständig zu verwerfen.

**Fehlerbehandlung:** `load_session` wirft unbehandelte Ausnahmen, wenn die Datei nicht existiert (`FileNotFoundError`) oder das JSON-Format ungültig ist (`json.JSONDecodeError`). Eine robustere Version könnte spezifische Session-Ausnahmen definieren.

---

## 9.7 Zusammenfassung

Das Session-Management von Claw Code folgt dem Prinzip "so einfach wie möglich, aber nicht einfacher". Drei kompakte Module -- `session_store.py`, `history.py` und `transcript.py` -- decken gemeinsam die gesamte Bandbreite der Zustandsverwaltung ab: von der In-Memory-Protokollierung über die Kompaktierung bis hin zur Persistierung und Wiederherstellung. Die `QueryEnginePort` orchestriert diese Komponenten und bietet mit `from_saved_session` und `persist_session` zwei symmetrische Methoden, die den Lebenszyklus einer Session saüber einrahmen. Das Ergebnis ist ein Persistenzmodell, das ohne externe Abhängigkeiten auskommt, leicht testbar ist und dennoch alle Anforderungen eines interaktiven LLM-Clients erfuellt.


# Kapitel 10: Setup, Bootstrap & Initialisierung

## Einleitung

Jedes komplexe Softwaresystem steht vor der Herausforderung, seinen eigenen Startvorgang so zu organisieren, dass Abhängigkeiten korrekt aufgelöst, Ressourcen rechtzeitig bereitgestellt und Sicherheitsentscheidungen an der richtigen Stelle getroffen werden. In Claw Code ist dieser Prozess besonders vielschichtig: Bevor die erste Nutzeranfrage bearbeitet werden kann, muss das System seine Laufzeitumgebung inspizieren, Vorab-Ladeprozesse (Prefetches) starten, Vertrauensentscheidungen treffen, Befehle und Werkzeuge registrieren und schließlich den passenden Betriebsmodus wahlen. Dieses Kapitel widmet sich vollständig dem Zusammenspiel der sechs Quelldateien, die diesen Ablauf implementieren: `setup.py`, `prefetch.py`, `deferred_init.py`, `bootstrap_graph.py`, `context.py` und `system_init.py`. Wir werden jede Datenstruktur, jede Funktion und jede Entwurfsentscheidung im Detail durchleuchten.

---

## 10.1 Der Workspace-Setup-Prozess (`setup.py`)

Die Datei `src/setup.py` bildet das Herzstück der Initialisierungslogik. Sie importiert sowohl die Prefetch-Infrastruktur als auch das Deferred-Init-Subsystem und orchestriert deren Zusammenspiel in einer einzigen, koharenten Ablauffolge.

### 10.1.1 Die Klasse `WorkspaceSetup`

```python
@dataclass(frozen=True)
class WorkspaceSetup:
    python_version: str
    implementation: str
    platform_name: str
    test_command: str = 'python3 -m unittest discover -s tests -v'
```

`WorkspaceSetup` ist ein unveränderliches (frozen) Dataclass, das die grundlegenden Laufzeitparameter des Systems erfasst. Die vier Felder haben folgende Bedeutung:

- **`python_version`**: Ein String der Form `"3.12.1"`, der die aktuelle Python-Version im Format `major.minor.patch` enthalt. Die Erzeugung erfolgt in `build_workspace_setup()` durch Zusammensetzen der ersten drei Elemente von `sys.version_info`.

- **`implementation`**: Der Name der Python-Implementierung, wie ihn `platform.python_implementation()` liefert -- also typischerweise `"CPython"`, aber auch `"PyPy"` oder `"GraalPy"` ware denkbar. Dieses Feld ermöglicht es dem System, implementierungsspezifische Optimierungen oder Warnungen auszugeben.

- **`platform_name`**: Ein ausführlicher Plattform-String, der durch `platform.platform()` erzeugt wird und Informationen wie Betriebssystem, Version und Architektur enthalt (z.B. `"Linux-6.18.5-x86_64-with-glib2.39"`).

- **`test_command`**: Ein vorkonfigurierter Befehl zum Ausfuhren der Test-Suite. Der Standardwert `'python3 -m unittest discover -s tests -v'` nutzt den eingebauten `unittest`-Discovery-Mechanismus und sucht rekursiv im Verzeichnis `tests` nach Testmodulen. Der Parameter `-v` sorgt für ausführliche Ausgabe. Dieser Wert ist als Default gesetzt, kann aber bei der Instanziierung uberschrieben werden.

### 10.1.2 Die Methode `startup_steps()`

```python
def startup_steps(self) -> tuple[str, ...]:
    return (
        'start top-level prefetch side effects',
        'build workspace context',
        'load mirrored command snapshot',
        'load mirrored tool snapshot',
        'prepare parity audit hooks',
        'apply trust-gated deferred init',
    )
```

Diese Methode gibt ein Tupel mit exakt sechs Strings zuruck, die die logischen Schritte des Startvorgangs in der richtigen Reihenfolge benennen. Jeder Schritt reprasentiert eine klar abgegrenzte Phase:

1. **`start top-level prefetch side effects`** -- Hier werden die drei Prefetch-Operationen (`mdm_raw_read`, `keychain_prefetch`, `project_scan`) gestartet. Der Begriff "side effects" ist bewusst gewahlt: Diese Operationen haben Nebeneffekte auf den Systemzustand, indem sie Daten vorladen, die spater benötigt werden.

2. **`build workspace context`** -- Der `PortContext` wird aufgebaut, der die Verzeichnisstruktur des Projekts erfasst und Dateizahler berechnet.

3. **`load mirrored command snapshot`** -- Die verfügbaren Befehle (Commands) werden aus dem Command-Registry geladen. Der Begriff "mirrored" deutet darauf hin, dass diese Befehle als Spiegel (Paritätskopie) des TypeScript-Originals zu verstehen sind.

4. **`load mirrored tool snapshot`** -- Analog werden die verfügbaren Werkzeuge (Tools) geladen.

5. **`prepare parity audit hooks`** -- Audit-Hooks werden vorbereitet, die die Paritätstreue zwischen der Python-Portierung und dem TypeScript-Original uberwachen.

6. **`apply trust-gated deferred init`** -- Der abschließende Schritt fuhrt die vertrauensabhängige verzogerte Initialisierung durch. Nur wenn `trusted=True` gilt, werden Plugins, Skills, MCP-Prefetches und Session-Hooks aktiviert.

Die Reihenfolge ist nicht zufallig gewahlt: Prefetches müssen zuerst starten, damit ihre Ergebnisse möglichst fruh verfügbar sind. Der Kontext muss vor den Befehlen und Werkzeugen stehen, da diese möglicherweise Kontextinformationen benötigen. Die Parity-Hooks müssen vor dem Deferred-Init vorbereitet sein, damit auch die verzogerte Initialisierung überwacht werden kann. Und das Deferred-Init kommt zuletzt, weil es von der Vertrauensentscheidung abhangt, die erst nach dem CLI-Parsing feststeht.

### 10.1.3 Die Klasse `SetupReport`

```python
@dataclass(frozen=True)
class SetupReport:
    setup: WorkspaceSetup
    prefetches: tuple[PrefetchResult, ...]
    deferred_init: DeferredInitResult
    trusted: bool
    cwd: Path
```

`SetupReport` ist die zentrale Ergebnisstruktur des gesamten Setup-Prozesses. Sie bundelt alle Informationen, die wahrend der Initialisierung gewonnen würden:

- **`setup`**: Die `WorkspaceSetup`-Instanz mit den Laufzeitparametern.
- **`prefetches`**: Ein Tupel von `PrefetchResult`-Objekten -- eines für jede der drei Prefetch-Operationen.
- **`deferred_init`**: Das Ergebnis der verzogerten Initialisierung als `DeferredInitResult`.
- **`trusted`**: Ein boolescher Wert, der den Vertrauensstatus der aktuellen Sitzung angibt.
- **`cwd`**: Das aktuelle Arbeitsverzeichnis als `Path`-Objekt.

Die Methode `as_markdown()` erzeugt eine menschenlesbare Markdown-Darstellung des gesamten Reports. Dabei werden die Python-Version, die Plattform, der Vertrauensstatus und das Arbeitsverzeichnis aufgelistet, gefolgt von den Prefetch-Ergebnissen und den Deferred-Init-Details. Diese Methode ist besonders nützlich für Diagnose- und Debugging-Zwecke, da sie einen vollständigen Überblick über den Startzustand des Systems liefert.

### 10.1.4 Die Funktion `run_setup()`

```python
def run_setup(cwd: Path | None = None, trusted: bool = True) -> SetupReport:
    root = cwd or Path(__file__).resolve().parent.parent
    prefetches = [
        start_mdm_raw_read(),
        start_keychain_prefetch(),
        start_project_scan(root),
    ]
    return SetupReport(
        setup=build_workspace_setup(),
        prefetches=tuple(prefetches),
        deferred_init=run_deferred_init(trusted=trusted),
        trusted=trusted,
        cwd=root,
    )
```

`run_setup()` ist die Einstiegsfunktion, die den gesamten Setup-Ablauf ausführt. Sie akzeptiert zwei optionale Parameter:

- `cwd`: Das Arbeitsverzeichnis. Falls `None`, wird automatisch das Elternverzeichnis des `src`-Ordners ermittelt -- also das Projektwurzelverzeichnis.
- `trusted`: Der Vertrauensstatus, standardmäßig `True`.

Die Funktion startet zunächst alle drei Prefetch-Operationen in Reihenfolge, baut dann das `WorkspaceSetup`-Objekt und fuhrt das Deferred-Init aus. Alle Ergebnisse werden in einem `SetupReport` zusammengefasst und zurückgegeben. Bemerkenswert ist, dass die Prefetches als Liste gesammelt und dann in ein Tupel konvertiert werden -- dies stellt die Unveränderlichkeit des `SetupReport` sicher.

---

## 10.2 Prefetch-Operationen (`prefetch.py`)

Die Datei `src/prefetch.py` definiert die Prefetch-Infrastruktur: einen leichtgewichtigen Mechanismus, um kostspielige I/O-Operationen fruhzeitig anzustoßen.

### 10.2.1 Die Klasse `PrefetchResult`

```python
@dataclass(frozen=True)
class PrefetchResult:
    name: str
    started: bool
    detail: str
```

Jedes Prefetch-Ergebnis tragt drei Informationen:

- **`name`**: Ein maschinenlesbarer Bezeichner wie `"mdm_raw_read"`, `"keychain_prefetch"` oder `"project_scan"`.
- **`started`**: Ein boolescher Wert, der angibt, ob die Operation erfolgreich gestartet würde. In der aktuellen Implementierung ist dieser Wert stets `True`, da es sich um simulierte Operationen handelt. In einer Produktionsumgebung könnte das Starten eines Prefetches fehlschlagen -- etwa wenn eine Netzwerkverbindung nicht verfügbar ist.
- **`detail`**: Ein menschenlesbarer Beschreibungstext, der den Zweck und Status der Operation zusammenfasst.

### 10.2.2 Die drei Prefetch-Funktionen

**`start_mdm_raw_read()`** simuliert das Vorladen von MDM-Rohdaten (Mobile Device Management). In einem realen System würden hier Konfigurationsdaten von einem MDM-Server abgefragt -- etwa erlaubte Aktionen, Richtlinieneinstellungen oder Gerateinformationen. Der Prefetch stellt sicher, dass diese Daten bereits im Speicher liegen, wenn sie spater benötigt werden, anstatt den Nutzer durch eine synchrone Netzwerkanfrage zu blockieren.

**`start_keychain_prefetch()`** simuliert das Vorladen von Keychain-Daten. Die Keychain (Schlüsselkette) enthalt Authentifizierungstoken, API-Schlüssel und andere sicherheitsrelevante Daten. Durch das fruhzeitige Laden dieser Daten wird vermieden, dass der erste authentifizierte API-Aufruf durch eine Keychain-Abfrage verzogert wird. Der Detailtext verweist explizit auf den "trusted startup path", was darauf hindeutet, dass das Keychain-Prefetching besonders im vertrauenswurdigen Modus relevant ist.

**`start_project_scan(root: Path)`** simuliert einen Scan des Projektwurzelverzeichnisses. Dieser Schritt analysiert die Verzeichnisstruktur, identifiziert relevante Dateien und baut ein initiales Verstandnis der Projektstruktur auf. Der übergebene `root`-Parameter bestimmt, welches Verzeichnis gescannt wird. In der simulierten Implementierung wird der Pfad lediglich im Detailtext vermerkt; in der Praxis würde hier ein tatsächlicher Dateisystemscan stattfinden.

Alle drei Funktionen folgen demselben Muster: Sie erzeugen ein `PrefetchResult` mit einem eindeutigen Namen, `started=True` und einem beschreibenden Detail-String. Dieses einheitliche Interface macht es leicht, weitere Prefetch-Operationen hinzuzufugen, ohne die aufrufende Logik in `setup.py` anpassen zu müssen -- es genügt, eine neue Funktion zu definieren, die ein `PrefetchResult` zurückgibt, und sie in die Liste in `run_setup()` einzufugen.

---

## 10.3 Verzogerte Initialisierung (`deferred_init.py`)

Die Datei `src/deferred_init.py` implementiert das Konzept der vertrauensabhängigen verzogerten Initialisierung -- einen Mechanismus, der sicherstellt, dass potenziell riskante Subsysteme nur dann aktiviert werden, wenn die aktuelle Sitzung als vertrauenswurdig eingestuft würde.

### 10.3.1 Die Klasse `DeferredInitResult`

```python
@dataclass(frozen=True)
class DeferredInitResult:
    trusted: bool
    plugin_init: bool
    skill_init: bool
    mcp_prefetch: bool
    session_hooks: bool
```

Diese Klasse enthalt funf boolesche Felder, die den Aktivierungsstatus der vier vertrauensabhängigen Subsysteme sowie den Vertrauensstatus selbst festhalten:

- **`trusted`**: Spiegelt den übergebenen Vertrauensstatus wider.
- **`plugin_init`**: Gibt an, ob die Plugin-Initialisierung durchgeführt würde. Plugins erweitern die Funktionalität des Systems um zusätzliche Fähigkeiten.
- **`skill_init`**: Gibt an, ob Skills geladen würden. Skills sind spezialisierte Fähigkeiten, die kontextabhängig aufgerufen werden können.
- **`mcp_prefetch`**: Gibt an, ob MCP-Daten (Model Context Protocol) vorgeladen würden. MCP ermöglicht die Kommunikation mit externen Diensten und Werkzeugen.
- **`session_hooks`**: Gibt an, ob Session-Hooks registriert würden. Diese Hooks ermöglichen es, bei bestimmten Ereignissen wahrend einer Sitzung automatisch Code auszufuhren.

Die Methode `as_lines()` erzeugt ein Tupel von formatierten Strings -- einen pro Subsystem -- die den jeweiligen Aktivierungsstatus anzeigen. Diese Methode wird vom `SetupReport` in seiner `as_markdown()`-Methode verwendet.

### 10.3.2 Die Funktion `run_deferred_init()`

```python
def run_deferred_init(trusted: bool) -> DeferredInitResult:
    enabled = bool(trusted)
    return DeferredInitResult(
        trusted=trusted,
        plugin_init=enabled,
        skill_init=enabled,
        mcp_prefetch=enabled,
        session_hooks=enabled,
    )
```

Die Logik ist bewusst einfach gehalten: Der Parameter `trusted` wird in einen booleschen Wert konvertiert (was bei einem bereits booleschen Parameter ein No-Op ist, aber robuster gegenüber truthy/falsy-Werten macht), und dieser Wert wird für alle vier Subsysteme verwendet.

**Wenn `trusted=True`**: Alle vier Subsysteme werden aktiviert (`plugin_init=True`, `skill_init=True`, `mcp_prefetch=True`, `session_hooks=True`). Das System lauft mit voller Funktionalität.

**Wenn `trusted=False`**: Alle vier Subsysteme werden deaktiviert. Das System lauft in einem eingeschrankten Modus, in dem keine Plugins geladen, keine Skills initialisiert, keine MCP-Daten vorgeladen und keine Session-Hooks registriert werden. Dies ist ein Sicherheitsmechanismus: In einer nicht vertrauenswurdigen Umgebung könnte das Laden von Plugins oder das Ausfuhren von Hooks ein Risiko darstellen.

Diese binare Alles-oder-Nichts-Logik ist eine bewusste Entwurfsentscheidung. In einer differenzierteren Implementierung könnte man einzelne Subsysteme unabhängig voneinander steuern. Die aktuelle Implementierung bevorzugt jedoch Einfachheit und Vorhersagbarkeit: Entweder ist das System vollständig vertrauenswurdig oder es ist es nicht, und die Konsequenzen sind in beiden Fallen klar definiert.

---

## 10.4 Der Bootstrap-Graph (`bootstrap_graph.py`)

Die Datei `src/bootstrap_graph.py` formalisiert den gesamten Startvorgang als gerichteten Graphen mit sieben aufeinanderfolgenden Phasen.

### 10.4.1 Die Klasse `BootstrapGraph`

```python
@dataclass(frozen=True)
class BootstrapGraph:
    stages: tuple[str, ...]
```

Die Klasse ist minimal: Sie enthalt lediglich ein Tupel von Stage-Bezeichnern. Die Methode `as_markdown()` erzeugt eine Markdown-Auflistung aller Phasen, was für Dokumentations- und Diagnosezwecke nützlich ist.

### 10.4.2 Die sieben Phasen des Bootstrap-Graphen

Die Funktion `build_bootstrap_graph()` erzeugt den konkreten Graphen mit folgenden sieben Phasen:

**Phase 1: `top-level prefetch side effects`**

Dies ist die allererste Phase und hat die hochste Priorität. Noch bevor irgendwelche Parsing- oder Validierungslogik ausgeführt wird, werden die Prefetch-Operationen gestartet. Der Grund: Prefetches involvieren typischerweise I/O-Operationen (Netzwerk, Dateisystem), die Latenz verursachen. Je fruher sie gestartet werden, desto großer ist die Wahrscheinlichkeit, dass ihre Ergebnisse bereits verfügbar sind, wenn sie spater abgefragt werden.

**Phase 2: `warning handler and environment guards`**

In dieser Phase werden Warnungs-Handler und Umgebungsschutzvorrichtungen eingerichtet. Warnungs-Handler fangen Python-Warnings ab und leiten sie in das Logging-System um. Umgebungsschutzvorrichtungen (Environment Guards) uberprüfen, ob die Laufzeitumgebung den Mindestanforderungen entspricht -- etwa die richtige Python-Version, vorhandene Umgebungsvariablen oder notwendige Systemressourcen. Falls eine Guard-Bedingung nicht erfullt ist, wird der Startvorgang abgebrochen, bevor weitere Initialisierung stattfindet.

**Phase 3: `CLI parser and pre-action trust gate`**

Hier werden die Kommandozeilenargumente geparst und die Vertrauensentscheidung getroffen. Der CLI-Parser interpretiert die übergebenen Argumente und Flags. Das "Trust Gate" ist eine Sicherheitsschranke, die vor der Ausführung jeglicher Aktionen uberprüft, ob die aktuelle Sitzung vertrauenswurdig ist. Diese Entscheidung beeinflusst direkt das spatere Deferred-Init in Phase 5.

**Phase 4: `setup() + commands/agents parallel load`**

In dieser Phase geschehen zwei Dinge gleichzeitig: Die `run_setup()`-Funktion wird ausgeführt (was die Prefetch-Ergebnisse sammelt und das `WorkspaceSetup` aufbaut), und parallel dazu werden die Befehle und Agenten geladen. Die Parallelisierung ist ein wichtiger Performanzgewinn: Da das Laden von Commands und Agents unabhängig vom Workspace-Setup ist, können beide Vorgange uberlappend stattfinden.

**Phase 5: `deferred init after trust`**

Nachdem die Vertrauensentscheidung aus Phase 3 feststeht und das Setup aus Phase 4 abgeschlossen ist, wird nun die verzogerte Initialisierung durchgeführt. Hier entscheidet sich, ob Plugins, Skills, MCP-Prefetches und Session-Hooks aktiviert werden oder nicht.

**Phase 6: `mode routing: local / remote / ssh / teleport / direct-connect / deep-link`**

Diese Phase wahlt den Betriebsmodus des Systems. Claw Code unterstützt sechs verschiedene Modi:

- **local**: Lokale Ausführung auf dem gleichen Rechner.
- **remote**: Verbindung zu einem entfernten Server.
- **ssh**: Ausführung über eine SSH-Verbindung.
- **teleport**: Ein spezieller Fernzugriffsmodus, der möglicherweise ein Teleport-kompatibles Netzwerk nutzt.
- **direct-connect**: Direkte Verbindung ohne Vermittler.
- **deep-link**: Ausführung über einen Deep Link, der spezifische Aktionen oder Kontexte direkt ansteuert.

Das Mode-Routing analysiert die CLI-Argumente und die Umgebungskonfiguration, um den passenden Modus zu wahlen, und leitet die Ausführung an den entsprechenden Handler weiter.

**Phase 7: `query engine submit loop`**

Die letzte Phase startet die Hauptschleife des Systems: den Query-Engine-Submit-Loop. In dieser Schleife wartet das System auf Nutzeranfragen, ubermittelt sie an die Query-Engine, empfangt Antworten und stellt diese dar. Diese Schleife lauft, bis der Nutzer die Sitzung beendet.

### 10.4.3 Diagramm der sieben Bootstrap-Phasen

**CLAW CODE BOOTSTRAP GRAPH**

1. **Phase 1: Prefetch Side Effects**
   - `start_mdm_raw_read()`
   - `start_keychain_prefetch()`
   - `start_project_scan(root)`

2. **Phase 2: Warning Handler und Environment Guards**
   - Python-Warnings umleiten
   - Umgebung validieren

3. **Phase 3: CLI Parser und Pre-Action Trust Gate**
   - Argumente parsen
   - `trusted = True / False` entscheiden

4. **Phase 4a/4b** (parallel):
   - **4a: run_setup()** -- WorkspaceSetup, Prefetches
   - **4b: Commands/Agents parallel laden**

5. **Phase 5: Deferred Init After Trust**
   - `trusted=True` --> alles aktiviert; `trusted=False` --> alles deaktiviert
   - Betrifft: plugin_init, skill_init, mcp_prefetch, session_hooks

6. **Phase 6: Mode Routing**
   - Verfuegbare Modi: local, remote, ssh, teleport, direct-connect, deep-link

7. **Phase 7: Query Engine Submit Loop**
   - Zyklus: READ --> PROCESS --> RENDER --> (zurueck zu READ)

---

## 10.5 Der Projektkontext (`context.py`)

Die Datei `src/context.py` stellt den `PortContext` bereit -- eine Datenstruktur, die das gesamte Projektlayout erfasst und quantifiziert.

### 10.5.1 Die Klasse `PortContext`

```python
@dataclass(frozen=True)
class PortContext:
    source_root: Path
    tests_root: Path
    assets_root: Path
    archive_root: Path
    python_file_count: int
    test_file_count: int
    asset_file_count: int
    archive_available: bool
```

Die acht Felder lassen sich in zwei Gruppen unterteilen:

**Verzeichnispfade:**
- **`source_root`**: Das Wurzelverzeichnis des Quellcodes (`<projekt>/src`).
- **`tests_root`**: Das Wurzelverzeichnis der Tests (`<projekt>/tests`).
- **`assets_root`**: Das Wurzelverzeichnis für statische Ressourcen (`<projekt>/assets`).
- **`archive_root`**: Das Verzeichnis, das den TypeScript-Snapshot des Originals enthalt (`<projekt>/archive/claude_code_ts_snapshot/src`). Dieser Pfad ist besonders aufschlussreich: Er zeigt, dass das Projekt eine archivierte Kopie des originalen TypeScript-Quellcodes mitfuhrt, die als Referenz für die Paritätsprüfung dient.

**Zahler und Verfügbarkeit:**
- **`python_file_count`**: Die Anzahl der `.py`-Dateien im `source_root`, rekursiv gezahlt.
- **`test_file_count`**: Die Anzahl der `.py`-Dateien im `tests_root`, rekursiv gezahlt.
- **`asset_file_count`**: Die Anzahl aller Dateien im `assets_root`, rekursiv gezahlt (ohne Einschränkung auf eine bestimmte Endung).
- **`archive_available`**: Ein boolescher Wert, der angibt, ob das Archivverzeichnis überhaupt existiert. Dies ist wichtig, weil das Archiv optional sein könnte -- etwa wenn das Repository ohne den Archivordner geklont würde.

### 10.5.2 Die Funktion `build_port_context()`

```python
def build_port_context(base: Path | None = None) -> PortContext:
    root = base or Path(__file__).resolve().parent.parent
    source_root = root / 'src'
    tests_root = root / 'tests'
    assets_root = root / 'assets'
    archive_root = root / 'archive' / 'claude_code_ts_snapshot' / 'src'
```

Die Funktion akzeptiert ein optionales Basisverzeichnis und leitet daraus die vier Unterpfade ab. Die Dateizahler werden durch Generator-Ausdrucke mit `rglob()` berechnet:

```python
python_file_count=sum(1 for path in source_root.rglob('*.py') if path.is_file()),
```

Dieses Muster ist speichereffizient: Anstatt alle Pfade in eine Liste zu laden, wird jeder Pfad einzeln geprüft und gezahlt. Der `if path.is_file()`-Filter stellt sicher, dass Verzeichnisse, die zufallig auf `.py` enden (theoretisch möglich), nicht mitgezahlt werden.

### 10.5.3 Die Funktion `render_context()`

```python
def render_context(context: PortContext) -> str:
```

Diese Hilfsfunktion erzeugt eine einfache zeilenbasierte Textdarstellung des Kontexts. Sie listet alle acht Felder untereinander auf und ist für die Konsolenausgabe oder Logdateien gedacht. Im Gegensatz zur `as_markdown()`-Methode des `SetupReport` verwendet sie kein Markdown-Format, sondern einfache `Schluessel: Wert`-Zeilen.

---

## 10.6 Die System-Init-Nachricht (`system_init.py`)

Die Datei `src/system_init.py` bildet die oberste Integrationsschicht: Sie fuhrt das Setup aus, fragt die registrierten Befehle und Werkzeuge ab und fasst alles in einer einzigen Init-Nachricht zusammen.

### 10.6.1 Die Funktion `build_system_init_message()`

```python
def build_system_init_message(trusted: bool = True) -> str:
    setup = run_setup(trusted=trusted)
    commands = get_commands()
    tools = get_tools()
    lines = [
        '# System Init',
        '',
        f'Trusted: {setup.trusted}',
        f'Built-in command names: {len(built_in_command_names())}',
        f'Loaded command entries: {len(commands)}',
        f'Loaded tool entries: {len(tools)}',
        '',
        'Startup steps:',
        *(f'- {step}' for step in setup.setup.startup_steps()),
    ]
    return '\n'.join(lines)
```

Diese Funktion ist der zentrale Einstiegspunkt für die Systemmeldung, die zu Beginn einer Sitzung angezeigt wird. Sie:

1. Fuhrt `run_setup()` aus, was alle Prefetches startet und das Deferred-Init durchführt.
2. Ruft `get_commands()` auf, um die Liste aller registrierten Befehle zu erhalten.
3. Ruft `get_tools()` auf, um die Liste aller registrierten Werkzeuge zu erhalten.
4. Ruft `built_in_command_names()` auf, um die Anzahl der eingebauten Befehlsnamen zu ermitteln.

Die erzeugte Nachricht ist ein Markdown-formatierter String, der folgende Informationen enthalt:

- Den Vertrauensstatus der Sitzung.
- Die Anzahl der eingebauten Befehlsnamen (aus `built_in_command_names()`).
- Die Anzahl der geladenen Command-Eintrage (aus `get_commands()`).
- Die Anzahl der geladenen Tool-Eintrage (aus `get_tools()`).
- Die vollständige Liste der sechs Startup-Schritte.

Diese Nachricht dient als Startup-Bericht: Sie informiert den Nutzer (oder das aufrufende System) darüber, in welchem Zustand sich das System nach der Initialisierung befindet. Die Zahlen für Commands und Tools sind besonders nützlich, um auf einen Blick zu erkennen, ob alle erwarteten Erweiterungen korrekt geladen würden.

Bemerkenswert ist die Trennung zwischen `built_in_command_names()` und `get_commands()`: Erstere liefert nur die Namen der eingebauten Befehle (als flache Liste von Strings), wahrend letztere die vollständigen Command-Eintrage zurückgibt (als Liste von Objekten mit Metadaten). Diese Unterscheidung ermöglicht es, sowohl die Gesamtzahl als auch die eingebaute Untermenge getrennt zu berichten.

---

## 10.7 Zusammenspiel der Komponenten

Die sechs Dateien bilden eine klare Abhängigkeitshierarchie:

```
system_init.py
    |
    +-- setup.py
    |       |
    |       +-- prefetch.py       (PrefetchResult, 3 Startfunktionen)
    |       +-- deferred_init.py  (DeferredInitResult, run_deferred_init)
    |
    +-- commands.py               (get_commands, built_in_command_names)
    +-- tools.py                  (get_tools)

bootstrap_graph.py                (eigenständig, dokumentiert den Ablauf)
context.py                        (eigenständig, baut PortContext auf)
```

`system_init.py` steht an der Spitze und orchestriert alles. `setup.py` ist die mittlere Schicht, die `prefetch.py` und `deferred_init.py` zusammenfuhrt. `bootstrap_graph.py` und `context.py` sind eigenständige Module, die keine Abhängigkeiten zu den anderen Setup-Dateien haben und unabhängig verwendet werden können.

Dieses Design folgt dem Prinzip der minimalen Kopplung: Jedes Modul hat eine klar definierte Verantwortlichkeit und kennt nur die Module, die es direkt benötigt. Die Prefetch-Operationen wissen nichts über das Deferred-Init; der Bootstrap-Graph kennt keine konkreten Implementierungsdetails; und der PortContext ist vollständig unabhängig vom Rest der Initialisierungslogik.

---

## 10.8 Entwurfsentscheidungen und Architekturprinzipien

### Unveränderlichkeit durch `frozen=True`

Samtliche Dataclasses in diesen sechs Dateien verwenden `frozen=True`. Dies bedeutet, dass ihre Felder nach der Erzeugung nicht mehr verändert werden können. Diese Entscheidung hat mehrere Vorteile: Sie verhindert versehentliche Mutationen, macht die Objekte hashbar (und damit als Dictionary-Schlüssel oder in Sets verwendbar) und signalisiert klar, dass es sich um Werteobjekte handelt, die den Zustand zu einem bestimmten Zeitpunkt einfrieren.

### Simulation statt realer I/O

Die Prefetch-Funktionen und das Deferred-Init sind bewusst als Simulationen implementiert. Sie fuhren keine tatsächlichen Netzwerkaufrufe oder Dateisystemoperationen durch (mit Ausnahme der Dateizahlung in `build_port_context()`). Dies ermöglicht es, die gesamte Initialisierungslogik deterministisch zu testen, ohne externe Abhängigkeiten oder Infrastruktur zu benötigen.

### Vertrauensmodell als binarer Schalter

Das Vertrauensmodell (`trusted=True/False`) ist bewusst als einfacher boolescher Schalter implementiert. Dies vermeidet die Komplexität eines mehrstufigen Berechtigungssystems und macht die Konsequenzen für den Entwickler sofort klar: Entweder ist alles aktiviert oder nichts. Für ein Produktionssystem könnte man dieses Modell zu einem feingranularen Berechtigungssystem erweitern, aber für die aktuelle Phase des Projekts ist die Einfachheit ein Vorteil.

### Der Bootstrap-Graph als deklaratives Modell

Der Bootstrap-Graph beschreibt den Ablauf deklarativ als Tupel von Strings, anstatt ihn imperativ als Abfolge von Funktionsaufrufen zu implementieren. Dies hat den Vorteil, dass der Graph als Dokumentation dient, ohne gleichzeitig ausführbarer Code sein zu müssen. Er kann für Visualisierung, Validierung und Diagnose verwendet werden, ohne dass die tatsächliche Ausführungslogik betroffen ist.

---

## 10.9 Zusammenfassung

Der Startvorgang von Claw Code ist ein sorgfaltig orchestrierter Prozess, der von `system_init.py` gesteuert und von `setup.py` koordiniert wird. Die drei Prefetch-Operationen (MDM-Rohdaten, Keychain, Projektscan) werden fruhzeitig gestartet, um Latenz zu minimieren. Die verzogerte Initialisierung stellt sicher, dass sicherheitsrelevante Subsysteme nur in vertrauenswurdigen Umgebungen aktiviert werden. Der Bootstrap-Graph formalisiert diesen Ablauf in sieben klar definierten Phasen, vom ersten Prefetch bis zum Query-Engine-Submit-Loop. Der PortContext erfasst die Projektstruktur quantitativ und ermöglicht es dem System, informierte Entscheidungen über verfügbare Ressourcen zu treffen. Zusammen bilden diese Komponenten ein robustes, testbares und klar strukturiertes Initialisierungssystem.


# Kapitel 11: Ausführungsschicht & Laufzeitmodi

## 11.1 Einleitung

Die vorhergehenden Kapitel haben gezeigt, wie Claw Code den gesamten Befehlskatalog und Werkzeugkatalog des Originals in Form von Snapshot-Dateien erfasst, in `PortingModule`-Instanzen überführt und über die Module `commands.py` und `tools.py` zugänglich macht. Doch ein Katalog allein genügt nicht -- ein CLI-Werkzeug muss Befehle *ausführen* können. In diesem Kapitel widmen wir uns der Schicht, die genau diese Aufgabe übernimmt: der **Ausführungsschicht** (*Execution Layer*). Sie besteht aus drei Dateien, die jeweils einen eigenständigen Aspekt der Laufzeit abdecken:

1. **`src/execution_registry.py`** -- Die zentrale Registry, die Befehle und Tools als ausführbare Wrapper-Objekte zusammenführt.
2. **`src/remote_runtime.py`** -- Laufzeitmodi für entfernte Verbindungen (Remote, SSH, Teleport).
3. **`src/direct_modes.py`** -- Direktmodi für unmittelbare Verbindungen (Direct-Connect, Deep-Link).

Gemeinsam bilden diese drei Module das Rückgrat dessen, was in einem vollständigen CLI als Dispatch-Schicht fungieren würde -- mit einem entscheidenden Unterschied: Claw Code führt keine echten Operationen aus. Stattdessen setzt es konsequent auf **Shim-Ausführung**, also auf Platzhalter-Implementierungen, die das Verhalten des Originals nachbilden, ohne tatsächlich in das System einzugreifen. Warum diese Entscheidung getroffen würde und welche architektonischen Vorteile sie bietet, ist das zentrale Thema dieses Kapitels.

---

## 11.2 MirroredCommand und MirroredTool

### 11.2.1 Wrapper um den Katalog

Die Klassen `MirroredCommand` und `MirroredTool` in `execution_registry.py` sind unveränderliche Datenklassen (`frozen=True`), die als Brücke zwischen dem statischen Katalog und der Ausführungslogik dienen. Jede Instanz kapselt exakt zwei Informationen:

```python
@dataclass(frozen=True)
class MirroredCommand:
    name: str
    source_hint: str

    def execute(self, prompt: str) -> str:
        return execute_command(self.name, prompt).message
```

```python
@dataclass(frozen=True)
class MirroredTool:
    name: str
    source_hint: str

    def execute(self, payload: str) -> str:
        return execute_tool(self.name, payload).message
```

Das Feld `name` identifiziert den Befehl oder das Tool eindeutig -- es entspricht dem `name`-Feld des zugrunde liegenden `PortingModule`. Das Feld `source_hint` gibt an, aus welchem Bereich des Originals der Eintrag stammt (beispielsweise `"commands/slash_commands.ts"` oder `"tools/bash_tool.ts"`). Diese beiden Felder werden direkt aus dem jeweiligen `PortingModule` übernommen, wenn die Registry aufgebaut wird.

### 11.2.2 Die execute()-Methode

Beide Klassen besitzen eine `execute()`-Methode, die den jeweiligen Eintrag "ausführt". Bei `MirroredCommand` nimmt die Methode einen `prompt: str` entgegen -- dies entspricht dem Textargument, das ein Benutzer einem Slash-Befehl mitgeben würde (z. B. `/review bitte prüfe die Testabdeckung`). Bei `MirroredTool` nimmt die Methode einen `payload: str` entgegen -- dies entspricht den Eingabedaten, die ein Tool zur Verarbeitung benötigt (z. B. der Dateipfad für ein Dateilesetool oder ein Bash-Kommando für das Bash-Tool).

Intern delegieren beide Methoden an die gleichnamigen Funktionen aus den Katalogmodulen:

- `MirroredCommand.execute(prompt)` ruft `execute_command(self.name, prompt)` auf und gibt das `.message`-Attribut des resultierenden `CommandExecution`-Objekts zurück.
- `MirroredTool.execute(payload)` ruft `execute_tool(self.name, payload)` auf und gibt das `.message`-Attribut des resultierenden `ToolExecution`-Objekts zurück.

### 11.2.3 Was execute_command() und execute_tool() tatsächlich tun

Ein Blick in `commands.py` und `tools.py` offenbart den Kern der Shim-Ausführung. Die Funktion `execute_command()` in `commands.py` (Zeilen 75-80) sucht zunächst das passende `PortingModule` über `get_command(name)`. Wird kein Eintrag gefunden, wird ein `CommandExecution`-Objekt mit `handled=False` und einer Fehlermeldung zurückgegeben. Wird ein Eintrag gefunden, erzeugt die Funktion eine **formatierte Statusnachricht** der Form:

```
Mirrored command 'review' from commands/slash_commands.ts would handle prompt 'bitte prüfe die Testabdeckung'.
```

Analog verhält sich `execute_tool()` in `tools.py` (Zeilen 81-86):

```
Mirrored tool 'BashTool' from tools/bash_tool.ts would handle payload 'ls -la'.
```

Es findet also keine echte Ausführung statt. Kein Bash-Befehl wird gestartet, keine Datei wird gelesen, kein SSH-Tunnel wird aufgebaut. Die Methode beschreibt lediglich, *was* geschehen *würde*, wenn die echte Implementierung vorhanden wäre. Dies ist der fundamentale Charakter der Shim-Ausführung.

### 11.2.4 Der Rückgabewert: Nur die Nachricht

Bemerkenswert ist, dass `MirroredCommand.execute()` und `MirroredTool.execute()` nicht das vollständige `CommandExecution`- bzw. `ToolExecution`-Objekt zurückgeben, sondern nur dessen `message`-Feld als `str`. Damit bieten die Wrapper eine vereinfachte Schnittstelle: Der Aufrufer erhält einen lesbaren Text, der den Ausführungsstatus beschreibt, ohne sich mit den internen Feldern `handled`, `source_hint` oder `prompt`/`payload` befassen zu müssen. Diese Entscheidung folgt dem Prinzip der Informationskapselung -- die Wrapper verbergen die Komplexität des Dispatch-Mechanismus hinter einer einzigen String-Rückgabe.

---

## 11.3 ExecutionRegistry

### 11.3.1 Aufbau und Struktur

Die Klasse `ExecutionRegistry` ist das zentrale Objekt der Ausführungsschicht. Sie bündelt alle ausführbaren Befehle und Tools in zwei unveränderlichen Tupeln:

```python
@dataclass(frozen=True)
class ExecutionRegistry:
    commands: tuple[MirroredCommand, ...]
    tools: tuple[MirroredTool, ...]
```

Die Verwendung von `tuple` statt `list` ist kein Zufall. In Kombination mit `frozen=True` wird sichergestellt, dass eine einmal erstellte Registry weder verändert noch erweitert werden kann. Dies entspricht dem funktionalen Prinzip der Unveränderlichkeit (*immutability*), das sich wie ein roter Faden durch das gesamte Claw-Code-Projekt zieht. Eine unveränderliche Registry hat mehrere Vorteile:

- **Thread-Sicherheit:** Mehrere Teile des Systems können gleichzeitig auf die Registry zugreifen, ohne dass Synchronisationsmechanismen benötigt werden.
- **Vorhersagbarkeit:** Der Zustand der Registry ändert sich nach der Erstellung nicht. Jeder Aufruf von `command()` oder `tool()` liefert bei gleichem Eingabewert garantiert dasselbe Ergebnis.
- **Testbarkeit:** Tests können eine Registry mit bekanntem Inhalt erstellen und sich darauf verlassen, dass kein Seiteneffekt den Zustand verändert.

### 11.3.2 Case-insensitive Lookup: command() und tool()

Die Methode `command(name)` durchsucht das `commands`-Tupel linear nach einem Eintrag, dessen Name -- unabhängig von Groß- und Kleinschreibung -- mit dem übergebenen `name` übereinstimmt:

```python
def command(self, name: str) -> MirroredCommand | None:
    lowered = name.lower()
    for command in self.commands:
        if command.name.lower() == lowered:
            return command
    return None
```

Die Methode `tool(name)` funktioniert identisch, durchsucht jedoch das `tools`-Tupel:

```python
def tool(self, name: str) -> MirroredTool | None:
    lowered = name.lower()
    for tool in self.tools:
        if tool.name.lower() == lowered:
            return tool
    return None
```

Beide Methoden geben `None` zurück, wenn kein passender Eintrag gefunden wird. Der Rückgabetyp `MirroredCommand | None` bzw. `MirroredTool | None` macht dies auf Typebene explizit und zwingt den Aufrufer, den Fehlerfall zu behandeln.

Die Case-Insensitivität ist eine bewusste Designentscheidung, die die Benutzerfreundlichkeit erhöht. Ein Benutzer, der `/Review` statt `/review` eingibt, oder ein Aufrufer, der `bashtool` statt `BashTool` anfordert, wird dennoch den richtigen Eintrag finden. Dies spiegelt das Verhalten des Originals wider, das ebenfalls eine gewiße Toleranz gegenüber der Schreibweise von Befehlsnamen aufweist.

### 11.3.3 Lineare Suche statt Dictionary

Auffällig ist, dass sowohl `command()` als auch `tool()` eine lineare Suche über das Tupel durchführen, anstatt ein Dictionary mit vorberechneten Schlüsseln zu verwenden. Bei einem Dictionary-basierten Ansatz wäre der Lookup in O(1) statt O(n). Warum würde trotzdem die lineare Suche gewählt?

Die Antwort liegt in der Größe der Kataloge und der Prioritätensetzung des Projekts. Der Befehlskatalog und der Werkzeugkatalog umfassen zusammen einige Dutzend Einträge -- eine Größenordnung, bei der die lineare Suche praktisch keinen messbaren Geschwindigkeitsnachteil gegenüber einem Dictionary-Lookup hat. Gleichzeitig bleibt der Code durch die lineare Iteration maximal einfach und lesbar. Es gibt keinen zusätzlichen Initialisierungsschritt, keine Schlüssel-Normalisierung beim Aufbau, und keine Möglichkeit, dass Schlüssel und Einträge auseinanderlaufen. Die Einfachheit des Codes wird also über die theoretische Effizienz gestellt -- eine pragmatische Entscheidung, die für ein Spiegelungsprojekt durchaus angemessen ist.

### 11.3.4 build_execution_registry()

Die Factory-Funktion `build_execution_registry()` ist der einzige vorgesehene Weg, eine `ExecutionRegistry`-Instanz zu erzeugen:

```python
def build_execution_registry() -> ExecutionRegistry:
    return ExecutionRegistry(
        commands=tuple(MirroredCommand(module.name, module.source_hint) for module in PORTED_COMMANDS),
        tools=tuple(MirroredTool(module.name, module.source_hint) for module in PORTED_TOOLS),
    )
```

Die Funktion iteriert über die globalen Tupel `PORTED_COMMANDS` und `PORTED_TOOLS` -- also über die aus den Snapshot-Dateien geladenen `PortingModule`-Instanzen -- und erzeugt für jedes Modul ein entsprechendes `MirroredCommand`- bzw. `MirroredTool`-Objekt. Die Felder `name` und `source_hint` werden dabei eins zu eins übernommen.

Dieses Factory-Pattern hat den Vorteil, dass die Kopplung zwischen Katalog und Registry an genau einer Stelle stattfindet. Wenn sich die Struktur der Snapshot-Daten ändert oder neue Felder hinzukommen, muss nur diese eine Funktion angepasst werden. Gleichzeitig bleibt die `ExecutionRegistry`-Klasse selbst frei von jeglicher Ladungslogik und kennt weder Dateipfade noch JSON-Formate.

---

## 11.4 Laufzeitmodi: RuntimeModeReport

### 11.4.1 Die Datenklasse

Das Modul `remote_runtime.py` definiert die Datenklasse `RuntimeModeReport`, die das Ergebnis eines Laufzeitmodus-Starts beschreibt:

```python
@dataclass(frozen=True)
class RuntimeModeReport:
    mode: str
    connected: bool
    detail: str

    def as_text(self) -> str:
        return f'mode={self.mode}\nconnected={self.connected}\ndetail={self.detail}'
```

Die drei Felder haben folgende Bedeutung:

- **`mode`**: Identifiziert den Laufzeitmodus als String (z. B. `'remote'`, `'ssh'`, `'teleport'`).
- **`connected`**: Gibt an, ob die Verbindung als hergestellt gilt. In der aktuellen Shim-Implementierung wird dieses Feld immer auf `True` gesetzt, da die Verbindung nicht tatsächlich aufgebaut wird -- der Platzhalter nimmt optimistisch an, dass alles funktionieren würde.
- **`detail`**: Eine menschenlesbare Beschreibung des aktuellen Zustands.

Die Methode `as_text()` erzeugt eine einfache Schlüssel-Wert-Darstellung, die sich für Logging, Debugging und Statusanzeigen eignet. Das Format ist bewusst schlicht gehalten -- kein JSON, kein YAML, sondern einfache `key=value`-Paare, getrennt durch Zeilenumbrüche.

### 11.4.2 Die drei Laufzeitmodus-Funktionen

Das Modul stellt drei Funktionen bereit, die jeweils einen spezifischen Laufzeitmodus repräsentieren:

**`run_remote_mode(target: str) -> RuntimeModeReport`**

```python
def run_remote_mode(target: str) -> RuntimeModeReport:
    return RuntimeModeReport('remote', True, f'Remote control placeholder prepared for {target}')
```

Diese Funktion bildet den Remote-Modus ab, in dem das Original eine Verbindung zu einer entfernten Instanz herstellt und Befehle dorthin delegiert. In Claw Code wird lediglich ein Report mit dem Modus `'remote'` und einer Platzhalter-Beschreibung erzeugt.

**`run_ssh_mode(target: str) -> RuntimeModeReport`**

```python
def run_ssh_mode(target: str) -> RuntimeModeReport:
    return RuntimeModeReport('ssh', True, f'SSH proxy placeholder prepared for {target}')
```

Der SSH-Modus bildet den Fall ab, in dem über SSH eine Verbindung zu einem entfernten Host hergestellt wird. Im Original würde hier eine SSH-Sitzung eröffnet, Schlüssel ausgetauscht und ein Kanal aufgebaut. In Claw Code entsteht stattdessen ein Report, der diesen Vorgang beschreibt, ohne ihn durchzuführen.

**`run_teleport_mode(target: str) -> RuntimeModeReport`**

```python
def run_teleport_mode(target: str) -> RuntimeModeReport:
    return RuntimeModeReport('teleport', True, f'Teleport resume/create placeholder prepared for {target}')
```

Der Teleport-Modus ist eine Abstraktion für das Fortsetzen oder Erstellen einer entfernten Sitzung -- ein Konzept, das im Original als Möglichkeit existiert, laufende Sitzungen auf einem anderen Host fortzusetzen oder neue zu starten. Der Report signalisiert, dass ein solcher Vorgang vorbereitet würde.

Alle drei Funktionen folgen demselben Muster: Sie nehmen ein `target` entgegen (typischerweise einen Hostnamen oder eine URL), erzeugen ein `RuntimeModeReport`-Objekt mit `connected=True` und einer beschreibenden `detail`-Nachricht, und geben dieses zurück. Es gibt keine Seiteneffekte, keine Netzwerkzugriffe, keine Zustandsänderungen. Die Funktionen sind reine Funktionen im mathematischen Sinne.

---

## 11.5 Direktmodi: DirectModeReport

### 11.5.1 Die Datenklasse

Das Modul `direct_modes.py` definiert mit `DirectModeReport` eine zur `RuntimeModeReport` analoge Datenklasse:

```python
@dataclass(frozen=True)
class DirectModeReport:
    mode: str
    target: str
    active: bool

    def as_text(self) -> str:
        return f'mode={self.mode}\ntarget={self.target}\nactive={self.active}'
```

Der Unterschied zur `RuntimeModeReport` liegt in den Feldern:

- **`mode`**: Der Modus-Identifikator (z. B. `'direct-connect'` oder `'deep-link'`).
- **`target`**: Das Ziel der Verbindung, direkt als Feld gespeichert (bei `RuntimeModeReport` ist das Ziel nur in der `detail`-Nachricht enthalten).
- **`active`**: Gibt an, ob der Modus als aktiv gilt -- analog zu `connected` bei `RuntimeModeReport`, aber mit einem semantisch passenderem Namen, da Direktmodi keine "Verbindung" im klassischen Sinne herstellen.

Die Methode `as_text()` folgt demselben `key=value`-Format wie bei `RuntimeModeReport`. Beide Report-Klassen teilen also dasselbe Ausgabemuster, sind aber bewusst als separate Klassen modelliert, da sie unterschiedliche Domänenkonzepte repräsentieren.

### 11.5.2 Die beiden Direktmodus-Funktionen

**`run_direct_connect(target: str) -> DirectModeReport`**

```python
def run_direct_connect(target: str) -> DirectModeReport:
    return DirectModeReport(mode='direct-connect', target=target, active=True)
```

Der Direct-Connect-Modus bildet den Fall ab, in dem das CLI eine direkte Verbindung zu einer API-Endstelle oder einem lokalen Dienst herstellt, ohne den Umweg über SSH oder Remote-Proxies. Im Original würde hier ein HTTP-Client konfiguriert, eine WebSocket-Verbindung geöffnet oder eine ähnliche direkte Kommunikation aufgebaut.

**`run_deep_link(target: str) -> DirectModeReport`**

```python
def run_deep_link(target: str) -> DirectModeReport:
    return DirectModeReport(mode='deep-link', target=target, active=True)
```

Der Deep-Link-Modus dient der Integration mit externen Anwendungen über Deep-Links -- URLs, die eine bestimmte Aktion in einer Zielanwendung auslösen. Im Original könnte dies verwendet werden, um eine IDE zu öffnen, einen Browser an eine bestimmte Stelle zu lenken oder eine externe Anwendung mit vordefinierten Parametern zu starten.

Auch hier gilt: Beide Funktionen sind reine Funktionen ohne Seiteneffekte. Sie erzeugen ausschließlich Report-Objekte, die den *beabsichtigten* Vorgang beschreiben.

---

## 11.6 Das Zusammenspiel der Ausführungsschicht

Die drei Module bilden zusammen eine kohärente Ausführungsschicht mit klarer Arbeitsteilung:

| Modul | Verantwortung | Ausgabe |
|---|---|---|
| `execution_registry.py` | Befehle und Tools ausführen | `str` (Statusnachricht) |
| `remote_runtime.py` | Entfernte Laufzeitmodi starten | `RuntimeModeReport` |
| `direct_modes.py` | Direkte Verbindungsmodi starten | `DirectModeReport` |

Der Informationsfluss ist dabei streng unidirektional: Die Snapshot-Daten fließen aus den JSON-Dateien über `PORTED_COMMANDS`/`PORTED_TOOLS` in die `ExecutionRegistry`, die wiederum über `MirroredCommand`/`MirroredTool` an den Aufrufer zurückgibt. Die Laufzeitmodi stehen orthogonal dazu -- sie befassen sich nicht mit der Ausführung einzelner Befehle, sondern mit der Frage, *wie* und *wo* die Ausführung stattfinden soll.

In einem vollständig implementierten System würde die Laufzeitmoduswahl *vor* der Befehlsausführung stattfinden: Zuerst wird entschieden, ob lokal, remote, via SSH oder per Teleport gearbeitet wird, und dann werden Befehle im gewählten Kontext dispatched. Claw Code bildet beide Aspekte ab -- Modusauswahl und Befehlsausführung -- jedoch jeweils als Shim.

---

## 11.7 Warum Shim-Ausführung?

### 11.7.1 Die architektonische Gründentscheidung

Die Entscheidung, Shim-Ausführung statt echter Ausführung zu implementieren, ist keine Sparmaßnahme und kein Zeichen von Unvollständigkeit. Sie ist eine **bewusste architektonische Entscheidung**, die aus der Natur des Claw-Code-Projekts folgt.

Claw Code ist ein **Spiegelungsprojekt** (*mirroring project*). Sein Zweck ist es, die Architektur, die Oberfläche und die Strukturen des Originals in einer anderen Sprache (Python statt TypeScript) nachzubilden, um sie studierbar, testbar und vergleichbar zu machen. Es geht nicht darum, ein funktional äquivalentes CLI zu bauen -- es geht darum, die **Architektur des Originals sichtbar zu machen**.

Echte Ausführung würde dieses Ziel nicht nur verfehlen, sondern aktiv behindern:

1. **Sicherheitsrisiken:** Das Original führt Bash-Befehle aus, liest und schreibt Dateien, öffnet Netzwerkverbindungen. Eine echte Reimplementierung dieser Funktionen birgt erhebliche Risiken, insbesondere wenn die Implementierung nicht vollständig getestet ist.

2. **Funktionale Divergenz:** Jede echte Implementierung eines Tools würde zwangsläufig von der Originalimplementierung abweichen -- sei es in Randfällen, Fehlerbehandlung oder Timing. Diese Abweichungen würden den Vergleich zwischen Original und Spiegel erschweren.

3. **Wartungsaufwand:** Echte Implementierungen müssen mit dem Original Schritt halten. Bei jeder Änderung am Original müsste auch die Claw-Code-Implementierung aktualisiert werden. Shim-Ausführung macht dies trivial: Nur die Snapshot-Daten müssen aktualisiert werden.

4. **Fokus auf Struktur:** Claw Code konzentriert sich auf die *Struktur* des Systems -- welche Befehle gibt es, welche Tools, wie sind sie organisiert, wie werden sie dispatched. Die Shim-Ausführung bewahrt genau diese strukturelle Information, ohne den Blick durch Implementierungsdetails zu verstellen.

### 11.7.2 Wie die Shim-Ausführung das Original widerspiegelt

Die Shim-Ausführung ist nicht beliebig gewählt. Sie bildet die **Dispatch-Schnittstellen** des Originals exakt nach:

- Im Original gibt es eine Registry, die Befehle und Tools verwaltet. In Claw Code gibt es die `ExecutionRegistry`.
- Im Original werden Befehle über einen Namen gesucht und mit einem Prompt aufgerufen. In Claw Code geschieht dasselbe über `MirroredCommand.execute(prompt)`.
- Im Original werden Tools über einen Namen gesucht und mit einem Payload aufgerufen. In Claw Code geschieht dasselbe über `MirroredTool.execute(payload)`.
- Im Original gibt es verschiedene Laufzeitmodi (Remote, SSH, Teleport). In Claw Code gibt es die entsprechenden `run_*`-Funktionen.
- Im Original gibt es Direktverbindungsmodi. In Claw Code gibt es `run_direct_connect()` und `run_deep_link()`.

Der entscheidende Punkt ist, dass die **Schnittstellen identisch** sind. Ein Aufrufer, der `registry.command('review').execute('prüfe den Code')` schreibt, interagiert mit derselben API, die auch in einem echten System existieren würde. Der einzige Unterschied liegt im Rückgabewert: Statt eines echten Ausführungsergebnisses erhält der Aufrufer eine beschreibende Nachricht.

Dies ist das Prinzip des **Architektur-Isomorphismus**: Die Struktur der Spiegel-Implementierung ist isomorph zur Struktur des Originals, auch wenn die Semantik der Operationen vereinfacht ist. Man kann sich Claw Code als ein Architekturmodell vorstellen -- wie ein maßstabsgetreues Modell eines Gebäudes, das alle Räume, Türen und Flure zeigt, in dem aber kein Wasser durch die Leitungen fließt.

### 11.7.3 Der Wert der Shim-Nachrichten

Die von den Shim-Funktionen erzeugten Nachrichten sind nicht bloße Platzhalter -- sie sind **maschinenlesbare Dokumentation**. Die Nachricht `"Mirrored command 'review' from commands/slash_commands.ts would handle prompt 'prüfe den Code'."` enthält drei wesentliche Informationen:

1. **Den Namen des Befehls** (`review`), was eine Zuordnung zum Katalog ermöglicht.
2. **Die Herkunft im Original** (`commands/slash_commands.ts`), was eine Rückverfolgung zum Quellcode des Originals erlaubt.
3. **Den übergebenen Prompt**, was eine Nachvollziehbarkeit der beabsichtigten Aktion gewährleistet.

In Tests können diese Nachrichten geparst werden, um sicherzustellen, dass der Dispatch korrekt funktioniert -- dass der richtige Befehl gefunden, die richtige Quelldatei referenziert und der richtige Prompt weitergereicht würde. Die Shim-Ausführung ist also nicht stumm, sondern explizit und transparent.

---

## 11.8 Designmuster und Prinzipien

### 11.8.1 Frozen Dataclasses als Grundbaustein

Alle sechs Datenklassen in den drei Modulen (`MirroredCommand`, `MirroredTool`, `ExecutionRegistry`, `CommandExecution`, `ToolExecution`, `RuntimeModeReport`, `DirectModeReport`) verwenden `frozen=True`. Dies ist kein Zufall, sondern ein durchgängiges Designprinzip: Die Ausführungsschicht erzeugt ausschließlich unveränderliche Werte. Einmal erzeugt, kann kein Report und kein Wrapper nachträglich verändert werden. Dies eliminiert eine ganze Klasse von Fehlern (unbeabsichtigte Mutation) und macht den Code leichter zu testen und zu debuggen.

### 11.8.2 Factory-Funktionen statt Konstruktoren

Sowohl `build_execution_registry()` als auch die `run_*`-Funktionen folgen dem Factory-Muster: Sie erzeugen konfigurierte Objekte und geben sie zurück, anstatt den Aufrufer mit den Details der Konfiguration zu belasten. Dies entkoppelt die Erzeugungslogik von der Verwendung und ermöglicht es, die Erzeugung zentral zu ändern, ohne die Aufrufer anzupassen.

### 11.8.3 Reine Funktionen

Alle `run_*`-Funktionen in `remote_runtime.py` und `direct_modes.py` sind reine Funktionen: Sie haben keine Seiteneffekte, greifen nicht auf globalen Zustand zu und liefern bei gleicher Eingabe immer dieselbe Ausgabe. Dies macht sie trivial testbar -- ein Test muss lediglich prüfen, ob die Felder des zurückgegebenen Reports die erwarteten Werte enthalten.

### 11.8.4 Bewusste Trennung von Report-Typen

Obwohl `RuntimeModeReport` und `DirectModeReport` strukturell ähnlich sind, werden sie als separate Klassen modelliert. Dies folgt dem Prinzip der semantischen Typisierung: Zwei Konzepte, die zufällig ähnliche Felder haben, sind nicht dasselbe Konzept. Ein Remote-Modus und ein Direct-Connect-Modus haben unterschiedliche Semantiken, unterschiedliche Fehlerfälle und unterschiedliche zukünftige Erweiterungsmöglichkeiten. Die Trennung in separate Klassen macht diese Unterscheidung auf Typebene sichtbar und verhindert, dass ein `RuntimeModeReport` versehentlich dort verwendet wird, wo ein `DirectModeReport` erwartet wird.

---

## 11.9 Integration in das Gesamtsystem

Die Ausführungsschicht ist nicht isoliert, sondern fügt sich in die Gesamtarchitektur von Claw Code ein:

- Die `ExecutionRegistry` wird über `build_execution_registry()` erzeugt und kann an übergeordnete Schichten (z. B. einen Dispatcher oder eine CLI-Hauptschleife) übergeben werden.
- Die Laufzeitmodus-Reports können von einer Konfigurationsschicht ausgewertet werden, um zu entscheiden, welcher Modus aktiv ist.
- Die `as_text()`-Methoden der Reports liefern eine einheitliche Textdarstellung, die für Logging, Debugging und Benutzerausgaben verwendet werden kann.

Die Ausführungsschicht bildet damit die unterste Schicht des Dispatch-Stacks: Sie weiß, *was* ausgeführt werden kann und *wie* die Ausführung konfiguriert ist, aber sie entscheidet nicht *wann* oder *ob* etwas ausgeführt wird. Diese Entscheidung liegt bei den darüber liegenden Schichten -- dem Befehlsparser, dem Berechtigungssystem und der Sitzungsverwaltung.

---

## 11.10 Zusammenfassung

Die Ausführungsschicht von Claw Code besteht aus drei Modulen, die zusammen 100 Zeilen Python umfassen und dennoch die gesamte Dispatch- und Laufzeitlogik des Originals strukturell abbilden:

- **`execution_registry.py`** stellt mit `MirroredCommand`, `MirroredTool` und `ExecutionRegistry` eine vollständige, unveränderliche Registry bereit, die Befehle und Tools über case-insensitive Lookups zugänglich macht und über Shim-Ausführung bedient.
- **`remote_runtime.py`** bildet mit `RuntimeModeReport` und den drei `run_*`-Funktionen die entfernten Laufzeitmodi (Remote, SSH, Teleport) als Platzhalter ab.
- **`direct_modes.py`** bildet mit `DirectModeReport` und den zwei `run_*`-Funktionen die Direktverbindungsmodi (Direct-Connect, Deep-Link) als Platzhalter ab.

Die durchgängige Verwendung von Shim-Ausführung ist die zentrale Designentscheidung dieser Schicht. Sie ermöglicht es, die Architektur des Originals vollständig nachzubilden -- mit allen Schnittstellen, Datenflüssen und Dispatch-Pfaden --, ohne die Risiken und den Aufwand einer echten Implementierung in Kauf nehmen zu müssen. Die Shim-Nachrichten dienen dabei als maschinenlesbare Dokumentation, die den beabsichtigten Ausführungspfad beschreibt und in Tests verifiziert werden kann.

Dieses Kapitel hat gezeigt, dass die Ausführungsschicht nicht trotz, sondern *wegen* ihrer Einfachheit einen wesentlichen Beitrag zur Architekturspiegelung leistet. Die bewusste Beschränkung auf Shim-Ausführung ist kein Kompromiss, sondern eine Stärke: Sie hält den Fokus auf der Struktur und verhindert, dass Implementierungsdetails den Blick auf das Wesentliche verstellen -- die Architektur des Originals.


# Kapitel 12: Die Subsystem-Architektur

## 12.1 Einführung: Das Problem der strukturellen Abbildung

Wer ein komplexes Softwaresystem in eine andere Sprache portiert -- oder auch nur eine Referenzimplementierung davon erstellt --, steht vor einem fundamentalen Dilemma. Einerseits möchte man die Struktur des Originals möglichst getreu abbilden, damit Entwickler, die das Original kennen, sich sofort zurechtfinden. Andererseits wäre es unsinnig, tausende Dateien eins zu eins zu kopieren, wenn der Zweck des neuen Projekts nicht die vollständige Reimplementierung ist, sondern die Schaffung eines Python-Geruests, das die Architektur dokumentiert, Metadaten bereitstellt und als Ausgangspunkt für zukünftige Portierungen dient.

Das Claw-Code-Projekt löst dieses Dilemma durch ein elegantes Architekturmuster, das wir in diesem Kapitel im Detail untersuchen werden: die **Subsystem-Platzhalter-Architektur**. Jedes der 29 Subsysteme des originalen TypeScript-Projekts wird durch genau zwei Artefakte repräsentiert -- ein Python-Paket mit einer minimalen `__init__.py`-Datei und eine JSON-Metadatendatei, die den Umfang und die Struktur des Originals beschreibt. Gemeinsam bilden diese 58 Dateien (29 Python-Pakete plus 29 JSON-Dateien) das Rückgrat der gesamten Claw-Code-Architektur.

## 12.2 Das einheitliche Muster: Anatomie einer `__init__.py`-Datei

Die bemerkenswerteste Eigenschaft der Subsystem-Architektur ist ihre vollständige Uniformitaet. Jede einzelne der 29 `__init__.py`-Dateien folgt exakt demselben Muster. Es gibt keine Abweichungen, keine Sonderfaelle, keine subsystemspezifischen Erweiterungen. Betrachten wir das Muster am Beispiel des `bridge`-Subsystems:

```python
"""Python package placeholder for the archived `bridge` subsystem."""

from __future__ import annotations

import json
from pathlib import Path

SNAPSHOT_PATH = Path(__file__).resolve().parent.parent / 'reference_data' / 'subsystems' / 'bridge.json'
_SNAPSHOT = json.loads(SNAPSHOT_PATH.read_text())

ARCHIVE_NAME = _SNAPSHOT['archive_name']
MODULE_COUNT = _SNAPSHOT['module_count']
SAMPLE_FILES = tuple(_SNAPSHOT['sample_files'])
PORTING_NOTE = f"Python placeholder package for '{ARCHIVE_NAME}' with {MODULE_COUNT} archived module references."

__all__ = ['ARCHIVE_NAME', 'MODULE_COUNT', 'PORTING_NOTE', 'SAMPLE_FILES']
```

Dieses Muster lässt sich in fünf klar abgegrenzte Abschnitte gliedern, die wir nun einzeln untersuchen.

### 12.2.1 Der Docstring

Jede Datei beginnt mit einem einzeiligen Docstring der Form:

```python
"""Python package placeholder for the archived `<name>` subsystem."""
```

Der Begriff "placeholder" ist hier bewusst gewählt. Er signalisiert unmissverstaendlich, dass dieses Paket keine funktionale Implementierung enthält, sondern als Stellvertreter für das urspruengliche TypeScript-Subsystem dient. Das Wort "archived" verstärkt diese Botschaft: Die Module des Originals sind nicht verloren, sondern archiviert -- ihre Existenz ist dokumentiert, auch wenn ihr Code hier nicht vorliegt.

### 12.2.2 Die Importe

```python
from __future__ import annotations

import json
from pathlib import Path
```

Die Importliste ist minimalistisch. `from __future__ import annotations` aktiviert die verzoegerte Auswertung von Typ-Annotationen (PEP 563), was in diesem konkreten Fall zwar nicht strikt notwendig ist, aber eine Best Practice darstellt, die das Projekt durchgehend befolgt. Die einzigen genutzten Standardbibliotheksmodule sind `json` für das Parsen der Metadaten und `pathlib.Path` für die plattformübergreifende Pfadkonstruktion.

Das Fehlen externer Abhängigkeiten ist ein wichtiger Designaspekt: Jedes Subsystem-Paket kann importiert werden, ohne dass irgendwelche Pakete installiert sein müssen, die über die Python-Standardbibliothek hinausgehen.

### 12.2.3 Die Pfadkonstruktion und das Laden der Metadaten

```python
SNAPSHOT_PATH = Path(__file__).resolve().parent.parent / 'reference_data' / 'subsystems' / 'bridge.json'
_SNAPSHOT = json.loads(SNAPSHOT_PATH.read_text())
```

Diese beiden Zeilen bilden das Herzschlagwerk des Musters. Die Pfadkonstruktion verdient besondere Aufmerksamkeit:

1. `Path(__file__)` liefert den Pfad der aktuellen `__init__.py`-Datei, beispielsweise `/home/user/claw-code_claude/src/bridge/__init__.py`.
2. `.resolve()` wandelt diesen in einen absoluten, kanonischen Pfad um und löst dabei symbolische Links auf.
3. `.parent` navigiert zum Verzeichnis des Pakets: `.../src/bridge/`.
4. `.parent` navigiert eine weitere Ebene nach oben: `.../src/`.
5. `/ 'reference_data' / 'subsystems' / 'bridge.json'` konstruiert den vollständigen Pfad zur JSON-Metadatendatei.

Das Ergebnis ist ein Pfad wie `/home/user/claw-code_claude/src/reference_data/subsystems/bridge.json`. Bemerkenswert ist, dass die Pfadkonstruktion relativ zum Standort der `__init__.py`-Datei erfolgt, nicht relativ zum Arbeitsverzeichnis. Dadurch funktioniert der Import zuverlässig, unabhängig davon, von welchem Verzeichnis aus das Programm gestartet wird.

Die zweite Zeile liest den gesamten Inhalt der JSON-Datei als Text ein (`SNAPSHOT_PATH.read_text()`) und parst ihn mit `json.loads()` in ein Python-Dictionary. Das führende Unterstrich-Präfix von `_SNAPSHOT` signalisiert, dass diese Variable als modulintern betrachtet werden soll -- sie erscheint bewusst nicht in der `__all__`-Liste.

Ein wichtiger Nebeneffekt: Das Laden und Parsen der JSON-Datei geschieht zum Importzeitpunkt. Sobald ein anderes Modul `import bridge` oder `from bridge import MODULE_COUNT` ausführt, wird die JSON-Datei gelesen. Dies ist eine bewusste Designentscheidung: Die Metadaten stehen sofort nach dem Import zur Verfügung, ohne dass ein expliziter Initialisierungsschritt erforderlich wäre.

### 12.2.4 Die exportierten Konstanten

```python
ARCHIVE_NAME = _SNAPSHOT['archive_name']
MODULE_COUNT = _SNAPSHOT['module_count']
SAMPLE_FILES = tuple(_SNAPSHOT['sample_files'])
PORTING_NOTE = f"Python placeholder package for '{ARCHIVE_NAME}' with {MODULE_COUNT} archived module references."
```

Aus dem geparsten Dictionary werden vier benannte Konstanten extrahiert:

- **`ARCHIVE_NAME`** (str): Der kanonische Name des Subsystems, wie er im Original verwendet wird. In den meisten Faellen stimmt er mit dem Paketnamen überein (z. B. `"bridge"`, `"utils"`, `"components"`). Eine bemerkenswerte Ausnahme ist das Subsystem `native_ts`, dessen `archive_name` den Wert `"native-ts"` trägt -- der Bindestrich im Originalnamen ist in Python als Paketname nicht zulässig, weshalb der `package_name` zu `"native_ts"` wird, während der `archive_name` die originale Schreibweise bewahrt.

- **`MODULE_COUNT`** (int): Die Anzahl der Module (TypeScript-Dateien) im originalen Subsystem. Dieser Wert reicht von 1 (bei `coordinator`, `moreright`, `schemas`, `outputStyles`, `voice`, `assistant` und `bootstrap`) bis zu 564 (bei `utils`). Wie wir in Abschnitt 12.4 sehen werden, variiert die Größe der Subsysteme enorm.

- **`SAMPLE_FILES`** (tuple): Ein Tupel mit den Dateinamen der originalen Module. Die Konvertierung von der JSON-Liste zum Python-Tupel mit `tuple()` ist eine bewusste Entscheidung: Tupel sind unveränderlich und signalisieren, dass diese Sammlung nicht modifiziert werden soll. Bei kleinen Subsystemen enthält dieses Tupel saemtliche Dateien; bei großen Subsystemen wie `utils` (564 Module) oder `components` (389 Module) enthält es eine repräsentative Auswahl von bis zu 25 Eintraegen.

- **`PORTING_NOTE`** (str): Ein menschenlesbarer Hinweistext, der dynamisch aus `ARCHIVE_NAME` und `MODULE_COUNT` zusammengesetzt wird. Für das `bridge`-Subsystem lautet er beispielsweise: `"Python placeholder package for 'bridge' with 31 archived module references."`. Dieser String dient als schnelle Orientierung und kann von Werkzeugen, Dokumentationsgeneratoren oder interaktiven Shells ausgegeben werden.

### 12.2.5 Die `__all__`-Liste

```python
__all__ = ['ARCHIVE_NAME', 'MODULE_COUNT', 'PORTING_NOTE', 'SAMPLE_FILES']
```

Die explizite `__all__`-Definition kontrolliert, was bei einem `from bridge import *`-Statement exportiert wird. Bemerkenswert ist, dass `SNAPSHOT_PATH` hier zwar nicht aufgeführt ist, aber dennoch als regulaeres Modulattribut zugänglich bleibt -- es wird lediglich nicht bei Wildcard-Importen eingeschlossen. Die private Variable `_SNAPSHOT` wird durch ihren Unterstrich-Präfix ohnehin von Wildcard-Importen ausgeschlossen.

## 12.3 Das JSON-Metadaten-Format

Jede der 29 JSON-Dateien im Verzeichnis `src/reference_data/subsystems/` folgt einem einheitlichen Schema mit exakt vier Feldern:

```json
{
  "archive_name": "bridge",
  "package_name": "bridge",
  "module_count": 31,
  "sample_files": [
    "bridge/bridgeApi.ts",
    "bridge/bridgeConfig.ts",
    "bridge/bridgeDebug.ts",
    ...
  ]
}
```

### 12.3.1 `archive_name` (string)

Der kanonische Name des Subsystems in seiner urspruenglichen Schreibweise. Dieser Wert entspricht dem Verzeichnisnamen im originalen TypeScript-Projekt. Wie bereits erwähnt, weicht er bei `native-ts` vom Python-Paketnamen `native_ts` ab, da Python-Paketnamen keine Bindestriche enthalten duerfen.

### 12.3.2 `package_name` (string)

Der Python-konforme Paketname. In 28 von 29 Faellen ist er identisch mit dem `archive_name`. Nur bei `native_ts`/`native-ts` unterscheiden sich die beiden Werte. Dieses Feld ermöglicht es Werkzeugen, die korrekte Zuordnung zwischen dem originalen TypeScript-Verzeichnis und dem Python-Paket herzustellen.

### 12.3.3 `module_count` (integer)

Die Gesamtzahl der TypeScript-Module im originalen Subsystem. Dieser Wert ist eine exakte Zaehlung, nicht eine Schätzung. Er dient als Masseinheit für die Komplexitaet und den Umfang des jeweiligen Subsystems und ermöglicht Paritaetsprüfungen -- etwa um festzustellen, welcher Prozentsatz des Originals bereits portiert würde.

### 12.3.4 `sample_files` (array of strings)

Ein Array mit den relativen Dateipfaden der originalen TypeScript-Module. Die Pfade verwenden die Konventionen des Originals, einschließlich der TypeScript-Endungen `.ts` und `.tsx`. Bei Subsystemen mit wenigen Modulen (wie `coordinator` mit einem einzigen Modul `coordinatorMode.ts`) enthält dieses Array saemtliche Dateien. Bei großen Subsystemen wird eine repräsentative Stichprobe aufgeführt.

Die Dateipfade enthalten dabei stets den Subsystem-Ordner als Präfix, zum Beispiel `"bridge/bridgeApi.ts"` statt nur `"bridgeApi.ts"`. Diese Konvention sorgt dafür, dass die Pfade auch außerhalb ihres JSON-Kontextes eindeutig zuzuordnen sind.

## 12.4 Die 29 Subsysteme im Überblick

Die folgende Aufstellung listet alle 29 Subsysteme in absteigender Reihenfolge nach Modulzahl. Sie verdeutlicht die enorme Bandbreite: Das größte Subsystem (`utils`) umfasst 564 Module, während sieben Subsysteme aus nur einem einzigen Modul bestehen.

### 12.4.1 Die großen Subsysteme (100+ Module)

**utils (564 Module)** -- Das mit Abstand größte Subsystem ist die Werkzeugbibliothek. Sie enthält eine schier endlose Sammlung von Hilfsfunktionen und -klassen: vom `CircularBuffer` über `Shell`-Abstraktion, `QueryGuard`, `agentContext` bis hin zu spezialisierten Modulen wie `ansiToPng`, `apiPreconnect` oder `authFileDescriptor`. Die schiere Größe von 564 Modulen zeigt, dass die urspruengliche Anwendung eine umfangreiche interne Infrastruktur aufgebaut hat. Nahezu jede andere Komponente im System duerfte direkte oder indirekte Abhängigkeiten zu `utils` haben.

**components (389 Module)** -- Das zweitgrößte Subsystem umfasst die UI-Komponenten. Dateien wie `App.tsx`, `AgentProgressLine.tsx`, `BridgeDialog.tsx` oder `ContextVisualization.tsx` verraten, dass es sich um React-Komponenten handelt (die `.tsx`-Endung deutet auf JSX-Syntax hin). Bemerkenswert ist die Vielfalt: Von Dialogen (`AutoModeOptInDialog`, `BypassPermissionsModeDialog`, `CostThresholdDialog`) über Statusanzeigen (`CoordinatorAgentStatus`, `CompactSummary`) bis zu spezialisierten Eingabe-Widgets (`BaseTextInput`, `ConfigurableShortcutHint`). Dieses Subsystem bildet die gesamte Benutzeroberflaeche der Anwendung ab.

**services (130 Module)** -- Die Service-Schicht kapselt die Geschäftslogik. Hier finden sich klar strukturierte Subdomaenen: `AgentSummary` für Zusammenfassungen, `MagicDocs` für intelligente Dokumentation, `PromptSuggestion` für kontextabhängige Vorschlaege, `SessionMemory` für sitzungsübergreifende Erinnerungen. Der `analytics`-Bereich mit Modulen wie `datadog.ts`, `growthbook.ts` und `firstPartyEventLogger.ts` zeigt eine ausgefeilte Telemetrie-Infrastruktur. Die `api`-Untergruppe mit `claude.ts`, `client.ts` und `errorUtils.ts` bildet die Schnittstelle zum Backend.

**hooks (104 Module)** -- Dieses Subsystem enthält React-Hooks, ein Entwurfsmuster für zustandsbehaftete Logik in funktionalen Komponenten. Besonders auffaellig ist das `notifs`-Unterverzeichnis mit 17 spezialisierten Benachrichtigungs-Hooks: `useAutoModeUnavailableNotification`, `useDeprecationWarningNotification`, `useRateLimitWarningNotification` und viele mehr. Das `toolPermission`-Unterverzeichnis mit `PermissionContext.ts` und spezialisierten Handlern (`coordinatorHandler`, `interactiveHandler`, `swarmWorkerHandler`) zeigt ein differenziertes Berechtigungssystem.

### 12.4.2 Die mittleren Subsysteme (10-99 Module)

**bridge (31 Module)** -- Das Bridge-Subsystem implementiert die Kommunikationsbrücke zwischen verschiedenen Laufzeitumgebungen. Module wie `bridgeApi.ts`, `bridgeMessaging.ts`, `bridgePermissionCallbacks.ts` und `remoteBridgeCore.ts` deuten auf ein ausgefeiltes Nachrichtenprotokoll hin. `jwtUtils.ts` und `flushGate.ts` weisen auf Authentifizierung und Flusskontrolle hin. Dieses Subsystem ist offensichtlich geschaeftskritisch für die Anbindung an externe Systeme.

**constants (21 Module)** -- Eine Sammlung von Konstantendefinitionen, die das gesamte System durchziehen. Die Dateinamen sind selbstdokumentierend: `apiLimits.ts` definiert API-Grenzen, `betas.ts` steuert Feature-Flags für Betafunktionen, `cyberRiskInstruction.ts` enthält Sicherheitsrichtlinien, `prompts.ts` und `systemPromptSections.ts` definieren die Grundstruktur der KI-Prompts, und `spinnerVerbs.ts` sowie `turnCompletionVerbs.ts` steuern die Benutzeroberflaeche während Wartezeiten.

**skills (20 Module)** -- Das Skill-System repräsentiert erweiterbare Fähigkeiten der Anwendung. Im `bundled`-Unterverzeichnis finden sich fest eingebaute Skills wie `claudeApi.ts`, `loop.ts`, `remember.ts`, `simplify.ts` und `verify.ts`. `loadSkillsDir.ts` deutet darauf hin, dass neben den fest eingebauten Skills auch externe, verzeichnisbasierte Skills geladen werden koennen -- ein klassisches Plugin-Muster.

**cli (19 Module)** -- Das Kommandozeilen-Interface mit Handlern für verschiedene Befehle (`auth.ts`, `autoMode.ts`, `mcp.tsx`, `plugins.ts`), IO-Modulen (`remoteIO.ts`, `structuredIO.ts`) und einem bemerkenswerten `transports`-Unterverzeichnis mit `HybridTransport.ts`, `SSETransport.ts`, `WebSocketTransport.ts` und `WorkerStateUploader.ts` -- was auf multiple Kommunikationsstrategien hindeutet.

**keybindings (14 Module)** -- Ein vollständiges Tastenkürzel-System mit `defaultBindings.ts`, `loadUserBindings.ts`, `parser.ts`, `resolver.ts`, `validate.ts` und React-Integration (`KeybindingContext.tsx`, `useKeybinding.ts`). Die Existenz von `reservedShortcuts.ts` und `template.ts` deutet auf ein ausgereiftes, konfigurierbares System hin.

**migrations (11 Module)** -- Datenmigrationsskripte, die den Übergang zwischen verschiedenen Versionen der Anwendung ermöglichen. Die Dateinamen erzaehlen die Versionsgeschichte: `migrateFennecToOpus.ts`, `migrateLegacyOpusToCurrent.ts`, `migrateOpusToOpus1m.ts`, `migrateSonnet1mToSonnet45.ts`, `migrateSonnet45ToSonnet46.ts`. Man erkennt die Abfolge der Modellgenerationen und die Notwendigkeit, Benutzerkonfigurationen bei jedem Modellwechsel zu aktualisieren.

**types (11 Module)** -- TypeScript-Typdefinitionen, darunter `command.ts`, `hooks.ts`, `permissions.ts` und `plugin.ts`. Bemerkenswert sind die generierten Typen unter `generated/events_mono/`, die auf ein Schema-basiertes Codegenerierungssystem hindeuten -- vermutlich für Event-Tracking und Protokollpuffer.

### 12.4.3 Die kleinen Subsysteme (2-9 Module)

**memdir (8 Module)** -- Das Memory-Directory-System verwaltet persistente Erinnerungen. `findRelevantMemories.ts` sucht kontextabhängig nach relevanten Eintraegen, `memoryScan.ts` durchforstet den Speicher, `memoryAge.ts` verwaltet die Alterung von Eintraegen, und `teamMemPaths.ts` sowie `teamMemPrompts.ts` zeigen eine Team-Dimension des Erinnerungssystems.

**entrypoints (8 Module)** -- Die Einstiegspunkte der Anwendung: `cli.tsx` für die Kommandozeile, `mcp.ts` für das Model Context Protocol, `init.ts` für die Initialisierung. Das `sdk`-Unterverzeichnis mit `controlSchemas.ts`, `coreSchemas.ts` und `coreTypes.ts` definiert die SDK-Schnittstelle.

**buddy (6 Module)** -- Ein verspieltes Feature: `CompanionSprite.tsx` und `sprites.ts` deuten auf ein animiertes Begleit-Maskottchen hin. `companion.ts`, `prompt.ts` und `useBuddyNotification.tsx` integrieren dieses Feature in die Anwendung. Ein charmantes Detail in einer sonst streng technischen Architektur.

**state (6 Module)** -- Das zentrale Zustandsverwaltungssystem mit `AppState.tsx`, `AppStateStore.ts`, `store.ts` und `selectors.ts` -- ein klassisches State-Management-Muster, wie es aus Redux oder ähnlichen Bibliotheken bekannt ist. `teammateViewHelpers.ts` zeigt, dass der Zustand auch Multi-User-Szenarien unterstützt.

**vim (5 Module)** -- Eine Vim-Emulation mit `motions.ts`, `operators.ts`, `textObjects.ts`, `transitions.ts` und `types.ts`. Diese fünf Module bilden die grundlegenden Bausteine eines Vim-kompatiblen Editors: Bewegungen (wie `w`, `b`, `e`), Operatoren (wie `d`, `c`, `y`), Textobjekte (wie `iw`, `ap`) und Zustandsübergaenge zwischen den Modi.

**native_ts (4 Module)** -- TypeScript-Wrapper für native Bibliotheken: `color-diff` für Farbvergleiche, `file-index` für Dateiindizierung und `yoga-layout` für das Yoga-Layoutsystem (eine Cross-Platform-Layout-Engine von Meta). Dieses Subsystem ist das einzige, bei dem `archive_name` (`"native-ts"`) und `package_name` (`"native_ts"`) voneinander abweichen.

**remote (4 Module)** -- Fernsteuerungsfunktionalitaet mit `RemoteSessionManager.ts`, `SessionsWebSocket.ts`, `remotePermissionBridge.ts` und `sdkMessageAdapter.ts`. Dieses Subsystem ermöglicht die Steuerung der Anwendung aus der Ferne, beispielsweise über eine Web-Oberflaeche.

**screens (3 Module)** -- Die Hauptbildschirme der Anwendung: `Doctor.tsx` für die Systemdiagnose, `REPL.tsx` für die interaktive Sitzung und `ResumeConversation.tsx` für die Wiederaufnahme frueherer Gespraeche.

**server (3 Module)** -- Serverseitige Funktionalitaet für Direktverbindungen: `createDirectConnectSession.ts`, `directConnectManager.ts` und `types.ts`. Ein kompaktes, fokussiertes Subsystem.

**plugins (2 Module)** -- Das Plugin-System mit `builtinPlugins.ts` und `bundled/index.ts`. Die geringe Modulzahl täuscht: Dieses Subsystem dient als Registrierung und Lademechanismus für Plugins, die selbst in anderen Subsystemen definiert sein koennen.

**upstreamproxy (2 Module)** -- Ein Proxy-Subsystem mit `relay.ts` und `upstreamproxy.ts`, das vermutlich die Weiterleitung von Anfragen an vorgelagerte Server ermöglicht.

### 12.4.4 Die minimalen Subsysteme (1 Modul)

Sieben Subsysteme bestehen aus nur einem einzigen Modul:

**coordinator (1 Modul: `coordinatorMode.ts`)** -- Steuert den Koordinatormodus, in dem die Anwendung als Orchestrator für mehrere Agenten fungiert.

**moreright (1 Modul: `useMoreRight.tsx`)** -- Ein React-Hook, der vermutlich die "Mehr anzeigen"-Funktionalitaet in der rechten Seitenleiste steuert.

**schemas (1 Modul: `hooks.ts`)** -- Validierungsschemata für das Hook-System.

**outputStyles (1 Modul: `loadOutputStylesDir.ts`)** -- Laedt konfigurierbare Ausgabestile aus einem Verzeichnis.

**voice (1 Modul: `voiceModeEnabled.ts`)** -- Feature-Flag für die Sprachsteuerung.

**assistant (1 Modul)** -- Das zentrale Assistenten-Paket, das trotz seiner Modulzahl von 1 eine fundamentale Rolle in der Architektur spielt, da es den Kernbegriff "Assistent" im Namensraum verankert.

**bootstrap (1 Modul: `state.ts`)** -- Der Initialisierungszustand für den Anwendungsstart.

## 12.5 Statistische Analyse: Die Verteilung der Komplexitaet

Die Gesamtzahl aller Module über alle 29 Subsysteme beträgt circa 1.372. Die Verteilung ist extrem ungleich:

| Größenklasse | Subsysteme | Module gesamt | Anteil |
|---|---|---|---|
| Groß (100+) | 4 | 1.187 | ~86,5 % |
| Mittel (10-99) | 7 | 127 | ~9,3 % |
| Klein (2-9) | 11 | 51 | ~3,7 % |
| Minimal (1) | 7 | 7 | ~0,5 % |

Diese Verteilung folgt einem typischen Potenzgesetz: Eine kleine Anzahl von Subsystemen konzentriert einen überproportional großen Anteil der Komplexitaet. Allein `utils` und `components` umfassen zusammen 953 Module -- nahezu 70 Prozent des Gesamtsystems. Dies spiegelt ein gängiges Muster in gewachsenen Softwaresystemen wider, bei dem Werkzeug- und UI-Bibliotheken dazu neigen, über die Zeit erheblich anzuwachsen.

Für die Portierungsplanung ergibt sich daraus eine klare Priorisierung: Wer die vier großen Subsysteme (`utils`, `components`, `services`, `hooks`) portiert, hat bereits 86,5 Prozent des Modulumfangs abgedeckt. Gleichzeitig sind diese vier Subsysteme natürlich die komplexesten und erfordern den größten Aufwand.

## 12.6 Der Datenfluss: Vom JSON zum Python-Namensraum

Um das Zusammenspiel zwischen JSON-Metadaten und Python-Paketen vollständig zu verstehen, lohnt es sich, den Datenfluss Schritt für Schritt nachzuvollziehen. Betrachten wir, was geschieht, wenn ein Entwickler in einer Python-Shell folgenden Befehl eingibt:

```python
from bridge import MODULE_COUNT, SAMPLE_FILES
print(f"Das Bridge-Subsystem umfasst {MODULE_COUNT} Module.")
print(f"Beispieldateien: {SAMPLE_FILES[:3]}")
```

1. Python sucht das Paket `bridge` im Suchpfad und findet `src/bridge/__init__.py`.
2. Der Interpreter führt den Code in `__init__.py` aus.
3. `Path(__file__).resolve().parent.parent` ergibt `.../src/`.
4. Der Pfad `.../src/reference_data/subsystems/bridge.json` wird konstruiert.
5. `SNAPSHOT_PATH.read_text()` liest die JSON-Datei als String.
6. `json.loads()` parst den String in ein Dictionary:
   ```python
   {'archive_name': 'bridge', 'package_name': 'bridge', 'module_count': 31, 'sample_files': [...]}
   ```
7. Die Werte werden in die Modulkonstanten `ARCHIVE_NAME`, `MODULE_COUNT`, `SAMPLE_FILES` und `PORTING_NOTE` übertragen.
8. Die angeforderten Namen `MODULE_COUNT` und `SAMPLE_FILES` werden in den importierenden Namensraum gebunden.
9. Die Ausgabe erscheint:
   ```
   Das Bridge-Subsystem umfasst 31 Module.
   Beispieldateien: ('bridge/bridgeApi.ts', 'bridge/bridgeConfig.ts', 'bridge/bridgeDebug.ts')
   ```

Dieser Fluss zeigt, wie die Trennung zwischen statischen Daten (JSON) und dynamischer Logik (Python) saüber eingehalten wird. Die JSON-Dateien sind reine Datencontainer; die `__init__.py`-Dateien sind reine Lademechanismen. Keine der beiden Schichten enthält Geschäftslogik.

## 12.7 Architekturentscheidungen und ihre Begründung

### 12.7.1 Warum Platzhalter statt echter Implementierung?

Die Entscheidung, 29 Subsysteme als Platzhalter statt als vollständige Portierungen zu implementieren, gründet auf drei wesentlichen Überlegungen:

**Erstens: Metadaten-Abfrage zur Laufzeit.** Die Platzhalter-Architektur ermöglicht es, zur Laufzeit Informationen über die Struktur des Originalsystems abzufragen, ohne dass eine vollständige Portierung vorliegen muss. Ein Werkzeug zur Portierungsplanung kann beispielsweise alle 29 Subsysteme importieren, ihre `MODULE_COUNT`-Werte summieren und so den Gesamtumfang der ausstehenden Arbeit bestimmen. Ein Paritaetsprüfungsskript kann die `SAMPLE_FILES` mit tatsaechlich vorhandenen Python-Modulen vergleichen und den Portierungsfortschritt messen.

**Zweitens: Unterstützung der Paritaetsprüfung.** Im Claw-Code-Projekt existieren bereits Module wie `parity_audit.py` und `port_manifest.py`, die die strukturelle Übereinstimmung zwischen Original und Portierung prüfen. Die JSON-Metadaten liefern die Referenzdaten für diese Prüfungen. Ohne die Platzhalter-Architektur müssten diese Werkzeuge die Metadaten aus einer separaten Quelle beziehen -- beispielsweise aus einer monolithischen Konfigurationsdatei oder aus dem Dateisystem des Originalprojekts. Die dezentrale Speicherung in 29 JSON-Dateien, die jeweils direkt neben ihrem zugehörigen Python-Paket liegen, ist sowohl wartungsfreundlicher als auch robuster.

**Drittens: Vermeidung proprietaeren Codes.** Das Originalprojekt ist proprietaere Software. Eine vollständige Portierung würde bedeuten, den gesamten Quellcode zu kopieren und in Python zu übersetzen -- ein Vorgang, der sowohl urheberrechtlich problematisch als auch praktisch überfluessig wäre, solange das Ziel nicht die Ersetzung des Originals ist. Die Platzhalter-Architektur dokumentiert die Existenz und Struktur des Originals, ohne dessen Implementierungsdetails preiszugeben. Die `sample_files`-Listen zeigen lediglich Dateinamen, nicht Dateiinhalte.

### 12.7.2 Warum JSON statt Python-Literale?

Eine naheliegende Alternative wäre gewesen, die Metadaten direkt als Python-Literale in den `__init__.py`-Dateien zu speichern:

```python
# Hypothetische Alternative (NICHT so implementiert)
ARCHIVE_NAME = "bridge"
MODULE_COUNT = 31
SAMPLE_FILES = ("bridge/bridgeApi.ts", "bridge/bridgeConfig.ts", ...)
```

Die Entscheidung für JSON bietet jedoch mehrere Vorteile:

- **Sprachunabhängigkeit:** Die JSON-Dateien koennen von jedem Werkzeug gelesen werden, nicht nur von Python. Ein Shell-Skript, ein JavaScript-Tool oder ein CI/CD-Pipeline-Schritt kann die Metadaten direkt parsen.
- **Generierbarkeit:** Die JSON-Dateien würden offensichtlich automatisiert aus dem Originalprojekt generiert. Die Generierung eines JSON-Objekts ist einfacher und weniger fehleranfaellig als die Generierung von syntaktisch korrektem Python-Code.
- **Trennung von Daten und Code:** Änderungen an den Metadaten (etwa wenn im Original ein neues Modul hinzukommt) erfordern nur eine Änderung in der JSON-Datei. Der Python-Code in `__init__.py` bleibt unverändert. Diese Trennung vereinfacht automatisierte Updates erheblich.

### 12.7.3 Warum 29 separate Dateien statt einer einzigen?

Eine weitere Alternative wäre eine einzige, monolithische JSON-Datei gewesen, die alle 29 Subsysteme beschreibt. Die Entscheidung für separate Dateien folgt dem Prinzip der Lokalitaet: Jedes Subsystem verwaltet seine eigenen Metadaten. Dies erleichtert partielle Updates, vereinfacht das Debugging (bei einem Fehler weiß man sofort, welche JSON-Datei betroffen ist) und unterstützt parallele Entwicklung (zwei Entwickler koennen gleichzeitig an verschiedenen Subsystemen arbeiten, ohne Merge-Konflikte zu riskieren).

## 12.8 Praktische Nutzung: Beispiele und Anwendungsfaelle

### 12.8.1 Portierungsfortschritt ermitteln

```python
import importlib

subsystems = ['components', 'utils', 'services', 'hooks', 'bridge',
              'constants', 'skills', 'cli', 'keybindings', 'migrations',
              'types', 'memdir', 'entrypoints', 'buddy', 'state',
              'vim', 'native_ts', 'remote', 'screens', 'server',
              'plugins', 'upstreamproxy', 'coordinator', 'moreright',
              'schemas', 'outputStyles', 'voice', 'assistant', 'bootstrap']

total = 0
for name in subsystems:
    mod = importlib.import_module(name)
    total += mod.MODULE_COUNT
    print(f"{name:20s} {mod.MODULE_COUNT:4d} Module")

print(f"\nGesamt: {total} Module im Original")
```

### 12.8.2 Subsystem-Informationen abfragen

```python
from bridge import ARCHIVE_NAME, MODULE_COUNT, SAMPLE_FILES, PORTING_NOTE

print(PORTING_NOTE)
# Ausgabe: Python placeholder package for 'bridge' with 31 archived module references.

for f in SAMPLE_FILES[:5]:
    print(f"  - {f}")
```

### 12.8.3 Maschinenlesbare Bestandsaufnahme

```python
import json
from pathlib import Path

subsystem_dir = Path('src/reference_data/subsystems')
report = {}
for json_file in sorted(subsystem_dir.glob('*.json')):
    data = json.loads(json_file.read_text())
    report[data['archive_name']] = data['module_count']

print(json.dumps(report, indent=2, sort_keys=True))
```

## 12.9 Die Verzeichnisstruktur im Überblick

Die Subsystem-Architektur manifestiert sich in einer klaren Verzeichnisstruktur innerhalb von `src/`:

```
src/
  reference_data/
    subsystems/
      assistant.json
      bootstrap.json
      bridge.json
      buddy.json
      ... (29 JSON-Dateien insgesamt)
  assistant/
    __init__.py
  bootstrap/
    __init__.py
  bridge/
    __init__.py
  buddy/
    __init__.py
  ... (29 Paketverzeichnisse insgesamt)
```

Jedes der 29 Paketverzeichnisse enthält mindestens eine `__init__.py`-Datei. Diese Datei macht das Verzeichnis zu einem importierbaren Python-Paket und stellt gleichzeitig die Verbindung zur zugehörigen JSON-Metadatendatei her. Die `reference_data/subsystems/`-Verzeichnisstruktur ist bewusst von den Paketverzeichnissen getrennt -- sie gehört nicht zu einem bestimmten Subsystem, sondern dient als zentrale Datenablage für alle 29 Subsysteme.

## 12.10 Zusammenfassung

Die Subsystem-Architektur von Claw Code ist ein Paradebeispiel für durchdachtes Software-Design unter ungewoehnlichen Randbedingungen. Anstatt 1.372 TypeScript-Module blind in Python zu übersetzen oder die Strukturinformationen des Originals zu verwerfen, wählt das Projekt einen dritten Weg: Jedes der 29 Subsysteme wird durch ein minimales, aber informationsreiches Platzhalter-Paket repräsentiert.

Das einheitliche Muster -- identische `__init__.py`-Dateien, die ihre Metadaten aus standardisierten JSON-Dateien laden -- bietet mehrere entscheidende Vorteile:

- **Konsistenz:** Wer ein Subsystem kennt, kennt alle. Es gibt keine Sonderfaelle oder Überraschungen.
- **Wartbarkeit:** Änderungen am Muster koennen mechanisch auf alle 29 Pakete angewandt werden.
- **Abfragbarkeit:** Jedes Subsystem gibt programmatisch Auskunft über seinen Umfang und seine Struktur.
- **Erweiterbarkeit:** Neue Subsysteme koennen durch simples Kopieren des Musters und Erstellen einer JSON-Datei hinzugefuegt werden.
- **Integritaet:** Die Metadaten ermöglichen automatisierte Paritaetsprüfungen zwischen Original und Portierung.

Die 29 Subsysteme reichen von winzigen Einzelmodul-Paketen wie `voice` (1 Modul: `voiceModeEnabled.ts`) bis hin zu massiven Bibliotheken wie `utils` (564 Module). Zusammen dokumentieren sie die vollständige Oberflaeche eines komplexen TypeScript-Systems in einer Form, die sowohl für Menschen lesbar als auch für Maschinen auswertbar ist -- und die dabei keinen einzigen proprietaeren Codebaustein preisgibt.


# Kapitel 13: Paritaetsprüfung & Qualitaetssicherung

## 13.1 Einführung

In jedem größeren Software-Portierungsprojekt stellt sich frueher oder später eine zentrale Frage: Wie nahe ist der aktuelle Stand der Portierung am Original? Wenn ein umfangreiches TypeScript-Projekt nach Python übertragen wird, genuegt es nicht, einzelne Dateien zu übersetzen und auf das Beste zu hoffen. Es braucht systematische Werkzeuge, die den Fortschritt messen, Luecken aufdecken und den Gesamtzustand des Projekts quantifizieren koennen.

Das Claw-Code-Projekt löst dieses Problem mit drei eng verzahnten Bausteinen: dem **Parity Audit** (`src/parity_audit.py`), der die strukturelle Abdeckung zwischen dem archivierten TypeScript-Original und dem Python-Port misst; dem **Port Manifest** (`src/port_manifest.py`), das eine aktuelle Bestandsaufnahme des Python-Quellbaums liefert; und einer umfassenden **Testsuite** (`tests/test_porting_workspace.py`), die mit 24 Testmethoden das gesamte System end-to-end validiert, ohne auf Mocking zurückzugreifen.

Dieses Kapitel analysiert alle drei Komponenten im Detail. Wir beginnen mit dem Parity Audit, gehen dann zum Port Manifest über und schließen mit einer eingehenden Betrachtung der Testsuite ab.

---

## 13.2 Der Parity Audit (`src/parity_audit.py`)

### 13.2.1 Architektonischer Überblick

Die Datei `src/parity_audit.py` umfasst 139 Zeilen und bildet das Herzstück der Paritaetsmessung. Ihre Aufgabe ist es, den aktuellen Zustand des `src/`-Verzeichnisses mit den bekannten Strukturen des archivierten TypeScript-Originals zu vergleichen. Dabei werden mehrere Dimensionen der Abdeckung erfasst: Root-Dateien, Verzeichnisse, Gesamtdateizahl, Befehlsabdeckung und Werkzeugabdeckung.

Die Datei beginnt mit der Definition von vier Pfadkonstanten, die den gesamten Audit verankern:

```python
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent / 'archive' / 'claude_code_ts_snapshot' / 'src'
CURRENT_ROOT = Path(__file__).resolve().parent
REFERENCE_SURFACE_PATH = CURRENT_ROOT / 'reference_data' / 'archive_surface_snapshot.json'
COMMAND_SNAPSHOT_PATH = CURRENT_ROOT / 'reference_data' / 'commands_snapshot.json'
TOOL_SNAPSHOT_PATH = CURRENT_ROOT / 'reference_data' / 'tools_snapshot.json'
```

`ARCHIVE_ROOT` zeigt auf das archivierte TypeScript-Original unter `archive/claude_code_ts_snapshot/src`. `CURRENT_ROOT` ist das aktuelle `src/`-Verzeichnis des Python-Ports. Die drei JSON-Pfade verweisen auf Referenzdaten, die beim Erstellen des Archivs generiert würden und als Sollwerte für den Vergleich dienen.

### 13.2.2 ARCHIVE_ROOT_FILES: Die 18 Root-Datei-Mappings

Das Dictionary `ARCHIVE_ROOT_FILES` definiert eine explizite Zuordnung von 18 TypeScript-Quelldateien zu ihren erwarteten Python-Äquivalenten:

```python
ARCHIVE_ROOT_FILES = {
    'QueryEngine.ts': 'QueryEngine.py',
    'Task.ts': 'task.py',
    'Tool.ts': 'Tool.py',
    'commands.ts': 'commands.py',
    'context.ts': 'context.py',
    'cost-tracker.ts': 'cost_tracker.py',
    'costHook.ts': 'costHook.py',
    'dialogLaunchers.tsx': 'dialogLaunchers.py',
    'history.ts': 'history.py',
    'ink.ts': 'ink.py',
    'interactiveHelpers.tsx': 'interactiveHelpers.py',
    'main.tsx': 'main.py',
    'projectOnboardingState.ts': 'projectOnboardingState.py',
    'query.ts': 'query.py',
    'replLauncher.tsx': 'replLauncher.py',
    'setup.ts': 'setup.py',
    'tasks.ts': 'tasks.py',
    'tools.ts': 'tools.py',
}
```

Diese Zuordnungen spiegeln die zentralen Einstiegspunkte des Originals wider. Jede Zeile repräsentiert eine Kerndatei des TypeScript-Projekts und ihr Python-Gegenstück. Bemerkenswert ist, dass die Benennung nicht immer eins-zu-eins übernommen wird: `Task.ts` wird zu `task.py` (Kleinschreibung gemäß Python-Konvention), `cost-tracker.ts` wird zu `cost_tracker.py` (Bindestrich durch Unterstrich ersetzt), während `QueryEngine.ts` seinen CamelCase-Namen als `QueryEngine.py` behält. Die `.tsx`-Dateien (React-Komponenten wie `dialogLaunchers.tsx`, `interactiveHelpers.tsx`, `main.tsx`, `replLauncher.tsx`) werden ebenfalls auf reine `.py`-Dateien abgebildet, da die React-spezifische Rendering-Schicht in Python durch andere Mechanismen ersetzt wird.

Diese 18 Mappings bilden die "Root-Schicht" des Audits. Sie repräsentieren die oberste Ebene der Architektur: Einstiegspunkte, zentrale Engines, Hookpoints und Hilfsmodule, die direkt im Wurzelverzeichnis des Quellbaums liegen.

### 13.2.3 ARCHIVE_DIR_MAPPINGS: Die 35 Verzeichnis-Mappings

Das zweite Dictionary erfasst die Verzeichnisstruktur des Originals mit 35 Eintraegen:

```python
ARCHIVE_DIR_MAPPINGS = {
    'assistant': 'assistant',
    'bootstrap': 'bootstrap',
    'bridge': 'bridge',
    'buddy': 'buddy',
    'cli': 'cli',
    'commands': 'commands.py',
    'components': 'components',
    'constants': 'constants',
    'context': 'context.py',
    'coordinator': 'coordinator',
    'entrypoints': 'entrypoints',
    'hooks': 'hooks',
    ...
}
```

Hier zeigt sich ein wichtiges Architekturmuster des Portierungsprojekts: Nicht jedes TypeScript-Verzeichnis wird als eigenes Python-Package portiert. Manche Verzeichnisse werden zu einzelnen Dateien konsolidiert. So wird das gesamte `commands/`-Verzeichnis des Originals (das möglicherweise dutzende `.ts`-Dateien enthielt) im Python-Port durch eine einzige Datei `commands.py` abgebildet. Dasselbe gilt für `context/` (wird zu `context.py`), `ink/` (zu `ink.py`), `query/` (zu `query.py`), `tasks/` (zu `tasks.py`) und `tools/` (zu `tools.py`).

Die übrigen 29 Verzeichnisse behalten ihre Struktur als eigene Verzeichnisse bzw. Packages bei: `assistant`, `bootstrap`, `bridge`, `buddy`, `cli`, `components`, `constants`, `coordinator`, `entrypoints`, `hooks`, `keybindings`, `memdir`, `migrations`, `moreright`, `native_ts` (umbenannt von `native-ts`), `outputStyles`, `plugins`, `remote`, `schemas`, `screens`, `server`, `services`, `skills`, `state`, `types`, `upstreamproxy`, `utils`, `vim` und `voice`. Diese Vielfalt an Subsystemen zeigt den Umfang des Originalprojekts und die Breite der Portierungsarbeit.

### 13.2.4 ParityAuditResult: Die Ergebnis-Datenklasse

Das Ergebnis eines Audits wird in einer unveränderlichen Datenklasse (`frozen=True`) gekapselt:

```python
@dataclass(frozen=True)
class ParityAuditResult:
    archive_present: bool
    root_file_coverage: tuple[int, int]
    directory_coverage: tuple[int, int]
    total_file_ratio: tuple[int, int]
    command_entry_ratio: tuple[int, int]
    tool_entry_ratio: tuple[int, int]
    missing_root_targets: tuple[str, ...]
    missing_directory_targets: tuple[str, ...]
```

Jedes Feld erfuellt eine spezifische Rolle:

- **`archive_present`** (`bool`): Gibt an, ob das lokale Archiv des TypeScript-Originals vorhanden ist. Wenn der Archivordner fehlt (etwa in einer CI-Umgebung ohne das vollständige Repository), kann der Audit zwar laufen, liefert aber nur eingeschraenkte Ergebnisse.

- **`root_file_coverage`** (`tuple[int, int]`): Ein Paar aus (gefundene Dateien, erwartete Dateien). Bei vollständiger Abdeckung wäre dies `(18, 18)`. Der erste Wert zählt, wie viele der 18 erwarteten Python-Dateien im aktuellen `src/`-Verzeichnis tatsaechlich existieren.

- **`directory_coverage`** (`tuple[int, int]`): Analog für Verzeichnisse. Bei 35 erwarteten Zielen und 28 gefundenen wäre der Wert `(28, 35)`.

- **`total_file_ratio`** (`tuple[int, int]`): Verhältnis der aktuellen Python-Dateien zur Gesamtzahl der TypeScript-ähnlichen Dateien im Archiv. Dies wird aus der Referenzdatei `archive_surface_snapshot.json` geladen und gibt einen übergreifenden Indikator für den Portierungsfortschritt.

- **`command_entry_ratio`** (`tuple[int, int]`): Verhältnis der portierten Befehle zur Gesamtzahl im Original. Der erste Wert kommt aus `commands_snapshot.json`, der zweite aus der Referenzdatei.

- **`tool_entry_ratio`** (`tuple[int, int]`): Dasselbe für Werkzeuge (Tools). Quelle ist `tools_snapshot.json` gegenüber der Referenz.

- **`missing_root_targets`** (`tuple[str, ...]`): Eine Liste der Python-Dateinamen aus `ARCHIVE_ROOT_FILES`, die im aktuellen `src/`-Verzeichnis nicht gefunden würden. Diese Liste benennt konkret, welche Root-Dateien noch fehlen.

- **`missing_directory_targets`** (`tuple[str, ...]`): Analog die fehlenden Verzeichnis- oder Dateiziele aus `ARCHIVE_DIR_MAPPINGS`.

Die Verwendung von `frozen=True` und ausschließlich unver aenderlichen Typen (`bool`, `tuple`) macht `ParityAuditResult` zu einem wertbasierten, thread-sicheren Objekt. Es kann bedenkenlos zwischengespeichert, serialisiert oder in Tests verglichen werden, ohne dass Seiteneffekte befürchtet werden müssen.

### 13.2.5 `run_parity_audit()`: Die Kernlogik

Die Funktion `run_parity_audit()` führt den eigentlichen Vergleich durch:

```python
def run_parity_audit() -> ParityAuditResult:
    current_entries = {path.name for path in CURRENT_ROOT.iterdir()}
    root_hits = [target for target in ARCHIVE_ROOT_FILES.values() if target in current_entries]
    dir_hits = [target for target in ARCHIVE_DIR_MAPPINGS.values() if target in current_entries]
    missing_roots = tuple(target for target in ARCHIVE_ROOT_FILES.values() if target not in current_entries)
    missing_dirs = tuple(target for target in ARCHIVE_DIR_MAPPINGS.values() if target not in current_entries)
    current_python_files = sum(1 for path in CURRENT_ROOT.rglob('*.py') if path.is_file())
    reference = _reference_surface()
    ...
```

Der Algorithmus folgt einem klaren Schema:

1. **Bestandsaufnahme**: Alle Eintraege (Dateien und Verzeichnisse) im aktuellen `src/`-Verzeichnis werden als Menge von Namen erfasst (`current_entries`).

2. **Root-Abgleich**: Für jedes Ziel in `ARCHIVE_ROOT_FILES.values()` wird geprüft, ob es in `current_entries` existiert. Treffer werden in `root_hits` gesammelt, Fehlstellen in `missing_roots`.

3. **Verzeichnis-Abgleich**: Dasselbe geschieht für `ARCHIVE_DIR_MAPPINGS.values()` mit `dir_hits` und `missing_dirs`.

4. **Python-Dateizaehlung**: Ein rekursiver Scan (`rglob('*.py')`) zählt alle Python-Dateien im gesamten Quellbaum.

5. **Referenzdaten laden**: Die Funktion `_reference_surface()` liest `archive_surface_snapshot.json` ein, das Sollwerte wie `total_ts_like_files`, `command_entry_count` und `tool_entry_count` enthält.

6. **Snapshot-Zaehlung**: Die Hilfsfunktion `_snapshot_count()` liest die JSON-Arrays in `commands_snapshot.json` und `tools_snapshot.json` und gibt deren Laenge zurück.

7. **Ergebnis-Assembly**: Alle gesammelten Werte werden zu einem `ParityAuditResult` zusammengefuegt.

Bemerkenswert ist, dass die Funktion keine Ausnahmen wirft, wenn das Archiv fehlt. Stattdessen wird `archive_present=ARCHIVE_ROOT.exists()` gesetzt und der Aufrufer kann das Ergebnis entsprechend interpretieren.

### 13.2.6 `to_markdown()`: Berichtsformatierung

Die Methode `to_markdown()` auf `ParityAuditResult` erzeugt einen menschenlesbaren Markdown-Bericht:

```python
def to_markdown(self) -> str:
    lines = ['# Parity Audit']
    if not self.archive_present:
        lines.append('Local archive unavailable; parity audit cannot compare against the original snapshot.')
        return '\n'.join(lines)
    lines.extend([
        '',
        f'Root file coverage: **{self.root_file_coverage[0]}/{self.root_file_coverage[1]}**',
        f'Directory coverage: **{self.directory_coverage[0]}/{self.directory_coverage[1]}**',
        ...
    ])
```

Wenn das Archiv nicht vorhanden ist, wird sofort ein Kurztext zurückgegeben. Andernfalls werden alle fünf Metriken in fettgedruckten Bruchzahlen dargestellt, gefolgt von Listen der fehlenden Root-Dateien und Verzeichnisse. Falls nichts fehlt, erscheint `- none`. Diese Formatierung eignet sich sowohl für die Terminalausgabe (via `src.main parity-audit`) als auch für die Integration in automatisierte Berichte.

---

## 13.3 Das Port Manifest (`src/port_manifest.py`)

### 13.3.1 Zweck und Aufbau

Während der Parity Audit den Python-Port gegen das TypeScript-Original misst, liefert das Port Manifest eine eigenständige Bestandsaufnahme des Python-Quellbaums. Die Datei `src/port_manifest.py` umfasst 53 Zeilen und besteht aus einer Datenklasse und einer Erzeuger-Funktion.

### 13.3.2 Die Datenklasse `PortManifest`

```python
@dataclass(frozen=True)
class PortManifest:
    src_root: Path
    total_python_files: int
    top_level_modules: tuple[Subsystem, ...]
```

Die drei Felder erfassen:

- **`src_root`** (`Path`): Der Wurzelpfad des gescannten Quellbaums. Standardmäßig ist dies `src/`, kann aber über den Parameter von `build_port_manifest()` überschrieben werden.

- **`total_python_files`** (`int`): Die Gesamtzahl aller `.py`-Dateien im Quellbaum.

- **`top_level_modules`** (`tuple[Subsystem, ...]`): Eine nach Dateizahl absteigend sortierte Liste der Top-Level-Module. Jedes Modul wird durch die Datenklasse `Subsystem` repräsentiert, die in `src/models.py` definiert ist:

```python
@dataclass(frozen=True)
class Subsystem:
    name: str
    path: str
    file_count: int
    notes: str
```

`Subsystem` erfasst also den Namen, den Pfad relativ zum Projektverzeichnis, die Anzahl der enthaltenen Python-Dateien und einen beschreibenden Text.

### 13.3.3 `build_port_manifest()`: Filesystem-Scan und Modulzaehlung

Die Erzeuger-Funktion führt den eigentlichen Scan durch:

```python
def build_port_manifest(src_root: Path | None = None) -> PortManifest:
    root = src_root or DEFAULT_SRC_ROOT
    files = [path for path in root.rglob('*.py') if path.is_file()]
    counter = Counter(
        path.relative_to(root).parts[0] if len(path.relative_to(root).parts) > 1 else path.name
        for path in files
        if path.name != '__pycache__'
    )
```

Der Algorithmus ist elegant in seiner Einfachheit:

1. **Dateien sammeln**: Alle `.py`-Dateien werden rekursiv aufgelistet.

2. **Top-Level-Zuordnung**: Für jede Datei wird der erste Pfadteil relativ zum Root bestimmt. Dateien in Unterverzeichnissen werden ihrem übergeordneten Verzeichnis zugeordnet (z.B. `utils/formatting.py` wird dem Modul `utils` zugeordnet). Dateien direkt im Root-Verzeichnis behalten ihren eigenen Dateinamen als Schlüssel (z.B. `main.py`).

3. **Cache-Ausschluss**: `__pycache__`-Eintraege werden herausgefiltert, um kompilierte Bytecode-Dateien nicht mitzuzaehlen.

4. **Zaehlung**: `collections.Counter` zählt die Dateien pro Top-Level-Modul und ermöglicht über `most_common()` eine absteigende Sortierung.

Anschließend werden die Zaehlungen in `Subsystem`-Objekte umgewandelt:

```python
notes = {
    '__init__.py': 'package export surface',
    'main.py': 'CLI entrypoint',
    'port_manifest.py': 'workspace manifest generation',
    'query_engine.py': 'port orchestration summary layer',
    'commands.py': 'command backlog metadata',
    'tools.py': 'tool backlog metadata',
    'models.py': 'shared dataclasses',
    'task.py': 'task-level planning structures',
}
modules = tuple(
    Subsystem(name=name, path=f'src/{name}', file_count=count,
              notes=notes.get(name, 'Python port support module'))
    for name, count in counter.most_common()
)
```

Das `notes`-Dictionary ordnet bekannten Dateinamen beschreibende Texte zu. Alle unbekannten Module erhalten den Standardtext `'Python port support module'`. Die Methode `to_markdown()` auf `PortManifest` formatiert diese Informationen als Aufzaehlungsliste mit Dateianzahlen und Beschreibungen.

### 13.3.4 Zusammenspiel mit dem Parity Audit

Port Manifest und Parity Audit ergaenzen sich komplementaer: Das Manifest beantwortet die Frage "Was haben wir?", der Audit beantwortet "Was fehlt noch?". Beide werden über die CLI (`src.main summary` bzw. `src.main parity-audit`) zugänglich gemacht und durch die Query Engine (`QueryEnginePort.from_workspace()`) in einem übergreifenden Bericht zusammengeführt.

---

## 13.4 Die Testsuite (`tests/test_porting_workspace.py`)

### 13.4.1 Philosophie und Testarchitektur

Die Testdatei `tests/test_porting_workspace.py` enthält 24 Testmethoden in einer einzigen Testklasse `PortingWorkspaceTests`, die von `unittest.TestCase` erbt. Das herausragende Merkmal dieser Suite ist ihr konsequenter Verzicht auf Mocking. Statt einzelne Funktionen zu isolieren und ihre Abhängigkeiten zu simulieren, führen die Tests echte Operationen gegen den realen Quellbaum durch. CLI-Tests starten tatsaechliche Subprozesse mit `subprocess.run()`, Manifest-Tests scannen das echte Dateisystem, und Parity-Tests laden die realen Referenzdaten.

Dieser Ansatz hat tiefgreifende Konsequenzen: Die Tests sind **empfindlich gegenüber echten DatenÄnderungen**. Wenn eine Datei umbenannt wird, ein Verzeichnis hinzukommt oder eine Referenzdatei aktualisiert wird, koennen Tests fehlschlagen. Das ist beabsichtigt -- die Suite dient als Fruehwarnsystem für unbeabsichtigte StrukturÄnderungen.

Die Importe am Dateianfang zeigen die Abhängigkeiten:

```python
from src.commands import PORTED_COMMANDS
from src.parity_audit import run_parity_audit
from src.port_manifest import build_port_manifest
from src.query_engine import QueryEnginePort
from src.tools import PORTED_TOOLS
```

### 13.4.2 Manifest-Tests

**`test_manifest_counts_python_files`**: Der grundlegendste Test der Suite. Er ruft `build_port_manifest()` auf und prüft zwei Bedingungen: Die Gesamtzahl der Python-Dateien muss mindestens 20 betragen, und die Liste der Top-Level-Module darf nicht leer sein.

```python
def test_manifest_counts_python_files(self) -> None:
    manifest = build_port_manifest()
    self.assertGreaterEqual(manifest.total_python_files, 20)
    self.assertTrue(manifest.top_level_modules)
```

Dieser Test würde fehlschlagen, wenn ein katastrophaler Refactoring-Fehler die meisten Python-Dateien loeschen würde. Die Schwelle von 20 ist bewusst niedrig gewählt -- sie soll nicht den exakten Bestand prüfen, sondern nur sicherstellen, dass der Quellbaum überhaupt substantiell vorhanden ist.

### 13.4.3 Query-Engine-Tests

**`test_query_engine_summary_mentions_workspace`**: Dieser Test erzeugt eine `QueryEnginePort`-Instanz über die Fabrikmethode `from_workspace()` und prüft, ob die gerenderte Zusammenfassung die erwarteten Überschriften enthält:

```python
def test_query_engine_summary_mentions_workspace(self) -> None:
    summary = QueryEnginePort.from_workspace().render_summary()
    self.assertIn('Python Porting Workspace Summary', summary)
    self.assertIn('Command surface:', summary)
    self.assertIn('Tool surface:', summary)
```

Dieser Test validiert die Integration zwischen Query Engine, Port Manifest, Kommando-Inventar und Tool-Inventar. Wenn eine dieser Komponenten ausfaellt oder ihr Format ändert, schlaegt der Test fehl.

### 13.4.4 CLI-Integrationstests

Die größte Kategorie der Suite sind die CLI-Integrationstests. Sie starten den Python-Interpreter als Subprozess und führen verschiedene CLI-Befehle aus. Das Muster ist immer dasselbe:

```python
result = subprocess.run(
    [sys.executable, '-m', 'src.main', '<befehl>', ...],
    check=True,
    capture_output=True,
    text=True,
)
self.assertIn('<erwarteter_text>', result.stdout)
```

`check=True` sorgt dafür, dass jeder Nicht-Null-Exit-Code eine `CalledProcessError`-Ausnahme auslöst, die den Test sofort scheitern lässt. `capture_output=True` und `text=True` erfassen stdout und stderr als Strings zur Überprüfung.

Die einzelnen CLI-Tests decken das gesamte Befehlsspektrum ab:

**`test_cli_summary_runs`**: Testet den `summary`-Befehl und prüft, ob die Ausgabe die Workspace-Zusammenfassung enthält.

**`test_parity_audit_runs`**: Testet den `parity-audit`-Befehl und prüft auf die Überschrift "Parity Audit".

**`test_commands_and_tools_cli_run`**: Testet die Befehle `commands` und `tools` mit Filtern (`--limit 5`, `--query review` bzw. `--query MCP`). Prüft, ob die Ausgabe `Command entries:` bzw. `Tool entries:` enthält.

**`test_route_and_show_entry_cli_run`**: Testet drei Befehle in Folge: `route` (Routing einer Anfrage zu passenden Eintraegen), `show-command` (Detailansicht eines Befehls) und `show-tool` (Detailansicht eines Tools). Dieser Test validiert die Such- und Anzeigefunktionalitaet des Systems.

```python
def test_route_and_show_entry_cli_run(self) -> None:
    route_result = subprocess.run(
        [sys.executable, '-m', 'src.main', 'route', 'review MCP tool', '--limit', '5'],
        check=True, capture_output=True, text=True,
    )
    show_command = subprocess.run(
        [sys.executable, '-m', 'src.main', 'show-command', 'review'],
        check=True, capture_output=True, text=True,
    )
    show_tool = subprocess.run(
        [sys.executable, '-m', 'src.main', 'show-tool', 'MCPTool'],
        check=True, capture_output=True, text=True,
    )
    self.assertIn('review', route_result.stdout.lower())
    self.assertIn('review', show_command.stdout.lower())
    self.assertIn('mcptool', show_tool.stdout.lower())
```

**`test_bootstrap_cli_runs`**: Testet den `bootstrap`-Befehl, der eine vollständige Laufzeitsitzung startet. Die Ausgabe muss `Runtime Session`, `Startup Steps` und `Routed Matches` enthalten.

**`test_exec_command_and_tool_cli_run`**: Testet die `exec-command`- und `exec-tool`-Befehle, die einzelne Befehle bzw. Tools ausführen. Die erwarteten Ausgaben sind `"Mirrored command 'review'"` und `"Mirrored tool 'MCPTool'"`.

**`test_setup_report_and_registry_filters_run`**: Testet den `setup-report`-Befehl sowie gefilterte Auflistungen (`--no-plugin-commands`, `--simple-mode`, `--no-mcp`). Dieser Test validiert, dass die verschiedenen Filteroptionen die CLI nicht zum Absturz bringen und die erwarteten Überschriften weiterhin erscheinen.

**`test_load_session_cli_runs`**: Einer der komplexeren Tests. Er erzeugt zunächst eine Bootstrap-Session über die Python-API, extrahiert deren Session-ID aus dem persistierten Pfad und laedt sie dann über den `load-session`-CLI-Befehl erneut:

```python
def test_load_session_cli_runs(self) -> None:
    from src.runtime import PortRuntime
    session = PortRuntime().bootstrap_session('review MCP tool', limit=5)
    session_id = Path(session.persisted_session_path).stem
    result = subprocess.run(
        [sys.executable, '-m', 'src.main', 'load-session', session_id],
        check=True, capture_output=True, text=True,
    )
    self.assertIn(session_id, result.stdout)
    self.assertIn('messages', result.stdout)
```

Dieser Test validiert den gesamten Session-Lebenszyklus: Erzeugung, Persistierung und Wiederherstellung.

**`test_tool_permission_filtering_cli_runs`**: Testet das Tool-Berechtigungssystem über den `--deny-prefix`-Filter. Wenn `mcp` als abgelehntes Präfix angegeben wird, darf `MCPTool` nicht in der Ausgabe erscheinen:

```python
def test_tool_permission_filtering_cli_runs(self) -> None:
    result = subprocess.run(
        [sys.executable, '-m', 'src.main', 'tools', '--limit', '10', '--deny-prefix', 'mcp'],
        check=True, capture_output=True, text=True,
    )
    self.assertIn('Tool entries:', result.stdout)
    self.assertNotIn('MCPTool', result.stdout)
```

Dies ist einer der wenigen Tests, der eine Negativbedingung (`assertNotIn`) prüft. Er stellt sicher, dass das Berechtigungssystem tatsaechlich Eintraege herausfiltert.

**`test_turn_loop_cli_runs`**: Testet den `turn-loop`-Befehl, der eine mehrstufige Ausführungsschleife simuliert. Mit `--max-turns 2` und `--structured-output` wird geprüft, ob die Ausgabe Turnnummern und Abbruchgründe enthält.

**`test_remote_mode_clis_run`**: Testet drei Fernzugriffsmodi: `remote-mode`, `ssh-mode` und `teleport-mode`. Jeder muss seinen jeweiligen Modusnamen in der Ausgabe enthalten.

**`test_flush_transcript_cli_runs`**: Testet den `flush-transcript`-Befehl und prüft auf `flushed=True` in der Ausgabe.

**`test_command_graph_and_tool_pool_cli_run`**: Testet die strukturellen Übersichtsbefehle `command-graph` und `tool-pool`.

**`test_setup_report_mentions_deferred_init`**: Ein spezifischerer Test für den Setup-Bericht, der prüft, ob die verzoegte Initialisierung korrekt dokumentiert wird (`Deferred init:` und `plugin_init=True`).

**`test_bootstrap_graph_and_direct_modes_run`**: Testet `bootstrap-graph`, `direct-connect-mode` und `deep-link-mode`.

### 13.4.5 Inventory-Tests

**`test_command_and_tool_snapshots_are_nontrivial`**: Prüft direkt die importierten Daten `PORTED_COMMANDS` und `PORTED_TOOLS` auf Mindestgrößen:

```python
def test_command_and_tool_snapshots_are_nontrivial(self) -> None:
    self.assertGreaterEqual(len(PORTED_COMMANDS), 150)
    self.assertGreaterEqual(len(PORTED_TOOLS), 100)
```

Diese Schwellenwerte (150 Befehle, 100 Tools) dienen als Regressionsschutz: Wenn ein fehlerhafter Import oder eine Änderung an den Snapshot-Dateien die Listen drastisch verkürzt, schlaegt dieser Test an.

**`test_subsystem_packages_expose_archive_metadata`**: Prüft, ob die Subsystem-Packages (`assistant`, `bridge`, `utils`) ihre Metadaten korrekt exponieren:

```python
def test_subsystem_packages_expose_archive_metadata(self) -> None:
    from src import assistant, bridge, utils
    self.assertGreater(assistant.MODULE_COUNT, 0)
    self.assertGreater(bridge.MODULE_COUNT, 0)
    self.assertGreater(utils.MODULE_COUNT, 100)
    self.assertTrue(utils.SAMPLE_FILES)
```

Besonders bemerkenswert ist die Prüfung `utils.MODULE_COUNT > 100`, die zeigt, dass das `utils`-Subsystem im Original über 100 Module umfasste -- ein Hinweis auf die Größe des TypeScript-Originals.

### 13.4.6 Session- und Runtime-Tests

**`test_bootstrap_session_tracks_turn_state`**: Dieser Test verwendet die Python-API direkt (ohne CLI-Subprozess) und prüft den internen Zustand einer Bootstrap-Session:

```python
def test_bootstrap_session_tracks_turn_state(self) -> None:
    from src.runtime import PortRuntime
    session = PortRuntime().bootstrap_session('review MCP tool', limit=5)
    self.assertGreaterEqual(len(session.turn_result.matched_tools), 1)
    self.assertIn('Prompt:', session.turn_result.output)
    self.assertGreaterEqual(session.turn_result.usage.input_tokens, 1)
```

Hier wird geprüft, ob die Session mindestens ein gematchtes Tool enthält, ob die Ausgabe einen Prompt-Abschnitt hat und ob die Usage-Informationen (Eingabe-Token) plausible Werte enthalten.

### 13.4.7 Parity-Tests

**`test_root_file_coverage_is_complete_when_local_archive_exists`**: Der zentrale Paritaetstest, der die Ergebnisse von `run_parity_audit()` validiert:

```python
def test_root_file_coverage_is_complete_when_local_archive_exists(self) -> None:
    audit = run_parity_audit()
    if audit.archive_present:
        self.assertEqual(audit.root_file_coverage[0], audit.root_file_coverage[1])
        self.assertGreaterEqual(audit.directory_coverage[0], 28)
        self.assertGreaterEqual(audit.command_entry_ratio[0], 150)
        self.assertGreaterEqual(audit.tool_entry_ratio[0], 100)
```

Dieser Test ist bedingt: Er prüft nur bei vorhandenem Archiv. Dann verlangt er aber volle Root-File-Abdeckung (alle 18 von 18), mindestens 28 von 35 Verzeichnissen, mindestens 150 Befehle und mindestens 100 Tools. Die bedingte Ausführung ist ein pragmatischer Kompromiss: In Umgebungen ohne Archiv-Zugang würde ein strikter Test ständig fehlschlagen.

### 13.4.8 Registry-Tests

**`test_execution_registry_runs`**: Testet die Execution Registry, die Befehle und Tools als ausführbare Objekte bereitstellt:

```python
def test_execution_registry_runs(self) -> None:
    from src.execution_registry import build_execution_registry
    registry = build_execution_registry()
    self.assertGreaterEqual(len(registry.commands), 150)
    self.assertGreaterEqual(len(registry.tools), 100)
    self.assertIn('Mirrored command', registry.command('review').execute('review security'))
    self.assertIn('Mirrored tool', registry.tool('MCPTool').execute('fetch mcp resources'))
```

Dieser Test geht über bloße Zaehlung hinaus: Er führt tatsaechlich einen Befehl und ein Tool aus und prüft die Rückgabewerte. Das Wort "Mirrored" in der Ausgabe deutet darauf hin, dass die aktuelle Implementierung die Befehle noch nicht vollständig portiert hat, sondern sie als "gespiegelte" Platzhalter ausführt.

### 13.4.9 Permission-Tests

Der Test `test_tool_permission_filtering_cli_runs` (bereits in Abschnitt 13.4.4 beschrieben) ist der zentrale Berechtigungstest. Er stellt sicher, dass das `--deny-prefix`-System tatsaechlich Tools aus der Ausgabe entfernt, wenn deren Name mit dem angegebenen Präfix beginnt. Dies ist kritisch für Sicherheitsszenarien, in denen bestimmte Tools (etwa MCP-basierte externe Werkzeuge) gezielt blockiert werden sollen.

---

## 13.5 Zusammenspiel der drei Komponenten

Die drei in diesem Kapitel behandelten Dateien bilden ein geschlossenes Qualitaetssicherungssystem:

1. **Port Manifest** scannt den Quellbaum und liefert aktuelle Kennzahlen (Gesamtdateien, Module, Dateiverteilung).

2. **Parity Audit** vergleicht diese Kennzahlen mit den Referenzdaten des TypeScript-Originals und identifiziert Luecken.

3. **Testsuite** validiert beides -- sowohl die korrekte Funktion der Audit-Werkzeuge als auch die Integritaet der gesamten CLI und Runtime.

Dieses Dreigespann erzeugt einen Feedbackkreislauf: Wenn ein Entwickler eine neue Datei portiert, aktualisiert sich das Manifest automatisch beim nächsten Scan. Der Parity Audit reflektiert die verbesserte Abdeckung. Und die Tests stellen sicher, dass dabei nichts anderes kaputtgegangen ist.

Die Entscheidung gegen Mocking in der Testsuite ist dabei von besonderer Bedeutung. In einem Portierungsprojekt, bei dem sich die interne Struktur ständig weiterentwickelt, würden umfangreiche Mocks ständig hinterherhinken und falsche Sicherheit vermitteln. Die End-to-End-Tests dagegen fangen tatsaechliche Brueche auf -- allerdings zum Preis längerer Ausführungszeiten und der Abhängigkeit von einem korrekt eingerichteten Arbeitsverzeichnis.

---

## 13.6 Quantitative Schwellenwerte und ihre Bedeutung

Über die gesamte Testsuite hinweg finden sich wiederkehrende Schwellenwerte:

| Metrik | Schwellenwert | Bedeutung |
|--------|---------------|-----------|
| `total_python_files` | >= 20 | Minimalbestand des Quellbaums |
| `PORTED_COMMANDS` | >= 150 | Mindestanzahl portierter Befehle |
| `PORTED_TOOLS` | >= 100 | Mindestanzahl portierter Werkzeuge |
| `directory_coverage` | >= 28 | Mindestens 28 von 35 Verzeichnissen abgebildet |
| `root_file_coverage` | 18/18 | Vollständige Abdeckung aller Root-Dateien |
| `utils.MODULE_COUNT` | > 100 | Archiv-Metadaten für das utils-Subsystem |

Diese Schwellenwerte sind bewusst als Untergrenzen formuliert. Sie steigen nicht automatisch mit dem Projektfortschritt, sondern dienen als Sicherheitsnetz gegen Regressionen. Wenn das Projekt wächst, koennen und sollten diese Werte nach oben angepasst werden.

---

## 13.7 Zusammenfassung

Das Paritaetsprüfungs- und Qualitaetssicherungssystem von Claw Code verfolgt einen pragmatischen, datengetriebenen Ansatz. Der Parity Audit misst die strukturelle Nähe zum Original über fünf klar definierte Metriken. Das Port Manifest liefert die Grundlage dafür durch einen automatisierten Filesystem-Scan. Und die Testsuite bindet alles zusammen, indem sie sowohl die Werkzeuge selbst als auch das gesamte CLI end-to-end validiert.

Die Architektur zeigt, wie Qualitaetssicherung in einem Portierungsprojekt aussehen kann: nicht als nachtraegliche Pflicht, sondern als integraler Bestandteil des Entwicklungsworkflows. Jeder CLI-Befehl wird getestet, jede Metrik wird validiert, und fehlende Portierungsziele werden namentlich aufgelistet. So wird der Fortschritt messbar und die nächsten Schritte offensichtlich.


# Kapitel 14: Zusammenfassung und Ausblick

## 14.1 Einleitung: Was wir gebaut haben -- und warum es wichtig ist

Dieses Buch hat sich in dreizehn Kapiteln mit einem Projekt beschaeftigt, das in einer einzigen Nacht entstand und seither nicht aufgehört hat, Fragen aufzuwerfen -- technische, architektonische und ethische. Claw Code begann als Reaktion auf die Offenlegung des Claude-Code-Quellcodes am 31. Maerz 2026 und würde innerhalb weniger Stunden zu einem der am schnellsten wachsenden Open-Source-Projekte auf GitHub. Doch hinter den 30.000 Stars und den Schlagzeilen steckt eine tiefere Geschichte: die Geschichte eines systematischen Versuchs, eine komplexe Agent-Harness-Architektur zu verstehen, zu dokumentieren und in einer anderen Programmiersprache von Grund auf nachzubauen.

In diesem abschließenden Kapitel ziehen wir Bilanz. Wir schauen zurück auf den aktuellen Stand des Projekts, fassen die architektonischen Errungenschaften zusammen, würdigen die eingesetzten Design Patterns und blicken nach vorn -- auf die Rust-Portierung, auf offene Fragen und auf das, was andere Entwicklerinnen und Entwickler aus diesem Projekt lernen koennen.

---

## 14.2 Der aktuelle Stand des Projekts

### 14.2.1 Zahlen und Fakten

Zum Zeitpunkt der Drucklegung umfasst der Python-Quellbaum unter `src/` rund 66 Python-Dateien, verteilt auf 32 Verzeichnisse beziehungsweise Subsystem-Pakete. Die Gesamtstruktur des Repositories ist bewusst schlank gehalten:

- **66 Python-Dateien** im `src/`-Baum, von Root-Level-Modulen wie `models.py`, `commands.py`, `tools.py` und `query_engine.py` bis hin zu Subsystem-Platzhalter-Paketen wie `cli/`, `hooks/`, `skills/`, `voice/` und vielen weiteren.
- **207 gespiegelte Befehle** und **184 gespiegelte Tools**, erfasst als JSON-Referenzdaten unter `src/reference_data/` und über `lru_cache`-gestützte Ladefunktionen in `commands.py` und `tools.py` zugänglich gemacht.
- **24 CLI-Befehle** über `main.py` erreichbar, darunter `summary`, `manifest`, `subsystems`, `commands`, `tools` und `parity-audit`.
- **49 Testfaelle** in der `tests/`-Verzeichnisstruktur, die den aktuellen Python-Arbeitsbereich verifizieren.
- **Keine externen Abhängigkeiten**: Das gesamte Projekt laeuft mit der Python-Standardbibliothek. Keine `requirements.txt`, kein `pip install`, keine Third-Party-Pakete. Dies ist eine bewusste Designentscheidung, die wir in den frueheren Kapiteln ausführlich begründet haben.

### 14.2.2 Was abgedeckt ist

Die Root-Datei-Abdeckung -- also die Frage, ob für jede wesentliche Datei im urspruenglichen TypeScript-Quellbaum ein Python-Äquivalent existiert -- ist weitgehend vollständig. Jedes der über 30 Subsystem-Verzeichnisse des Originals hat ein entsprechendes Python-Paket erhalten, und zwar nicht als leere Huelsen, sondern als strukturierte Platzhalter, die über JSON-Snapshots die Metadaten des Originals referenzieren. Ein typisches Subsystem-Paket wie `src/cli/__init__.py` laedt beim Import seinen JSON-Snapshot aus `src/reference_data/subsystems/cli.json` und stellt Informationen wie den Archivnamen, die Modulanzahl und Beispieldateien als Python-Konstanten bereit.

Die Verzeichnis-Abdeckung ist ebenfalls weitgehend komplett. Die 32 Unterverzeichnisse unter `src/` spiegeln die Subsystemstruktur des Originals wider: `assistant/`, `bootstrap/`, `bridge/`, `buddy/`, `cli/`, `components/`, `constants/`, `coordinator/`, `entrypoints/`, `hooks/`, `keybindings/`, `memdir/`, `migrations/`, `moreright/`, `native_ts/`, `outputStyles/`, `plugins/`, `reference_data/`, `remote/`, `schemas/`, `screens/`, `server/`, `services/`, `skills/`, `state/`, `types/`, `upstreamproxy/`, `utils/`, `vim/` und `voice/`. Jedes dieser Verzeichnisse repräsentiert ein eigenständiges Subsystem der urspruenglichen Agent-Harness-Architektur.

### 14.2.3 Was noch fehlt

Trotz dieser beeindruckenden Abdeckung muss klar gesagt werden: Der Python-Baum ist noch kein vollständiges Laufzeitäquivalent. Er hat weniger ausführbare Schichten als das Original. Die meisten Subsystem-Pakete sind strukturelle Platzhalter, die Metadaten bereitstellen, aber keine vollständige Laufzeitlogik implementieren. Die README des Projekts formuliert es unmissverstaendlich:

> Der aktuelle Python-Arbeitsbereich ist noch kein vollständiger 1:1-Ersatz für das Originalsystem, aber die primaere Implementierungsoberflaeche ist jetzt Python.

Das bedeutet: Die Befehls- und Tool-Inventare sind vollständig gespiegelt. Die Architektur ist klar nachgezeichnet. Aber die tiefen Ausführungspfade -- das tatsaechliche Routing von Prompts durch die Tool-Kette, die Echtzeit-Interaktion mit einem Sprachmodell, die komplexen Seiteneffekte der Agentenschleife -- sind in Python noch nicht in der gleichen Tiefe implementiert wie im TypeScript-Original.

---

## 14.3 Architektonische Errungenschaften

### 14.3.1 Saubere Drei-Schichten-Trennung

Die vielleicht wichtigste architektonische Errungenschaft von Claw Code ist die konsequente Trennung in drei Schichten, die sich durch den gesamten Python-Baum zieht:

1. **Datenmodellschicht** (`models.py`, `permissions.py`, `context.py`): Frozen Dataclasses definieren die unveränderlichen Strukturen des Systems. `Subsystem`, `PortingModule`, `PermissionDenial`, `UsageSummary`, `PortContext`, `ToolPermissionContext` -- all diese Typen sind als `@dataclass(frozen=True)` deklariert und damit nach ihrer Erzeugung unveränderlich. Dies eliminiert eine ganze Klasse von Fehlern, die in veraenderbaren Datenstrukturen auftreten koennen.

2. **Orchestrierungsschicht** (`query_engine.py`, `runtime.py`, `execution_registry.py`, `system_init.py`): Diese Schicht verbindet Datenmodelle mit Ausführungslogik. Die `QueryEnginePort`-Klasse ist das Herzstaeck: Sie verwaltet Sessions, verarbeitet Nachrichten, trackt Token-Budgets, kompaktiert Transkripte und persistiert den Zustand. Die `RuntimeSession` in `runtime.py` buendelt alle Aspekte einer Laufzeitsitzung in einem einzigen, zusammenhaengenden Objekt. Die `ExecutionRegistry` stellt eine einheitliche Schnittstelle für das Auffinden und Ausführen von gespiegelten Befehlen und Tools bereit.

3. **Präsentationsschicht** (`main.py`, `port_manifest.py`): Der CLI-Einstiegspunkt und die Manifest-Generierung bilden die äußerste Schicht. Sie transformieren die internen Datenstrukturen in menschenlesbare Ausgaben -- Markdown-Zusammenfassungen, tabellarische Auflistungen, Paritaetsprüfberichte.

Diese Trennung ist nicht nur ästhetisch befriedigend, sondern hat handfeste Vorteile: Jede Schicht kann unabhängig getestet, erweitert und -- im Fall der Rust-Portierung -- einzeln neu implementiert werden.

### 14.3.2 JSON-getriebene Referenzdaten

Ein zentrales Designprinzip von Claw Code ist die Auslagerung von Referenzdaten in JSON-Dateien. Die 207 Befehle und 184 Tools sind nicht als Python-Code hartcodiert, sondern in `commands_snapshot.json` und `tools_snapshot.json` unter `src/reference_data/` abgelegt. Ebenso haben alle Subsystem-Pakete ihre Metadaten in separaten JSON-Dateien unter `src/reference_data/subsystems/`.

Dieses Prinzip hat mehrere Vorteile:

- **Trennung von Daten und Logik**: Die JSON-Dateien koennen unabhängig vom Python-Code aktualisiert werden, etwa wenn sich das Original ändert.
- **Maschinenlesbarkeit**: Andere Werkzeuge -- einschließlich der Paritaetsprüfung -- koennen die JSON-Daten direkt konsumieren, ohne Python importieren zu müssen.
- **Nachvollziehbarkeit**: Die JSON-Snapshots bilden eine Art Vertrag zwischen dem Original und der Portierung. Jeder Eintrag dokumentiert Name, Verantwortlichkeit und Herkunftshinweis.

Die Ladefunktionen `load_command_snapshot()` und `load_tool_snapshot()` nutzen `@lru_cache(maxsize=1)`, um die JSON-Daten nur einmal zu lesen und dann im Speicher vorzuhalten. Dies ist ein sauberer Kompromiss zwischen Leistung und Einfachheit.

### 14.3.3 Trust-Gating für sichere Ausführung

Das Trust-Gating-System, implementiert in `permissions.py`, `system_init.py` und `setup.py`, stellt sicher, dass bestimmte Operationen nur in vertrauenswürdigen Kontexten ausgeführt werden. Die `ToolPermissionContext`-Klasse arbeitet mit einem Deny-List-Ansatz: Sie prüft, ob ein Tool-Name in der `deny_names`-Menge enthalten ist oder mit einem der `deny_prefixes` beginnt.

Die `run_setup()`-Funktion in `setup.py` akzeptiert einen `trusted`-Parameter, der den gesamten Initialisierungsfluss beeinflusst. Im nicht vertrauenswürdigen Modus werden bestimmte Deferred-Init-Schritte übersprungen und Prefetch-Operationen eingeschraenkt. Dies spiegelt ein fundamentales Designprinzip des Original-Claude-Code wider: Ein Agent-Harness muss in der Lage sein, zwischen vertrauenswürdigen und nicht vertrauenswürdigen Umgebungen zu unterscheiden, weil die Tools, die er bereitstellt -- Dateisystemzugriff, Codeausführung, Netzwerkkommunikation -- reale Seiteneffekte haben koennen.

### 14.3.4 Token-basiertes Prompt-Routing

Die `QueryEnginePort`-Klasse implementiert ein Token-basiertes Budget-System, das die Lebensdauer einer Session steuert. Jeder `submit_message()`-Aufruf berechnet die projizierte Token-Nutzung und kann die Session mit dem Stop-Reason `max_budget_reached` beenden, wenn das konfigurierte Maximum überschritten wird. Parallel dazu gibt es ein Turn-basiertes Limit (`max_turns`), das unabhängig vom Token-Verbrauch greift.

Dieses duale Begrenzungssystem -- Turns und Tokens -- ist typisch für Agent-Harness-Architekturen: Man möchte sowohl die Laenge einer Konversation als auch die Kosten kontrollieren koennen, und beide Dimensionen sind nicht immer korreliert.

### 14.3.5 Session-Lifecycle mit Persistenz

Der Session-Lifecycle in Claw Code umfasst mehrere Stufen: Erzeugung (mit `uuid4()`-basierter Session-ID), Nachrichtenverarbeitung, Transkript-Kompaktierung, Flush und Persistenz. Die `StoredSession`-Dataclass in `session_store.py` serialisiert den Zustand als JSON in das `.port_sessions/`-Verzeichnis. Sessions koennen später über `load_session()` wiederhergestellt werden, und die `QueryEnginePort.from_saved_session()`-Factory-Methode rekonstruiert den vollständigen Engine-Zustand aus einer gespeicherten Session.

Die `TranscriptStore`-Klasse implementiert ein Sliding-Window-Kompaktierungsverfahren: Wenn die Anzahl der Eintraege `compact_after_turns` übersteigt, werden nur die letzten Eintraege behalten. Dies verhindert unbegrenztes Wachstum des Arbeitsspeichers, ohne den Kontext der juengsten Interaktion zu verlieren -- ein Muster, das auch im Original-Claude-Code zu finden ist.

---

## 14.4 Die Rust-Portierung

### 14.4.1 Motivation

Während der Python-Baum als Verstaendnis- und Dokumentationswerkzeug hervorragend funktioniert, hat er inhaerent Grenzen als Laufzeitumgebung. Pythons Global Interpreter Lock, die dynamische Typisierung und die vergleichsweise langsame Ausführungsgeschwindigkeit machen es für eine produktive Agent-Harness-Laufzeit weniger geeignet.

Die Rust-Portierung, die auf dem `dev/rust`-Branch begonnen würde und auch bereits im Hauptzweig unter `rust/` sichtbar ist, verfolgt ein ambitionierteres Ziel: eine speichersichere, performante Harness-Laufzeitumgebung, die potenziell als echte Alternative zum TypeScript-Original dienen könnte.

### 14.4.2 Aktuelle Struktur

Das `rust/`-Verzeichnis enthält bereits eine organisierte Crate-Struktur:

- `crates/api/` -- API-Schnittstellen
- `crates/commands/` -- Befehlsverarbeitung
- `crates/compat-harness/` -- Kompatibilitaetsschicht
- `crates/runtime/` -- Laufzeitumgebung
- `crates/rusty-claude-cli/` -- CLI-Frontend
- `crates/tools/` -- Tool-Ausführung

Diese Struktur spiegelt die Drei-Schichten-Architektur des Python-Baums wider, nutzt aber Rusts Crate-System für eine noch strengere Modultrennung. Jede Crate hat ihren eigenen Namensraum, ihre eigenen Abhängigkeiten und ihre eigene Kompilierungseinheit.

### 14.4.3 Was die Rust-Portierung verspricht

Das Rust-Äquivalent bringt mehrere Vorteile:

- **Speichersicherheit ohne Garbage Collection**: Rusts Ownership-System garantiert Speichersicherheit zur Kompilierzeit. Für ein System, das langlebige Sessions verwaltet und parallel Tool-Ausführungen koordiniert, ist dies ein wesentlicher Vorteil.
- **Hohe Performanz**: Kompilierter Rust-Code erreicht C/C++-ähnliche Geschwindigkeit, was für das Parsen großer JSON-Snapshots, das Routing von Befehlen und die Verwaltung von Token-Budgets relevant ist.
- **Typsicherheit**: Rusts statisches Typsystem faengt Fehler ab, die in Python erst zur Laufzeit auftreten würden. Die Frozen-Dataclass-Garantien, die wir in Python explizit einfordern müssten, sind in Rust der Normalzustand.
- **Einbettbarkeit**: Ein Rust-Binary kann als eigenständiges Kommandozeilenwerkzeug ausgeliefert werden, ohne Python-Interpreter oder virtuelle Umgebung.

---

## 14.5 Offene Fragen

### 14.5.1 Ethische Implikationen der Reimplementierung

Wie bereits in Kapitel 2 dieses Buches ausführlich diskutiert, wirft die Clean-Room-Reimplementierung eines proprietaeren Systems fundamentale ethische Fragen auf. Das Projekt existiert in einer Grauzone: Der offengelegte Quellcode würde studiert, um die Architektur zu verstehen, aber die Python-Portierung würde von Grund auf geschrieben, ohne Code zu kopieren.

Doch reicht das? Die Frage, ob ein architekturelles Verstaendnis, das aus der Lektuere proprietaeren Codes gewonnen würde, in einer Neuimplementierung verwendet werden darf, ist nicht nur juristisch, sondern auch moralisch komplex. Das Projekt selbst reflektiert diese Spannung: Die README verweist auf einen Essay mit dem Titel "Is Legal the Same as Legitimate? AI Reimplementation and the Erosion of Copyleft", der die Erosion von Copyleft-Prinzipien im Zeitalter der KI-Reimplementierung thematisiert.

Diese Debatte ist nicht akademisch. Sie betrifft die gesamte Open-Source-Community und die Frage, wie geistiges Eigentum in einer Welt geschuetzt werden kann, in der KI-Systeme Code lesen, verstehen und funktional äquivalente Implementierungen in anderen Sprachen erzeugen koennen.

### 14.5.2 Wie weit kann und soll die Paritaet getrieben werden?

Die aktuelle Paritaet -- vollständige Befehls- und Tool-Inventare, vollständige Verzeichnisstruktur, aber unvollständige Laufzeittiefe -- wirft die Frage auf: Wie weit soll man gehen? Es gibt hier ein Kontinuum:

- **Strukturelle Paritaet**: Jedes Verzeichnis, jede Datei hat ein Äquivalent. Dies ist weitgehend erreicht.
- **API-Paritaet**: Jede öffentliche Funktion und Klasse hat ein Äquivalent mit kompatibler Signatur. Dies ist teilweise erreicht.
- **Verhaltensparitaet**: Für jeden Input erzeugt das System denselben Output. Dies ist noch weit entfernt.
- **Laufzeitparitaet**: Das System kann das Original in der Praxis ersetzen. Dies ist das erklaerte Ziel der Rust-Portierung.

Jede Paritaetsstufe erfordert exponentiell mehr Aufwand als die vorherige. Und jede Stufe wirft die ethische Frage von Kapitel 2 mit erneuter Schärfe auf: Ab welchem Punkt wird eine "inspirierte" Reimplementierung zur funktionalen Kopie?

### 14.5.3 Die Zukunft von Copyleft im Zeitalter von KI-Reimplementierung

Claw Code ist ein Fallbeispiel für eine Entwicklung, die weit über dieses einzelne Projekt hinausreicht. Wenn KI-Systeme in der Lage sind, eine Codebasis in Sprache A zu lesen und eine funktional äquivalente Codebasis in Sprache B zu erzeugen, was bedeutet das für:

- **GPL und LGPL**: Koennen Copyleft-Lizenzen eine Reimplementierung in einer anderen Sprache erfassen, wenn kein einziges Byte kopiert würde?
- **Clean-Room-Verfahren**: Genuegt es, dass der reimplementierende Entwickler den Originalcode nicht selbst gelesen hat, wenn die KI, die er verwendet, es getan hat?
- **Trade Secrets**: Kann eine architektonische Entscheidung -- etwa die Drei-Schichten-Trennung oder das Token-basierte Routing -- als Geschaeftsgeheimnis geschuetzt werden, wenn sie aus der Analyse eines geleakten Quellcodes rekonstruiert würde?

Diese Fragen haben keine einfachen Antworten. Aber Claw Code zwingt uns, sie zu stellen. Und allein darin liegt ein Wert, der über den technischen Beitrag des Projekts hinausgeht.

---

## 14.6 Design Patterns: Eine Zusammenfassung

Über die gesamte Codebasis hinweg setzt Claw Code eine konsistente Menge von Design Patterns ein, die hier noch einmal zusammengefasst werden sollen:

### 14.6.1 Frozen Dataclasses

Das am häufigsten verwendete Pattern im Projekt. Nahezu jede Datenstruktur -- `Subsystem`, `PortingModule`, `PermissionDenial`, `UsageSummary`, `PortContext`, `ToolPermissionContext`, `CommandExecution`, `ToolExecution`, `WorkspaceSetup`, `SetupReport`, `PortManifest`, `StoredSession`, `QueryEngineConfig`, `TurnResult`, `RoutedMatch`, `MirroredCommand`, `MirroredTool`, `ExecutionRegistry` -- ist als `@dataclass(frozen=True)` deklariert. Dies erzwingt Unveränderlichkeit nach der Erzeugung und macht die Objekte automatisch hashbar. In einem System, das Sessions verwaltet und Zustandsübergaenge trackt, ist diese Unveränderlichkeit ein mächtiges Werkzeug gegen eine ganze Klasse von Bugs.

### 14.6.2 LRU-Caching

Die Funktionen `load_command_snapshot()` und `load_tool_snapshot()` verwenden `@lru_cache(maxsize=1)`, um die JSON-Referenzdaten nur einmal von der Festplatte zu lesen. Da sich diese Daten während der Laufzeit nicht ändern, ist dies ein sauberer und effizienter Ansatz. Das Pattern wird konsequent nur dort eingesetzt, wo es sinnvoll ist -- bei idempotenten, reinen Funktionen ohne Seiteneffekte.

### 14.6.3 Factory Methods

Mehrere Klassen bieten klassenmethodenbasierte Factory-Methoden an: `QueryEnginePort.from_workspace()` erzeugt eine Engine aus dem aktuellen Arbeitsbereich, `QueryEnginePort.from_saved_session()` rekonstruiert eine Engine aus einer gespeicherten Session, und `ToolPermissionContext.from_iterables()` erzeugt einen Berechtigungskontext aus Listen statt aus Frozensets. Diese Factories kapseln die Konstruktionslogik und bieten eine klare, benannte Schnittstelle für unterschiedliche Erzeugungsszenarien.

### 14.6.4 Builder Pattern

Die Funktionen `build_port_context()`, `build_port_manifest()`, `build_command_backlog()`, `build_tool_backlog()`, `build_workspace_setup()`, `build_system_init_message()` und `build_execution_registry()` folgen einem einheitlichen Builder-Namensschema. Jede dieser Funktionen sammelt Informationen aus verschiedenen Quellen, konstruiert ein komplexes Objekt und gibt es zurück. Die Konsistenz dieses Namensschemas -- immer `build_*` -- macht den Code selbstdokumentierend.

### 14.6.5 Strategy Pattern

Das Permission-System implementiert ein Strategy Pattern: Die `ToolPermissionContext`-Klasse kapselt eine Filterungsstrategie (Deny-Liste plus Präfix-Matching), die von außen injiziert werden kann. Die Funktion `filter_tools_by_permission_context()` in `tools.py` wendet diese Strategie auf eine Menge von Tools an, ohne die Filtermechanik selbst zu kennen. Dies erlaubt es, verschiedene Berechtigungsstrategien auszutauschen, ohne die Tool-Lade- und Ausführungslogik zu ändern.

---

## 14.7 Was man aus diesem Projekt lernen kann

### 14.7.1 Agent-Harness-Architektur verstehen

Claw Code ist, soweit öffentlich bekannt, die detaillierteste Dokumentation einer Agent-Harness-Architektur in der Open-Source-Welt. Wer verstehen möchte, wie ein System wie Claude Code intern funktioniert -- wie Prompts geroutet werden, wie Tools ausgewählt und ausgeführt werden, wie Sessions verwaltet und persistiert werden, wie Berechtigungen durchgesetzt werden --, findet in diesem Projekt eine reichhaltige Quelle.

Die Architektur zeigt, dass ein modernes Agent-Harness weit mehr ist als eine Schleife, die Prompts an ein Sprachmodell sendet und Antworten zurückgibt. Es ist ein komplexes System mit eigenem Zustandsmanagement, eigener Berechtigungslogik, eigenem Token-Budgeting, eigener Session-Persistenz und eigener Tool-Registry. Diese Komplexitaet zu verstehen, ist für jeden Entwickler wertvoll, der an der nächsten Generation von KI-gestützten Werkzeugen arbeitet.

### 14.7.2 Clean-Room-Reimplementierung als Methode

Das Projekt demonstriert, wie eine Clean-Room-Reimplementierung als Methode des technischen Verstaendnisses eingesetzt werden kann. Indem man ein System in einer anderen Sprache nachbaut, ist man gezwungen, jede Designentscheidung bewusst nachzuvollziehen. Man kann nicht einfach Code kopieren; man muss ihn verstehen. Dieser Prozess des erzwungenen Verstaendnisses führt oft zu tieferen Einsichten als das bloße Lesen des Originalcodes.

Gleichzeitig zeigt das Projekt die Grenzen dieses Ansatzes: Die strukturelle Paritaet ist relativ schnell erreichbar, aber die Verhaltensparitaet erfordert ein Vielfaches an Aufwand. Die Reimplementierung deckt Designentscheidungen auf, aber sie kann die impliziten Annahmen und die gelebte Erfahrung der Originalentwickler nicht vollständig erfassen.

### 14.7.3 Modulare Python-Architektur ohne Abhängigkeiten

Für Python-Entwickler bietet Claw Code ein lehrreiches Beispiel dafür, wie eine nicht-triviale Anwendung vollständig ohne externe Abhängigkeiten strukturiert werden kann. Die Kombination aus `dataclasses`, `json`, `pathlib`, `functools.lru_cache`, `uuid`, `platform` und `unittest` -- alles Module der Standardbibliothek -- reicht aus, um ein System mit Dutzenden von Modulen, einer CLI-Schnittstelle, Session-Persistenz und einem Testsuite zu bauen.

Diese Abhängigkeitsfreiheit ist nicht nur eine technische Kuriosiaet. Sie hat praktische Vorteile: Das Projekt lässt sich auf jedem System mit einer Python-3-Installation ausführen, ohne dass Pakete installiert, virtuelle Umgebungen konfiguriert oder Versionskonflikte gelöst werden müssen. In einer Welt, in der selbst einfache Python-Projekte oft Dutzende transitiver Abhängigkeiten mit sich bringen, ist diese Schlankheit bemerkenswert -- und nachahmungswürdig.

---

## 14.8 Ein Blick nach vorn

### 14.8.1 Die nächsten Schritte

Die Zukunft von Claw Code liegt auf mehreren Achsen:

1. **Rust-Portierung abschließen**: Die sechs Crates unter `rust/crates/` müssen mit Laufzeitlogik gefuellt werden. Das Ziel ist ein eigenständiges Binary, das als Agent-Harness funktioniert.

2. **Laufzeittiefe in Python erhöhen**: Auch der Python-Baum kann und soll weiter vertieft werden. Die Subsystem-Platzhalter koennen schrittweise durch ausführbare Module ersetzt werden.

3. **Paritaetsprüfung automatisieren**: Der `parity-audit`-Befehl kann zum kontinuierlichen Regressionstest ausgebaut werden, der bei jedem Commit prüft, ob die Portierung mit dem Original synchron bleibt.

4. **Community-Beitraege ermöglichen**: Die modulare Struktur und die klare Trennung der Subsysteme laden zu Beitraegen ein. Jedes Subsystem kann unabhängig bearbeitet werden.

### 14.8.2 Die größere Bedeutung

Claw Code ist mehr als ein technisches Projekt. Es ist ein Experiment an der Schnittstelle von Reverse Engineering, KI-Ethik und Open-Source-Kultur. Es zeigt, dass die Offenlegung von Quellcode -- ob beabsichtigt oder nicht -- eine Kaskade von Reaktionen auslösen kann, die weit über das urspruengliche Ereignis hinausgeht. Es zeigt, dass die Grenzen zwischen "verstehen", "dokumentieren" und "reimplementieren" fliessend sind. Und es zeigt, dass die Open-Source-Community in der Lage ist, innerhalb von Stunden auf ein Ereignis zu reagieren und etwas Eigenes daraus zu schaffen.

Die 30.000 GitHub-Stars sind ein Indikator für das Interesse, aber nicht für den Wert des Projekts. Der wirkliche Wert liegt in dem, was wir über Agent-Harness-Architekturen gelernt haben, in den Fragen, die wir aufgeworfen haben, und in der Methodik, die wir demonstriert haben.

---

## 14.9 Schlusswort

Als Sigrid Jin sich an jenem fruehen Morgen des 31. Maerz 2026 hinsetzte und begann, die Kernfunktionen des Claude-Code-Harness nach Python zu portieren, könnte sie nicht wissen, dass daraus das am schnellsten wachsende GitHub-Repository der Geschichte werden würde. Aber vielleicht war das auch nicht der Punkt. Der Punkt war: verstehen, wie es funktioniert. Und dann: es besser machen.

Dieses Buch hat versucht, diesen Verstehensprozess nachzuzeichnen -- von der Architekturanalyse über die Designentscheidungen bis hin zu den ethischen Implikationen. Wenn Sie, liebe Leserin, lieber Leser, aus dieser Lektuere mitnehmen, dass Agent-Harness-Systeme keine Black Boxes sein müssen, dass modulare Architektur ohne Abhängigkeiten möglich ist und dass technische Neugier manchmal die staerkste Triebfeder für Innovation ist, dann hat dieses Buch seinen Zweck erfuellt.

Die Zukunft von Claw Code ist offen. Die Rust-Portierung wird die Laufzeitluecke schließen. Die Community wird die Subsysteme vertiefen. Und die ethische Debatte über KI-Reimplementierung wird weitergehen -- hoffentlich mit der Nuanciertheit und Ernsthaftigkeit, die sie verdient.

In diesem Sinne: Das Projekt ist nicht abgeschlossen. Es hat gerade erst begonnen.
