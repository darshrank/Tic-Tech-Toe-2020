import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
import pandas as pd
from tensorflow import keras
tfds.disable_progress_bar()

array = [0 for i in range(100)]
labels = [0 for i in range(100)]


for i in range(40):
    s = 'image3/' + str(i + 1) + '.jpg'
    m = cv2.imread(s)  
    #print(m.shape)
    m = m / 255.0
    #print(m)
    # Output img with window name as 'image' 
    #plt.imshow(m[:,:,0],cmap = "Greys_r")  
    
      
    # Maintain output window utill 
    # user presses a key 
    #cv2.waitKey(0)         
      
    # Destroying present windows on screen
    
    #m = m[:,:,2]
    #print(m.shape)
    width = int(m.shape[1]*0.05)
    height = int(m.shape[0]*0.05)
    dim = (width,height)
    res = cv2.resize(m,dim,interpolation = cv2.INTER_AREA)
    #print(res.shape)
    array[i] = res
    labels[i] = 1
    #plt.imshow(res[:,:,0],cmap ="Greys_r")
#cv2.destroyAllWindows() 


test = [0 for i in range(15)]
test_labels = [0 for i in range(15)]


for i in range(10):
    s = 'image1/' + str(i + 1) + '.jpg'
    #print(s)
    m = cv2.imread(s)  
    s1 ='image3/' +str(40 + i + 1) + '.jpg'
    #print(m.shape)
    m = m / 255.0
    m1 = cv2.imread(s1)
    m1 = m1/255.0
    #print(m)
    # Output img with window name as 'image' 
    #plt.imshow(m[:,:,0],cmap = "Greys_r")  
    
      
    # Maintain output window utill 
    # user presses a key 
    #cv2.waitKey(0)         
      
    # Destroying present windows on screen
    
    #m = m[:,:,2]
    #print(m.shape)
    width = 75
    height = 75
    dim = (width,height)
    res = cv2.resize(m,dim,interpolation = cv2.INTER_AREA)
    res1 = cv2.resize(m1,dim,interpolation = cv2.INTER_AREA)
    test[i] = res1
    #print(res.shape)
    array[40 + i] = res
    test_labels[i] = 1;
#print(array[42])


for i in range(50):
    s = 'image2/' + str(i + 1) + '.jpg'
    m = cv2.imread(s)  
    #print(m.shape)
    m = m / 255.0
    #print(m)
    # Output img with window name as 'image' 
    #plt.imshow(m[:,:,0],cmap = "Greys_r")  
    
      
    # Maintain output window utill 
    # user presses a key 
    #cv2.waitKey(0)         
      
    # Destroying present windows on screen
    
    #m = m[:,:,2]
    #print(m.shape)
    width = 75
    height = 75
    dim = (width,height)
    res = cv2.resize(m,dim,interpolation = cv2.INTER_AREA)
    #print(res.shape)
    array[50 + i] = res
    #plt.imshow(res[:,:,0],cmap ="Greys_r")
    
    
for i in range(5):
    s = 'image1/' + str(10 + i + 1) + '.jpg'
    #print(s)
    m = cv2.imread(s)  
    m = m / 255.0
    width = 75
    height = 75
    dim = (width,height)
    res = cv2.resize(m,dim,interpolation = cv2.INTER_AREA)
    test[10 + i] = res
    test_labels[10 + i] = 0
    
    
array = np.array(array)
labels = np.array(labels)


test_labels = np.array(test_labels)
print(array.shape)
array = array[:,:,:,0]
train_labels = labels
test_images = np.array(test)
test_images = test_images[:,:,:,0]
test_images = test_images.reshape(15,75,75,1)


print(labels.shape)
train_images = array.reshape(100,75,75,1)
print(array.shape)



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

print(test_labels.shape)
model.evaluate(test_images,test_labels)