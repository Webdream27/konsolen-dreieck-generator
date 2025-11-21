# Gleichschenkliges Dreieck (Sternchen-Generator)

Ein Python-Algorithmus zur visuellen Ausgabe geometrischer Formen in der Konsole.

## Aufgabenstellung
Entwicklung eines Programms, das:
1.  Die Höhe eines Dreiecks vom Benutzer einliest.
2.  Ein **gleichschenkliges Dreieck** aus Sternchen (`*`) auf dem Bildschirm ausgibt.
3.  Die Formatierung (Zentrierung) korrekt berechnet.

## Technische Umsetzung
Der Code demonstriert das Verständnis von Schleifen und String-Manipulation:
*   **Input-Validierung:** Sicherstellung, dass nur positive Ganzzahlen verarbeitet werden.
*   **Algorithmus:** Berechnung der Form in einer Schleife:
    *   **Zentrierung:** Die Anzahl der vorangestellten Leerzeichen nimmt pro Zeile ab (`höhe - 1 - i`).
    *   **Breite:** Die Anzahl der Sternchen erhöht sich pro Zeile immer um 2 (ungerade Zahlen: 1, 3, 5...), realisiert durch die Formel `2 * i + 1`.
*   **String-Multiplikation:** Effiziente Erstellung der Zeilen durch Python-Syntax (z.B. `" " * n`).

## Nutzung
Führen Sie das Skript in der Konsole aus:

```bash
python main.py
