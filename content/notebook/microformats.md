---
created: 2026-05-31
last updated: 2026-10-14
publish: true
title: Microformats
---

# Microformats

Siehe: [[Semantic Web]], [[HTML]]

Lightweight Ansatz (ab ca. 2005), semantische Bedeutung direkt über bereits existierende [[HTML]]-Attribute (primär `class`) auszudrücken, statt eine neue Syntax einzuführen. Man nutzt also normales HTML, hält sich aber an eine informelle Namenskonvention, sodass Software (z.B. Browser-Erweiterungen, [[Search Engines|Suchmaschinen]]) die Struktur erkennen kann.

Bekannte/zentrale Formate: ([microformats2](https://microformats.org/2014/03/05/getting-started-with-microformats2))
- [`h-card`](https://microformats.org/wiki/h-card): Personen-/Kontaktdaten, mit verschiedenen Properties:
	- `p-name` (auch `p-given-name`, `p-nickname`, etc.)
	- `u-email`
	- `u-logo`
	- `p-tel` (z.B.: `<span class="p-tel">+49 30 123456</span>`)
	- …
- [`h-feed`](https://microformats.org/wiki/h-feed): für “list” pages, die einzelne entries auflisten
	- `p-name`: Name des feeds
	- `p-author`
	- `u-url`
	- `u-photo`
	- …
- [`h-entry`](https://microformats.org/wiki/h-entry): für die einzelnen entries, also content wie blogposts, Properties:
	- `p-name`: Name des Eintrags
	- `p-summary`
	- `e-content`: Vollständiger content
	- `dt-published`
	- `dt-updated`
	- `p-author`
	- `p-category`
	- …
- `h-calendar`: Termine/Events
- `h-review`: Bewertungen
- …

Speziell für [[Hyperlinks]]:
- `rel="tag"`: [[Tags]]
- `rel="me"`: Links zu anderen/externen Seiten, die auch zu dir gehören (z.B. [[Social Media]]-Profile)
- …

Eng verwandt ist das Prinzip **POSH** (*Plain Old Semantic HTML*): einfach die bereits existierenden, semantisch sinnvollen [[HTML]]-Elemente korrekt verwenden (`<article>`, `<time>`, `<address>` statt generischen `<div>`s mit [[CSS]]-Klassen). Microformats bauen im Grunde auf diesem POSH-Gedanken auf und erweitern ihn um zusätzliche Konventionen für Fälle, die reines HTML nicht abdeckt.

Vorteil gegenüber [[RDFa]]/[[Microdata]]: sehr niedrige Einstiegshürde, kein zusätzliches Vokabular-System nötig. Nachteil: informelle, community-getriebene Spezifikation statt offiziellem [[W3C]]-Standard, dadurch weniger Robustheit/Eindeutigkeit bei komplexeren Datenstrukturen.

Siehe auch: [[Microdata]], [[RDFa]]

---

- ↩
	- [Wikipedia](https://de.wikipedia.org/wiki/Mikroformat)
	- [Microformats Wiki](https://microformats.org/wiki/Main_Page)
		- Eintrag: [POSH](https://microformats.org/wiki/posh)
	- Siehe auch: [Markup Validation Service](https://validator.w3.org/)