import threading

import app_gui as gui
import time
import window_timer
from threading import Thread

if __name__ == "__main__":
    t = threading.Thread(target=window_timer.main_func)
    t2 = threading.Thread(target=gui.main_func)
    t.start()
    time.sleep(2)
    t2.start()