# Automated-Optical-Inspection
自動光學檢查（Automated Optical Inspection, AOI）是一種利用光學影像技術來自動檢查產品外觀或電路板製造品質的檢測方法。通過專門的軟體分析影像中的特徵，例如缺陷、短路、錯位或元件缺失等。這種技術廣泛應用於電子製造業，以確保產品符合質量標準，減少人為檢測的誤差，提高生產效率。

Automated Optical Inspection (AOI) Automated Optical Inspection (AOI) is a method that uses optical imaging technology to automatically inspect the appearance of products or the manufacturing quality of circuit boards. Specialized software analyzes features in the images, such as defects, short circuits, misalignment, or missing components. This technology is widely used in the electronics manufacturing industry to ensure that products meet quality standards, reduce human inspection errors, and improve production efficiency.

此程式使用AIdea的影像資料集，內容包括大量的瑕疵影像，使用基於Resnet神經網路進行分類。

This program uses an image dataset from AIdea, which includes a large number of defect images. It classifies these images using a ResNet-based neural network.

# ResNet
ResNet（Residual Network）是一種深度神經網路架構。當網路變得很深時，學習效果可能反而會變差。為了解決這個問題，ResNet引入了殘差塊（Residual Block）的概念，讓網路學習層與層之間的殘差，而不是直接學習輸入到輸出的映射。這樣訊息可以直接跳過一些層，讓網路更容易學習到有效的特徵，避免因為層數過多而影響效果。

ResNet ResNet (Residual Network) is a deep neural network architecture. When a network becomes very deep, its learning performance may actually worsen. To address this issue, ResNet introduces the concept of a Residual Block, allowing the network to learn the residuals between layers rather than directly mapping inputs to outputs. This enables information to bypass certain layers, making it easier for the network to learn effective features, thus avoiding the negative impact of having too many layers.

<img src="ResNet_structure.jpg">

source: https://arxiv.org/pdf/1512.03385.pdf

# Results

<img src="AOI 瑕疵分類_結果.png">

訓練20次accuracy為0.9700，val_accuracy為0.9919，而測試結果accuracy達到0.9839704

After 20 training epochs, the accuracy reached 0.9700, the validation accuracy was 0.9919, and the test accuracy achieved 0.9839704.

# Final Ranking

取得第181名於619位參賽者中

Ranked 181st out of 619 participants.

<img src="AOI 瑕疵分類.png">
