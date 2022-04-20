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
import window_timer as wt
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
        self.current = CurrentWD()
        self.graph = CurrentGraph()
        self.half = half
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        week = QPushButton("Week", self.main_wind)

        week.setStyleSheet(f"min-width: {self.half}px;")
        week.setFont(QFont("Agenda One", 10))

        day = QPushButton("Day", self.main_wind)

        day.setStyleSheet(f"min-width: {self.half}px;")
        day.setFont(QFont("Agenda One", 10))

        hbox.addWidget(week)
        hbox.addWidget(day)

        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        all_parts = QVBoxLayout()
        all_parts.addLayout(hbox)
        all_parts.addWidget(self.current)
        all_parts.addWidget(self.graph)

        for i in range(5):
            app = AppInfo("F", "F")
            all_parts.addWidget(app)

        all_parts.setContentsMargins(5, 5, 5, 5)
        all_parts.setSpacing(0)
        self.setLayout(all_parts)


class CurrentWD(QWidget):
    """
    Creates class for switching days/weeks
    """
    def __init__(self):
        super().__init__()
        # self.parent = parent
        self.init_ui()

    def init_ui(self):
        m = QHBoxLayout()
        label = QPushButton("<", self)
        label2 = QLabel("Date Date Date", self)
        label2.setAlignment(Qt.AlignCenter)
        label2.setFont(QFont('Agenda One', 12))
        label3 = QPushButton(">", self)

        m.addWidget(label)
        m.addWidget(label2)
        m.addWidget(label3)

        m.setStretch(0, 10) # set stretch for relative spacings, size policy for absolute relative max and min
        m.setStretch(1, 80)
        m.setStretch(2, 10)

        m.setContentsMargins(0, 0, 0, 0)
        #m.setSpacing(0)
        self.setLayout(m)


class CurrentGraph(QDialog):
    """
    Contains the current graph according to button presses
    """
    def __init__(self):
        super().__init__()
        self.figure = Figure()
        self.figure.set_figwidth(2)
        self.figure.set_figheight(2.5)
        self.figure.set_facecolor("#cecece")
        q = QWidget()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.plot()

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [2 for i in range(10)]

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()


class AppInfo(QWidget):
    """
    Contains a single app's name and it's time
    """
    def __init__(self, name, time):
        super().__init__()
        self.name = name
        self.time = time

        h = QHBoxLayout()
        app = QPushButton(name, self)
        app.setFlat(True)

        app.setStyleSheet("text-align: left")

        time = QPushButton(time, self)
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