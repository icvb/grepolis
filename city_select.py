from pynput.mouse import Button, Controller
import time
mouse = Controller()

def standard():
    time.sleep(1)
    mouse.click(Button.left, 1)
    mouse.position = (86,51)
    time.sleep(2)
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
    elif city == "Aeten":
        mouse.position = (632,134)
        standard()
    elif city == "Alzoc":
        mouse.position = (632,161)
        standard()
    elif city == "Anaxes":
        mouse.position = (632,180)
        standard()
    elif city == "Atzerri":
        mouse.position = (632,199)
        standard()
    elif city == "Bespin":
        mouse.position = (632,224)
        standard()
    elif city == "Bestine":
        mouse.position = (632,245)
        standard()
    elif city == "Carida":
        mouse.position = (632,268)
        standard()
    elif city == "Eriadu":
        mouse.position = (632,314)
        standard()
    elif city == "Fondor":
        mouse.position = (631,333)
        standard()
    elif city == "Ilum":
        mouse.position = (632,314)
        standard()
    elif city == "Jabiim":
        mouse.position = (632,314)
        standard()
    
    else:
        print "error"
        return "error"

    
        
