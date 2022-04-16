import win32process as proc
import win32gui as gui
import time as time
import psutil as util
import win32pdh as pdh
from win32com.server.exception import COMException

# import psutil


class MainTimer:
    times = {}
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1200

    def __init__(self, apps=[], wmi_apps=[]):
        self.apps = apps
        self.wmi_apps = wmi_apps

    def get_processes(self, hwnd, extra):
        if gui.IsWindowVisible(hwnd):
            # print(f'Window Id: {proc.GetWindowThreadProcessId(hwnd)[0]}, Window Name: {gui.GetWindowText(hwnd)}')
            self.apps.append(proc.GetWindowThreadProcessId(hwnd)[1])
        #print(self.apps)

    def window_bounds(self, hwnd, extra):
        if gui.IsWindowVisible(hwnd):
            print(gui.GetClientRect(hwnd))

if __name__ == "__main__":

    m = MainTimer()
    # somehow enumwindows passes all the handlers into the func
    gui.EnumWindows(m.window_bounds, None)

    for i in range(100):
        time.localtime()
        gui.EnumWindows(m.get_processes, None)
        foreProc = proc.GetWindowThreadProcessId(gui.GetForegroundWindow())[1]
        for p in util.process_iter(['pid', 'name']):
            if p.pid == foreProc:
                print(p.info)
        print(time.localtime())

"""
Checklist - 
declare current resolution width and height as static vars

Check if Window in foreground:
    if window is on either left side or right side, detect dual split windows and find matching window
        Take time for both windows
        - use getwindowrect to see if a window's upper left is the dual split coordinate
        - WARNING - dual split coordinates are different depending if the window is the foreground window or not""
    if windows in either corners, detect corner windows
        Take time for all current visible windows
        
    if ANY OTHER window size state (full screen, partial screen)
        Take time for current foreground window
        
    Save to times
    Every x seconds, call update method that writes times to json/csv
    
    All good
    
"""




# oiaefnoaesnfae
#bfas;ehf ioasefb aesf