from win32api import GetSystemMetrics
import win32api, win32con
import pyautogui

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))

pyautogui.size()
print(pyautogui.size())



def move(x,y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


