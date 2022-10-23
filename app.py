#m1
from asyncio import sleep
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


#m2
import pyautogui





#Method 1
def method1():
    time.sleep(1)
    button = Button.right
    mouse = Controller()
    mouse.click(button=button)
#Method 1



#Method 2
# pip install pyautogui
def method2():
    pyautogui.click(500,100)
#Method 2




#Keyboard Start
def keb():
    pyautogui.typewrite("Hello World")
#Keyboard End





#Main Function Start
def main():
    method2()
    time.sleep(1)
    keb()

if __name__=="__main__":
    main()
#Main Function End
