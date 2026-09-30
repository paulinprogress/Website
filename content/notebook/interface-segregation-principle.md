---
created: 2026-02-05
last updated: 2026-09-12
publish: true
title: Interface Segregation Principle
---

# Interface Segregation Principle (ISP)

Siehe: [[SOLID]], [[Programmierung]]

Klassen sollten nicht gezwungen sein, von [[Interfaces]] abzuhängen, die sie nicht nutzen. Statt eines großen, universellen Interfaces sind mehrere kleine, spezifische Interfaces vorzuziehen, die jeweils nur die für einen bestimmten Client relevanten Methoden enthalten.

Ein "fettes" Interface zwingt implementierende Klassen dazu, auch Methoden zu implementieren, die für sie fachlich irrelevant sind (oft mit leerem Body oder geworfener Exception als Behelf) – ein Hinweis, dass eigentlich mehrere Rollen in einem Interface vermischt wurden.

**Beispiel:** Ein Interface `Arbeiter` mit den Methoden `arbeiten()` und `essenPause()` zwingt eine Klasse `Roboter`, auch `essenPause()` zu implementieren, obwohl das für einen Roboter keinen Sinn ergibt. Besser: getrennte Interfaces `Arbeitend` und `Pausierend`, die `Mensch` beide implementiert und `Roboter` nur `Arbeitend`.

Ziel: Clients sind nur von dem abhängig, was sie tatsächlich brauchen – Änderungen an nicht genutzten Teilen eines Interfaces wirken sich dadurch nicht auf sie aus.

---

- ↩
	- …