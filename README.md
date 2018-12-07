For a direct access :
1)The keras model, given the input images are in greyscale format are stored in  	new_model_num3_greyoutput.h5 while for coloured are stored in  	new_model_num_coluoured.h5 . 
2) Given the converted numpy array of imput images in greyscale or RGB accordingly, implementing the code basictest.py
 will provide the basic output.The code for the conversion of images to RGB or greyscale is provided in roverrover.py.
 
 Detailed explaination of the code :
 1) The images are converted into corresponding RGB, greyscale values through basic openCV functions in roverrover.py
 2) These are fed into a CNN network developed using keras whose code is found in try.py.
 3) The CNN Network was trained using a dataset available of a tennis match with around 0.3M examples with hyperparameters of the CNN being tuned using the paper https://github.com/ameyanjarlekar/MRT/blob/master/Reno_Convolutional_Neural_Networks_CVPR_2018_paper.pdf provided in the repo . 
 4) The network was further retrained using a 5,000 odd dataset collected from the image frames of the past videos available of the competition with just the feedforward network weights modified during this process.
 
 Working implementation of the code :
 1) The plan is to make the rover collect images during a 360 degree rotation of itself. This image data is then fed into an unsupervised algorithm (https://github.com/iitbmartian/Autonomous_Subsystem/tree/master/Ball_Detection/Unsupervised/src) which primarily detects green pastures and creates a cropped image window over these pastures.
 2)These images are then sent to the supervised algo which provides the image with the max probability of getting a ball.
 
