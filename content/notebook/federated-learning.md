---
created: 2026-10-01
last updated: null
publish: true
title: Federated Learning
---

# Federated Learning (FL)

Siehe: [[Machine Learning]], [[Informationstechnik & Infrastruktur]], [[Privatsphäre & Datenschutz]]

Trainingsansatz für ML-Modelle, bei dem die Trainingsdaten nicht zentral gesammelt, sondern [[Dezentralisierung|dezentral]] an den jeweiligen Endpunkten (z.B. Smartphones, Krankenhäuser, Banken) belassen werden. Statt Daten an einen zentralen [[Server]] zu schicken, wird lokal trainiert und nur die aktualisierten Modellparameter zurückgeschickt – die Rohdaten verlassen das Gerät nie. (Siehe auch: [[Edge Computing]])

Motivation:

- Daten sind oft von Natur aus verteilt: zwischen Organisationen (Gesundheitswesen, Behörden, Finanzen, Fertigung) oder zwischen Endgeräten (PC, Handy, Laptop)
- Teils rechtliche/praktische Gründe, Daten gar nicht erst zentral sammeln zu dürfen/wollen ([[Privatsphäre & Datenschutz|Datenschutz]], regulatorische Auflagen), aber auch technische Gründe, warum das nicht möglich ist
- Außerdem: Im Kontext der Diskussion, dass wir ggf. nicht mehr genügend neue Trainingsdaten für [[Large Language Models|LLMs]] haben: die geschätzte Menge an privaten E-Mails/Textnachrichten übersteigt alle sonst für LLM-Training verfügbaren Daten um ein Vielfaches → demonstriert das Potenzial von FL

Ablauf (ein Trainingszyklus):

1. **Initialization** – Server initialisiert ein globales Modell
2. **Communication round** – Server schickt das globale Modell an teilnehmende Clients. Eine sehr hohe Clientzahl pro Runde hat diminishing returns; im Mobile-Kontext werden z.B. oft nur ~100 zufällig ausgewählte Clients pro Runde einbezogen
3. **Client training & model update** – jeder Client trainiert das erhaltene Modell auf seinem lokalen Datensatz und schickt nur das aktualisierte Modell zurück
4. **Model aggregation** – der Server aggregiert die eingehenden Updates über einen Aggregations[[Algorithmen|algorithmus]] (z.B. **FedAvg**, **QFedAvg**, **FedAdam**) zu einem neuen globalen Modell
5. **Convergence check** – sind die Konvergenzkriterien erfüllt, endet der Prozess; sonst zurück zu Schritt 2

[[Privatsphäre & Datenschutz|Privacy]] & [[Cybersecurity]]: Trotz des Grundprinzips ("Daten bleiben lokal") ist FL nicht automatisch sicher – die übermittelten Modell-Updates können selbst Rückschlüsse auf die Trainingsdaten erlauben. Mögliche Angreifer können sein: 1) ein teilnehmender Client, 2) der Server selbst, 3) externe Dritte. Wichtige Angriffsklassen:

- **Member Inference Attack** – Rückschluss, ob ein bestimmter Datenpunkt am Training beteiligt war
- **Attribute Inference Attack** – Rückschluss auf nicht beobachtete Attribute der Trainingsdaten
- **Reconstruction Attack** – Rekonstruktion konkreter Trainingsdaten-Samples (z.B. Data-Reconstruction-Angriff durch einen böswilligen Server, Wang et al. 2018)

Gängige Gegenmaßnahme: [[Differential Privacy]] (DP) – in FL konkret über zwei Mechanismen:

- **Clipping** – begrenzt die Sensitivity (maximale Veränderung des Outputs durch Hinzufügen/Entfernen eines einzelnen Datenpunkts) und dämpft den Einfluss von Ausreißern
- **Noising** – fügt kalibriertes Rauschen hinzu, um den Output statistisch ununterscheidbar zu machen

Je nachdem, wo dies ansetzt:

- **Central DP** – Server clippt die eingehenden Client-Updates und fügt dem aggregierten globalen Modell Rauschen hinzu (setzt Vertrauen in den Server voraus)
- **Local DP** – jeder Client führt Clipping & Noising bereits lokal durch, bevor das Update überhaupt den Server erreicht (kein Serververtrauen nötig, dafür i.d.R. schlechtere Modellqualität bei gleichem Privacy-Budget)

Bandbreite: Durch die Größe von komplexen Modellen kann schnell eine große Bandbreite erreicht werden. Grobe Formel für den Kommunikationsaufwand: `(Modellgröße out + Modellgröße in) × Kohortengröße × ausgewählter Anteil × Anzahl Runden`. Ansätze zur Reduktion:

- **Update-Größe reduzieren**: Sparsification (nur Gradienten über einem Schwellenwert kommunizieren), Quantization (weniger Bits pro Skalar)
- **Seltener kommunizieren**: vortrainierte Modelle als Ausgangspunkt (ggf. nur bestimmte Layer trainieren/übertragen), mehr lokale Epochen vor jedem Senden (Risiko: kann Konvergenz behindern)

Implementierung/[[Programmierung]]: [[Open Source]]-Frameworks wie **[[Flower]]**, **[[NVIDIA FLARE]]**, **OpenFL**, **Substra**, **PySyft**/**PyGrid** – i.d.R. in Kombination mit gängigen ML-Frameworks wie [[PyTorch]] oder [[TensorFlow]].

---

- ↩
	- (Alexander Jung, 2025) Federated Learning - From Theory to Practice ([Weblink](https://github.com/alexjungaalto/FederatedLearning/blob/main/FLBook.pdf))
	- [(DeepLearning.AI) Intro to Federated Learning](https://www.deeplearning.ai/courses/intro-to-federated-learning)
	- [(Apheris, 2024) Top 7 Open-Source Frameworks for Federated Learning](https://www.apheris.com/resources/top-7-open-source-frameworks-for-federated-learning)