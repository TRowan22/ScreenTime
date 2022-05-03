"""
Working on it
"""
import jsonutils as jsutils
import numpy as np
import os


class TotalCreator:
    """
    Retrieves data from the running total and sends it to the GUI

    get_day_total - returns array containing the total minutes spent each hour in day
    get_week_total - returns array containing the total hours spent each day in week
    """

    def __init__(self, name):
        self.path = jsutils.JsonUtils.find_current_path()
        self.data = jsutils.JsonUtils.read(self.path)
        self.name = name

    def get_day_total(self, day):
        """
        :param day: the day we wanted to check
        :return: the hours spent on the computer during that day in an array
        """
        app = self.data[self.name][str(day)]
        hours = np.array(list(app.values()))

        hours = hours / 60

        return list(hours)

    def get_week_total(self):
        """
        :return: the hours spent on the computer each day in an array for a week
        """
        total = []
        for i in range(7):
            total.append(sum(self.get_day_total(i)))

        total = np.array(total) / 60

        return list(total)

    def set_path(self, curr_week):
        """
        Sets this object's data path to another file
        :param curr_week: the week file we want to find
        :return: Whether the file currently exists
        """

        path = jsutils.JsonUtils.convert_file(curr_week)
       # print(curr_week, os.path.isfile(path))
        if os.path.isfile(path):
            self.path = path
            self.data = jsutils.JsonUtils.read(self.path)
            return True
        else:
            return False

    def get_names(self):
        """
        :return: the names of all apps read in a certain weekly file
        """
        return self.data.keys()
