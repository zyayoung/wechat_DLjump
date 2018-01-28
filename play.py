import os,time
os.environ['KERAS_BACKEND']='tensorflow'

import subprocess,pickle
from PIL import Image,ImageFilter
from keras import models
import numpy as np

model = models.load_model('model.h5')

def getscreenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system('adb pull /sdcard/autojump.png .')

def jump(distance,x,y,i,j):
    press_time = distance * 1.45
    press_time = int(press_time)
    cmd = 'adb shell input swipe %d %d %d %d '%(x,y,i,j) + str(press_time)
    print(cmd)
    os.system(cmd)

while True:
    getscreenshot()
    img = Image.open('autojump.png').crop((0, 500, 1080, 1300))
    img = img.resize((img.width/8, img.height/8), Image.ANTIALIAS)
    img = img.filter(ImageFilter.CONTOUR)
    img = np.array(img.convert('L'))*1.0/255
    
    pre=model.predict(img.reshape(1,100,135,1))
    src_x=pre[0][2]*1080
    src_y=pre[0][3]*800
    dst_x=pre[0][0]*1080
    dst_y=pre[0][1]*800
    print src_x, src_y, dst_x, dst_y
    distance = (dst_x - src_x)**2 + (dst_y - src_y)**2
    distance = (distance ** 0.5)
    print('distance = ', distance)
    jump(distance,540,1650,540,1650)
    time.sleep(2.5)
    
