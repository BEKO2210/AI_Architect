# Claw Code — Vollständige Anleitung

Diese Anleitung erklärt dir präzise, was dieses Projekt kann, wie du es benutzt und was hinter jedem Befehl steckt.

---

## Was ist dieses Projekt?

Claw Code ist eine **Python-Nachbildung** der Claude-Code-Agent-Harness-Architektur. Es ist kein direkter Copy-Paste des Originalcodes, sondern ein eigenständiger Rewrite, der die Architekturmuster und Designkonzepte nachbildet.

Das Projekt bietet dir:
- Einen vollständigen **Befehls- und Tool-Katalog** (~150 Befehle, ~100 Tools), gespiegelt aus dem archivierten TypeScript-Original
- Eine **Laufzeitumgebung** mit Prompt-Routing, Session-Management und Turn-Schleifen
- **Paritätsprüfungen**, um den Fortschritt der Python-Portierung gegenüber dem Original zu messen
- **Session-Persistenz** zum Speichern und Wiederherstellen von Sitzungen

---

## Voraussetzungen

- **Python 3.8** oder neuer
- **Keine externen Abhängigkeiten** — alles läuft mit der Python-Standardbibliothek
- Ausführung erfolgt immer über: `python3 -m src.main <BEFEHL>`

---

## Alle verfügbaren Befehle

### 1. Arbeitsbereich inspizieren

#### `summary` — Portierungsübersicht anzeigen
Zeigt eine Markdown-Zusammenfassung des gesamten Python-Arbeitsbereichs: wie viele Dateien existieren, welche Subsysteme portiert sind und was im Backlog steht.

```bash
python3 -m src.main summary
```

#### `manifest` — Dateistruktur anzeigen
Listet alle Python-Dateien im Projekt auf, gruppiert nach Modulen, mit Dateianzahl pro Modul.

```bash
python3 -m src.main manifest
```

#### `subsystems` — Module auflisten
Zeigt die Top-Level-Python-Module (Subsysteme) an. Mit `--limit` kannst du die Anzahl begrenzen.

```bash
python3 -m src.main subsystems
python3 -m src.main subsystems --limit 10
```

#### `setup-report` — Umgebungsbericht
Zeigt einen Bericht über deine Python-Version, Plattform, Implementierung und den Status der Prefetch- und Deferred-Init-Stufen.

```bash
python3 -m src.main setup-report
```

---

### 2. Befehle und Tools durchsuchen

#### `commands` — Befehlskatalog anzeigen
Listet alle gespiegelten Befehle aus dem archivierten Snapshot auf. Du kannst filtern, suchen und Plugin-/Skill-Befehle ausblenden.

```bash
python3 -m src.main commands                          # Alle Befehle anzeigen
python3 -m src.main commands --limit 10               # Nur die ersten 10
python3 -m src.main commands --query "git"             # Nach "git" suchen
python3 -m src.main commands --no-plugin-commands      # Plugin-Befehle ausblenden
python3 -m src.main commands --no-skill-commands       # Skill-Befehle ausblenden
```

#### `tools` — Tool-Katalog anzeigen
Listet alle gespiegelten Tools auf. Unterstützt Berechtigungsfilter zum Blockieren bestimmter Tools.

```bash
python3 -m src.main tools                             # Alle Tools anzeigen
python3 -m src.main tools --limit 10                  # Nur die ersten 10
python3 -m src.main tools --query "file"              # Nach "file" suchen
python3 -m src.main tools --simple-mode               # Vereinfachte Ansicht
python3 -m src.main tools --no-mcp                    # MCP-Tools ausblenden
python3 -m src.main tools --deny-tool Bash             # "Bash"-Tool blockieren
python3 -m src.main tools --deny-prefix mcp__          # Alle Tools mit Prefix "mcp__" blockieren
```

#### `show-command` — Einzelnen Befehl anzeigen
Zeigt detaillierte Informationen zu einem bestimmten Befehl (Name, Verantwortlichkeit, Quellhinweis).

```bash
python3 -m src.main show-command "commit"
```

#### `show-tool` — Einzelnes Tool anzeigen
Zeigt detaillierte Informationen zu einem bestimmten Tool.

```bash
python3 -m src.main show-tool "Read"
```

---

### 3. Befehle und Tools ausführen

#### `exec-command` — Befehlsshim ausführen
Führt einen gespiegelten Befehl mit einem Prompt aus. Gibt eine simulierte Ausführungsantwort zurück.

```bash
python3 -m src.main exec-command "commit" "Fix the login bug"
```

#### `exec-tool` — Tool-Shim ausführen
Führt ein gespiegeltes Tool mit einer Payload aus.

```bash
python3 -m src.main exec-tool "Read" '{"file": "main.py"}'
```

---

### 4. Prompt-Routing und Sitzungen

#### `route` — Prompt routen
Nimmt einen Prompt entgegen und findet die am besten passenden Befehle und Tools anhand von Token-Ähnlichkeit. So siehst du, welche Befehle/Tools für eine bestimmte Anfrage relevant wären.

