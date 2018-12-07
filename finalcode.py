import cv2
import numpy as np
import keras
from keras.models import load_model
# Can be integrated in the unsupervised code

def test(array):
	# a = np.load("/home/ameya/Desktop/MRT/no_ball_h3.npy")
	new_model = load_model('/home/ameya/Desktop/MRT/new_model_num_coluoured.h5')
	b = (new_model.predict(array, batch_size=None, verbose=0, steps=None))
	i = 0
	store = 0
	big = 0
	while i< len(b):
		z = big
		big = max(big,b[i][0])
		if big > z:
			store = i
		i = i+1
	return store 



