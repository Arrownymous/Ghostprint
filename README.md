# Ghostprint 🕵️‍♂️🧩

Ghostprint is een nieuwe open source tool die je digitale voetafdruk inzichtelijk maakt — gericht op privacy, veiligheid en transparantie. Of je nu journalist, activist, onderzoeker of gewoon privacybewust bent: Ghostprint helpt je te begrijpen waar jouw gegevens (mogelijk) online zichtbaar zijn.

> 🚧 Deze tool is in actieve ontwikkeling. De huidige versie is een werkende MVP die gebruikmaakt van gesimuleerde scanresultaten. Toekomstige versies zullen geavanceerde OSINT-scans uitvoeren, integraties bieden met tools zoals Sherlock, en een veilig gebruikersdashboard bevatten.

---

## 🎯 Doel van dit project

Ghostprint wil een **eenvoudige, veilige en effectieve** manier bieden om iemands digitale blootstelling te controleren — beginnend bij e-mailgebaseerde OSINT-scans. Het uiteindelijke doel is een platform waarmee gebruikers:

- Online profielen kunnen opsporen
- Digitale sporen kunnen analyseren of verwijderen
- Bewust keuzes kunnen maken over hun privacy

---

## 🧱 MVP Features

- ✅ Eenvoudige REST API (`/api/scan`)
- ✅ JSON-rapportage op basis van e-mailadres
- ✅ Unieke `scan_id` per sessie
- ✅ Bestandsopslag van resultaten in `/scans`
- ✅ Frontend met HTML en JavaScript voor basisgebruik

---

## 📦 Projectstructuur
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
venv\Scripts\activate     (voor Windows)
source venv/bin/activate  (voor macOS/Linux)

3. Installeer vereisten

pip install flask

(of gebruik: pip install -r requirements.txt als die aanwezig is)

## API gebruiken

Start de server:

python main.py

POST /api/scan

URL: http://127.0.0.1:5000/api/scan
Headers: Content-Type: application/json
Body:

{
  "email": "jan@example.com"
}

Response:

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

- MVP met fake resultaten
- Integratie met Sherlock voor OSINT-scan
- Downloadbare rapporten (PDF, CSV)
- Gebruikersauthenticatie
- Gehoste SaaS-versie met dashboard

## Licentie

MIT License — vrij te gebruiken, aan te passen en commercieel in te zetten.
Zie het LICENSE-bestand voor details.

## .gitignore

Zorg dat je deze mappen uitsluit in .gitignore:

__pycache__/
*.pyc
venv/
scans/
.vscode/
.env

Als scans/ al in Git zat, verwijder die zo:

git rm -r --cached scans/
git commit -m "Verwijder scanresultaten uit versiebeheer"

## Gemaakt door

Stijn Schoonderwoerd
Contact via GitHub of LinkedIn

"In een wereld waarin alles online blijft, helpt Ghostprint je om weer even onzichtbaar te worden."

