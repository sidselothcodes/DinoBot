from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pyautogui
import time

# Constants
DINOSAUR_GAME_URL = "https://elgoog.im/t-rex/"
JUMP_PIXEL_VALUE = (83, 83, 83)  
RESTART_BUTTON_COR = (956, 429)  
XCOR_1, XCOR_2, YCOR = 745, 765, 460 
JUMP_COUNT = 0 


options = Options()
options.add_argument("--incognito")


chrome_driver_path = "/usr/local/bin/chromedriver-mac-x64/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)


driver.get(DINOSAUR_GAME_URL)
driver.maximize_window()


time.sleep(5)


pyautogui.click(RESTART_BUTTON_COR)
time.sleep(1)  
pyautogui.press('space') 


def jump():
    """Simulate a jump by pressing the space key."""
    pyautogui.keyDown('space')
    time.sleep(0.1)  
    pyautogui.keyUp('space')
    print("Jump!")


while True:
    im = pyautogui.screenshot() 


    print(f"Pixel 1: {im.getpixel((XCOR_1, YCOR))}")
    print(f"Pixel 2: {im.getpixel((XCOR_2, YCOR))}")
    print(f"Pixel 3: {im.getpixel((XCOR_1 + 1, YCOR))}")


    px1 = im.getpixel((XCOR_1, YCOR))
    px2 = im.getpixel((XCOR_2, YCOR))
    px3 = im.getpixel((XCOR_1 + 1, YCOR))


    if px1 == JUMP_PIXEL_VALUE or px2 == JUMP_PIXEL_VALUE or px3 == JUMP_PIXEL_VALUE:
        jump()  
        JUMP_COUNT += 1 


        if JUMP_COUNT == 8:
            XCOR_2 += 5  
            JUMP_COUNT = 0 


    time.sleep(0.01)
