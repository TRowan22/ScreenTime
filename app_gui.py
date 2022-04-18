"""
Week - Day buttons

Graph

List of apps          Time Spent
(bar scaled by how much time spent)
"""
import sys
import window_timer as wt
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget, \
    QPushButton, QLineEdit, QHBoxLayout, QDockWidget, QSizePolicy
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
        self.half = half
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        week = QPushButton("Week", self.main_wind)

        week.setStyleSheet(f"min-width: {self.half}px;")

        day = QPushButton("Day", self.main_wind)

        day.setStyleSheet(f"min-width: {self.half}px;")

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
        label2.setFont(QFont('Arial', 12))
        label3 = QPushButton(">", self)

        m.addWidget(label)
        m.addWidget(label2)
        m.addWidget(label3)

        m.setStretch(0, 10) #set stretch for relative spacings, size policy for absolute relative max and min
        m.setStretch(1, 80)
        m.setStretch(2, 10)

        m.setContentsMargins(0, 0, 0, 0)
        #m.setSpacing(0)
        self.setLayout(m)


class CurrentGraph(QWidget):
    """
    Contains the current graph according to button presses
    """
    def __init__(self):
        super().__init__()
        self.timer = wt.MainTimer()
        self.initUi()

    def initUI(self):
        current = QHBoxLayout()


class AppInfo(QWidget):
    """
    Contains a single app's name and it's time
    """
    def __init__(self, name, time):
        super().__init__()
        self.name = name
        self.time = time

        h = QHBoxLayout()
        app = QLabel(name, self)
        time = QLabel(time, self)
        time.setAlignment(Qt.AlignRight)

        h.addWidget(app)
        h.addWidget(time)
        h.setContentsMargins(0, 0, 0, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())