```bash
python3 -m src.main route "Erstelle einen neuen Branch"
python3 -m src.main route "Erstelle einen neuen Branch" --limit 5
```

#### `bootstrap` — Vollständige Sitzung starten
Baut eine komplette Laufzeitsitzung auf: sammelt Workspace-Kontext, führt Setup durch, erstellt ein System-Init-Nachricht, routet den Prompt und erzeugt einen Session-Bericht.

```bash
python3 -m src.main bootstrap "Analysiere die Codebasis"
python3 -m src.main bootstrap "Analysiere die Codebasis" --limit 5
```

#### `turn-loop` — Multi-Turn-Schleife ausführen
Führt eine zustandsbehaftete Schleife mit mehreren Durchgängen (Turns) aus. Simuliert, wie ein Agent mehrere Schritte hintereinander ausführt.

```bash
python3 -m src.main turn-loop "Refaktoriere die Datei"
python3 -m src.main turn-loop "Refaktoriere die Datei" --max-turns 3
python3 -m src.main turn-loop "Refaktoriere die Datei" --structured-output   # JSON-Ausgabe
```

---

### 5. Session-Verwaltung

#### `flush-transcript` — Sitzungsprotokoll speichern
Speichert das aktuelle Sitzungsprotokoll (Transcript) dauerhaft auf der Festplatte im Ordner `.port_sessions/`.

```bash
python3 -m src.main flush-transcript "Meine aktuelle Sitzung"
```

#### `load-session` — Gespeicherte Sitzung laden
Lädt eine zuvor gespeicherte Sitzung anhand ihrer Session-ID wieder.

```bash
python3 -m src.main load-session <SESSION_ID>
```

Die Session-ID wird beim Speichern mit `flush-transcript` oder `bootstrap` in der Ausgabe angezeigt.

---

### 6. Laufzeitmodi simulieren

Diese Befehle simulieren verschiedene Verbindungsmodi, wie sie in der Original-Harness-Architektur vorkommen:

```bash
python3 -m src.main remote-mode "server.example.com"         # Remote-Modus
python3 -m src.main ssh-mode "user@server.example.com"       # SSH-Modus
python3 -m src.main teleport-mode "cluster.example.com"      # Teleport-Modus
python3 -m src.main direct-connect-mode "10.0.0.1:8080"      # Direktverbindung
python3 -m src.main deep-link-mode "app://workspace/project"  # Deep-Link-Modus
```

Jeder Modus gibt einen `RuntimeModeReport` oder `DirectModeReport` mit Modus-Name, Ziel und Status zurück.

---

### 7. Architekturanalyse

#### `command-graph` — Befehlsgraph anzeigen
Segmentiert alle Befehle in drei Kategorien:
- **Builtins** — eingebaute Systembefehle
- **Plugin-like** — Plugin-artige Befehle
- **Skill-like** — Skill-artige Befehle

```bash
python3 -m src.main command-graph
```

#### `tool-pool` — Tool-Pool anzeigen
Zeigt den zusammengestellten Tool-Pool mit Standardeinstellungen und Filteroptionen.

```bash
python3 -m src.main tool-pool
```

#### `bootstrap-graph` — Bootstrap-Phasen anzeigen
Zeigt die 7 Startphasen der Laufzeitumgebung:
1. Prefetch
2. Trust Gate
3. CLI Parser
4. Setup
5. Deferred Init
6. Mode Routing
7. Query Submit

```bash
python3 -m src.main bootstrap-graph
```

---

### 8. Paritätsprüfung

#### `parity-audit` — Portierungsfortschritt messen
Vergleicht den Python-Arbeitsbereich mit dem archivierten TypeScript-Snapshot (falls lokal vorhanden) und zeigt:
- **Root-Datei-Abdeckung** — wie viele Originaldateien im Python-Port existieren
- **Verzeichnis-Abdeckung** — wie viele Subsysteme als Python-Pakete gespiegelt sind
- **Befehls-/Tool-Einträge** — Vollständigkeit des Befehls- und Tool-Katalogs

```bash
python3 -m src.main parity-audit
```

---

### 9. Tests ausführen

Das Projekt enthält **49 Testfälle**, die alle CLI-Befehle und Kernfunktionen abdecken.

```bash
python3 -m unittest discover -s tests -v
```

---

## Projektstruktur im Detail

