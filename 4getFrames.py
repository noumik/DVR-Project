import cv2
import numpy as np
import os

results_file = open('results.txt', 'r')

i = int(1)
for line in results_file:
	
	hrs1 = int(line[0:2]) * 3600000
	mins1 = int(line[2:4]) * 60000
	sec1 = int(line[4:6]) * 1000
	mills1 = int(line[6:9])
	total1 = hrs1 + mins1 + sec1 + mills1
	
	hrs2 = int(line[9:11]) * 3600000
	mins2 = int(line[11:13]) * 60000
	sec2 = int(line[13:15]) * 1000
	mills2 = int(line[15:18])
	total2 = hrs2 + mins2 + sec2 + mills2
	
	currentframe = (total1 + total2)/2
	vidcap = cv2.VideoCapture('C:/Users/Noumik/Videos/out.mp4')
	vidcap.set(cv2.CAP_PROP_POS_MSEC,currentframe)					         # just cue to x sec. position
	success,image = vidcap.read()
	if success:
		if(i<10):
			filename = "000" + str(i) + ".png"
		elif(i<100):
			filename = "00" + str(i) + ".png"
		elif(i<1000):
			filename = "0" + str(i) + ".png"
		elif(i<10000):
			filename = str(i) + ".png"
		print(filename)
		
		b_channel, g_channel, r_channel = cv2.split(image)
		alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 #creating a dummy alpha channel image.
		img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
		
		path = 'C:/Users/Noumik/Videos/frames'
		cv2.imwrite(os.path.join(path , filename), img_BGRA)     # save frame as PNG file
		i = i + 1
#		cv2.imshow("20sec",image)
#		cv2.waitKey()
		
results_file.close()