# Ghostprint 🕵️‍♂️

Ghostprint is een minimalistische open source tool waarmee je jouw digitale voetafdruk kunt scannen — gericht op privacy, veiligheid en bewustwording. Ideaal voor journalisten, onderzoekers of iedereen die controle wil over online aanwezigheid.

> 🚧 Deze tool is nog in ontwikkeling. De huidige MVP gebruikt gesimuleerde scanresultaten om de API en frontend werkend te testen. In de toekomst worden echte OSINT-scanners zoals Sherlock toegevoegd.

---

## 🎯 Doel

Ghostprint helpt je te begrijpen waar jouw e-mailadres mogelijk online opduikt. Het uiteindelijke doel is een complete Zero-Trace Privacy Suite die eenvoudig te gebruiken is, maar krachtig onder de motorkap.

---

## ✨ Features

- REST API (Flask) om e-mailadressen te scannen
- Genereert unieke `scan_id` en JSON-resultaten
- Resultaten worden lokaal opgeslagen in `scans/`
- Simpele frontend (HTML + JavaScript) inbegrepen
- Voorbereid op uitbreiding naar echte OSINT-integraties

---

## 🧱 Bestandsoverzicht
ghostprint/
├── main.py # Flask backend
├── index.html # Eenvoudige frontend
├── scans/ # Output map met scanresultaten (.json)
├── .gitignore
├── README.md
└── requirements.txt # (optioneel, zie onder)

text

---

## �️ Installatie

### 1. Clone het project

```bash
git clone https://github.com/jouwgebruikersnaam/ghostprint.git
cd ghostprint
2. Start een virtuele omgeving
bash
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  ← macOS/Linux
3. Installeer vereisten
bash
pip install flask
(of gebruik: pip install -r requirements.txt als die aanwezig is)
▶️ API Gebruiken
Start de server:

bash
python main.py
POST /api/scan

text
URL: http://127.0.0.1:5000/api/scan
Headers: Content-Type: application/json
Body:
json
{
  "email": "jan@example.com"
}
Response:

json
{
  "scan_id": "uuid-...",
  "result": {
    "email": "jan@example.com",
    "accounts_found": [
      "github.com/jan",
      "linkedin.com/in/jan"
    ],
    "status": "completed"
  }
}
🌐 Frontend gebruiken
Open index.html in je browser

Vul een e-mailadres in

Bekijk het gesimuleerde resultaat

Gebruik eventueel de Live Server extensie in VSCode voor gemak.

🛣️ Roadmap (toekomst)
✅ MVP met fake resultaten

🔍 Integratie met Sherlock voor OSINT-scan

📁 Downloadbare rapporten (PDF, CSV)

🔒 Gebruikersauthenticatie

🌍 Gehoste SaaS-versie met dashboard

⚖️ Licentie
MIT License — vrij te gebruiken, aan te passen en commercieel in te zetten.
Zie het LICENSE-bestand voor details.

text

I've made the following improvements:
1. Properly formatted all code blocks with triple backticks
2. Added consistent heading levels
3. Improved list formatting
4. Separated sections more clearly
5. Fixed some minor formatting issues from the original text
6. Made sure all special characters display correctly in Markdown
Ik wil het graag in 1 markdown box hebben zodat ik de gehele text in 1 keer kopier
Hier is de volledige tekst in één markdown blok dat je in één keer kunt kopiëren:

markdown
# Ghostprint 🕵️‍♂️

Ghostprint is een minimalistische open source tool waarmee je jouw digitale voetafdruk kunt scannen — gericht op privacy, veiligheid en bewustwording. Ideaal voor journalisten, onderzoekers of iedereen die controle wil over online aanwezigheid.

> 🚧 Deze tool is nog in ontwikkeling. De huidige MVP gebruikt gesimuleerde scanresultaten om de API en frontend werkend te testen. In de toekomst worden echte OSINT-scanners zoals Sherlock toegevoegd.

---

## 🎯 Doel

Ghostprint helpt je te begrijpen waar jouw e-mailadres mogelijk online opduikt. Het uiteindelijke doel is een complete Zero-Trace Privacy Suite die eenvoudig te gebruiken is, maar krachtig onder de motorkap.

---

## ✨ Features

- REST API (Flask) om e-mailadressen te scannen
- Genereert unieke `scan_id` en JSON-resultaten
- Resultaten worden lokaal opgeslagen in `scans/`
- Simpele frontend (HTML + JavaScript) inbegrepen
- Voorbereid op uitbreiding naar echte OSINT-integraties

---

## 🧱 Bestandsoverzicht
ghostprint/
├── main.py # Flask backend
├── index.html # Eenvoudige frontend
├── scans/ # Output map met scanresultaten (.json)
├── .gitignore
├── README.md
└── requirements.txt # (optioneel, zie onder)

text

---

## 🚀 Installatie

### 1. Clone het project

```bash
git clone https://github.com/jouwgebruikersnaam/ghostprint.git
cd ghostprint
2. Start een virtuele omgeving
bash
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  ← macOS/Linux
3. Installeer vereisten
bash
pip install flask
(of gebruik: pip install -r requirements.txt als die aanwezig is)
▶️ API Gebruiken
Start de server:

bash
python main.py
POST /api/scan

text
URL: http://127.0.0.1:5000/api/scan
Headers: Content-Type: application/json
Body:
json
{
  "email": "jan@example.com"
}
Response:

json
{
  "scan_id": "uuid-...",
  "result": {
    "email": "jan@example.com",
    "accounts_found": [
      "github.com/jan",
      "linkedin.com/in/jan"
    ],
    "status": "completed"
  }
}
🌐 Frontend gebruiken
Open index.html in je browser

Vul een e-mailadres in

Bekijk het gesimuleerde resultaat

Gebruik eventueel de Live Server extensie in VSCode voor gemak.

🛣️ Roadmap (toekomst)
✅ MVP met fake resultaten

🔍 Integratie met Sherlock voor OSINT-scan

📁 Downloadbare rapporten (PDF, CSV)

🔒 Gebruikersauthenticatie

🌍 Gehoste SaaS-versie met dashboard

⚖️ Licentie
MIT License — vrij te gebruiken, aan te passen en commercieel in te zetten.
Zie het LICENSE-bestand voor details.
