---
created: 2026-05-31
last updated: null
publish: true
title: Microformats
---

# Microformats

Siehe: [[Semantic Web]], [[HTML]]

Lightweight Ansatz (ab ca. 2005), semantische Bedeutung direkt über bereits existierende [[HTML]]-Attribute (primär `class`) auszudrücken, statt eine neue Syntax einzuführen. Man nutzt also normales HTML, hält sich aber an eine informelle Namenskonvention, sodass Software (z.B. Browser-Erweiterungen, [[Search Engines|Suchmaschinen]]) die Struktur erkennen kann.

Beispiel: `<span class="tel">+49 30 123456</span>` markiert eine Telefonnummer nach dem `hCard`-Microformat (Personen-/Kontaktdaten, angelehnt an den [[vCard]]-Standard). Weitere bekannte Formate: `hCalendar` (Termine/Events, angelehnt an [[iCalendar]]), `hReview` (Bewertungen), `rel="tag"` ([[Tags|Tagging]]).

Eng verwandt ist das Prinzip **POSH** (*Plain Old Semantic HTML*): einfach die bereits existierenden, semantisch sinnvollen HTML-Elemente korrekt verwenden (`<article>`, `<time>`, `<address>` statt generischer `<div>`s mit [[CSS]]-Klassen). Microformats bauen im Grunde auf diesem POSH-Gedanken auf und erweitern ihn um zusätzliche Konventionen für Fälle, die reines HTML nicht abdeckt.

Vorteil gegenüber [[RDFa]]/[[Microdata]]: sehr niedrige Einstiegshürde, kein zusätzliches Vokabular-System nötig. Nachteil: informelle, community-getriebene Spezifikation statt offiziellem [[W3C]]-Standard, dadurch weniger Robustheit/Eindeutigkeit bei komplexeren Datenstrukturen.

Siehe auch: [[Microdata]], [[RDFa]]

---

- ↩
	- [Wikipedia](https://de.wikipedia.org/wiki/Mikroformat)
	- [Microformats Wiki](https://microformats.org/wiki/Main_Page)
		- Eintrag: [POSH](https://microformats.org/wiki/posh)
	- Siehe auch: [Markup Validation Service](https://validator.w3.org/)