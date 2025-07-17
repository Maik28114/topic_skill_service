import json
import os

# Importiert die notwendigen Module: json zum Arbeiten mit JSON-Dateien
# und os für Funktionen rund um das Dateisystem.
class JsonDataManager:

    def __init__(self):
        pass
# Initialisiert eine neue Instanz der Klasse. Hier werden aktuell keine Attribute gesetzt.

    def read_data(self, filepath):
        if not os.path.exists(filepath):
            return []
        # Überprüft, ob die Datei existiert. Falls nicht, wird eine leere Liste zurückgegeben.   
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
            # Öffnet und lädt die JSON-Datei. Gibt die gelesenen Daten zurück.
        except json.JSONDecodeError:
            print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
            return []
        # Gibt eine Fehlermeldung aus, wenn die Datei kein valides JSON enthält, und gibt eine leere Liste zurück.
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
            return []
        # Gibt bei allen anderen Fehlern ebenfalls eine Fehlermeldung und eine leere Liste zurück.


    def write_data(self, filepath, data):
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
# Erstellt den Verzeichnispfad für die Datei, falls dieser noch nicht existiert.
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
                return True
            # Schreibt die Daten als schön formatierte JSON-Datei. Gibt True zurück, wenn erfolgreich.
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten beim Schreiben von {filepath}: {e}")
            return False
        # Gibt bei Fehlern beim Schreiben eine Fehlermeldung und False zurück.



