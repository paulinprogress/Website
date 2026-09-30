---
created: 2026-02-05
last updated: 2026-09-12
publish: true
title: Dependency Inversion Principle
---

# Dependency Inversion Principle (DIP)

Siehe: [[SOLID]], [[Programmierung]]

Module höherer Abstraktionsebene sollten nicht von Modulen niedrigerer Abstraktionsebene abhängen – beide sollten stattdessen von Abstraktionen (z.B. [[Interfaces]]) abhängen. Zusätzlich: Abstraktionen sollten nicht von Details abhängen, sondern Details von Abstraktionen.

"Höhere Ebene" meint hier fachliche/orchestrierende Logik (z.B. `Bestellservice`), "niedrigere Ebene" meint konkrete technische Implementierungen (z.B. `MySQLDatenbank`, `SMTPMailversand`). Ohne dieses Prinzip hängt fachlicher Code direkt an konkreten technischen Details – ein Wechsel der Technologie (z.B. andere [[Databases|Datenbank]]) erzwingt dann Änderungen an der fachlichen Logik selbst.

**Beispiel:** `Bestellservice` sollte nicht direkt `MySQLDatenbank` instanziieren, sondern von einem Interface `Datenspeicher` abhängen. `MySQLDatenbank` implementiert dieses Interface. `Bestellservice` kennt damit nur die Abstraktion – welche konkrete Implementierung tatsächlich verwendet wird, wird von außen übergeben (siehe [[Dependency Injection]]).

Wichtig: **Dependency Inversion ≠ [[Dependency Injection]]** – Injection ist eine gängige *Technik*, um Inversion praktisch umzusetzen (Abhängigkeiten werden von außen "injiziert" statt selbst erzeugt), aber nicht zwingend dasselbe Konzept.

Siehe auch: [[Inversion of Control]]

---

- ↩
	- …