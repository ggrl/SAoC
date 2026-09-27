import numpy as np
import cv2
from PIL import ImageGrab as ig
import time
import configs.UI_config as UI_config
import src.dik_keys as dik_keys
import importlib
from pynput.mouse import Button, Controller
from pynput import mouse


mouse = Controller()

resolution = '1366'
UI_config.current = importlib.import_module(f"configs.UI_config_{resolution}")


def test_health():
            target = ig.grab(bbox=(UI_config.targetx1,UI_config.targety1,UI_config.targetx2,UI_config.targety2))
            target_frame = np.array(target)
            tredpx = 0
            tgreenpx = 0
            tbluepx = 0
            region = target_frame[:UI_config.targeth, :UI_config.targetw]
            tredpx, tgreenpx, tbluepx = region.sum(axis=(0, 1), dtype=np.int64)[:3]
            #print("red", tredpx)
            #print("green", tgreenpx)
            #print("blue", tbluepx)
            pixelsum = [tredpx, tbluepx, tgreenpx]
            pixelsum.sort()
            print("Pixelsum:",pixelsum[2] - pixelsum[0])

            targetbar = ig.grab(bbox=(UI_config.targetbarx1,UI_config.targetbary1,UI_config.targetbarx2,UI_config.targetbary2))
            targetbar_frame = np.array(targetbar)

            region_bar = targetbar_frame[:UI_config.targeth, :UI_config.targetw]
            tbredpx = region_bar[:, :, 0].sum(dtype=np.int64)
            tbgreenpx = region_bar[:, :, 1].sum(dtype=np.int64)
            tbbluepx = region_bar[:, :, 2].sum(dtype=np.int64)
            print("Rote Pixel:", tbredpx)
            print("Grüne Pixel:", tbgreenpx)
            print("Blaue Pixel:", tbbluepx)



                

def test_bars():

    bars = ['healthbar', 'endubar', 'manabar', 'targetbar']

    for bar in bars:

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

        print('-----')
        print(bar, ':')
        print('-----')

        print("Rote Pixel:", tbredpx)
        print("Grüne Pixel:", tbgreenpx)
        print("Blaue Pixel:", tbbluepx)


def test_UI():
       print("Healthbar-position:", UI_config.current.healthbarx1, UI_config.current.healthbary1, UI_config.current.healthbarx2, UI_config.current.healthbary2)
       mouse.position = UI_config.current.healthbarx1, UI_config.current.healthbary1
       time.sleep(1)
       mouse.position = UI_config.current.healthbarx2, UI_config.current.healthbary2
       time.sleep(1)
       print("Endubar-position:", UI_config.current.endubarx1, UI_config.current.endubary1, UI_config.current.endubarx2, UI_config.current.endubary2)
       mouse.position = UI_config.current.endubarx1, UI_config.current.endubary1 
       time.sleep(1)
       mouse.position = UI_config.current.endubarx2, UI_config.current.endubary2
       time.sleep(1)
       print("Manabar-position:", UI_config.current.manabarx1, UI_config.current.manabary1, UI_config.current.manabarx2, UI_config.current.manabary2)
       mouse.position = UI_config.current.manabarx1, UI_config.current.manabary1
       time.sleep(1)
       mouse.position = UI_config.current.manabarx2, UI_config.current.manabary2
       time.sleep(1)
       print("Targetbar-position:", UI_config.current.targetbarx1, UI_config.current.targetbary1, UI_config.current.targetbarx2, UI_config.current.targetbary2)
       mouse.position = UI_config.current.targetbarx1, UI_config.current.targetbary1
       time.sleep(1)
       mouse.position = UI_config.current.targetbarx2, UI_config.current.targetbary2
       time.sleep(1)

while True:
        test_bars()
        test_UI()
        time.sleep(4)


