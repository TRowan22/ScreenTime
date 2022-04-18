"""
Week - Day buttons

Graph

List of apps          Time Spent
(bar scaled by how much time spent)
"""
import sys
import calendar
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget, \
    QPushButton, QLineEdit, QHBoxLayout, QDockWidget
from PyQt5.QtGui import QPixmap, QPalette, QIcon
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.WINDOW_WIDTH = int(1920 / 4)
        self.WINDOW_HEIGHT = int(1200 / 4)

        self.week = WeekDay(self, int(self.WINDOW_WIDTH / 2))
        self.init_app()
        self.show()

    def init_app(self):
        self.setStyleSheet("background-color: #cecece;")
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)


class WeekDay(QWidget):
    """
    Widget of buttons that decides whether a week or a day graph is shown
    """
    def __init__(self, main_wind, half):
        super().__init__(main_wind)
        self.main_wind = main_wind
        self.current = CurrentWD(main_wind)
        self.half = half
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        week = QPushButton("Week", self.main_wind)

        week.setStyleSheet(f"min-width: {self.half}px;")

        day = QPushButton("Day", self.main_wind)

        day.setStyleSheet(f"min-width: {self.half}px;")
        day.move(self.half, 0)

        hbox.addWidget(week)
        hbox.addWidget(day)

        all_parts = QVBoxLayout()
        all_parts.addLayout(hbox)
        all_parts.addWidget(self.current)
        self.setLayout(all_parts)

class CurrentWD(QWidget):
    def __init__(self , parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        m = QHBoxLayout()
        label = QLabel("a", self.parent)
        label.move(200, 0)
        m.addWidget(label)
        self.setLayout(m)



class CurrentGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUI(self):
        current = QHBoxLayout()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())