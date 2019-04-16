import time
from pynput.keyboard import Key, Controller
import numpy as np
import pyautogui
import imutils
import cv2
#Function for resetting and reloading the game to the save point
def reset_reload():
    resetter = Controller()
    resetter.press('i')
    time.sleep(0.5)
    resetter.release('i')
    time.sleep(2)
    #1
    resetter.press('z')
    time.sleep(0.5)
    resetter.release('z')
    #2
    time.sleep(0.5)
    resetter.press('z')
    time.sleep(0.5)
    resetter.release('z')
    time.sleep(0.5)
    #3
    resetter.press('z')
    time.sleep(0.5)
    resetter.release('z')


def encounter_pkmn():
    encounter = Controller()
    encounter.press('z')
    time.sleep(0.5)
    encounter.release('z')
    time.sleep(0.5)
    encounter.press('z')
    time.sleep(0.5)
    encounter.release('z')

#Returns True if pokemon is shiny
def isShiny(non_shiny):
    #Taking screenshot and cropping out Giratina from the image
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = imutils.resize(image, width=600)
    giratina = image[97:178,180:274]
    #Comparing with a non shiny reference
    difference = cv2.subtract(non_shiny, giratina)
    #If there is no difference between the reference and the image, then the encountered pokemon is not shiny
    if(not np.any(difference)):
        return(False)
    else:
        return(True)



    #Capture Screenshot