```
.
├── src/                          # Hauptquellcode
│   ├── main.py                   # CLI-Einstiegspunkt (24 Befehle)
│   ├── runtime.py                # Prompt-Routing, Session-Bootstrapping, Turn-Ausführung
│   ├── query_engine.py           # Session-Zustand, Transkript, Nachrichtenverarbeitung
│   ├── commands.py               # Befehlskatalog (~150 Einträge)
│   ├── tools.py                  # Tool-Katalog (~100 Einträge)
│   ├── models.py                 # Datenklassen (Subsystem, PortingModule, etc.)
│   ├── port_manifest.py          # Arbeitsbereich-Scanner
│   ├── context.py                # Workspace-Kontext (Pfade, Dateianzahl)
│   ├── setup.py                  # Umgebungserkennung und Prefetch
│   ├── parity_audit.py           # Portierungsfortschritt-Vergleich
│   ├── session_store.py          # Session-Persistenz (.port_sessions/)
│   ├── transcript.py             # Sitzungsprotokoll-Verwaltung
│   ├── permissions.py            # Tool-Zugriffskontrolle
│   ├── execution_registry.py     # Einheitliche Befehls-/Tool-Ausführung
│   ├── command_graph.py          # Befehlskategorisierung
│   ├── bootstrap_graph.py        # Bootstrap-Phasen-Definition
│   ├── tool_pool.py              # Tool-Pool-Zusammenstellung
│   ├── system_init.py            # System-Startmeldung
│   ├── history.py                # Session-Event-Protokoll
│   ├── prefetch.py               # Simulierte Vorab-Ladevorgänge
│   ├── deferred_init.py          # Verzögerte Initialisierung (Trust-abhängig)
│   ├── direct_modes.py           # Direct-Connect / Deep-Link Modi
│   ├── remote_runtime.py         # Remote / SSH / Teleport Modi
│   ├── reference_data/           # JSON-Snapshots (Befehle, Tools, Subsysteme)
│   └── <subsystem-pakete>/       # 30+ Subsystem-Platzhalter (assistant, bridge, etc.)
├── tests/
│   └── test_porting_workspace.py # 49 Testfälle
├── assets/                       # Bilder und Screenshots
├── .port_sessions/               # Gespeicherte Sitzungen (wird automatisch erstellt)
└── README.md                     # Projektbeschreibung (Deutsch)
```

---

## Architektur-Überblick

Das Projekt folgt einem **Drei-Schichten-Modell**:

### Schicht 1: Spiegelungsschicht
`commands.py` und `tools.py` laden die archivierten JSON-Snapshots als unveränderliche Referenzdaten. Diese Daten repräsentieren den Befehls- und Tool-Katalog des Originalsystems.

### Schicht 2: Orchestrierungsschicht
`runtime.py` und `query_engine.py` koordinieren das Prompt-Routing, verwalten Sessions und führen die Turn-Schleifen aus. Hier passiert die eigentliche "Intelligenz" des Systems.

### Schicht 3: Infrastrukturschicht
`setup.py`, `context.py` und `session_store.py` kümmern sich um Umgebungserkennung, Persistenz und Logging.

### Trust-Gating (Vertrauensstufen)
Die verzögerte Initialisierung (`deferred_init.py`) wird über einen `trusted`-Parameter gesteuert:
- **trusted=True** → Plugins, Skills, MCP-Prefetch und Session-Hooks werden aktiviert
- **trusted=False** → Alle verzögerten Initialisierungen werden deaktiviert

### Session-Lebenszyklus
```
1. QueryEnginePort.from_workspace()        → Neue Sitzung erstellen
2. submit_message(prompt, commands, tools)  → Prompt verarbeiten
3. compact_messages_if_needed()             → Transkript komprimieren
4. persist_session()                        → Auf Festplatte speichern
5. load_session(session_id)                 → Später wiederherstellen
```

---

## Typische Arbeitsabläufe

### "Ich will verstehen, was das Projekt kann"
```bash
python3 -m src.main summary
python3 -m src.main manifest
python3 -m src.main subsystems --limit 50
```

### "Ich will den Befehlskatalog durchsuchen"
```bash
python3 -m src.main commands --query "git"
python3 -m src.main show-command "commit"
python3 -m src.main command-graph
```

### "Ich will wissen, welche Tools es gibt"
```bash
python3 -m src.main tools --query "read"
python3 -m src.main show-tool "Bash"
python3 -m src.main tool-pool
```

### "Ich will sehen, wie ein Prompt geroutet wird"
```bash
python3 -m src.main route "Lies die Datei main.py"
python3 -m src.main bootstrap "Erstelle einen Unit-Test"
python3 -m src.main turn-loop "Analysiere den Code" --max-turns 3
```

### "Ich will den Portierungsfortschritt prüfen"
```bash
python3 -m src.main parity-audit
python3 -m src.main bootstrap-graph
```

### "Ich will die Tests ausführen"
```bash
python3 -m unittest discover -s tests -v
```

---

## Hinweise

- Alle Befehle werden mit `python3 -m src.main` ausgeführt — es gibt keine separate Installation.
- Die JSON-Snapshots in `src/reference_data/` sind die Grundlage für den Befehls- und Tool-Katalog.
- Gespeicherte Sitzungen landen in `.port_sessions/` als JSON-Dateien.
- Die Subsystem-Pakete (z.B. `src/assistant/`, `src/bridge/`) sind Platzhalter, die Metadaten aus den JSON-Snapshots laden — sie enthalten noch keine vollständige Funktionalität.
- Das Projekt hat **keine externen Abhängigkeiten** — nur Python-Standardbibliothek.
