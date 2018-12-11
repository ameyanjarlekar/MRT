import numpy as np
import argparse
import imutils
import utils
import cv2
import time
from os import listdir
from os.path import isfile, join

# high and low colour boundaries in RGB 152 85.0 78.4
high_thresh = {'low':(28,100,120), 'high':(48,200,230)}
low_thresh = {'low':(28,0,80), 'high':(57,255,255)}
high_thresh_sunny = {'low':(20,60,120), 'high':(48,200,230)}
low_thresh_sunny = {'low':(20,0,80), 'high':(57,255,255)}

########################## debugging #################################
# high_thresh = {'low':(28,100,120), 'high':(48,200,230)}
# low_thresh = {'low':(28,0,80), 'high':(57,255,255)}
######################################################################

def detect_ball(image):
	# shrink image
	img = imutils.resize(image, width=600)

	# display input image default

	# BGR to HSV
	image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


	# gaussian blur (Maybe not necessary)
	# image = cv2.GaussianBlur(image, (11, 11), 0)

	# display blurred image
	# cv2.imshow("hsv", blurred_img)
	# cv2.waitKey(0)

	masked_high = cv2.inRange(image, high_thresh['low'], high_thresh['high'])
	masked_low = cv2.inRange(image, low_thresh['low'], low_thresh['high'])
	if (not np.any(masked_high)):
		# print "calc sunny"
		masked_high = cv2.inRange(image, high_thresh_sunny['low'], high_thresh_sunny['high'])
		masked_low = cv2.inRange(image, low_thresh_sunny['low'], low_thresh_sunny['high'])

	########################## debugging #################################
	# masked_high = np.array([[0, 0, 0, 0, 0],
	# 						[0, 1, 1, 1, 0],
	# 						[0, 1, 1, 1, 0],
	# 						[0, 1, 1, 1, 0],
	# 						[0, 0, 0, 0, 0]])
	# masked_low = np.array([[1, 1, 1, 1, 0],
	# 						[1, 1, 1, 1, 0],
	# 						[1, 1, 1, 1, 0],
	# 						[1, 1, 1, 1, 0],
	# 						[1, 1, 1, 1, 0]])
	#####################################################################

	hyst_mask = utils.hyst_threshold(masked_high,masked_low)
	return img, hyst_mask

	# kernel = np.ones((5, 5), np.uint8)
	# hyst_mask = cv2.erode(hyst_mask, kernel, iterations=2)
	# hyst_mask = cv2.dilate(hyst_mask, kernel, iterations=2)
	# res = cv2.bitwise_and(image,image,mask = hyst_mask)

	########################## debugging #################################
	# print "masked_high\n"
	# print masked_high
	# print "masked_low\n"
	# print masked_low
	# print "hyst_mask\n"
	# print hyst_mask
	# display masked image
	######################################################################

	# Make the grey scale image have three channels
	# masked_high = cv2.cvtColor(masked_high, cv2.COLOR_GRAY2BGR)
	# masked_low = cv2.cvtColor(masked_low, cv2.COLOR_GRAY2BGR)
	# hyst_mask = cv2.cvtColor(hyst_mask, cv2.COLOR_GRAY2BGR)

	# numpy_horizontal1 = np.hstack((image, hyst_mask))
	# numpy_horizontal2 = np.hstack((masked_low, masked_high))

	# numpy_vertical = np.vstack((numpy_horizontal1, numpy_horizontal2))
	# return numpy_vertical

	# display input image
	# cv2.imshow("hsv", image)
	# cv2.waitKey(0)
	# cv2.imshow("hsv", masked_high)
	# cv2.waitKey(0)
	# cv2.imshow("hsv", masked_low)
	# cv2.waitKey(0)
	# cv2.imshow("hsv", hyst_mask)
	# cv2.waitKey(0)

def getWindow(image, mask):
	x,y,w,h = cv2.boundingRect(mask)
	s = max(w,h)
	if (s < 40): s = 40

	x1 = x-5
	y1 = y-5
	x2 = x+5+s
	y2 = y+5+s

	if x1 < 0:
		x2 = x2 - x1
		x1 = 0
	if y1 < 0:
		y2 = y2 - y1
		y1 = 0
	if x2 >= image.shape[1]:
		x1 = max(0,x1-(x2-image.shape[1]))
		x2 = image.shape[1]-1
	if y2 >= image.shape[0]:
		y1 = max(0,y1-(y2-image.shape[0]))
		y2 = image.shape[0]-1

	window = image[y1:y2,x1:x2]
	window = cv2.resize(window,(50,50))
	# cv2.rectangle(image,(x1,y1),(x2,y2),(255,255,255),2)
	return window

def getMultiWindow(image, mask):
	windows = []
	# mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
	_, contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	print len(contours)
	for contour in contours:
		# print contour
		x,y,w,h = cv2.boundingRect(contour)
		s = max(w,h)

		x1 = x-5
		y1 = y-5
		x2 = x+5+s
		y2 = y+5+s

		if x1 < 0:
			x2 = x2 - x1
			x1 = 0
		if y1 < 0:
			y2 = y2 - y1
			y1 = 0
		if x2 >= mask.shape[1]:
			x1 = max(0,x1-(x2-mask.shape[1]))
			x2 = mask.shape[1]-1
		if y2 >= mask.shape[0]:
			y1 = max(0,y1-(y2-mask.shape[0]))
			y2 = mask.shape[0]-1

		window = image[y1:y2,x1:x2]
		print window.shape
		window = cv2.resize(window,(50,50))
		windows.append(window)
		# cv2.rectangle(image, (x1,y1), (x2,y2), (255, 0, 0), 2)
		# cv2.imshow("i",image)
		# cv2.waitKey()
	np.array(windows)
	return windows

def getMultiWindowArray(image, mask):
	windows = []
	# mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
	_, contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	print len(contours)
	for contour in contours:
		# print contour
		x,y,w,h = cv2.boundingRect(contour)
		s = max(w,h)

		x1 = x-5
		y1 = y-5
		x2 = x+5+s
		y2 = y+5+s

		if x1 < 0:
			x2 = x2 - x1
			x1 = 0
		if y1 < 0:
			y2 = y2 - y1
			y1 = 0
		if x2 >= mask.shape[1]:
			x1 = max(0,x1-(x2-mask.shape[1]))
			x2 = mask.shape[1]-1
		if y2 >= mask.shape[0]:
			y1 = max(0,y1-(y2-mask.shape[0]))
			y2 = mask.shape[0]-1

		window = image[y1:y2,x1:x2]
		print window.shape
		window = cv2.resize(window,(50,50))
		windows.append(window)
		# cv2.rectangle(image, (x1,y1), (x2,y2), (255, 0, 0), 2)
		# cv2.imshow("i",image)
		# cv2.waitKey()
	setup = np.array(windows)
	return setup
