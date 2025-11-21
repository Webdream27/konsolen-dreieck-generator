""" *********************************************
Aufgabe 5 Gleichschenkliges Dreieck mit Sternchen
**********************************************""" 

# Eingabe der Hoehe mit Validierung, um sicherzustellen, dass es eine positive Ganzzahl ist
while True:
    try:
        hoehe = int(input("Geben Sie die Hoehe des Dreiecks (positive Ganzzahl) ein: "))
        if hoehe > 0:
            break # Schleife verlassen, wenn die Eingabe gueltig ist
        else:
            print("Die Hoehe muss groesser als Null sein.")
    except ValueError:
        print("Ungueltige Eingabe. Bitte geben Sie eine Ganzzahl ein.")

print("\n--- Dreieck-Ausgabe ---")

# Aufbau des Dreiecks, Zeile für Zeile
# i laeuft von 0 bis hoehe-1
for i in range(hoehe):
    # 1. Berechnung der benoetigten Leerzeichen am Anfang der Zeile
    # Die Leerzeichen nehmen von der Spitze zur Basis ab (von hoehe-1 bis 0)
    anzahl_leerzeichen = hoehe - 1 - i

    # 2. Berechnung der benoetigten Sternchen in der Zeile
    # Die Sternchenanzahl ist immer ungerade (1, 3, 5, ...)
    # Formel: 2 * i + 1
    anzahl_sternchen = 2 * i + 1

    # Erstellung der Teilstrings
    leerzeichen = " " * anzahl_leerzeichen
    sternchen = "*" * anzahl_sternchen

    # 3. Ausgabe der kompletten Zeile
    print(leerzeichen + sternchen)


