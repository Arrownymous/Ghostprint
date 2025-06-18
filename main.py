from flask import Flask, request, jsonify
import os
import uuid
import json

app = Flask(__name__)

# Zorg dat er een map is om scans in op te slaan
SCAN_DIR = "./scans"
os.makedirs(SCAN_DIR, exist_ok=True)

@app.route("/api/scan", methods=["POST"])
def scan():
    try:
        data = request.get_json()

        email = data.get("email")
        if not email:
            return jsonify({"error": "Email is verplicht"}), 400

        # Maak unieke scan ID en output pad
        scan_id = str(uuid.uuid4())
        output_file = os.path.join(SCAN_DIR, f"{scan_id}.json")

        # Nep scanresultaat (fake OSINT)
        fake_result = {
            "email": email,
            "accounts_found": [
                f"github.com/{email.split('@')[0]}",
                f"linkedin.com/in/{email.split('@')[0]}"
            ],
            "status": "completed"
        }

        # Sla resultaat op als JSON-bestand
        with open(output_file, "w") as f:
            json.dump(fake_result, f)

        # Geef resultaat terug
        return jsonify({"scan_id": scan_id, "result": fake_result})

    except Exception as e:
        return jsonify({"error": "Serverfout", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

