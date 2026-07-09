---
created: 2024-04-10
last updated: 2025-04-13
publish: true
title: Machine Learning
---

# Machine Learning

Siehe: [[Computer Science]]

Die *ersten* großen Durchbrüche in der [[Künstliche Intelligenz|KI]] kamen vor allem in Bezug auf Aufgaben, die für Menschen intellektuell anspruchsvoll, für Computer aber relativ leicht zu lösen waren, weil sie sich als Liste formaler [[Mathematik|mathematischer]] Regeln beschreiben ließen. Die große Schwierigkeit lag aber tatsächlich in den Aufgaben, die für den Menschen relativ *einfach und intuitiv* sind, sich aber nur schwer formal beschreiben lassen [[(Goodfellow et al., 2016) Deep Learning|(Goodfellow et al., 2016)]]. Dazu gehören zum Beispiel [[Spracherkennung]] oder [[Objekterkennung]].

ML bezieht sich auf einen Ansatz, bei dem Computer mit der Fähigkeit ausgestattet werden, selbstständig Wissen zu generieren, indem sie aus Erfahrungen [[Lernen|lernen]] und Muster aus Rohdaten extrahieren. Dies ermöglicht es ihnen, Aufgaben allein auf der Grundlage von Beispielen und ohne explizite Programmierung der Regeln zu lösen.

In [[(Goodfellow et al., 2016) Deep Learning|(Goodfellow et al., 2016)]] wird eine formale Definition aus [[(Tom M. Mitchell, 1997) Machine Learning|(Mitchell, 1997)]] noch einmal aufgegliedert, um einen besseren Überblick zu erhalten:

>*A computer program is said to learn from experience $E$ with respect to some class of tasks $T$ and performance measure $P$, if its performance at tasks in $T$, as measured by $P$, improves with experience $E$.*

Zur Aufgabe $T$:

- [[Klassifikation]] (z.B. [[Bildklassifikation]])
- [[Regression]]
- [[Anomaliedetektion]]
- Strukturierte Ausgabe (siehe: [[Generative Modelle]])
	- [[Synthetische Daten]]
	- [[Bildsegmentierung]]
	- [[Maschinelle Übersetzung]]
- [[Denoising]]
- …

Zum Leistungsmaß $P$:

- [[Accuracy]]
- [[Precision]]
- [[Recall]]
- …

Zur Erfahrung $E$:

- [[Supervised Learning]]
- [[Unsupervised Learning]]
- [[Semi-Supervised Learning]]
- [[Self-Supervised Learning]]
- [[Reinforcement Learning]]

Beim maschinellen Lernen werden typischerweise [[Neuronale Netze|künstliche neuronale Netze]] verwendet, die auf dem mathematischen Modell des [[McCulloch-Pitts-Neuron]] basieren. Diese Netze sind in verschiedene Schichten von Neuronen gegliedert, welche die gegebenen Eingabedaten schrittweise verarbeiten. Jedes Neuron verfügt über erlernbare Parameter, die bestimmen, wie es die Eingabe verarbeitet, wodurch das Netz seine Parameter so anpassen kann, dass die richtige Ausgabe berechnet wird. Unter [[Deep Learning]] versteht man die Verwendung von Netzwerken mit vielen Schichten.

Weitere Themen im Bereich Machine Learning:

- [[Fine-tuning]]
- [[Datenaugmentation]]
- [[Synthetische Daten]]
- [[Out-of-Distribution]] (Detektion)
- [[Contrastive Learning]]

Einzelne Modell-Architekturen:

- [[Convolutional Neural Networks]]
- [[Autoencoder]] / [[Variational Autoencoder]]
- [[U-Net]]
- [[Generative Adversarial Networks]]
- [[Transformer]]
- [[Diffusionsmodelle]]

---

- ↩
	- [[(Goodfellow et al., 2016) Deep Learning]] ([Weblink](https://www.deeplearningbook.org/))
	- [[(Zhi-Hua Zhou, 2021) Machine Learning]]
	- [[(Tom M. Mitchell, 1997) Machine Learning]]