import pyautogui

pyautogui.keyDown("alt")
pyautogui.keyDown("tab")

pyautogui.keyUp("alt")
pyautogui.keyUp("tab")

str = "./nikto.pl -h http://www.example.com"
pyautogui.write(str)

pyautogui.keyDown("enter")
pyautogui.keyUp("enter")