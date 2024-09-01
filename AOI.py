#讀取壓縮讀取壓縮檔
import zipfile
f = zipfile.ZipFile("./drive/MyDrive/aoi/train_images.zip")
f.extractall("./datasets")

#創建6種訓練資料目錄

import os
for class_num in range(6):
  os.makedirs(f"/content/train_images/{class_num}", exist_ok=True)
  os.makedirs("/content/test_images/test", exist_ok=True)

#整理圖像數據，將它們根據其類別分組到不同的目錄中

import shutil
import pandas as pd
imageAns = pd.read_csv("/content/drive/MyDrive/aoi/train.csv")
for class_num in range(6):
    class00 = imageAns[imageAns["Label"] == class_num]
    class_list = class00["ID"]
    for c in class_list:
        shutil.move('/content/datasets/train_images/' + str(c),
                    '/content/train_images/' + str(class_num) + "/" + str(c))
  

# 圖像增強
from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(
    rescale= 1./255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.05
)

# 設定訓練集和驗證集
train_generator = datagen.flow_from_directory(
    directory="/content/train_images/",
    target_size=(Size, Size),
    batch_size=16,
    class_mode='sparse',
    shuffle=True,
    subset='training'  # 使用 'training' 表示訓練集
)

valid_generator = datagen.flow_from_directory(
    directory="/content/train_images/",
    target_size=(Size, Size),
    batch_size=16,
    class_mode='sparse',
    shuffle=False,  # 在驗證集中不需要洗牌
    subset='validation'  # 使用 'validation' 表示驗證集
)


# 載入Resnet
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, BatchNormalization
from tensorflow.keras.models import Model
ResNetModel = ResNet50(input_shape=(Size, Size, 3), include_top=False, weights='imagenet')

x = ResNetModel.output
x = BatchNormalization()(x)
x = GlobalAveragePooling2D()(x)
y = Dense(6, activation="softmax")(x)
model = Model(inputs=ResNetModel.input, outputs=y)

# 定義optimizer和loss function

from tensorflow_addons.optimizers import RectifiedAdam
from tensorflow_addons.optimizers import Lookahead
from tensorflow.keras.losses import SparseCategoricalCrossentropy
Radam = RectifiedAdam(lr=1e-5)
Ranger = Lookahead(Radam, sync_period=6, slow_step_size=0.5)

model.compile(optimizer=Ranger,
              loss=SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

# 訓練設定
historhistory = model.fit(train_generator,
                    epochs=20, verbose=2,
                    validation_data=valid_generator)

#將訓練過程中模型的準確度曲線圖繪出
import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['Train', 'Valid'], loc='upper left')
plt.show()

 #輸入測試資料
import zipfile
f = zipfile.ZipFile("./drive/MyDrive/aoi/test_images.zip")
f.extractall("./datasets_test/")

#將測試資料調整和訓練資料一致
TestFlowed = Generator.flow_from_directory(
    directory = "/content/datasets_test/",
    target_size= (Size, Size),
    class_mode= None,
    shuffle= False,
    )