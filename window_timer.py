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
        self.times = {}

        current = datetime.date.today()
        current = current + datetime.timedelta(days=-current.weekday(), weeks=0)
        file = str(current) + ".json"
        self.path = rf"C:\Users\tsrow\PycharmProjects\ScreenTime\data\{file}"

    # add program
    def add(self):
        """
        Adds new file if one for the week not found yet
        Classifies files based on the Monday of the current week
        :return:
        """

        with open(self.path, 'w') as writefile:
            writefile.seek(0)
            json.dump({}, writefile, indent=4)

        with open(self.path, 'r') as outfile:
            outfile.seek(0)
            self.times = json.load(outfile)

    def update(self, name):
        """
        Updates the dictionary for the current app being viewed
        :return:
        """
        curr_day = str(datetime.date.today().weekday())
        curr_hour = datetime.datetime.now().hour

        if name not in self.times.keys():
            self.create_app(name)
        else:
            self.times[name][str(curr_day)][str(curr_hour)] += 1

    def create_app(self, name):
        """
        Creates an entry for the new app in the json
        :param name: The name of the program
        """
        days = range(7)
        hours = range(24)
        new_dict = {str(x):{str(y):0 for y in hours} for x in days}
        self.times.update({name: new_dict})

    def send_to_json(self):
        with open(self.path, 'w') as writefile:
            writefile.seek(0)
            json.dump(self.times, writefile, indent=4)


class MainTimer:
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1200

    def __init__(self, apps=[]):
        self.apps = apps
        self.timer = TimesStruct()
        self.currentDay = datetime.datetime.today().weekday()
        self.startSecond = datetime.datetime.now().second
        self.corners = {1080: (1536, 824), 1200: (1536, 920)}  # which tuple of pixels corresponds to a full screen window
        # each display size - 1440p, 4K, ultrawide need to be added

    def get_current_window(self):
        """
        Gets the current window, updates if the proper tick
        :return:
        """
        current_second = datetime.datetime.now().second
        fore_proc = proc.GetWindowThreadProcessId(gui.GetForegroundWindow())[1]
        for p in util.process_iter(['pid', 'name']):
            if p.pid == fore_proc and not self.startSecond == current_second:
                print(p.info)
                name = p.name()[0].upper() + p.name()[1:-4]
                print(name)
                self.timer.update(name)
                self.startSecond = datetime.datetime.now().second

    def get_processes(self, hwnd, extra):
        if gui.IsWindowVisible(hwnd):
            # print(f'Window Id: {proc.GetWindowThreadProcessId(hwnd)[0]}, Window Name: {gui.GetWindowText(hwnd)}')
            self.apps.append(proc.GetWindowThreadProcessId(hwnd)[1])
        #print(self.apps)

    """
    def window_bounds(self, hwnd, extra=None):
        if gui.IsWindowVisible(hwnd):
            print(hwnd, gui.GetClientRect(hwnd))
    """


if __name__ == "__main__":
    m = MainTimer()
    # somehow enumwindows passes all the handlers into the func
    ##gui.EnumWindows(m.window_bounds, None)
    for i in range(1, 10):
        m.get_current_window()
    m.timer.send_to_json()


# print(gui.GetClientRect(gui.GetForegroundWindow()))
"""
Checklist - 

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