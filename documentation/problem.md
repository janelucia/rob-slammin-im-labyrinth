# Problemdefinition

2 Probleme, zum einen der Roboter, der durch das Labyrinth fährt und seine Erkenntnisse an die KI schickt. 
Zum anderen die KI, die das Labyrinth kartografiert, den kürzesten Weg zwischen farbigen Tiles berechnet und den Roboter navigiert.

## Problem Roboter
**Zustandsraum**: 
 - Ein Labyrinth, welches aus Quadraten besteht, welche zwischen 0 und 4 Wänden haben kann und einen farbigen oder farblosen Boden haben können. 
 - Dazu einem Roboter, der sich darin bewegen kann, sich zu jeder Zeit im Labyrinth befindet und eine bestimmte Ausrichtung hat.

**Startzustand**:
**Bewegung**:
- Vorwärts: Der Roboter bewegt sich vorwärts, falls keine Wand im Weg ist.
- Rückwärts: Der Roboter bewegt sich rückwärts, falls keine Wand im Weg ist.

**Rotation**:
- Links drehen: Der Roboter dreht sich um 90° nach links.
- Rechts drehen: Der Roboter dreht sich um 90° nach rechts.

**Sensoraktionen**:
- Entfernungsbestimmung: Der Roboter misst die Entfernung zur nächsten Wand in eine Richtung.
- Farberkennung: Der Roboter erkennt die Farbe des Tiles unter ihm.

**Zielzustand**: 
- der Roboter hat alle Quadrate des Labyrinths, die er erreichen kann, befahren.

**Kosten**: 
- Bewegungskosten: konstante Kosten für jede Bewegung (B.: Energieverbrauch)
- Strafen: Läuft der Roboter gegen eine Wand, entstehen zusätzliche Kosten, da er sich zurückbewegen und neu ausrichten muss.

## Problem KI zur Labyrinthkartografierung
**Zustandsraum**: 
- Ein Labyrinth, welches aus Quadraten besteht, welche zwischen 0 und 4 Wänden haben kann und einen farbigen oder farblosen Boden haben können.
- ein vollständiger Zustand: 
  - aktuelle Karte des Labyrinths (Position der Wände und Farben der Böden)
  - Standort des Roboters (momentanes Quadrat und Orientierung)

**Startzustand**: 
- Leere Karte
- momentaner Standort des Roboters

**Aktionen**:

Kartografieren:
- Aktualisierung der Karte basierend auf Sensordaten des Roboters.

Pfadberechnung:
- Berechnung des kürzesten Weges zwischen farbigen Quadraten oder zwischen dem aktuellen Standort und einem Ziel.

Navigation:
- Senden von Steuerkommandos an den Roboter (z. B. vorwärts, links drehen).

**Zielzustand**: 
- Die Karte des Labyrinths ist vollständig erstellt, bestehend aus allen Quadraten, die erreichbar sind.
- Alle farbigen Quadrate wurden in der Karte markiert.
- Der kürzeste Weg zwischen farbigen Quadraten ist bekannt.

**Kosten**:
- Rechenzeit: Berechnung des kürzesten Weges.
- Speicherverbrauch: Speicherung und Aktualisierung der Karte.
