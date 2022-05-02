import threading

import app_gui as gui
import sys, time
import os
import window_timer
from threading import Thread
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    t = threading.Thread(target=window_timer.main_func)
    t2 = threading.Thread(target=gui.main_func)
    t.start()
    time.sleep(5)
    t2.start()