import time
import pyautogui
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
pyautogui.click(1215, 1061)
time.sleep(5)
pyautogui.write('facebook.com', interval=0.25)
pyautogui.press('enter')
time.sleep(7)
pyautogui.click(723, 560)
time.sleep(10)
pyautogui.write('yeu anh thuan hoang dep trai pro vip', interval=0.25)
pyautogui.click(920, 780)