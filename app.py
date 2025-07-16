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
        return []
        # Falls die Datei zwar existiert, aber fehlerhafte JSON-Syntax hat:
        # Zeige eine Fehlermeldung an und gib eine leere Liste zurück.
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
        return []
        # Jede andere Art von Fehler (z. B. Zugriffsfehler):
        # Gib eine Fehlermeldung aus und gib ebenfalls eine leere Liste zurück.


#### 6. Route "/topics" definieren: Gibt Themen zurück ####
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = read_json_file(TOPICS_FILE)
    # Liest den Inhalt der Datei "topics.json" anhand des zuvor definierten Pfades.
    return jsonify(topics)
    # Verpackt die eingelesenen Daten in eine JSON-Antwort und sendet sie an den Client (z. B. Browser oder API-Nutzer).

#### 7. Startpunkt der Anwendung ####
if __name__== '__main__':
    app.run(debug=True, port=5000)
    # Wenn dieses Skript direkt ausgeführt wird (nicht importiert),
    # wird der Webserver gestartet:
    # - Im Debug-Modus (zeigt Fehler im Browser, nützlich für Entwicklung),
    # - auf Port 5000 (Standardport für lokale Flask-Apps)




