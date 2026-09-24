import numpy as np
import cv2
from PIL import ImageGrab as ig
import time
import pynput
from pynput.keyboard import Key, Listener
from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput import mouse
import UI_config
import dik_keys

mouse = Controller()


def get_px(bar, color):
            image = ig.grab(bbox=(
                getattr(UI_config, bar + 'x1'),
                getattr(UI_config, bar + 'y1'),
                getattr(UI_config, bar + 'x2'),
                getattr(UI_config, bar + 'y2')
            ))
    
            frame = np.array(image)
    
            h = getattr(UI_config, bar + 'h')
            w = getattr(UI_config, bar + 'w')
    
            region_bar = frame[:h, :w]
    
            tbredpx = region_bar[:, :, 0].sum(dtype=np.int64)
            tbgreenpx = region_bar[:, :, 1].sum(dtype=np.int64)
            tbbluepx = region_bar[:, :, 2].sum(dtype=np.int64)
    
            
            if color == 'red':
                   print(bar,": red pixels:", tbredpx)
                   return tbredpx
            elif color == 'green':
                   print(bar,": green pixels:", tbgreenpx)
                   return tbgreenpx
            elif color == 'blue':
                   print(bar,": blue pixels:", tbbluepx) 
                   return tbbluepx
            else:
                   return None 
      


def targeting(pull_key, pull_weapon):
    screen = ig.grab(bbox=(UI_config.scrnx1,UI_config.scrny1,UI_config.scrnx2,UI_config.scrny2))
    current_frame = np.array(screen)
    previous_frame = current_frame
    print(pull_key)
    whiteten = cv2.imread('mob.jpg',0)

    targetingx = 1

    print('--------| targeting |---------')
    
    #while (True):
    for i in range(0,10):
        #print('x1')
        screen = ig.grab(bbox=(UI_config.scrnx1,UI_config.scrny1,UI_config.scrnx2,UI_config.scrny2))
        current_frame = np.array(screen)
        
        
    
        current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
        #print('x2')
        frame_difference = cv2.absdiff(current_frame_gray, previous_frame_gray)
    
        #cv2.imshow("current", current_frame_gray)
        #cv2.imshow("difference", frame_difference)

        

        previous_frame = current_frame
        ret,frame_thresh = cv2.threshold(frame_difference,3,255,0)

        #print('x3')
        ##contours, hierarchy = cv2.findContours(frame_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.imshow("frame_thresh", frame_thresh)

        frame_thresh_c = cv2.cvtColor(frame_thresh, cv2.COLOR_GRAY2BGR)

        #print('x4')
        find = cv2.matchTemplate(frame_thresh,whiteten,cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(find)

        top_left = max_loc
        bottom_right = (top_left[0]+20, top_left[1]+20)
        #print('x5')
        centerx = (max_loc[0]-3, max_loc[1]+3)

        centerx_ig = (centerx[0]+UI_config.scrnx1, centerx[1]+UI_config.scrny1) 
        
        cv2.circle(frame_thresh_c,(centerx), 20, (0,255,), 2)

        #print('x6')
        mouse.position = centerx_ig
        time.sleep(0.02)
        mouse.press(Button.left)
        time.sleep(0.05)
        mouse.release(Button.left)

        #print('x7')
        
        if get_px('targetbar', 'green') > 300000:
               print('New Target.')
               return True
           
        


def pull_check(pull_key, pull_weapon):    
    print('--------| pullcheck |---------')
    dik_keys.Press(pull_key)
    time.sleep(0.05)
    dik_keys.Press(pull_key)
    time.sleep(0.5)
    if get_px('cchat', 'green') - get_px('cchat', 'red') >= 3000:
        return True
    else:
        targeting(pull_key, pull_weapon)            

def test_targeting():        
            target = ig.grab(bbox=(UI_config.targetx1,UI_config.targety1,UI_config.targetx2,UI_config.targety2))
            target_frame = np.array(target)
             
            tredpx = 0
            tgreenpx = 0
            tbluepx = 0
            region = target_frame[:UI_config.targeth, :UI_config.targetw]
            tredpx, tgreenpx, tbluepx = region.sum(axis=(0, 1), dtype=np.int64)[:3]
            print("red", tredpx)
            print("green", tgreenpx)
            print("blue", tbluepx)

def test_targeting2():  
         cchat = ig.grab(bbox=(UI_config.cchatx1,UI_config.cchaty1,UI_config.cchatx2,UI_config.cchaty2))
         cchat_frame = np.array(cchat)
         redpx = 0
         greenpx = 0
         bluepx = 0
         region = cchat_frame[:UI_config.cchath, :UI_config.cchatw]
         redpx, greenpx, bluepx = region.sum(axis=(0, 1), dtype=np.int64)[:3]
         print("red",redpx)
         print("green", greenpx)
         print("blue", bluepx)           