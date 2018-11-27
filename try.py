import numpy as np
new=np.load("outputfinal.npy")
newa = np.load("outputfinalans.npy")

#sprint(len(a))


#outfile.seek(0)
#new = np.load(outfile)
#print(new.shape)
#outfileans.seek(0)
#newa = np.load(outfileans)
#print(newa.shape)
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, Dropout
model = Sequential()
model.add(Conv2D(64,5,padding='same',input_shape=(50,50,3)))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2, padding='same'))
model.add(Dropout(0.5))
model.add(Conv2D(64,5,padding='same'))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2, padding='same'))
model.add(Dropout(0.5))
model.add(Conv2D(64,5,padding='same'))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2, padding='same'))
model.add(Dropout(0.5))
model.add(Conv2D(64,5,padding='same'))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2, padding='same'))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(1))
model.add(keras.layers.Activation('softmax'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(new,newa,batch_size=256,epochs=50,validation_split=0.15)