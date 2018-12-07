import cv2
import pandas as pd
import os
import glob
import numpy as np
#files1 = glob.glob('/home/ameya/Desktop/MRT/ball pics_EDIT/*.jpg')
#files2 = glob.glob('/home/ameya/Desktop/MRT/superviedpics/*.png')
# files3 = glob.glob('/home/ameya/Desktop/MRT/ball pics_EDIT/*.jpeg')
# files4 =glob.glob('/home/ameya/Desktop/MRT/ball pics_EDIT/*.JPG')

# files5 = glob.glob('/home/ameya/Desktop/MRT/NO_BALL_PICS/*.jpg')
# files6 = glob.glob('/home/ameya/Desktop/MRT/NO_BALL_PICS/*.png')
# files7 = glob.glob('/home/ameya/Desktop/MRT/NO_BALL_PICS/*.jpeg')
#files8 = glob.glob('/home/ameya/Desktop/MRT/NO_BALL_PICS/*.JPG')
#new=np.load("/home/ameya/Desktop/MRT/outputfinalgrey.npy")
#print('a')

#testdata = []
#testdataout=[]
# for f1 in files1:
#     img = cv2.imread(f1,0)
#     img = cv2.resize(img,(50,50))
#     testdataout.append([1,0])
#     testdata.append(img)
#     print('1')
# print('a')

# for f1 in files2:
#     img = cv2.imread(f1)
#     img = cv2.resize(img,(50,50))
#     testdata.append(img)
#     #testdataout.append([1,0])
# print('a')
# for f1 in files3:
#     img = cv2.imread(f1,0)
#     img = cv2.resize(img,(50,50))
#     testdata.append(img)
#     testdataout.append([1,0])
# print('a')
# for f1 in files4:
#     img = cv2.imread(f1,0)
#     img = cv2.resize(img,(50,50))
#     testdata.append(img)
#     testdataout.append([1,0])
# print('a')
# for f1 in files5:
#     img = cv2.imread(f1,0)
#     img = cv2.resize(img,(50,50))
#     testdata.append(img)
#     testdataout.append([0,1])
# print('a')
# for f1 in files6:
#     img = cv2.imread(f1,0)
#     img = cv2.resize(img,(50,50))
#     testdata.append(img)
#     testdataout.append([0,1])
# print('a')
# for f1 in files7:
#     img = cv2.imread(f1,0)
#     img = cv2.resize(img,(50,50))
#     testdata.append(img)
#     testdataout.append([0,1])
# print('a')
# for f1 in files8:
#     img = cv2.imread(f1,0)
#     img = cv2.resize(img,(50,50))
#     testdata.append(img)
#     testdataout.append([0,1])
# print('a')
#a = np.array(testdata)
#b = np.array(testdataout)
#print('a')

#np.save("depthdata.npy",a)
#np.save("coloureddata.npy",b)
# newa = np.load("betterdatagrey.npy")
# newb = np.load("betterdatagreyout.npy")
# print(np.shape(newa))
# print(np.shape(newb))
a = np.load("/home/ameya/Desktop/MRT/no_ball_mainbuilding.npy")
print(np.shape(a))
i = 0
while i<225:
	cv2.waitKey(0)
	b = cv2.resize(np.array(a[i]),(1000,1000))
	i = i+1
	cv2.imshow('im',b)
#print(np.shape(np.array(testdata)))
from keras.models import load_model
new_model = load_model('/home/ameya/Desktop/MRT/new_model_num_coluoured.h5')
print(new_model.predict(a, batch_size=None, verbose=0, steps=None))
#np.save("trailpics.npy", a)
# b = np.load("trailpics.npy")
# cv2.waitKey(0)
# cv2.imshow('im',b[0])
# cv2.waitKey(0)
# i = 0

# import numpy as np
# import cv2
# data=np.load("/home/ameya/Desktop/MRT/outputfinalgreymod.npy")
# cv2.imshow('im',np.array(data[10]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[12]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[31]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[14]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[15]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[17]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[19]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[11]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[13]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[20]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[22]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[27]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[29]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[25]))
# cv2.waitKey(0)
# cv2.imshow('im',np.array(data[23]))
# cv2.waitKey(0)

# while i<8:
# 	print(i)
# 	cv2.imshow('im',a[i])
# 	cv2.waitKey(0)
# 	i = i+1

#for f1 in files2:
#    img = cv2.imread(f1,0)
#    img = cv2.resize(img,(50,50))
#    testdata.append(img)
