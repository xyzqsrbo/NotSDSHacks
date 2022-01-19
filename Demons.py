import numpy as np
import pyautogui
import time
import keyboard
import random
# Hold 1 for red, 2 for gray, 3 for crimson
# Hold q to quit, Hold w to pause, press e to resume
demon = 0

while demon == 0:
    if keyboard.is_pressed('1'):
        demon = 1
    elif keyboard.is_pressed('2'):
        demon = 2
    elif keyboard.is_pressed('3'):
        demon = 3

while keyboard.is_pressed('q') == False:
    
    #Pause thing
    if keyboard.is_pressed('w'):
        while 1:
            #choose demon while paused
            if keyboard.is_pressed('1'):
                demon = 1
            elif keyboard.is_pressed('2'):
                demon = 2
            elif keyboard.is_pressed('3'):
                demon = 3
            #exit pause
            if keyboard.is_pressed('e'):
                break
    
    #Swap demons you want to run
    if keyboard.is_pressed('1'):
        demon = 1
    elif keyboard.is_pressed('2'):
        demon = 2
    elif keyboard.is_pressed('3'):
        demon = 3
        
    if np.array_equal(pyautogui.pixel(1822,755), [96,41,30]):
        pyautogui.click(1823,757)
    if np.array_equal(pyautogui.pixel(744,152), [178,225,255]):
        pyautogui.click(898,296)
    if demon == 1:
        if np.array_equal(pyautogui.pixel(825,841), [156,45,52]): #red demons
            pyautogui.click(827,832)
    elif demon == 2:
        if np.array_equal(pyautogui.pixel(1006,884), [74,76,85]): #gray demons
            pyautogui.click(1006,884)
    elif demon == 3:
        #1006,884 74,76,85 #4A4C55
        if np.array_equal(pyautogui.pixel(1189,883), [140,44,57]): #crim demons
            pyautogui.click(1189,883)
    if np.array_equal(pyautogui.pixel(859,719), [34,6,45]):
        pyautogui.click(859,719)
    if np.array_equal(pyautogui.pixel(1162,815), [116,93,61]):
        time.sleep(9)
        if np.array_equal(pyautogui.pixel(1132,587), [61,19,22]): 
            pyautogui.click(1150,809)
    if np.array_equal(pyautogui.pixel(1021,972), [41,28,18]):
        pyautogui.click(1018,974)
    if np.array_equal(pyautogui.pixel(1782,73), [200,174,133]) and np.array_equal(pyautogui.pixel(1801,54), [138,115,69]): #auto
        pyautogui.click(1782,52)
    if np.array_equal(pyautogui.pixel(1048,658), [29,205,227]): #end fight
        pyautogui.click(1006,974)
    if np.array_equal(pyautogui.pixel(922,589), [158,77,52]): #deny friend
        pyautogui.click(919,590)
    if np.array_equal(pyautogui.pixel(919,584), [227,97,41]): #deny friend
        pyautogui.click(919,590)

    #some dumb fuck invited you than canceled like a retard
    #945,626 142,116,79 #8E744F
    if np.array_equal(pyautogui.pixel(1007,586), [56,187,131]):
        pyautogui.click(1007,586)
    if np.array_equal(pyautogui.pixel(1037,586), [151,125,80]):
        pyautogui.click(1027,586)

    #you got a literal retard to auto with you and you lost
    if pyautogui.pixel(1098,596)[0] == 250: 
        pyautogui.click(966,987)
    if pyautogui.pixel(1037,600)[0] == 164: 
        pyautogui.click(1027,600)
    if np.array_equal(pyautogui.pixel(917,631), [155,70,44]):
        pyautogui.click(917,631)
    if np.array_equal(pyautogui.pixel(1823,757), [94,39,29]): 
        pyautogui.click(1822,756)
    if np.array_equal(pyautogui.pixel(945,626), [142,116,79]): 
        pyautogui.click(935,626)
