"""
Week - Day buttons

Graph

List of apps          Time Spent
(bar scaled by how much time spent)
"""
import sys
import calendar
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPalette, QIcon
from PyQt5.QtCore import Qt

class WeekDay(QWidget):
    def __init__(self, main_wind):
        super().__init__(main_wind)
        self.main_wind = main_wind
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        week = QPushButton("Week", self.main_wind)

        week.setStyleSheet("min-width: 200px;")

        day = QPushButton("Day", self.main_wind)

        day.setStyleSheet("min-width: 200px;")
        day.move(200, 0)

        hbox.addWidget(week)
        hbox.addWidget(day)
        self.main_wind.setLayout(hbox)


class CurrentGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUI(self):
        current = QHBoxLayout()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.week = WeekDay(self)
        self.init_app()
        self.show()

    def init_app(self):
        self.setStyleSheet("background-color: #cecece;")
        self.setGeometry(0, 0, 400, 300)

        full = QVBoxLayout()
        full.addWidget(self.week)
        self.setLayout(full)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())