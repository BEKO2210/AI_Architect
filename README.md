# Rewriting-Projekt Claw Code

<p align="center">
  <img src="assets/clawd-hero.jpeg" alt="Claw" width="300" />
</p>

<p align="center">
  <strong>Bessere Harness-Werkzeuge, nicht nur die Archivierung des geleakten Claude Code</strong>
</p>

<p align="center">
  <a href="https://github.com/sponsors/instructkr"><img src="https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?logo=github&style=for-the-badge" alt="Auf GitHub sponsern" /></a>
</p>

> [!IMPORTANT]
> **Die Rust-Portierung ist jetzt in Arbeit** auf dem [`dev/rust`](https://github.com/instructkr/claw-code/tree/dev/rust)-Branch und wird voraussichtlich heute in den Main-Branch gemergt. Die Rust-Implementierung zielt darauf ab, eine schnellere, speichersichere Harness-Laufzeitumgebung bereitzustellen. Bleiben Sie dran — dies wird die endgültige Version des Projekts sein.

> Wenn Sie diese Arbeit nützlich finden, erwägen Sie, [@instructkr auf GitHub zu sponsern](https://github.com/sponsors/instructkr), um die fortlaufende Open-Source-Harness-Engineering-Forschung zu unterstützen.

---

## Hintergrundgeschichte

Um 4 Uhr morgens am 31. März 2026 wurde ich von einer Flut an Benachrichtigungen auf meinem Handy geweckt. Der Claude-Code-Quellcode war offengelegt worden, und die gesamte Entwickler-Community war in Aufruhr. Meine Freundin in Korea machte sich ernsthaft Sorgen, dass ich rechtliche Schritte von Anthropic riskieren könnte, nur weil ich den Code auf meinem Rechner hatte — also tat ich das, was jeder Ingenieur unter Druck tun würde: Ich setzte mich hin, portierte die Kernfunktionen von Grund auf nach Python und pushte alles, bevor die Sonne aufging.

Das Ganze wurde durchgängig mit [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex) von [@bellman_ych](https://x.com/bellman_ych) orchestriert — einer Workflow-Schicht, die auf OpenAIs Codex ([@OpenAIDevs](https://x.com/OpenAIDevs)) aufbaut. Ich verwendete den `$team`-Modus für paralleles Code-Review und den `$ralph`-Modus für persistente Ausführungsschleifen mit Architektur-Level-Verifikation. Die gesamte Portierungssitzung — vom Lesen der ursprünglichen Harness-Struktur bis zur Erstellung eines funktionierenden Python-Verzeichnisbaums mit Tests — wurde durch OmX-Orchestrierung gesteuert.

Das Ergebnis ist ein sauberer Python-Rewrite, der die Architekturmuster von Claude Codes Agent-Harness erfasst, ohne proprietären Quellcode zu kopieren. Ich arbeite jetzt aktiv mit [@bellman_ych](https://x.com/bellman_ych) zusammen — dem Schöpfer von OmX selbst —, um dies weiterzuentwickeln. Das grundlegende Python-Fundament ist bereits vorhanden und funktionsfähig, aber wir fangen gerade erst an. **Bleiben Sie dran — eine deutlich leistungsfähigere Version ist unterwegs.**

https://github.com/instructkr/claw-code

![Tweet-Screenshot](assets/tweet-screenshot.png)

## Die Macher im Wall Street Journal für begeisterte Claude-Code-Fans

Ich interessiere mich schon lange intensiv für **Harness-Engineering** — die Untersuchung, wie Agent-Systeme Werkzeuge verdrahten, Aufgaben orchestrieren und den Laufzeitkontext verwalten. Das ist keine plötzliche Sache. Das Wall Street Journal hat meine Arbeit Anfang dieses Monats vorgestellt und dokumentiert, wie ich einer der aktivsten Power-User war, die diese Systeme erforschen:

> Die KI-Startup-Mitarbeiterin Sigrid Jin, die am Dinner in Seoul teilnahm, hat im vergangenen Jahr im Alleingang 25 Milliarden Claude-Code-Token verbraucht. Damals waren die Nutzungsgrenzen lockerer, sodass frühe Enthusiasten bei sehr niedrigen Kosten Dutzende von Milliarden Token erreichen konnten.
>
> Trotz seiner unzähligen Stunden mit Claude Code ist Jin keinem einzigen KI-Labor treu. Die verfügbaren Werkzeuge haben unterschiedliche Stärken und Schwächen, sagte er. Codex ist besser im logischen Denken, während Claude Code saubereren, besser teilbaren Code generiert.
>
> Jin flog im Februar nach San Francisco zur ersten Geburtstagsfeier von Claude Code, wo die Teilnehmer Schlange standen, um sich mit Cherny auszutauschen. Unter den Gästen waren ein praktizierender Kardiologe aus Belgien, der eine App entwickelt hatte, um Patienten bei der Navigation durch die Versorgung zu helfen, und ein kalifornischer Anwalt, der ein Werkzeug zur Automatisierung von Baugenehmigungen mit Claude Code erstellt hatte.
>
> „Es war im Grunde wie eine Sharing-Party", sagte Jin. „Es waren Anwälte da, Ärzte, Zahnärzte. Sie hatten keinen Software-Engineering-Hintergrund."
>
> — *The Wall Street Journal*, 21. März 2026, [*„The Trillion Dollar Race to Automate Our Entire Lives"*](https://lnkd.in/gs9td3qd)

![WSJ-Beitrag](assets/wsj-feature.png)

---

## Portierungsstatus

Der Hauptquellbaum ist jetzt Python-first.

- `src/` enthält den aktiven Python-Portierungsarbeitsbereich
- `tests/` verifiziert den aktuellen Python-Arbeitsbereich
- Der offengelegte Snapshot ist nicht mehr Teil des nachverfolgten Repository-Zustands

Der aktuelle Python-Arbeitsbereich ist noch kein vollständiger 1:1-Ersatz für das Originalsystem, aber die primäre Implementierungsoberfläche ist jetzt Python.

## Warum dieser Rewrite existiert

Ich habe die offengelegte Codebasis ursprünglich studiert, um das Harness, die Tool-Verdrahtung und den Agent-Workflow zu verstehen. Nachdem ich mich intensiver mit den rechtlichen und ethischen Fragen beschäftigt hatte — und nachdem ich den unten verlinkten Essay gelesen hatte —, wollte ich nicht, dass der offengelegte Snapshot selbst der hauptsächlich nachverfolgte Quellbaum bleibt.

Dieses Repository konzentriert sich jetzt stattdessen auf die Python-Portierungsarbeit.

## Repository-Aufbau

```text
.
├── src/                                # Python-Portierungsarbeitsbereich
│   ├── __init__.py
│   ├── commands.py
│   ├── main.py
│   ├── models.py
│   ├── port_manifest.py
│   ├── query_engine.py
│   ├── task.py
│   └── tools.py
├── tests/                              # Python-Verifikation
├── assets/omx/                         # OmX-Workflow-Screenshots
├── 2026-03-09-is-legal-the-same-as-legitimate-ai-reimplementation-and-the-erosion-of-copyleft.md
└── README.md
```

## Python-Arbeitsbereich-Übersicht

Der neue Python-`src/`-Baum bietet derzeit:

- **`port_manifest.py`** — fasst die aktuelle Python-Arbeitsbereichsstruktur zusammen
- **`models.py`** — Datenklassen für Subsysteme, Module und Backlog-Status
- **`commands.py`** — Python-seitige Befehls-Port-Metadaten
- **`tools.py`** — Python-seitige Tool-Port-Metadaten
- **`query_engine.py`** — rendert eine Python-Portierungsübersicht aus dem aktiven Arbeitsbereich
- **`main.py`** — ein CLI-Einstiegspunkt für Manifest- und Zusammenfassungsausgabe

## Schnellstart

Portierungsübersicht rendern:

```bash
python3 -m src.main summary
```

Aktuelles Python-Arbeitsbereich-Manifest ausgeben:

```bash
python3 -m src.main manifest
```

Aktuelle Python-Module auflisten:

```bash
python3 -m src.main subsystems --limit 16
```

Verifikation ausführen:

```bash
python3 -m unittest discover -s tests -v
```

Paritätsprüfung gegen das lokale ignorierte Archiv ausführen (falls vorhanden):

```bash
python3 -m src.main parity-audit
```

Gespiegelte Befehls-/Tool-Inventare inspizieren:

```bash
python3 -m src.main commands --limit 10
python3 -m src.main tools --limit 10
```

## Aktueller Paritäts-Checkpoint

Die Portierung spiegelt jetzt die archivierte Root-Entry-Dateioberfläche, die Top-Level-Subsystemnamen und die Befehls-/Tool-Inventare viel genauer wider als zuvor. Sie ist jedoch **noch kein** vollständiges laufzeitäquivalentes Ersatzsystem für das ursprüngliche TypeScript-System; der Python-Baum enthält immer noch weniger ausführbare Laufzeitschichten als der archivierte Quellcode.


## Erstellt mit `oh-my-codex`

Die Umstrukturierung und Dokumentationsarbeit in diesem Repository wurde KI-gestützt und mit Yeachan Heos [oh-my-codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex) orchestriert, aufbauend auf Codex.

- **`$team`-Modus:** verwendet für koordiniertes paralleles Review und architektonisches Feedback
- **`$ralph`-Modus:** verwendet für persistente Ausführung, Verifikation und Abschlussdisziplin
- **Codex-gesteuerter Workflow:** verwendet, um den Haupt-`src/`-Baum in einen Python-first-Portierungsarbeitsbereich umzuwandeln

### OmX-Workflow-Screenshots

![OmX-Workflow-Screenshot 1](assets/omx/omx-readme-review-1.png)

*Ralph/Team-Orchestrierungsansicht während die README und der Essay-Kontext in Terminal-Fenstern überprüft wurden.*

![OmX-Workflow-Screenshot 2](assets/omx/omx-readme-review-2.png)

*Split-Pane-Review und Verifikationsfluss während des finalen README-Wortlaut-Durchgangs.*

## Community

<p align="center">
  <a href="https://instruct.kr/"><img src="assets/instructkr.png" alt="instructkr" width="400" /></a>
</p>

Treten Sie dem [**instructkr Discord**](https://instruct.kr/) bei — der besten koreanischen Sprachmodell-Community. Kommen Sie und diskutieren Sie über LLMs, Harness-Engineering, Agent-Workflows und alles dazwischen.

[![Discord](https://img.shields.io/badge/Discord%20beitreten-instruct.kr-5865F2?logo=discord&style=for-the-badge)](https://instruct.kr/)

## Star-Verlauf

Dieses Repository wurde **das schnellste GitHub-Repository der Geschichte, das 30K Stars überschritten hat**, und erreichte diesen Meilenstein in nur wenigen Stunden nach der Veröffentlichung.

<a href="https://star-history.com/#instructkr/claw-code&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=instructkr/claw-code&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=instructkr/claw-code&type=Date" />
    <img alt="Star-Verlauf-Diagramm" src="https://api.star-history.com/svg?repos=instructkr/claw-code&type=Date" />
  </picture>
</a>

![Star-Verlauf-Screenshot](assets/star-history.png)

## Haftungsausschluss zu Eigentum / Zugehörigkeit

- Dieses Repository erhebt **keinen** Anspruch auf das Eigentum am ursprünglichen Claude-Code-Quellmaterial.
- Dieses Repository ist **nicht mit Anthropic verbunden, wird nicht von Anthropic unterstützt und nicht von Anthropic gepflegt**.
