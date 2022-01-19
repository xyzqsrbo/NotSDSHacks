import numpy as np
import pyautogui
import pydirectinput
import time
import keyboard

while 1:
    #exit pause
    if keyboard.is_pressed('e'):
        break

while (keyboard.is_pressed("q") == False):

    #Pause thing
    if keyboard.is_pressed('w'):
        while 1:
            
            #exit pause
            if keyboard.is_pressed('e'):
                break
        
    if np.array_equal(pyautogui.pixel(1822,755), [96,41,30]):
        pyautogui.click(1823,757)
    if np.array_equal(pyautogui.pixel(744,152), [178,225,255]):
        pyautogui.click(898,296)
    #966,874 255,174,64 #FFAE40
    if np.array_equal(pyautogui.pixel(1217,238), [85,8,132]):
        pyautogui.click(1217,238)
    if np.array_equal(pyautogui.pixel(966,874), [255,174,64]):
        pyautogui.click(966,874)

    if np.array_equal(pyautogui.pixel(859,719), [34,6,45]):
        pyautogui.click(859,719)
    
    if np.array_equal(pyautogui.pixel(1162,815), [116,93,61]):

        try:  
            x, y = pyautogui.locateCenterOnScreen('gowther.png', grayscale = False, confidence = .5)  
        except TypeError:  
            pyautogui.click(863,813) 
        else:  
            try:  
                x, y = pyautogui.locateCenterOnScreen('liz.png', grayscale = False, confidence = .5)  
            except TypeError:  
                pyautogui.click(863,813)   
            else:  
                time.sleep(8.6)
                if np.array_equal(pyautogui.pixel(1132,587), [61,19,22]): 
                    pyautogui.click(1150,809)  
            finally:  
                pyautogui.click(863,813)
        finally:  
            pyautogui.click(863,813)
        
        
    if np.array_equal(pyautogui.pixel(1021,972), [41,28,18]):
        pyautogui.click(1018,974)

    
    
    #1487,854 194,180,178 #C2B4B2
    #1496,884 163,0,120 #A30078
    if np.array_equal(pyautogui.pixel(1496,884), [163,0,120]) and np.array_equal(pyautogui.pixel(1487,854), [194,180,178]): #first turn check
        time.sleep(3)
        pydirectinput.click(1589,927) #play cleanse
        pyautogui.mouseDown()
        pyautogui.mouseUp()
       
        #841,756 115,171,185 #73ABB9
        while np.array_equal(pyautogui.pixel(841,756), [115,171,185]) == False: #check for rank up before moving on
            demon = 0
        pydirectinput.click(1406,907) #play liz card
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(1.5)
        pydirectinput.click(1486,903) #play liz card
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        while 1:
            try:  
                x, y = pyautogui.locateCenterOnScreen('turn.png', grayscale = False, confidence = .8)  
            except TypeError:  
                demon = 0
            else:  
                pydirectinput.click(1776,934) #Use zara ST card (first slot)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(.5)
                pydirectinput.click(1314,907) #Use last card
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(.5)
                pydirectinput.click(1406,931) #Use second to last card
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                break
            finally:  
                demon = 0

        while 1:
            try:  
                x, y = pyautogui.locateCenterOnScreen('turn.png', grayscale = False, confidence = .8)  
            except TypeError:  
                demon = 0
            else:  
                pydirectinput.click(1794,937) #Use zara aoe card (first slot)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(.5)
                pydirectinput.click(1411,918) # use second to last card
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                time.sleep(.5)
                pydirectinput.click(1479,932) # use third to last card
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                break
            finally:  
                demon = 0
            
        

    if np.array_equal(pyautogui.pixel(1048,658), [29,205,227]): #end fight
        pyautogui.click(1006,974)
    if np.array_equal(pyautogui.pixel(922,589), [158,77,52]): #deny friend
        pyautogui.click(919,590)
    if np.array_equal(pyautogui.pixel(919,584), [227,97,41]): #deny friend
        pyautogui.click(919,590)
    if np.array_equal(pyautogui.pixel(1037,611), [182,158,110]):
        pyautogui.click(1037,611)

    #some dumb fuck invited you than canceled like a retard
    #945,626 142,116,79 #8E744F
    if np.array_equal(pyautogui.pixel(1007,586), [56,187,131]):
        pyautogui.click(1007,586)
    if np.array_equal(pyautogui.pixel(1037,586), [151,125,80]):
        pyautogui.click(1017,586)

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
