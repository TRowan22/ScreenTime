"""
Working on it
"""
import matplotlib.pyplot as plt
import jsonutils as jsutils
import numpy as np
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


class GraphCreator:
    def __init__(self):
        self.path = jsutils.find_current_path()
        self.data = jsutils.read(self.path)

    def create_day(self, day):
        day = self.data["RunningTotal"][day]

        hours = list(day.keys())
        seconds = list(day.values())

        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(hours, seconds, color='maroon',
                width=0.4)

        plt.xlabel("Hour")
        plt.ylabel("Minutes spent")
        plt.show()

    def create_day_test(self):
        day = one_app["Firefox"]["0"]

        hours = list(day.keys())
        seconds = np.array(list(day.values())) / 3600

        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(hours, seconds, color='maroon',
                width=0.4)

        plt.xlabel("Hour")
        plt.ylabel("Minutes spent")
        plt.show()

   # def create_week(self, week):


if __name__ == "__main__":
    g = GraphCreator()
    g.create_day_test()