---
created: 2024-07-21
last updated: 2025-04-27
publish: true
title: Convolutional Neural Networks
---

# Convolutional Neural Networks

Ein **Convolutional Neural Network** (CNN) ist ein spezielles [[Neuronale Netze|neuronales Netz]], das hauptsächlich zur [[Bildklassifikation]] entwickelt wurde. Es verwendet Konvolutionsschichten (convolution layers), um ein Eingangsbild Schritt für Schritt in immer abstraktere “Feature Maps” zu verarbeiten.

>![[(Lo et al., 2020) Convolutional Neural Network Architektur.webp]]
>
>Quelle: [Lo et al. (2020)](https://www.mdpi.com/1424-8220/20/12/3539)

Die Grundlagen für CNNs wurden in [(Fukushima, 1980)](https://www.rctn.org/bruno/public/papers/Fukushima1980.pdf) und vor allem [(LeCun, 1989)](https://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf) gelegt. Seit dem wurden eine Vielzahl von weiteren CNNs entwickelt, unter anderem:

- [[MNIST]]
- [[AlexNet]]
- [[ResNet]]
- …

Die Architektur eines CNN besteht typischerweise aus mehreren Schichten, die in der folgenden Reihenfolge angeordnet sind:

1. **Eingabeschicht (Input Layer)**: Diese Schicht nimmt die Rohdaten auf, z.B. ein Bild in Form eines 2D-Arrays von Pixelwerten.
2. **Faltungsschicht (Convolutional Layer)**: Diese Schicht führt die eigentliche Faltung (Convolution) durch, indem sie einen Filter (Kernel) über das Eingabebild verschiebt und Punktoperationen durchführt. Das Ergebnis ist eine Feature-Map, die lokale Merkmale des Bildes extrahiert. Jeder Filter kann unterschiedliche Merkmale wie Kanten, Ecken oder Texturen erkennen.

>![[(IBM) What are convolutional neural networks (Filter).webp]]
>
>Quelle: [IBM](https://www.ibm.com/think/topics/convolutional-neural-networks)

3. **Aktivierungsschicht (Activation Layer)**: Nach jeder Faltungsschicht wird normalerweise eine Aktivierungsfunktion angewendet, um nichtlineare Eigenschaften des Netzwerks zu modellieren. Die häufig verwendete Aktivierungsfunktion ist die [[ReLU]] (Rectified Linear Unit), die alle negativen Werte auf Null setzt und positive Werte unverändert lässt.
4. **Pooling-Schicht (Pooling Layer)**: Diese Schicht reduziert die räumliche Dimension der Feature-Maps, was die Berechnungen effizienter macht und die Gefahr von Überanpassung ([[Overfitting]]) verringert. Die gängigsten Pooling-Methoden sind [[Max-Pooling]] (wählt den maximalen Wert in einem bestimmten Bereich) und [[Average-Pooling]] (berechnet den Durchschnittswert in einem bestimmten Bereich).
5. **Vollständig verbundene Schicht (Fully Connected Layer)**: Dies ist eine herkömmliche neuronale Netzwerkschicht, bei der jeder Neuron mit jedem Neuron der vorherigen Schicht verbunden ist. Sie kombiniert die extrahierten Merkmale, um das endgültige Ergebnis zu liefern, z.B. die Klassifikation des Bildes.
6. **Ausgabeschicht (Output Layer)**: In der letzten Schicht wird eine Aktivierungsfunktion wie [[Softmax]] verwendet, um die Wahrscheinlichkeitsverteilung der möglichen Klassen zu berechnen.

Das Training eines CNN erfolgt in der Regel durch [[Backpropagation]] und [[Gradient Descent]]. Während des Trainings passt das Netzwerk seine Filter und Gewichtungen an, um die Fehler zwischen den vorhergesagten und den tatsächlichen Werten zu minimieren. Zu den häufig verwendeten Optimierungsmethoden gehören der [[Stochastic Gradient Descent]] (SGD), Adam und RMSprop.

---

- ↩
	- Grundlegende Forschungsarbeiten:
		- [Fukushima (1980) - Neocognitron: A Self-organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position](https://www.rctn.org/bruno/public/papers/Fukushima1980.pdf)
		- [LeCun (1989) - Backpropagation Applied to Handwritten Zip Code Recognition](https://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf)