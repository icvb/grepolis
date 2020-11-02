# -*- coding: cp1250 -*-
from Hypori_kor import terkep
from pynput.mouse import Button, Controller
from city_select import select
import time

def farm ():
    mouse.position = (525,600)
    mouse.click(Button.left,1)
    #10 bezárás
    mouse.position=(1135,190)
    mouse.click(Button.left,1)
def refresh():
    mouse.position = (86,51)
    mouse.click(Button.left,1)

city = ["Hypori","Alzoc"]


mouse = Controller()
k = 0
while k!=len(city):
    y = terkep(city[k])
    select(city[k])
    "sziget nézet"
    mouse.position =(50,90)
    time.sleep(1)
    mouse.click(Button.left, 1)
    k=k+1
    if y == "error":
        print "error 66"
    else:
        i=0
        while i < 6:
            mouse.position = (y[i][0], y[i][1])
            mouse.click(Button.left,1)
            time.sleep(1)
            farm()
            i=i+1
