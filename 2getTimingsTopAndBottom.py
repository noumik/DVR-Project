import cv2
import numpy as np
import math
import time

whitetop = int(0)
whitebottom = int(0)
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
         color1 = image[69,382]
         hex1 = (color1[0] << 16) + (color1[1] << 8) + (color1[2])
         color2 = image[69,1913]
         hex2 = (color2[0] << 16) + (color2[1] << 8) + (color2[2])
         color3 = image[123,382]
         hex3 = (color3[0] << 16) + (color3[1] << 8) + (color3[2])
         color4 = image[123,1913]
         hex4 = (color4[0] << 16) + (color4[1] << 8) + (color4[2])
         color5 = image[946,382]
         hex5 = (color5[0] << 16) + (color5[1] << 8) + (color5[2])
         color6 = image[946,1913]
         hex6 = (color6[0] << 16) + (color6[1] << 8) + (color6[2])
         color7 = image[1000,381]
         hex7 = (color7[0] << 16) + (color7[1] << 8) + (color7[2])
         color8 = image[1000,1913]
         hex8 = (color8[0] << 16) + (color8[1] << 8) + (color8[2])
         if((hex1 == 16777215 and hex2 == 16777215 and hex3 == 16777215 and hex4 == 16777215) and whitetop == 0 and whitebottom == 0):
             whitetop = int(1)
             print("starttop")
#            print(frameId)
             videotime = frameId/fps
#            print(videotime)
             currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
             print(currentTime)
             timings_file.write(str(sub_number) + "\n")
             timings_file.write(currentTime + ",000 --> ")
         if((hex5 == 16777215 and hex6 == 16777215 and hex7 == 16777215 and hex8 == 16777215) and whitebottom == 0 and whitetop == 0):
             whitebottom = int(1)
             print("startbottom")
#            print(frameId)
             videotime = frameId/fps
#            print(videotime)
             currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
             print(currentTime)
             timings_file.write(str(sub_number) + "\n")
             timings_file.write(currentTime + ",000 --> ")  
         if((hex1 != 16777215 or hex2 != 16777215 or hex3 != 16777215 or hex4 != 16777215) and whitetop == 1):
             whitetop = int(0)
             print("endtop")
#            print(frameId)
             videotime = frameId/fps
#            print(videotime)
             currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
             print(currentTime)
             timings_file.write(currentTime + ",000\n")
             timings_file.write("text\n\n")
             sub_number = sub_number + 1
         if((hex5 != 16777215 or hex6 != 16777215 or hex7 != 16777215 or hex8 != 16777215) and whitebottom == 1):
             whitebottom = int(0)
             print("endbottom")
#            print(frameId)
             videotime = frameId/fps
#            print(videotime)
             currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
             print(currentTime)
             timings_file.write(currentTime + ",000\n")
             timings_file.write("text\n\n")
             sub_number = sub_number + 1
        
vidcap.release()
print ("Complete")
