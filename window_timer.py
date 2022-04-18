import win32process as proc
import win32gui as gui
import time as time
import psutil as util
import json
import datetime
import os
import win32pdh as pdh
from win32com.server.exception import COMException

# import psutil


class TimesStruct:
    def __init__(self):
        self.days = {}

    # add program
    def add(self):
        """
        Adds new file if one for the week not found yet
        Classifies files based on the Monday of the current week
        :return:
        """
        current = datetime.date.today()
        current = current + datetime.timedelta(days=-current.weekday(), weeks=1)
        file = str(current) + ".json"

        with open(rf"C:\Users\tsrow\PycharmProjects\ScreenTime\data\{file}", 'w') as writefile:
            writefile.seek(0)
            json.dump({}, writefile)

        with open(rf"C:\Users\tsrow\PycharmProjects\ScreenTime\data\{file}", 'r') as outfile:
            outfile.seek(0)
            self.days = json.load(outfile)

    # def update(self):


    # send program to json


class MainTimer:
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1200

    def __init__(self, apps=[], wmi_apps=[]):
        self.apps = apps
        self.timer = TimesStruct()
        self.currentDay = datetime.datetime.today().weekday()
        self.corners = {1080: (1536, 824), 1200: (1536, 920)}  # which tuple of pixels corresponds to a full screen window
        # each display size - 1440p, 4K, ultrawide need to be added

    def geetCurrentWindow(self):
        fore_proc = proc.GetWindowThreadProcessId(gui.GetForegroundWindow())[1]
        for p in util.process_iter(['pid', 'name']):
            if p.pid == fore_proc:
                print(p.info)
                print(p.name()[0].upper() + p.name()[1:-4])
                print(gui.GetClientRect(gui.GetForegroundWindow()))


    def get_processes(self, hwnd, extra):
        if gui.IsWindowVisible(hwnd):
            # print(f'Window Id: {proc.GetWindowThreadProcessId(hwnd)[0]}, Window Name: {gui.GetWindowText(hwnd)}')
            self.apps.append(proc.GetWindowThreadProcessId(hwnd)[1])
        #print(self.apps)

    def window_bounds(self, hwnd, extra=None):
        if gui.IsWindowVisible(hwnd):
            print(hwnd, gui.GetClientRect(hwnd))


if __name__ == "__main__":

    m = MainTimer()
    # somehow enumwindows passes all the handlers into the func
    gui.EnumWindows(m.window_bounds, None)

    times = TimesStruct()
    times.add()

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