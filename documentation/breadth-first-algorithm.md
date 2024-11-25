# Breitensuche

## Ziel:

- Systematische Erkundung des Labyrinths.
- Geeignet für vollständige Kartographierung oder das Finden eines bestimmten Ziels (z. B. Ausgang).

## Umsetzung:

1. Repräsentation des Labyrinths:

- Eine 2D-Matrix (z. B. grid[x][y]) speichert Informationen über Wände und besuchte Felder.
- Felder können die Zustände "unerforscht", "besucht" oder "Wand" haben.

2. Repräsentation von Roboter: Wo befindet er sich gerade im Labyrinth -> einfach die neueste Tile ist der momentane Standort vom Roboter
3. Datenstruktur:

- Eine Warteschlange speichert die Positionen, die als nächstes untersucht werden sollen.

4. Breitensuche machen
5. Integration mit Sensoren:

- Der Roboter bewegt sich in kleinen Schritten und prüft mit dem Infrarotsensor Hindernisse.
- Bei jedem Schritt aktualisiert er die Karte (grid) und fügt neue erreichbare Positionen in die Warteschlange ein.

## Vorteile:

- Systematische Erkundung.
- Garantiert vollständige Kartographierung.

## Herausforderung:

- Speicherbedarf steigt mit der Labyrinthgröße.
