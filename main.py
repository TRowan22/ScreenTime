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

    m = window_timer.MainTimer()
    t1 = Thread(target=m.update())
    t1.start()

    sys.exit(app.exec_())