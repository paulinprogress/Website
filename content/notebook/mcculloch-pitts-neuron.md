---
created: 2024-07-11
last updated: 2026-01-25
publish: true
title: McCulloch-Pitts-Neuron
---

# McCulloch-Pitts-Neuron

Auch bekannt als künstliches Neuron oder formales Neuron; einfaches [[Mathematik|mathematisches]] Modell eines [[Neurobiologie|biologischen]] [[Neuron|Neurons]], das 1943 von Warren McCulloch und Walter Pitts vorgeschlagen wurde. Es bildet die Grundlage für [[Neuronale Netze|künstliche neuronale Netze]] und entsprechend auch fürs [[Machine Learning]].

>![[(Zhi-Hua Zhou, 2021) Machine Learning (Neuron).webp|506]]
>
>Quelle: [[(Zhi-Hua Zhou, 2021) Machine Learning#Neural Networks|Zhi-Hua Zhou, 2021]]

Es besteht aus den folgenden Komponenten:

- **Eingaben (Inputs):** Das Neuron empfängt eine Reihe von Eingaben $x_1, x_2, …, x_n$. Diese Eingaben können entweder von externen Quellen oder von den Ausgaben anderer Neuronen in einem Netzwerk stammen.
- **Gewichte (Weights):** Jede Eingabe hat ein zugehöriges Gewicht $w_1,w_2,...,w_n$. Diese Gewichte bestimmen die Stärke und Richtung (positiv oder negativ) des Einflusses der jeweiligen Eingabe auf das Neuron.
- **Summation:** Das Neuron berechnet die gewichtete Summe aller Eingaben: $$ S = \sum_{i=1}^{n} w_i \cdot x_i $$
- **Schwellenwert (Threshold):** Das Neuron hat einen Schwellenwert $θ$, der bestimmt, ob das Neuron aktiviert wird oder nicht.
- **Aktivierungsfunktion:** Das McCulloch-Pitts-Neuron verwendet eine einfache binäre Aktivierungsfunktion. Wenn die gewichtete Summe $S$ die Schwelle $\theta$ überschreitet, wird das Neuron aktiviert und gibt eine Ausgabe von 1. Andernfalls bleibt das Neuron inaktiv und gibt eine Ausgabe von 0: $$y = \begin{cases} 1 & \text{wenn } S \geq \theta \\ 0 & \text{wenn } S < \theta \end{cases}$$
---

- ↩
	- [[(Zhi-Hua Zhou, 2021) Machine Learning]]
	- [[(Simply, 2023) Künstliche Intelligenz]]