import os
import time
import random
import numpy as np
import cv2
import shutil

from fn.find_nearest import find as cpp_find
from fn.find_nearest import yell as cpp_yell

def visualize(img_label: np.ndarray) -> np.ndarray:
    img_visualize = np.zeros((img_label.shape[0], img_label.shape[1], 3), dtype=np.uint8)
    
    #瞳孔區 畫藍色
    img_visualize[np.where(img_label == 0)]=(255,0,0)
    #眼白區 畫綠色
    img_visualize[np.where(img_label == 1)]=(0,255,0)
    #皮膚區 畫紅色
    img_visualize[np.where(img_label == 2)]=(0,0,255)
    #未定區 畫黃色
    img_visualize[np.where(img_label == 3)]=(0,255,255)
    #所有區域外的部分 畫紫色
    img_visualize[np.where(img_label == 4)]=(255,0,255)
    
    return img_visualize


if os.path.isdir('.\\output_visualize'):
    shutil.rmtree(f'.\\output_visualize')
while True:
    try:
        os.makedirs('.\\output_visualize', exist_ok=True)
    except:
        time.sleep(0.2)
    else:
        break


                
#cap = cv2.VideoCapture('D:\2019paper program\IR_RGB_transfer\output_G.avi')
#print cap.isOpened()
#for i in range(523):

a=0

count = len(os.listdir('.\\source'))

for img_file in os.listdir('.\\source'):
    if os.path.splitext(img_file)[1].lower() == '.png' and img_file[0] == 'p':
        img = cv2.imread(f'.\\source\\{img_file}')

        height = img.shape[0]
        weight = img.shape[1]
        
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_visualize = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        
        img_label = np.zeros(img.shape, dtype=np.uint8)
        # 標記: 瞳孔=0, 眼白=1, 皮膚=2, 重疊=3, 範圍外=4
        img_label[np.where(np.logical_and(img>=80,img<=84))] = 0
        img_label[np.where(np.logical_and(img>=86,img<=100))] = 1
        img_label[np.where(np.logical_and(img>=117,img<=128))] = 2
        img_label[np.where(np.logical_and(img>100,img<117))] = 3
        img_label[np.where(np.logical_and(img>=0,img<80))] = 4
        img_label[np.where(np.logical_and(img>=85,img<=85))] = 4
        img_label[np.where(np.logical_and(img>128,img<=255))] = 4
        # 排除右上/左上角的瞳孔部分(強制指定為皮膚)
        img_label[150:181, :][np.where(img_label[150:181, :]==0)] = 2
        
        img_visualize_step0 = visualize(img_label)
        
        # 條件1: 如果重疊(label=3) 同一個 row 有瞳孔，則判定為眼白
        white_of_eye_Y = set( np.where(img_label==0)[1] )
        for y, x in zip(*np.where(img_label==3)):
            if y in white_of_eye_Y:
                img_label[y,x] = 1
                
        img_visualize_step1 = visualize(img_label)

        # 條件2: 重疊(label=3)的 pixel，取最近的眼白或皮膚
        uy, ux = np.where(img_label==3)  # u: unknown
        wy, wx = np.where(img_label==1)
        sy, sx = np.where(img_label==2)
        res = cpp_find(ux, uy, wx, wy, sx, sy, True)
        res = np.array(res, dtype=np.uint8)
        
        # 確定要塗成眼白的區域
        to_white = (uy[np.where(res==1)], ux[np.where(res==1)])
        to_skin = (uy[np.where(res==0)], ux[np.where(res==0)])
        img_label[to_white] = 1
        img_label[to_skin] = 2
        
        # --- 把 label 的值轉成 visualize, 印到圖片上 ---
        img_visualize_step2 = visualize(img_label)
        cv2.imwrite(f'.\\output_visualize\\v{a:03d}_step0.png',img_visualize_step0)
        cv2.imwrite(f'.\\output_visualize\\v{a:03d}_step1.png',img_visualize_step1)
        cv2.imwrite(f'.\\output_visualize\\v{a:03d}_step2.png',img_visualize_step2)
        a += 1
        
        print(f'已處理 {a}/{count} 張')
        
        
        #for i in range(height):
        #    for j in range(weight):  
                
                
                
                
                

                #瞳孔範圍
                #if img[i,j]>0 and img[i,j]<=84:
                    #img[i,j]=img[i,j]*(40/84)+17
                    
                    
                #眼白範圍    
                #elif img[i,j]>90 and img[i,j]<=97:
                    #img[i,j]= (img[i,j]-69)*(48/7)
                    
                #皮膚範圍    
                #elif img[i,j]>100 and img[i,j]<=160:
                   # img[i,j] = img[i,j]*(40/60)+(178/3)
                #else:
                    #continue
                    #img[i,j]= (img[i,j]-69)*(48/7)
                
                
        #cv2.imshow('RGB_GRAY',img) ;cv2.waitKey(0)
        # cv2.imwrite('test%00d.png',img,i)
        
        
            
        
        
        
print('處理完畢\n')
print('瞳孔確定區:藍色 80~84 \n眼白確定區:綠色 86~100 \n皮膚確定區:紅色 117~128\n未定區:黃色 100~117\n除以上四區域以外:紫色 1~80,85,129~255')


