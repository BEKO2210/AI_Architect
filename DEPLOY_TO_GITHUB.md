# Anleitung: GitHub Pages Deployment

Diese Anleitung erklärt, wie du alle Dateien zu deinem GitHub-Repository hochlädst und GitHub Pages aktivierst.

## Schritt 1: Dateien vorbereiten

Kopiere die folgenden Dateien und Ordner in dein lokales Repository:

### Wichtige Dateien (Root-Verzeichnis):
```
index.html                    (Hauptseite Deutsch)
index_en.html                 (Hauptseite Englisch)
howto.html                    (How-To Guide Deutsch)
howto_en.html                 (How-To Guide Englisch)
impressum.html                (Impressum)
favicon.svg                   (Favicon)
og-image.svg                  (Social Media Bild)
robots.txt                    (SEO)
sitemap.xml                   (SEO)
manifest.json                 (PWA Manifest)
structured-data.json          (SEO Structured Data)
```

### EPUB Dateien (Download):
```
Claw_Code_Architecture_of_an_AI_Agent_Harness.epub      (Englisch)
Claw_Code_Architektur_eines_KI-Agent-Harness.epub       (Deutsch)
```

### How-To Ordner:
```
howto/
├── 01.html
├── 02.html
├── 03.html
├── 04.html
├── 05.html
├── 06.html
├── 07.html
├── 08.html
├── 09.html
└── 10.html
```

### GitHub Actions Workflow:
```
.github/
└── workflows/
    └── deploy.yml
```

### Optional (für Vollständigkeit):
```
ANLEITUNG.md                  (Komplette Befehlsreferenz)
README.md                     (Projektbeschreibung)
BOOK_CLAW_CODE_ARCHITECTURE.md    (Englische Buch-Version)
BUCH_CLAW_CODE_ARCHITEKTUR.md     (Deutsche Buch-Version)
```

## Schritt 2: GitHub Repository einrichten

### 2.1 Repository erstellen
1. Gehe zu https://github.com/new
2. Repository-Name: `AI_Architect` (oder dein gewählter Name)
3. Öffentlich (Public) wählen für GitHub Pages
4. README.md initialisieren (optional)

### 2.2 Dateien hochladen

#### Option A: Git Kommandozeile

```bash
# In deinem Projektordner
cd /pfad/zu/deinem/AI_Architect

# Git initialisieren (falls noch nicht geschehen)
git init

# Remote hinzufügen
git remote add origin https://github.com/BEKO2210/AI_Architect.git

# Alle Dateien hinzufügen
git add .

# Commit erstellen
git commit -m "Initial commit: Claw Code Website"

# Zu GitHub pushen
git push -u origin main
```

#### Option B: GitHub Web Interface

1. Gehe zu deinem Repository auf GitHub
2. Klicke auf "Add file" → "Upload files"
3. Ziehe alle Dateien in den Bereich oder wähle sie aus
4. Schreibe eine Commit-Nachricht: "Add website files"
5. Klicke "Commit changes"

## Schritt 3: GitHub Pages aktivieren

1. Gehe zu deinem Repository auf GitHub
2. Klicke auf "Settings" (oben rechts)
3. Scrolle zu "Pages" (linke Seitenleiste)
4. Unter "Source" wähle:
   - Branch: `main` (oder `master`)
   - Folder: `/ (root)`
5. Klicke "Save"

6. Optional: Benutzerdefinierte Domain
   - Unter "Custom domain" gib deine Domain ein (z.B. `ai-architect.de`)
   - Klicke "Save"
   - Erstelle DNS-Einträge bei deinem Domain-Provider

## Schritt 4: Deployment überprüfen

1. Gehe zu "Actions" Tab in deinem Repository
2. Warte bis der Workflow "Deploy to GitHub Pages" erfolgreich ist (grüner Haken)
3. Deine Website ist dann verfügbar unter:
   - `https://beko2210.github.io/AI_Architect/`
   - Oder deine benutzerdefinierte Domain

## Dateistruktur im Repository

```
AI_Architect/
├── .github/
│   └── workflows/
│       └── deploy.yml          # Automatisches Deployment
├── howto/
│   ├── 01.html
│   ├── 02.html
│   ├── ...
│   └── 10.html
├── index.html                  # Startseite
├── index_en.html               # Englische Startseite
├── howto.html                  # How-To Guide
├── howto_en.html               # How-To Guide EN
├── impressum.html              # Impressum
├── favicon.svg
├── og-image.svg
├── robots.txt
├── sitemap.xml
├── manifest.json
├── structured-data.json
├── Claw_Code_Architecture_of_an_AI_Agent_Harness.epub
├── Claw_Code_Architektur_eines_KI-Agent-Harness.epub
└── README.md                   # Optional
```

## Wichtige URLs nach Deployment

| Seite | URL |
|-------|-----|
| Startseite (DE) | `https://beko2210.github.io/AI_Architect/` |
| Startseite (EN) | `https://beko2210.github.io/AI_Architect/index_en.html` |
| How-To Guide | `https://beko2210.github.io/AI_Architect/howto.html` |
| How-To Sektion 1 | `https://beko2210.github.io/AI_Architect/howto/01.html` |
| EPUB Download | `https://beko2210.github.io/AI_Architect/Claw_Code_Architektur_eines_KI-Agent-Harness.epub` |

## Fehlerbehebung

### 404 Fehler
- Prüfe, ob die Dateien im Root-Verzeichnis sind
- Warte 5-10 Minuten nach dem Deployment
- Überprüfe die GitHub Actions Logs unter "Actions" Tab

### Bilder/EPUB nicht ladbar
- Stelle sicher, dass die Dateinamen exakt übereinstimmen (Groß-/Kleinschreibung!)
- Prüfe die URLs in den HTML-Dateien

### Workflow fehlschlägt
- Gehe zu "Actions" → "Deploy to GitHub Pages"
- Klicke auf den fehlgeschlagenen Workflow
- Lies die Fehlermeldung

## Schnell-Upload Script (PowerShell)

```powershell
# Alle Dateien zum Staging hinzufügen
git add *.html *.svg *.xml *.txt *.json *.md *.epub
git add howto/
git add .github/

# Commit und Push
git commit -m "Update website files"
git push origin main
```

## Support

Für Probleme mit GitHub Pages:
- https://docs.github.com/en/pages

Für DNS-Konfiguration mit Custom Domain:
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site
