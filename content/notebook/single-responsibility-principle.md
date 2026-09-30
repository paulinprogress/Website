---
created: 2026-02-05
last updated: 2026-09-12
publish: true
title: Single-Responsibility Principle
---

# Single-Responsibility Principle (SRP)

Siehe: [[SOLID]], [[Programmierung]]

Eine Klasse sollte nur einen einzigen Grund haben, sich zu ändern – also genau eine [[Verantwortung|Verantwortlichkeit]] (*responsibility*) besitzen.

"Verantwortlichkeit" meint hier nicht "eine Methode", sondern einen fachlichen Zuständigkeitsbereich bzw. einen Änderungstreiber. Enthält eine Klasse mehrere solcher Zuständigkeiten, führt eine Änderung an einer davon dazu, dass auch die andere(n) ungewollt betroffen sein können.

**Beispiel:** Eine Klasse `Rechnung`, die sowohl 1) Rechnungsbeträge berechnet als auch 2) die Rechnung als [[PDF]] formatiert und 3) in eine [[Databases|Datenbank]] speichert, hat drei Verantwortlichkeiten und drei unabhängige Gründe für Änderungen (Berechnungslogik, Layout, Speicherformat). Besser: drei separate Klassen (`RechnungsBerechnung`, `RechnungsFormatter`, `RechnungsRepository`), die jeweils nur von einem dieser Aspekte betroffen sind.

Ziel: [[Low Coupling, High Cohesion]], bessere Testbarkeit – Änderungen an einem fachlichen Aspekt bleiben lokal begrenzt.

---

- ↩
	- …