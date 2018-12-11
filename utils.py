
import numpy as np
import cv2
import Queue

np.set_printoptions(threshold='nan')
Visited = np.zeros((1,1))
low_mask = np.zeros((1,1))

clusterQ = Queue.Queue()

def hyst_threshold(mask_high,mask_low):
	global Visited, low_mask
	Visited = np.zeros(mask_low.shape)
	low_mask = mask_low

	for i in range(mask_high.shape[0]):
		for j in range(mask_high.shape[1]):
			if (Visited[i,j]==0 and mask_high[i,j]>0):
				clusterQ.put((i,j))
				while (not clusterQ.empty()):
					cluster()
	
	return Visited.astype(np.uint8)

def cluster():
	# if clusterQ.empty():
	# 	# print "done by empty"
	# 	return

	(i,j) = clusterQ.get()

	if (i<0 or j<0 or i>=Visited.shape[0] or j>=Visited.shape[1]):
		# print "done by index" + str((i,j))
		return

	# print "hyst: " + str(i) + str(j)
	if (Visited[i,j]>0):
		# print "done by Visited" + str((i,j))
		return

	if (low_mask[i,j]==0):
		# print "done by mask" + str((i,j))
		return

	# print (i,j)

	Visited[i,j] = 255
	# clusterQ.put((i-1,j-1))
	clusterQ.put((i-1,j))
	# clusterQ.put((i-1,j+1))
	clusterQ.put((i,j-1))
	clusterQ.put((i,j+1))
	# clusterQ.put((i+1,j-1))
	clusterQ.put((i+1,j))
	return
	# clusterQ.put((i+1,j+1))
