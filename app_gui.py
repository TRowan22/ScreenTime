"""
Week - Day buttons

Graph

List of apps          Time Spent
(bar scaled by how much time spent)
"""
import sys
import PyInstaller
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
import datetime
import numpy as np
import graphs as graph
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget, \
    QPushButton, QLineEdit, QHBoxLayout, QDockWidget, QSizePolicy, QDialog
from PyQt5.QtGui import QPixmap, QPalette, QIcon, QFont
from PyQt5.QtCore import *


class MainWindow(QWidget):
    """
    The main widget as a container for all other widgets
    """
    def __init__(self):
        super().__init__()
        self.WINDOW_WIDTH = int(1920 / 4)
        self.WINDOW_HEIGHT = int(1200 / 2)

        self.week = WeekDay(self, int(self.WINDOW_WIDTH / 2))
        self.init_app()
        self.show()

    def init_app(self):
        self.setStyleSheet("background-color: #cecece;")
        self.setFixedSize(self.WINDOW_WIDTH + 30, self.WINDOW_HEIGHT)


class WeekDay(QWidget):
    """
    Widget of buttons that decides whether a week or a day graph is shown
    """
    def __init__(self, main_wind, half):
        super().__init__(main_wind)
        self.main_wind = main_wind
        self.graph = CurrentGraph()
        self.current = CurrentWD(self.graph)
        self.half = half
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        week = QPushButton("Week", self.main_wind)

        week.setStyleSheet(f"min-width: {self.half}px;")
        week.setFont(QFont("Agenda One", 10))
        week.clicked.connect(lambda: self.clicked("week"))

        day = QPushButton("Day", self.main_wind)

        day.setStyleSheet(f"min-width: {self.half}px;")
        day.setFont(QFont("Agenda One", 10))
        day.clicked.connect(lambda: self.clicked("day"))

        hbox.addWidget(week)
        hbox.addWidget(day)

        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        all_parts = QVBoxLayout()
        all_parts.addLayout(hbox)
        all_parts.addWidget(self.current)
        all_parts.addWidget(self.graph)


        app = AppInfo("Pycharm64")
        all_parts.addWidget(app)

        all_parts.setContentsMargins(5, 5, 5, 5)
        all_parts.setSpacing(0)
        self.setLayout(all_parts)

    def clicked(self, mode):
        """
        Function that controls what happens to the app when the week button is clicked
        Clicked just doesn't error and returns error codes because they hate you
        """
        self.current.change_label(mode)


class CurrentWD(QWidget):
    """
    Creates class for switching days/weeks
    """
    def __init__(self, graphP):
        super().__init__();
        self.curr_date = datetime.date.today()
        self.week_start = self.curr_date + datetime.timedelta(days=-self.curr_date.weekday(), weeks=0)
        self.graph = graphP

        self.mode = "day"
        self.label = QPushButton("<", self)
        self.label2 = QLabel(self.curr_date.strftime("%A, %B %d, %Y"), self)
        self.label3 = QPushButton(">", self)
        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()

        self.label.clicked.connect(lambda: self.change_by_one(False))
        self.label3.clicked.connect(lambda: self.change_by_one(True))

        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFont(QFont('Agenda One', 10))

        hbox.addWidget(self.label)
        hbox.addWidget(self.label2)
        hbox.addWidget(self.label3)

        hbox.setStretch(0, 10) # set stretch for relative spacings, size policy for absolute relative max and min
        hbox.setStretch(1, 80)
        hbox.setStretch(2, 10)

        hbox.setContentsMargins(0, 0, 0, 0)
        #m.setSpacing(0)
        self.setLayout(hbox)

    def change_label(self, given_mode):
        """
        Changes whether the label displays time by weeks or days
        :param mode: Week mode or Day mode
        """
        self.curr_date = datetime.date.today()
        self.week_start = self.curr_date + datetime.timedelta(days=-self.curr_date.weekday(), weeks=0)

        self.check_mode(given_mode)
        self.graph.plot(given_mode, datetime.datetime.today().weekday())

    def change_by_one(self, forward):
        self.curr_date = self.curr_date + datetime.timedelta(days=(1 if forward else -1))
        self.week_start = self.week_start + datetime.timedelta(weeks=(1 if forward else -1))

        self.check_mode(self.mode)
        self.graph.change_by_one(self.mode, forward)

    def check_mode(self, mode):
        if mode == "day":
            self.label2.setText(self.curr_date.strftime("%A, %B %d, %Y"))
            self.mode = "day"
        if mode == "week":
            self.label2.setText(f'Week of Monday, {self.week_start.strftime("%B %d, %Y")}')
            self.mode = "week"



class CurrentGraph(QDialog):
    """
    Contains the current graph according to button presses
    """
    def __init__(self):
        super().__init__()
        self.data = graph.TotalCreator("RunningTotal")
        self.days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
        self.hours = range(24)
        self.mode_var = "day"
        self.curr_weekday = datetime.datetime.today().weekday()


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
        self.setLayout(layout)

        self.plot(self.mode_var, self.curr_weekday)

    def plot(self, mode, day):
        """
        :param mode: either week or day
        Plots either the week or day
        """
        # random data
        if mode == "day":
            data = self.data.get_day_total(day)
            x_axis = self.hours
        if mode == "week":
            data = self.data.get_week_total()
            x_axis = self.days

        self.mode_var = mode
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(x_axis, data, color='maroon', width=0.4)
        self.canvas.draw()

    def change_by_one(self, mode, forward):
        if mode == "day":
            temp_week = self.curr_weekday + (1 if forward else -1)

            if temp_week == 8:
                self.curr_weekday = 0
            elif temp_week == -1:
                self.curr_weekday = 7
            else:
                self.curr_weekday = temp_week
            print(self.curr_weekday)
        if mode == "week":
            self.data.set_path(self.curr_date + datetime.timedelta(days=-self.curr_date.weekday(), weeks=(1 if forward else -1)))
        self.plot(mode, self.curr_weekday)


class AppInfo(QWidget):
    """
    Contains a single app's name and it's time
    """
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.data = graph.TotalCreator(name)

        h = QHBoxLayout()
        app = QPushButton(name, self)
        app.setFont(QFont('Agenda One', 12))
        app.setFlat(True)

        app.setStyleSheet("text-align: left")

        total_time = np.sum(self.data.get_day_total(2))
        time = QPushButton(str(int(total_time)), self)
        time.setFont(QFont('Agenda One', 12))
        time.setFlat(True)

        time.setStyleSheet("text-align: right");

        h.addWidget(app)
        h.addWidget(time)
        h.setContentsMargins(50, 12, 55, 0)
        self.setLayout(h)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())