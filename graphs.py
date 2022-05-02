"""
Working on it
"""
import matplotlib.pyplot as plt
import jsonutils as jsutils
import numpy as np
import os
import datetime

one_app = {
            "Firefox": {
                # 0 IS MONDAY!!!
                "0": {
                    "0": 10, "1": 1500, "2": 3000, "3": 40000, "4": 140000, "5": 0,
                    "6": 0, "7": 0, "8": 0, "9": 100330, "10": 0, "11": 0,
                    "12": 0, "13": 0, "14": 70000, "15": 80000, "16": 100000, "17": 0,
                    "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0,
                },
                "1": {
                    "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                    "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,
                    "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                    "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0,
                },
                "2": {
                    "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                    "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,
                    "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                    "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0,
                },
                "3": {
                    "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                    "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,
                    "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                    "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0,
                },
                "4": {
                    "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                    "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,
                    "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                    "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0,
                },
                "5": {
                    "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                    "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,
                    "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                    "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0,
                },
                "6": {
                    "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                    "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,
                    "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                    "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0,
                }
            }
}


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
