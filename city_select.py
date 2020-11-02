from pynput.mouse import Button, Controller
import time
mouse = Controller()

def standard():
    time.sleep(1)
    mouse.click(Button.left, 1)
    mouse.position = (86,51)
    time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(1)
    mouse.position = (116,114)
    time.sleep(1)
    mouse.click(Button.left, 1)
    mouse.position =(50,90)
    time.sleep(1)
    mouse.click(Button.left, 1)
    

def select(city):
    mouse.position = (830,88)
    time.sleep(1)
    mouse.click(Button.left, 1)
    if city == "Hypori":
        mouse.position = (632,354)
        standard()
    elif city == "Alzoc":
        mouse.position = (632,159)
        standard()
    else:
        print "error"
        return "error"

    
        
