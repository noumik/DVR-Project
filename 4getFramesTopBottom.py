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
        vidcap.set(cv2.CAP_PROP_POS_MSEC,currentframe)                                           # just cue to x sec. position
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
                
        if(hex1 == 16777215 and hex2 == 16777215 and hex3 == 16777215 and hex4 == 16777215):
                        img_BGRA = img_BGRA[66:253, 379:1920]
        if(hex5 == 16777215 and hex6 == 16777215 and hex7 == 16777215 and hex8 == 16777215):
                        img_BGRA = img_BGRA[740:1080, 379:1920]
                
        path = 'C:/Users/Noumik/Videos/frames'
        cv2.imwrite(os.path.join(path , filename), img_BGRA)     # save frame as PNG file
        i = i + 1
#       cv2.imshow("20sec",image)
#       cv2.waitKey()
                
results_file.close()
