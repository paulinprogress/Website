---
created: 2026-05-31
last updated: null
publish: true
title: Microdata
---

# Microdata

Siehe: [[Semantic Web]], [[HTML]]

[[HTML]]5-Spezifikation ([WHATWG](https://whatwg.org/)) zum Einbetten strukturierter, maschinenlesbarer Daten direkt in bestehende HTML-Elemente über eine Reihe zusätzlicher Attribute:

- `itemscope` – markiert ein Element als Container für ein strukturiertes "Item" (z.B. eine Person, ein Produkt)
- `itemtype` – verweist per [[URL]] auf ein Vokabular, das definiert, welche Eigenschaften erlaubt sind (meist [Schema.org](https://schema.org/))
- `itemprop` – markiert innerhalb des Items einzelne Eigenschaften (z.B. `name`, `price`)

Beispiel:
```html
<div itemscope itemtype="https://schema.org/Person">
  <span itemprop="name">Max Mustermann</span>
</div>
```

Im Unterschied zu [[Microformats]] ist Microdata offizieller HTML-Standard mit klar definierter Attribut-Syntax statt informeller `class`-Konventionen – dadurch strenger spezifiziert, aber auch etwas ausführlicher im Markup. In der Praxis heute der häufigste Weg, [Schema.org](https://schema.org/)-Daten einzubetten, neben JSON-LD (das die Daten separat als Skript-Block statt inline im Markup einbettet und mittlerweile von Google klar bevorzugt wird).

Siehe auch: [[RDFa]], [[Microformats]]

---

- ↩
	- [WHATWG - Microdata](https://html.spec.whatwg.org/multipage/microdata.html#microdata)