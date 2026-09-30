---
created: 2026-01-27
last updated: null
publish: true
title: MVVM
---

# Model-View-ViewModel (MVVM)

Siehe: [[Software Development]]

Pattern, um [[UI Design|UI]] (“Views”) von Backend-Logik (“Models”) zu entkoppeln, mit “ViewModels” als Vermittler. Ähnlich wie [[MVC]], aber speziell für Desktop-Anwendungen.

Vorteile:
- UI weiß nichts von der Database
- Logik ist testable ohne UI
- Mehrere Views können dasselbe ViewModel verwenden
- Alles automatisch synchronisiert durch Data Binding

---

- ↩
	- …