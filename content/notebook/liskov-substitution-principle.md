---
created: 2026-02-05
last updated: 2026-09-12
publish: true
title: Liskov Substitution Principle
---

# Liskov Substitution Principle (LSP)

Siehe: [[SOLID]], [[Programmierung]]

Objekte einer Subklasse müssen sich überall dort einsetzen lassen, wo ein Objekt der Superklasse erwartet wird, ohne dass sich das Programmverhalten in unerwarteter Weise ändert oder Fehler auftreten.

Formuliert von [[Barbara Liskov]] (1987). Es genügt also nicht, dass eine Subklasse rein syntaktisch die Signatur der Superklasse erfüllt (z.B. via [[Vererbung]]) – sie muss auch deren *Verhaltensvertrag* einhalten: gleiche Vorbedingungen (nicht strenger), gleiche Nachbedingungen (nicht schwächer), keine neuen Exceptions, die der Aufrufer nicht erwartet.

**Klassisches Beispiel:** `Quadrat` als Subklasse von `Rechteck` erscheint naheliegend, verletzt aber LSP: Setzt man bei einem `Rechteck` Breite und Höhe unabhängig voneinander, würde ein `Quadrat` (bei dem Breite = Höhe gelten muss) eine der beiden Eigenschaften implizit mitändern – ein Aufrufer, der nur `Rechteck` kennt, erhält dadurch unerwartetes Verhalten.

Verletzungen dieses Prinzips zeigen sich oft durch Type Checks (`if (obj instanceof X)`) im aufrufenden Code oder durch Subklassen, die geerbte Methoden mit leerem Body oder geworfenen Exceptions überschreiben.

---

- ↩
	- …