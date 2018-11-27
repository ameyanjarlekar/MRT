# Repository to store various codes written for the Mars Rover Team
import os,random
#os.environ["KERAS_BACKEND"] = "tensorflow"
import numpy as np
from keras.utils import np_utils
import keras.models as models
from keras.layers.core import Reshape,Dense,Dropout,Activation,Flatten
from keras.layers.noise import GaussianNoise
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.regularizers import *
from keras.optimizers import adam
import matplotlib.pyplot as plt
import cPickle, random, sys, keras
import pickle
Xd = cPickle.load(open("/home/ameya/Desktop/DATA ANALYSIS COURSE/RML2016.10a_dict.pkl","rb"))
snrs,mods = map(lambda j: sorted(list(set(map(lambda x: x[j], Xd.keys())))), [1,0])
X = []  
print(mods)

