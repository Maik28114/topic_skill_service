#### 1.Importieren benötigter Module ####
import json # Zum Verarbeiten von JSON-Dateien(einlesen und schreiben)
import os   #  # Zum Arbeiten mit Dateipfaden und Dateisystemen(Pfade erstellen)
from flask import Flask, jsonify # Flask: Web-Framework für Python, jsonify: Umwandlung in eine JSON-Antwort.

#### 2. Flask-Anwendung initialisieren ####
app = Flask(__name__) 
# Erstellt eine Flask-App-Instanz mit dem aktuellen Dateinamen.
# Flask braucht dieses Objekt, um HTTP-Anfragen verarbeiten zu können (z.B. GET, POST).

#### 3. Pfade für die Daten festlegen ####
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data') 
# DATA_DIR ist der Pfad zum Ordner "data", basierend auf dem Ort der aktuellen Datei.
# os.path.dirname(__file__) gibt das Verzeichnis der aktuellen Datei zurück.
# os.path.join(...) fügt 'data' an diesen Pfad an.
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json') 
# TOPICS_FILE ist der komplette Pfad zur Datei "topics.json" im DATA_DIR-Ordner.

#### 4. Startseite definieren (Root-Route "/") ####
@app.route('/')
def hello_world():
    return 'Hello from Topic and Skill Service!'
# Wenn jemand die Startseite ("/") der Webanwendung aufruft,
# wird dieser Text im Browser angezeigt.

#### 5. Funktion zum Lesen einer JSON-Datei definieren ####
def read_json_file(filepath):
    if not os.path.exists(filepath):
        return []
        # Wenn die angegebene Datei nicht existiert, gib eine leere Liste zurück.


    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
            # Öffnet die Datei im Lesemodus mit UTF-8-Kodierung.
            # json.load(file) liest die Datei und wandelt sie in Python-Objekte (z. B. Liste oder Dictionary) um.       
    except json.JSONDecodeError:
        print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
  




