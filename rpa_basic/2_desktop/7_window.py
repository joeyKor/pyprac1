import pyautogui

fw = pyautogui.getActiveWindow() #현재 활성화된 창

print(fw.title)