import win32process as proc
import win32gui as gui
import time as time
import psutil as util
import win32pdh as pdh
from win32com.server.exception import COMException

# import psutil


class MainTimer:

    def __init__(self, apps=[], wmi_apps=[]):
        self.apps = apps
        self.wmi_apps = wmi_apps

    def get_processes(self, hwnd, extra):
        if gui.IsWindowVisible(hwnd):
            # print(f'Window Id: {proc.GetWindowThreadProcessId(hwnd)[0]}, Window Name: {gui.GetWindowText(hwnd)}')
            self.apps.append(proc.GetWindowThreadProcessId(hwnd)[1])
        #print(self.apps)



if __name__ == "__main__":

    m = MainTimer()
    # somehow enumwindows passes all the handlers into the func


   # m.wmi_get_process(foreProc)
   #
    for i in range(100):
        time.localtime()
        gui.EnumWindows(m.get_processes, None)
        foreProc = proc.GetWindowThreadProcessId(gui.GetForegroundWindow())[1]
        for p in util.process_iter(['pid', 'name']):
            if p.pid == foreProc:
                print(p.info)
        print(time.localtime())



    # 8 second time difference - bbng
