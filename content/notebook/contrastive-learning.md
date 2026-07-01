---
created: 2024-04-26
last updated: 2025-12-09
publish: true
title: Contrastive Learning
---

# Contrastive Learning

Ein [[Machine Learning]]-Verfahren, bei dem latente Repräsentation von Eingangsdaten erlernt werden (siehe: [[Representation Learning]]), und zwar so, dass ähnliche Daten im Repräsentationsraum möglichst nahe beieinander encodiert werden und unähnliche Daten möglichst weit entfernt voneinander. Dies hat sich als effektive Methode mit erstaunlicher [[Generalisierung|Generalisierungsfähigkeit]] und Robustheit gegenüber Adversarial Attacks erwiesen [[(Ran Liu, 2021) Understand and Improve Contrastive Learning Methods for Visual Representation - A Review|(Liu, 2021)]].

Während des Trainings werden Datenpunkte ausgewählt und mit positiven oder negativen Beispielen verglichen, indem Ähnlichkeitswerte im latenten Raum berechnet werden, z.B. als [[Cosine Similarity|Kosinus-Ähnlichkeiten]]. Die [[Verlustfunktionen|Verlustfunktion]] gibt dann ein Maß dafür, ob positive Paare (ähnliche Datenpunkte) tatsächlich hohe Ähnlichkeitswerte im latenten Raum aufweisen und ob negative Paare (unähnliche Datenpunkte) niedrigere Werte haben. Das Training ist in der Regel sehr rechenintensiv, da oft viele Beispiele gleichzeitig in einem Schritt verglichen werden.

>![[(Wang et al., 2022) MolCLR (t-SNE visualization).webp]]
>
>Besonders *fancy* Beispiel für einen mit CL erlernten Repräsentationsraum, visualisiert mit [[t-SNE]]. Aus: [Wang et al. (2021) - Molecular Contrastive Learning of Representations via Graph Neural Networks](https://arxiv.org/abs/2102.10056)

Contrastive Learning (CL) hat sich besonders im [[Unsupervised Learning|unüberwachten Lernen]] bewährt, obwohl es häufiger als [[Self-Supervised Learning|selbstüberwachtes Lernen]] bezeichnet wird, da die Kontrastierung der Daten in Form von Positiv- und Negativpaaren eine Art Selbstüberwachung darstellt.

In der unüberwachten / selbstüberwachten Form werden beim CL einzelne Instanzen unterschieden, d.h. jeder Datenpunkt wird effektiv als eine eigene “Klasse” betrachtet und von jedem anderen Datenpunkt unterschieden. Die dadurch erlernten Repräsentationen haben sich als viel genauer erwiesen als beim traditionellen [[Supervised Learning|überwachten Lernen]], wo sie ausschließlich für die Klassenunterscheidung optimiert sind [[(Keshtmand et al., 2022) Understanding the properties and limitations of contrastive learning for Out-of-Distribution detection|(Keshtmand et al., 2022)]]. Da die Methode nicht auf annotierte Daten angewiesen ist, kann sie ein sehr effizienter Ansatz sein, um Modelle vorzutrainieren, die sich durch [[Fine-tuning]] an spezifische Aufgaben anpassen können, während sie allgemeinere Merkmale lernen, die von der nachgelagerten Aufgabe unbeeinflusst sind [(Radford et al., 2021)](https://arxiv.org/abs/2103.00020). Einige bekannte Methoden sind:

- [[SimCLR]] (“Simple Framework for Contrastive Learning of Visual Representations”)
- [[MoCo]] (“Momentum Contrast”)
- [[BYOL]] (“Bootstrap Your Own Latent”)

Die positiven Beispiele werden in der Regel als [[Datenaugmentation|Augmentationen]] des ausgewählten Datenpunktes erzeugt, während als negative Beispiele zufällige andere Datenpunkte ausgewählt werden. Dies kann aber auch zu vielen “false negatives” führen (z. B. wenn zwei verschiedene Bilder von Hunden als genauso “unähnlich“ behandelt werden wie ein Bild von einem Hund und eines von einer Katze).

CL wurde auch für das [[Supervised Learning|überwachte Lernen]] angepasst. Hier wird nicht mehr jeder Datenpunkt als eigene Klasse betrachtet – stattdessen wird die “ground truth” Ähnlichkeit anhand der Klassenzugehörigkeiten bestimmt. Einige Modelle für das überwachte CL sind:

- [[SupCon]] (Supervised Contrastive Learning)
- [[GenSCL]] (Generalized Supervised Contrastive Learning)

---

- ↩
	- Umfassender Überblick: [Lil’Log - Contrastive Representation Learning](https://lilianweng.github.io/posts/2021-05-31-contrastive/)
	- Einige Methoden:
		- [[(Chen et al., 2020) A Simple Framework for Contrastive Learning of Visual Representations]] ([Weblink](https://arxiv.org/abs/2002.05709))
		- [[(Kalantidis et al., 2020) Hard Negative Mixing for Contrastive Learning]] ([Weblink](https://arxiv.org/abs/2010.01028))
		- [[(Khosla et al., 2020) Supervised Contrastive Learning]] ([Weblink](https://arxiv.org/abs/2004.11362))
		- [[(Jiang et al., 2022) Supervised Contrastive Learning with Hard Negative Samples]] ([Weblink](https://arxiv.org/abs/2209.00078))
		- [[(Tian et al., 2023) StableRep - Synthetic Images from Text-to-Image Models Make Strong Visual Representation Learners]] ([Weblink](https://arxiv.org/abs/2306.00984))
		- [[(Tian et al., 2023) Learning Vision from Models Rivals Learning Vision from Data]] ([Weblink](https://arxiv.org/abs/2312.17742))
		- [[(Cai et al., 2024) Uncertainty Inclusive Contrastive Learning for Leveraging Synthetic Images]] ([Weblink](https://openreview.net/forum?id=wNKOQVcMDS))
		- …
	- Andere wissenschaftliche Arbeiten:
		- [[(Xiao et al., 2020) What Should Not Be Contrastive in Contrastive Learning]] ([Weblink](https://arxiv.org/abs/2008.05659))
		- [[(Ran Liu, 2021) Understand and Improve Contrastive Learning Methods for Visual Representation - A Review|Ran Liu (2021) - Understand and Improve Contrastive Learning Methods for Visual Representation: A Review]] ([Weblink](https://arxiv.org/abs/2106.03259))
		- [Radford et al. (2021) - Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
		- [[(Sammani et al., 2022) Visualizing and Understanding Contrastive Learning]] ([Weblink](https://arxiv.org/abs/2206.09753))
		- [[(Keshtmand et al., 2022) Understanding the properties and limitations of contrastive learning for Out-of-Distribution detection]] ([Weblink](https://arxiv.org/abs/2211.03183))
		- …