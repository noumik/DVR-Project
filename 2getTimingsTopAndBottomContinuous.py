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

seconds = 0.2
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
          
         color19 = image[100,630]
         hex19 = (color19[0] << 16) + (color19[1] << 8) + (color19[2])
         color20 = image[100,730]
         hex20 = (color20[0] << 16) + (color20[1] << 8) + (color20[2])
         color21 = image[100,830]
         hex21 = (color21[0] << 16) + (color21[1] << 8) + (color21[2])
         color22 = image[100,930]
         hex22 = (color22[0] << 16) + (color22[1] << 8) + (color22[2])
         color23 = image[100,1030]
         hex23 = (color23[0] << 16) + (color23[1] << 8) + (color23[2])
         color24 = image[100,1130]
         hex24 = (color24[0] << 16) + (color24[1] << 8) + (color24[2])
         color25 = image[100,1235]
         hex25 = (color25[0] << 16) + (color25[1] << 8) + (color25[2])
         color26 = image[100,1340]
         hex26 = (color26[0] << 16) + (color26[1] << 8) + (color26[2])
         color27 = image[100,1450]
         hex27 = (color27[0] << 16) + (color27[1] << 8) + (color27[2])
         color28 = image[100,1590]
         hex28 = (color28[0] << 16) + (color28[1] << 8) + (color28[2]) 
         
         color39 = image[985,630]
         hex39 = (color39[0] << 16) + (color39[1] << 8) + (color39[2])
         color40 = image[985,730]
         hex40 = (color40[0] << 16) + (color40[1] << 8) + (color40[2])
         color41 = image[985,830]
         hex41 = (color41[0] << 16) + (color41[1] << 8) + (color41[2])
         color42 = image[985,930]
         hex42 = (color42[0] << 16) + (color42[1] << 8) + (color42[2])
         color43 = image[985,1030]
         hex43 = (color43[0] << 16) + (color43[1] << 8) + (color43[2])
         color44 = image[985,1130]
         hex44 = (color44[0] << 16) + (color44[1] << 8) + (color44[2])
         color45 = image[985,1235]
         hex45 = (color45[0] << 16) + (color45[1] << 8) + (color45[2])
         color46 = image[985,1340]
         hex46 = (color46[0] << 16) + (color46[1] << 8) + (color46[2])
         color47 = image[985,1450]
         hex47 = (color47[0] << 16) + (color47[1] << 8) + (color47[2])
         color48 = image[985,1590]
         hex48 = (color48[0] << 16) + (color48[1] << 8) + (color48[2])
          
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
             
             color9 = image[100,630]
             hex9 = (color9[0] << 16) + (color9[1] << 8) + (color9[2])
             color10 = image[100,730]
             hex10 = (color10[0] << 16) + (color10[1] << 8) + (color10[2])
             color11 = image[100,830]
             hex11 = (color11[0] << 16) + (color11[1] << 8) + (color11[2])
             color12 = image[100,930]
             hex12 = (color12[0] << 16) + (color12[1] << 8) + (color12[2])
             color13 = image[100,1030]
             hex13 = (color13[0] << 16) + (color13[1] << 8) + (color13[2])
             color14 = image[100,1130]
             hex14 = (color14[0] << 16) + (color14[1] << 8) + (color14[2])
             color15 = image[100,1235]
             hex15 = (color15[0] << 16) + (color15[1] << 8) + (color15[2])
             color16 = image[100,1340]
             hex16 = (color16[0] << 16) + (color16[1] << 8) + (color16[2])
             color17 = image[100,1450]
             hex17 = (color17[0] << 16) + (color17[1] << 8) + (color17[2])
             color18 = image[100,1590]
             hex18 = (color18[0] << 16) + (color18[1] << 8) + (color18[2])
        
         if(whitetop == 1):
            if((abs(hex19-hex9) > 1000000) or (abs(hex20-hex10) > 1000000) or (abs(hex21-hex11) > 1000000) or (abs(hex22-hex12) > 1000000) or (abs(hex23-hex13) > 1000000) or (abs(hex24-hex14) > 1000000) or (abs(hex25-hex15) > 1000000) or (abs(hex26-hex16) > 1000000) or (abs(hex27-hex17) > 1000000) or (abs(hex28-hex18) > 1000000)):
		#	if(hex19 != hex9 or hex20 != hex10 or hex21 != hex11 or hex22 != hex12 or hex23 != hex13 or hex24 != hex14 or hex25 != hex15 or hex26 != hex16 or hex27 != hex17 or hex28 != hex18):
                print("endtop")
                videotime = frameId/fps
                currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
                print(currentTime)
                timings_file.write(currentTime + ",000\n")
                timings_file.write("text\n\n")
                sub_number = sub_number + 1
                whitetop = int(0)
                
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
             
             color29 = image[985,630]
             hex29 = (color29[0] << 16) + (color29[1] << 8) + (color29[2])
             color30 = image[985,730]
             hex30 = (color30[0] << 16) + (color30[1] << 8) + (color30[2])
             color31 = image[985,830]
             hex31 = (color31[0] << 16) + (color31[1] << 8) + (color31[2])
             color32 = image[985,930]
             hex32 = (color32[0] << 16) + (color32[1] << 8) + (color32[2])
             color33 = image[985,1030]
             hex33 = (color33[0] << 16) + (color33[1] << 8) + (color33[2])
             color34 = image[985,1130]
             hex34 = (color34[0] << 16) + (color34[1] << 8) + (color34[2])
             color35 = image[985,1235]
             hex35 = (color35[0] << 16) + (color35[1] << 8) + (color35[2])
             color36 = image[985,1340]
             hex36 = (color36[0] << 16) + (color36[1] << 8) + (color36[2])
             color37 = image[985,1450]
             hex37 = (color37[0] << 16) + (color37[1] << 8) + (color37[2])
             color38 = image[985,1590]
             hex38 = (color38[0] << 16) + (color38[1] << 8) + (color38[2])
             
         if(whitebottom == 1):
             if((abs(hex39-hex29) > 1000000) or (abs(hex40-hex30) > 1000000) or (abs(hex41-hex31) > 1000000) or (abs(hex42-hex32) > 1000000) or (abs(hex43-hex33) > 1000000) or (abs(hex44-hex34) > 1000000) or (abs(hex45-hex35) > 1000000) or (abs(hex46-hex36) > 1000000) or (abs(hex47-hex37) > 1000000) or (abs(hex48-hex38) > 1000000)):
		   # if(((str(hex39)[0:1]) != (str(hex29)[0:1])) or ((str(hex40)[0:1]) != (str(hex30)[0:1])) or ((str(hex41)[0:1]) != (str(hex31)[0:1])) or ((str(hex42)[0:1]) != (str(hex32)[0:1])) or ((str(hex43)[0:1]) != (str(hex33)[0:1])) or ((str(hex44)[0:1]) != (str(hex34)[0:1])) or ((str(hex45)[0:1]) != (str(hex35)[0:1])) or ((str(hex46)[0:1]) != (str(hex36)[0:1])) or ((str(hex47)[0:1]) != (str(hex37)[0:1])) or ((str(hex48)[0:1]) != (str(hex38)[0:1]))): 
 #               print(hex39)
 #               print(hex29)
 #               print(hex40)
 #               print(hex30)
 #               print(hex41)
 #               print(hex31)
 #               print(hex42)
 #               print(hex32)
 #               print(hex43)
 #               print(hex33)
 #               print(hex44)
 #               print(hex34)
 #               print(hex45)
 #               print(hex35)
 #               print(hex46)
 #               print(hex36)
 #               print(hex47)
 #               print(hex37)
 #               print(hex48)
 #               print(hex38)
                print("endbottom")
                videotime = frameId/fps
                currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
                print(currentTime)
                timings_file.write(currentTime + ",000\n")
                timings_file.write("text\n\n")
                sub_number = sub_number + 1
                whitebottom = int(0)
                
#         if((hex1 != 16777215 or hex2 != 16777215 or hex3 != 16777215 or hex4 != 16777215) and whitetop == 1):
#             whitetop = int(0)
#             print("endtop")

#             videotime = frameId/fps

#             currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
#             print(currentTime)
#             timings_file.write(currentTime + ",000\n")
#             timings_file.write("text\n\n")
#             sub_number = sub_number + 1
#         if((hex5 != 16777215 or hex6 != 16777215 or hex7 != 16777215 or hex8 != 16777215) and whitebottom == 1):
#             whitebottom = int(0)
#             print("endbottom")

#             videotime = frameId/fps

#             currentTime = time.strftime('%H:%M:%S', time.gmtime(videotime))
#             print(currentTime)
#             timings_file.write(currentTime + ",000\n")
#             timings_file.write("text\n\n")
#             sub_number = sub_number + 1
        
vidcap.release()
print ("Complete")
