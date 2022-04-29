import threading

import app_gui as gui
import sys
import window_timer
from threading import Thread
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui.MainWindow()

    m = window_timer.MainTimer()
    t1 = Thread(target=m.update())
    t2 = Thread(target=window.show_window())
    t1.start()
    t2.start()

    sys.exit(app.exec_())