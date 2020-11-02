# -*- coding: cp1250 -*-
from Hypori_kor import terkep
from pynput.mouse import Button, Controller
from city_select import select
import time

def farm (size):
    if size == 1:  #10 perces várakozás
        mouse.position = (525,600)
        mouse.click(Button.left,1)
    elif size == 2: #40 perces
        mouse.position = (664,582)
        mouse.click(Button.left,1)
    elif size == 3: #3 órás várakozás
        mouse.position = (834,582)
        mouse.click(Button.left,1)
    elif size == 3: #8 órás várakozás
        mouse.position = (1000,582)
        mouse.click(Button.left,1)
    else:
        print "alma"
    #10 bezárás
    mouse.position=(1135,190)
    mouse.click(Button.left,1)
    
city = ["Hypori","Alzoc","Anaxes","Atzerri"]
size = 1


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
            farm(size)
            i=i+1
