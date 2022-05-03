import sys
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
import datetime
import numpy as np
import graphs as graph
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QLabel, QWidget, \
    QPushButton, QHBoxLayout, QDialog, QScrollArea, QGroupBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *


class MainWindow(QWidget):
    """
    The main widget as a container for all other widgets
    """
    def __init__(self):
        super().__init__()
        self.WINDOW_WIDTH = int(1920 / 4)
        self.WINDOW_HEIGHT = int(1200 / 1.9)

        self.week = WeekDay(self, self.WINDOW_HEIGHT, self.WINDOW_WIDTH)
        self.init_app()
        self.show()

    def init_app(self):
        self.setStyleSheet("background-color: #ffffff;")
        self.setFixedSize(self.WINDOW_WIDTH + 30, self.WINDOW_HEIGHT)


class WeekDay(QWidget):
    """
    Widget of buttons that decides whether a week or a day graph is shown
    """
    def __init__(self, main_wind, height, width):
        super().__init__(main_wind)
        self.main_wind = main_wind
        self.current = CurrentWD(height, width)
        self.half = int(width / 2)
        self.init_ui()

    def init_ui(self):
        """
        Creates the "week" and "day" that change the mode of the app
        """
        hbox = QHBoxLayout()
        week = QPushButton("Week", self.main_wind)

        week.setStyleSheet(f"min-width: {self.half}px;"
                           "background-color: #c0f6b8;")
        week.setFont(QFont("Agenda One", 10))
        week.clicked.connect(lambda: self.clicked("week"))

        day = QPushButton("Day", self.main_wind)

        day.setStyleSheet(f"min-width: {self.half}px;"
                          "background-color: #c0f6b8;")
        day.setFont(QFont("Agenda One", 10))
        day.clicked.connect(lambda: self.clicked("day"))

        hbox.addWidget(week)
        hbox.addWidget(day)

        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        all_parts = QVBoxLayout()
        all_parts.addLayout(hbox)
        all_parts.addWidget(self.current)

        all_parts.setContentsMargins(5, 5, 5, 5)
        all_parts.setSpacing(0)
        self.setLayout(all_parts)

    def clicked(self, mode):
        """
        Function that controls what happens to the app when the week button is clicked
        Changes current day/week label
        """
        self.current.change_label(mode)

        # app = AppInfo("Pycharm64")
        # all_parts.addWidget(app)


class CurrentWD(QWidget):
    """
    Creates class for switching days/weeks
    """
    def __init__(self, height, width):
        super().__init__()
        self.curr_date = datetime.date.today()
        self.graph = CurrentGraph(height, width)

        self.mode = "day"
        self.label = QPushButton("<", self)
        self.label2 = QLabel(self.curr_date.strftime("%A, %B %d, %Y"), self)
        self.label3 = QPushButton(">", self)
        self.init_ui()

    def init_ui(self):
        """
        Creates current day/week label and two buttons for moving forward and backward
        """
        hbox = QHBoxLayout()

        self.label.clicked.connect(lambda: self.change_by_one(False))
        self.label.setStyleSheet("background-color: #bef3f6;")
        self.label3.clicked.connect(lambda: self.change_by_one(True))
        self.label3.setStyleSheet("background-color: #bef3f6;")

        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFont(QFont('Agenda One', 10))
        self.label2.setStyleSheet("background-color: #bef3f6;")

        hbox.addWidget(self.label)
        hbox.addWidget(self.label2)
        hbox.addWidget(self.label3)

        hbox.setStretch(0, 10)  # set stretch for relative spacings,
        # size policy for absolute relative max and min
        hbox.setStretch(1, 80)
        hbox.setStretch(2, 10)

        hbox.setContentsMargins(0, 0, 0, 0)
        # m.setSpacing(0)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.graph)
        vbox.setContentsMargins(0, 0, 0, 0)

        self.setLayout(vbox)

    def change_label(self, given_mode):
        """
        Changes whether the label displays time by weeks or days
        :param given_mode: Week mode or Day mode
        """
        if given_mode == "day":
            self.curr_date = datetime.date.today()
        if given_mode == "week":
            self.curr_date += datetime.timedelta(days=-self.curr_date.weekday(), weeks=0)

        self.mode = given_mode
        self.check_mode(self.mode)
        self.graph.plot(self.mode, datetime.datetime.today().weekday())

    def change_by_one(self, forward):
        """
        Changes the day by either forward one or backwards one
        :param forward: whether we are moving forwards or backwards one
        """
        if self.mode == "day" and self.check_day(forward):
            self.curr_date += datetime.timedelta(days=(1 if forward else -1))
        if self.mode == "week" and self.check_week(forward):
            self.curr_date += datetime.timedelta(weeks=(1 if forward else -1))

        self.check_mode(self.mode)
        self.graph.change_by_one(self.mode, self.curr_date)

    def check_day(self, forward):
        """
        :param forward: whether we are moving forwards or backwards one day
        :return: whether the day exists in a data file
        """
        path = self.graph.set_path(self.curr_date + datetime.timedelta(days=-1))
        if forward and self.curr_date == datetime.date.today():
            return False
        if not forward and not path:
            return False
        return True

    def check_week(self, forward):
        """
        :param forward: whether we are moving forwards or backwards one week
        :return: whether the week file exists
        """
        path = self.graph.set_path(self.curr_date + datetime.timedelta(weeks=(1 if forward else -1)))
        if not path:
            return False
        return True

    def check_mode(self, mode):
        """
        Updates the date label to reflect the current date
        :param mode: either day or week
        """
        if mode == "day":
            self.label2.setText(self.curr_date.strftime("%A, %B %d, %Y"))
        if mode == "week":
            self.label2.setText(f'Week of Monday, {self.curr_date.strftime("%B %d, %Y")}')


