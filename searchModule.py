import pyautogui
import pyperclip

def openWiki():
    pyautogui.press('win')
    pyautogui.typewrite("https://www.wikipedia.org/")
    pyautogui.typewrite(["enter"])

def newTab():
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite("https://www.wikipedia.org/")
    pyautogui.typewrite(["enter"])

def searchWiki(title):
    pyautogui.click(1120, 570)
    pyautogui.typewrite(title)
    pyautogui.typewrite(["enter"])

def selectWeb():
    pyautogui.click(554, 53)
    pyautogui.hotkey('ctrl', 'c')
    url1 = pyperclip.paste()
    return url1

