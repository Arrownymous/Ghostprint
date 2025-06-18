# Ghostprint 🕵️‍♂️

Ghostprint is een minimalistische open source tool waarmee je jouw digitale voetafdruk kunt scannen — gericht op privacy, veiligheid en bewustwording. Ideaal voor journalisten, onderzoekers of iedereen die controle wil over online aanwezigheid.

> 🚧 Deze tool is nog in ontwikkeling. De huidige MVP gebruikt gesimuleerde scanresultaten om de API en frontend werkend te testen. In de toekomst worden echte OSINT-scanners zoals Sherlock toegevoegd.

## Doel

Ghostprint helpt je te begrijpen waar jouw e-mailadres mogelijk online opduikt. Het uiteindelijke doel is een complete Zero-Trace Privacy Suite die eenvoudig te gebruiken is, maar krachtig onder de motorkap.

## Features

- REST API (Flask) om e-mailadressen te scannen
- Genereert unieke `scan_id` en JSON-resultaten
- Resultaten worden lokaal opgeslagen in `scans/`
- Simpele frontend (HTML + JavaScript) inbegrepen
- Voorbereid op uitbreiding naar echte OSINT-integraties

## Bestandsoverzicht

ghostprint/
├── main.py             # Flask backend
├── index.html          # Eenvoudige frontend
├── scans/              # Output map met scanresultaten (.json)
├── .gitignore
├── README.md
└── requirements.txt    # (optioneel, zie onder)

## Installatie

1. Clone het project

git clone https://github.com/jouwgebruikersnaam/ghostprint.git
cd ghostprint

2. Start een virtuele omgeving

python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # macOS/Linux

3. Installeer vereisten

pip install flask

(of gebruik: pip install -r requirements.txt als die aanwezig is)

## API gebruiken

Start de server:

python main.py

### POST /api/scan

**URL:** http://127.0.0.1:5000/api/scan  
**Headers:** Content-Type: application/json  
**Body:**

{
  "email": "jan@example.com"
}

**Response:**

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

## Frontend gebruiken

1. Open index.html in je browser  
2. Vul een e-mailadres in  
3. Bekijk het gesimuleerde resultaat  

Gebruik eventueel de Live Server extensie in VSCode voor gemak.

## Roadmap (toekomst)

- ✅ MVP met fake resultaten  
- 🔍 Integratie met Sherlock voor OSINT-scan  
- 📁 Downloadbare rapporten (PDF, CSV)  
- 🔒 Gebruikersauthenticatie  
- 🌍 Gehoste SaaS-versie met dashboard  

## Licentie

MIT License — vrij te gebruiken, aan te passen en commercieel in te zetten.  
Zie het LICENSE-bestand voor details.

## Gemaakt door

Stijn Schoonderwoerd  
Contact via GitHub of LinkedIn

> "In een wereld waarin alles online blijft, helpt Ghostprint je om weer even onzichtbaar te worden."