class CurrentGraph(QDialog):
    """
    Contains the current graph according to button presses
    """
    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width
        self.name = "RunningTotal"
        self.data = graph.TotalCreator(self.name)
        self.curr_date = datetime.date.today()

        self.apps = QScrollArea()
        self.apps.setFixedHeight(300)
        self.days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
        self.hours = range(24)
        self.mode_var = "day"

        self.add_apps()

        self.figure = Figure()
        self.figure.set_figwidth(2)
        self.figure.set_figheight(2.5)
        self.figure.set_facecolor("#cecece")

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.apps)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        self.plot(self.mode_var, datetime.date.today().weekday())

    def add_apps(self):
        """
        Adds all apps seen in the current week file to the app list (displayed in the class below)
        """
        names = list(self.data.get_names())
        v_apps = QVBoxLayout()
        for x in names:
            if not x == "ShellExperienceHost":
                a = AppInfo(self, x, self.width, self.curr_date, self.mode_var)
                v_apps.addWidget(a)
        if self.name not in names:
            self.name = "RunningTotal"
            self.data = graph.TotalCreator(self.name)
        v_apps.setContentsMargins(5, 5, 5, 25)
        gb = QGroupBox()
        gb.setLayout(v_apps)
        gb.setAlignment(Qt.AlignCenter)
        self.apps.setWidget(gb)

    def plot(self, mode, day):
        """
        :param mode: either week or day
        :param day: the given day we want to plot (week mode will just plot the whole week)
        Plots either the week or day
        """

        self.mode_var = mode
        self.add_apps()
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # random data
        if mode == "day":
            data = self.data.get_day_total(day)
            x_axis = self.hours
            ax.axes.set_ylim(0, 60)
        if mode == "week":
            data = self.data.get_week_total()
            x_axis = self.days
            ax.axes.set_ylim(0, 24)

        ax.bar(x_axis, data, color='maroon', width=0.4)
        self.canvas.draw()

    def change_by_one(self, mode, date):
        """
        Changes the graph depending on the mode (day calculation handled in CurrentWD class)
        :param mode: either week or day
        :param date: the current date we are at (changed in the CurrentWD class)
        """
        self.mode_var = mode
        self.curr_date = date
        self.add_apps()
        self.plot(mode, date.weekday())

    def set_path(self, date):
        """
        :param date: the current date
        Sets a new data path according to the given date
        """
        week_date = date + datetime.timedelta(days=-date.weekday(), weeks=0)
        return self.data.set_path(week_date)

    def change_data_name(self, name):
        """
        Changes the graph to display the data of a specific app (or the total)
        :param name: the name of the app we want to display
        """
        self.name = name
        self.data = graph.TotalCreator(self.name)
        self.plot(self.mode_var, self.curr_date.weekday())


class AppInfo(QWidget):
    """
    Contains a single app's name and the time spent on the app
    """
    def __init__(self, parent, name, width, day, mode):
        super().__init__()
        self.parent = parent
        self.name = name
        self.data = graph.TotalCreator(name)
        self.set_path(day)
        self.width = int(width / 2.2)
        self.mode = mode

        h = QHBoxLayout()
        app = QPushButton(name)
        app.setFont(QFont('Agenda One', 12))
        app.setFlat(True)
        app.setMinimumWidth(self.width)
        app.setStyleSheet("text-align: left;"
                          "background-color: #bef3f6;")
        app.clicked.connect(self.change_graph)

        if mode == "day":
            times = self.data.get_day_total(day.weekday())
        if mode == "week":
            times = self.data.get_week_total()

        total_time = int(np.sum(times))
        time = QPushButton(str(total_time))
        time.setFont(QFont('Agenda One', 12))
        time.setMinimumWidth(self.width)
        time.setFlat(True)
        time.setStyleSheet("text-align: right;"
                           "background-color: #bef3f6;")
        time.clicked.connect(self.change_graph)

        h.addWidget(app)
        h.addWidget(time)
        h.setContentsMargins(0, 0, 0, 0)
        self.setLayout(h)

    def change_graph(self):
        """
        Changes what app the graph shows
        """
        self.parent.change_data_name(self.name)

    def set_path(self, date):
        """
        :param date: the current date
        Sets a new data path according to the given date
        """
        week_date = date + datetime.timedelta(days=-date.weekday(), weeks=0)
        # print(week_date)
        self.data.set_path(week_date)


"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
"""


def main_func():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())