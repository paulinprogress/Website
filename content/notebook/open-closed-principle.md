---
created: 2026-02-05
last updated: 2026-09-12
publish: true
title: Open-Closed Principle
---

# Open/Closed Principle (OCP)

Siehe: [[SOLID]], [[Programmierung]]

Software-Einheiten (Klassen, Module, Funktionen) sollten offen für Erweiterung, aber geschlossen für Modifikation sein.

Heißt: neues Verhalten sollte durch **Hinzufügen** von Code möglich sein, nicht durch **Ändern** von bereits bestehendem, funktionierendem Code. Bestehender Code, der bereits getestet und in Benutzung ist, wird dadurch nicht immer wieder angefasst und mit neuen Fehlerquellen belastet.

**Beispiel:** Eine Funktion `berechneFlaeche(form)` mit einer if/else-Kette für `Kreis`, `Rechteck`, `Dreieck` muss bei jeder neuen Form erweitert werden. Definiert man stattdessen ein [[Interfaces|Interface]] `Form` mit einer Methode `flaeche()`, kann jede neue Form als eigene Klasse implementiert werden, die dieses Interface erfüllt – die aufrufende Logik bleibt unverändert.

Technisch meist über Abstraktion (Interfaces/Abstrakte Klassen) und [[Polymorphismus]] realisiert: neues Verhalten = neue Implementierung einer bestehenden Abstraktion, statt Änderung an zentraler Logik.

---

- ↩
	- …