import cv2
import numpy as np
import math
import time

white = int(0)
timings_file = open('timings.srt', 'w')
sub_number = 1
#################### Setting up the file ################
videoFile = "out.mp4"
vidcap = cv2.VideoCapture(videoFile)
success,image = vidcap.read()

#################### Setting up parameters ################

seconds = 0.1
fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
multiplier = fps * seconds

#################### Initiate Process ################

while success:
    frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    success, image = vidcap.read()

    if frameId % multiplier == 0:
#        cv2.imwrite("frame%d.jpg" % frameId, image)
#        print("write")
         color1 = image[80,5]
         hex1 = (color1[0] << 16) + (color1[1] << 8) + (color1[2])
         color2 = image[80,1793]
         hex2 = (color2[0] << 16) + (color2[1] << 8) + (color2[2])
         color3 = image[115,5]
         hex3 = (color3[0] << 16) + (color3[1] << 8) + (color3[2])
         color4 = image[115,1793]
         hex4 = (color4[0] << 16) + (color4[1] << 8) + (color4[2])
         if((hex1 == 16777215 and hex2 == 16777215 and hex3 == 16777215 and hex4 == 16777215) and white == 0):
             white = int(1)
             print("start")
#            print(frameId)
             videotime = frameId/fps
#            print(videotime)
             currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
             print(currentTime)
             timings_file.write(str(sub_number) + "\n")
             timings_file.write(currentTime + ",000 --> ")
         if((hex1 != 16777215 or hex2 != 16777215 or hex3 != 16777215 or hex4 != 16777215) and white == 1):
             white = int(0)
             print("end")
#            print(frameId)
             videotime = frameId/fps
#            print(videotime)
             currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
             timings_file.write(currentTime + ",000\n")
             timings_file.write("text\n\n")
             sub_number = sub_number + 1
        
vidcap.release()
print ("Complete")
