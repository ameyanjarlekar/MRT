import cv2
import pandas as pd
import os
import glob
import numpy as np
img_dir = "C:/Users/lenovo/Desktop/rover//DatasetTennisCNN-CVPR18/" # Enter Directory of all images data_path = os.path.join(img_dir,'*png')
files = glob.glob("/media/ameya/Windows/Users/lenovo/Desktop/rover/DatasetTennisCNN-CVPR18/ball/*.png")
files1 = glob.glob("/media/ameya/Windows/Users/lenovo/Desktop/rover/DatasetTennisCNN-CVPR18/no_ball/*.png")
#files = glob.glob("/media/ameya/Windows/Users/lenovo/Desktop/rover/ball pics/IMG_6044.JPG")
data = []
datay = []
for f1 in files:
    img = cv2.imread(f1)
    datay.append([1])
    # print(datay)
    data.append(img)
 
for f2 in files1:
    img = cv2.imread(f2)
    datay.append([0])
    #img = cv2.resize(img,(50,50))
    data.append(img)
modify = np.array(data)
modifyans = np.array(datay)
#from tempfile import TemporaryFile
#np.savetxt('a.txt', modify, fmt='')
np.save("outputfinal.npy", modify)
np.save("outputfinalans.npy", modifyans)
#out=np.load("output.npy")
#print(out.shape())
#outfileans = TemporaryFile()
#np.save(outfileans, modifyans)
#outfile.seek(0)
#new = np.loadtxt('a.txt', dtype=double)
#print(new)
#outfileans.seek(0)
#newa = np.load(outfileans)
#print(newa)
import keras