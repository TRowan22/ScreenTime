import app_gui as gui
import sys
import window_timer
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui.MainWindow()
    sys.exit(app.exec_())

    m = window_timer.MainTimer()
    while True:
        m.get_current_window()

        m.timer.send_to_json()