import threading

import app_gui as gui
import sys
import os
import window_timer
from threading import Thread
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui.MainWindow()
    sys.exit(app.exec_())