import time
import datetime
from pynput.keyboard import Key, Controller
import os, subprocess
#Function for resetting and reloading the game to the save point
keyboard = Controller()
    
mgba_windowID = 0#0x2600006 #0x2c00006     #0x2600006

def change_window():
    #Switching tabs and getting to Desmume
    with keyboard.pressed(Key.alt_r):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    time.sleep(0.5)

def press_once(key, sltime = 0.2):
    keyboard.press(key)
    time.sleep(0.3)
    keyboard.release(key)
    time.sleep(sltime)

def reload():
    press_once('1')

def save():
    press_once('2')
    
def hard_save():
# remember to set enter to b
	press_once('z')
	press_once('z')
	press_once('z')
	press_once('b')
	press_once('x', 1)
	press_once('x')
	press_once('x')
   
#convert rawSH.jpg -crop 100x100+210+100 cropSH.jpg
def get_image():
    os.system('import -window '+mgba_windowID + ' rawSH.jpg')
    os.system('convert rawSH.jpg -crop 40x40+330+100 cropSH.jpg')
    
   
#list_img = ['crop.jpg', 'crop1.jpg', 'crop2.jpg']
#list_img = ["crop.jpg", "crop0.jpg"]
list_img = ["cropNotShiny.jpg"]
shiny_img = ["cropShiny.jpg"]

#Returns True if pokemon is shiny
def isShiny():
    #Taking screenshot and cropping out Giratina from the image
    # get windowID command " xwininfo -display :0 "
    get_image()
    shiny = 1
    for img in list_img:
    	returnC = subprocess.run(["compare", "-metric" ,"MSE" ,"cropSH.jpg" ,img, "output.jpg"], stderr=subprocess.PIPE).stderr
    	#print(returnC)
    	#if (len(returnC) < 8):
    	#if (returnC==0):
    	if (float(returnC.split()[0]) < 5):
    		shiny = 0
    if shiny:
    	returnC = subprocess.run(["compare", "-metric" ,"MSE" ,"cropSH.jpg" ,shiny_img[0], "output.jpg"], stderr=subprocess.PIPE).stderr
    	if (float(returnC.split()[0]) < 5): return True
    	else: return False
    else:
    	return False
    #Capture Screenshot

def trigger_encounter_from_reset():
	
	#reload()
	press_once('r', 2)
	press_once('x',0.3)
	press_once('x',1)
	press_once('x',1)
	press_once('x',1)
	press_once('x',0.5)
	press_once('x',0.5)
	press_once('x',0.5)
	press_once('x',0.5)
	press_once('x',0.3)
	press_once('x',0.5)
	
	press_once('x',0.3)
	press_once(Key.down,0.5)
	press_once('x',0.3)
	press_once('x',0.7)

def nothin():
	press_once('x', 0.5)
	press_once(Key.down, 0.3)
	press_once('x', 0.3)
	press_once('x', 0.3)
	press_once('x', 0.3)
	press_once('x', 0.2)

def trigger_encounter_from_state():
	reload()
	press_once('x', 0.2)
	press_once('z', 0.3)
	press_once('z', 0.3)
	press_once('z',0.2)
	press_once('z',0.2)

def open_mugshot():

	press_once('s', 0.4)
	press_once('y',0.1)
	press_once(Key.right, 0.1)
	press_once('x', 0.2)
	press_once('x', 0.2)
	time.sleep(0.8)
	
def get_wid():
	global mgba_windowID
	mgba_windowID = subprocess.getoutput("xwininfo -name 'mGBA - 0.11-8325-49d9b70e6' -int | sed 2q | tr -d '\n' | cut -c22-").split()[0]
	print("get wid", mgba_windowID)
	
if __name__ == "__main__":
    get_wid()
    print(datetime.datetime.now())
    change_window()
    c=0
	# f is the fastforward shortcut
    while True:
        press_once('y', 0.2)
        #if (c > 2000): break
        trigger_encounter_from_state()
        open_mugshot()
        #break
        time.sleep(0.1)
        if(isShiny()):
            #Code when shiny pokemon is encountered	
            # save()
            #hard_save()
            print("Shiny pokemon encountered after ",c+1,"encounters")
            #time.sleep(100)
            break
        c+=1
        if (c%50 == 0): 
        	print("Not Shiny, Encounter: ",c)
        	print(datetime.datetime.now())
        time.sleep(0.1)
