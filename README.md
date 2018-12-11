

 For a direct access :
1) To get output of direct livestream images from the video of IP_cam_10 use the code "runningcode.py", you need the supporting codes "utils.py", "basictest.py" , "detect_ball.py" and the file "ew_model_num_coluoured.h5" for executing the code.The input is consistent with the rover having a 360 degree turn with images taken at particular angle intervals with the output being the angle at which the probability of the ball being placed is the maximum.
2) The keras model, given the input images are in greyscale format are stored in  	new_model_num3_greyoutput.h5 while for coloured
are stored in  	new_model_num_coluoured.h5 . 
3) Connect the IP_cam_10 on your device and the laptop with a common wireless connection (a mobile hotspot will be just enough), and modify the ip address on the mobile cam in the code "runningcode.py"
4) Start the IP_cam on your laptop by first starting the roscore service in your corresponding workspace (will mostly be Rover_basestation) . Then provide the command rqt on the terminal to start the connect the IP_cam on your laptop.
 
 Detailed explaination of the code :
1) Given a folder, the images could be converted into corresponding RGB, greyscale values through basic openCV functions in roverrover.py
2) These are then fed into a CNN network developed using keras whose code is found in try.py.
3) The CNN Network was trained using a dataset available of a tennis match with around 0.3M examples with hyperparameters of the   CNN being tuned using the paper https://github.com/ameyanjarlekar/MRT/blob/master/Reno_Convolutional_Neural_Networks_CVPR_2018_paper.pdf provided in the repo . 
4) The network was further retrained using a 5,000 odd dataset collected from the image frames of the past videos available of the competition with just the feedforward network weights modified during this process.
 
 Working implementation of the code :
1) The plan is to make the rover collect images during a 360 degree rotation of itself. This image data is then fed into an    unsupervised algorithm (https://github.com/iitbmartian/Autonomous_Subsystem/tree/master/Ball_Detection/Unsupervised/src) which primarily detects green pastures and creates a cropped image window over these pastures.
2) The files "utils.py","detect_ball.py" create cropped images from the original image at places where a green pasture is observed and convert them into corresponding RGB/greyscale numpy arrays of size 50*50.
3) These images are then sent to the supervised algo which provides the image with the max probability of getting a ball.
 
