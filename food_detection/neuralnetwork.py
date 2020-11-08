import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv
import tensorflow as tf
import tensorflow_datasets as tfds
import pandas as pd
from tensorflow import keras
tfds.disable_progress_bar()



filename = 'train.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
xx = list(reader)
xx = np.array(xx).astype('float')
#print(xx.shape)
train_images = xx.reshape(100,75,75,1)


filename = 'train_out.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
xx = list(reader)
xx = np.array(xx).astype('float')
#print(xx.shape)
train_labels = xx



filename = 'test.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
xx = list(reader)
xx = np.array(xx).astype('float')
#print(xx.shape)
test_images = xx.reshape(15,75,75,1)


filename = 'test_out.csv'
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
xx = list(reader)
xx = np.array(xx).astype('float')
#print(xx.shape)
test_labels = xx


model = keras.Sequential([
    #keras.layers.AveragePooling2D(6,3,input_shape = (75,75,1)),
    keras.layers.Conv2D(64,3,activation = 'relu'),
    keras.layers.Conv2D(32,3,activation = 'relu'),
    #keras.layers.MaxPool2D(2,2),
    keras.layers.Dropout(0.5),
    keras.layers.Flatten(),
    keras.layers.Dense(128,activation = 'relu'),
    keras.layers.Dense(3,activation = 'softmax')
])
model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])
model.fit(train_images,train_labels,epochs = 6,batch_size = 32)

#print(test_labels.shape)
model.evaluate(test_images,test_labels)