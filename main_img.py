import os
import time
import numpy as np
import cv2
#a=0

#count = len(os.listdir('.\\source'))
     
    

#for img_file in os.listdir('.\\source'):

    #if os.path.splitext(img_file)[1].lower() == '.png' and img_file[0] == 'p':
        #img = cv2.imread('p%00d.png',i)
img = cv2.imread('ssd_visualize_frame0023.png')

height = img.shape[0]
weight = img.shape[1]

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#瞳孔
#img = np.where( np.logical_and(img>0 ,img<=205) , img=0, img )
#眼白
#img = np.where( np.logical_and(img>205, img<=210) ,img=125, img )
#皮膚
#img = np.where( np.logical_and(img>210, img<=255), img=255,img)
cv2.imshow('Ori',img); cv2.waitKey(0)

for i in range(height):
    for j in range(weight):  

        #瞳孔範圍
        if img[i,j]>0 and img[i,j]<=230:
            img[i,j]=0
            
            
        #眼白範圍    
        #elif img[i,j]>205 and img[i,j]<=210:
        #    img[i,j]= 125
            
        #皮膚範圍    
        #elif img[i,j]>210 and img[i,j]<=255:
         #   img[i,j] = 255
        else:
            #continue
            #img[i,j]= (img[i,j]-69)*(48/7)
            img[i,j]=255
          
cv2.imshow('RGB_GRAY',img) ;cv2.waitKey(0)
# cv2.imwrite('test%00d.png',img,i)

#if not os.path.isdir('./output'):
 #   os.makedirs('./output', exist_ok=True)

#cv2.imwrite(f'output/test{img_file[1:]}',img)
#a=a+1
        
#       # print('已處理%d/%d張'%(a,count))
        
#print('處理完畢')


