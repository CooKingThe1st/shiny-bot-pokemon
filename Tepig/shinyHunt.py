import time
import datetime
from pynput.keyboard import Key, Controller
import os, subprocess
#Function for resetting and reloading the game to the save point
keyboard = Controller()
    
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
   
def get_image():
    mgba_windowID = 0x3800006
    os.system('import -window '+str(mgba_windowID) + ' rawSH.jpg')
    os.system('convert rawSH.jpg -crop 100x100+210+100 cropSH.jpg')
    
   
#list_img = ['crop.jpg', 'crop1.jpg', 'crop2.jpg']
list_img = ['crop.jpg', 'crop0.jpg', 'crop00.jpg']
#Returns True if pokemon is shiny
def isShiny():
    #Taking screenshot and cropping out Giratina from the image
    # get windowID command " xwininfo -display :0 "
    get_image()
    shiny = 1
    for img in list_img:
    	returnC = subprocess.run(["compare", "-metric" ,"MSE" ,"cropSH.jpg" ,"crop.jpg", "output.jpg"], stderr=subprocess.PIPE).returncode
    	#print(returnC)
    	#if (len(returnC) < 8):
    	if (returnC==0):
    		shiny = 0
    if shiny:
    	save()
    	return True
    else:
    	return False
    #Capture Screenshot

def trigger_encounter():
	reload()
	#press_once('x',0.2)
	press_once('x',0.2)

if __name__ == "__main__":
	print(datetime.datetime.now())
	change_window()
	c=0
	# f is the fastforward shortcut
	with keyboard.pressed('f'):
	    while True:
	        if (c > 2000): break
	        trigger_encounter()
	        time.sleep(0.2)
	        if(isShiny()):
	            #Code when shiny pokemon is encountered	
	            save()
	            save()
	            save()
	            #hard_save()
	            print("Shiny pokemon encountered after ",c+1,"encounters")
	            time.sleep(100)
	            break
	        c+=1
	        if (c%50 == 0): 
	        	print("Not Shiny, Encounter: ",c)
	        	print(datetime.datetime.now())
	        time.sleep(0.1)
