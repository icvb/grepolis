# -*- coding: cp1250 -*-
from Hypori_kor import terkep
from pynput.mouse import Button, Controller
import time

def farm (size):
    if size == 1:  #10 perces v�rakoz�s
        mouse.position = (525,600)
        mouse.click(Button.left,1)
    elif size == 2:
        mouse.position = (664,582)
        mouse.click(Button.left,1)
    else:
        print "alma"
    #10 bez�r�s
    mouse.position=(1135,190)
    mouse.click(Button.left,1)
def refresh():
    mouse.position = (86,51)
    mouse.click(Button.left,1)

city = raw_input("k�rem adja meg a v�ros nev�t: ")
#size= raw_input ("Varakozasi ido: ")
size = 2
y = terkep(city)
mouse = Controller()

"bongeszo koordinatai"
mouse.position = (380, 840)
time.sleep(1)
"b�ng�sz�re kattint�s"
mouse.click(Button.left, 1)
time.sleep(1)

"sziget n�zet"
mouse.position =(50,90)
time.sleep(1)
mouse.click(Button.left, 1)

if y == "error":
    print "error 66"
else:
    
    i=0
    while i < 6:
        mouse.position = (y[i][0], y[i][1])
        mouse.click(Button.left,1)
        time.sleep(1)
        farm(size)
        i=i+1
