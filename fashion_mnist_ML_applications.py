import tensorflow as tf 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from tensorflow.keras import datasets,models,layers 
#download the fashion mnist data 
(training_images,training_labels),(test_images,test_labels)= datasets.fashion_mnist.load_data() 
#normilize processing 
training_images=training_images/255.0 
test_images=test_images/255.0 
#defining the model we are defining convolutions 
model=tf.keras.models.Sequential([ 
    tf.keras.layers.Conv2D(64,(3,3),activation='relu',input_shape=(28,28,1)), 
    tf.keras.layers.MaxPooling2D(2,2), 
    tf.keras.layers.Conv2D(64,(3,3),activation='relu'), 
    tf.keras.layers.MaxPooling2D(2,2), 
    tf.keras.layers.Flatten(), 
    tf.keras.layers.Dense(128, activation='relu'), 
    tf.keras.layers.Dense(10,activation='softmax') 
    ]) 
#compiling the model 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy' , 
metrics=['accuracy']) 
model.fit(training_images, training_labels, epochs=5) #fit operation 
test_loss, test_acc = model.evaluate(test_images, test_labels) 
print("Test accuracy is: " ,test_acc) 
#lets take an example 
prediction=model.predict(test_images).argmax(axis=1) 
print("prediction: ", prediction[100]) 
print("real: ", test_labels[100]) 
plt.imshow(test_images[100].reshape(28,28),cmap='gray') 
plt.show() 
