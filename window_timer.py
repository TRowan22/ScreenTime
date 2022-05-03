import win32process as proc
import win32gui as gui
import psutil as util
import datetime
import jsonutils as jsutils
import os
import threading, time


class TimesStruct:
    def __init__(self):
        """
        Finds the path of the week file that contains the current date
        If path is not a file yet, create it
        Else read the data from it
        """
        self.path = jsutils.JsonUtils.find_current_path()

        if os.path.isfile(self.path):
            self.times = jsutils.JsonUtils.read(self.path)
        else:
            self.add()

    # add program
    def add(self):
        """
        Adds new file if one for the week not found yet
        Classifies files based on the Monday of the current week
        :return:
        """

        jsutils.JsonUtils.write(self.path, {})
        self.times = jsutils.JsonUtils.read(self.path)
        self.create_app("RunningTotal")

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
            self.times[name][str(curr_day)][str(curr_hour)] += 5

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
        """
        Updates the current JSON file with modified data
        """
        jsutils.JsonUtils.write(self.path, self.times)


class MainTimer:
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1200

    def __init__(self):
        self.timer = TimesStruct()

    def get_current_window(self):
        """
        Gets the current window, updates if the proper tick
        """
        fore_proc = proc.GetWindowThreadProcessId(gui.GetForegroundWindow())[1]
        for p in util.process_iter(['pid', 'name']):
            if p.pid == fore_proc:
                name = p.name()[0].upper() + p.name()[1:-4]
                self.timer.update(name)
                #print(datetime.datetime.now().second)
                #print(name)
                self.timer.update("RunningTotal")

    def update(self):
        """
        Updates the json file the timer currently points to.
        """
        self.timer.send_to_json()


def main_func():
    m = MainTimer()
    m.update()

    start_time = datetime.datetime.now()
    while True:
        curr_time = datetime.datetime.now()
        if not start_time + datetime.timedelta(seconds=5) >= curr_time:
            m.get_current_window()
            m.timer.send_to_json()
            start_time = curr_time
        time.sleep(1)


