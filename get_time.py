import logging
from datetime import datetime, time, date
from time import sleep
import subprocess
import conf
import sys
from os import startfile

import win32con
import win32gui
import win32api

class WebLauncher:
    def __init__(self, logger):
        self.logger = logger
        self.filename = "Lecture_" + str(datetime.now().isoformat()).replace(".", "_").replace(":","-")
        self.recording = {}
        self.proc = None

        for i in conf.CLASS_MAP:
            self.recording[conf.CLASS_MAP[i]] = {
                "opened_meeting_tab": False, 
                "started_recording_tab": False
            }

    def isRealWindow(self, hWnd):
        '''Return True iff given window is a real Windows application window.'''
        if not win32gui.IsWindowVisible(hWnd):
            return False
        if win32gui.GetParent(hWnd) != 0:
            return False
        hasNoOwner = win32gui.GetWindow(hWnd, win32con.GW_OWNER) == 0
        lExStyle = win32gui.GetWindowLong(hWnd, win32con.GWL_EXSTYLE)
        if (((lExStyle & win32con.WS_EX_TOOLWINDOW) == 0 and hasNoOwner)
        or ((lExStyle & win32con.WS_EX_APPWINDOW != 0) and not hasNoOwner)):
            if win32gui.GetWindowText(hWnd):
                return True
        return False

    def getWindowSizes(self):
        '''
        Return a list of tuples (handler, (width, height)) for each real window.
        '''
        def callback(hWnd, windows):
            if not self.isRealWindow(hWnd):
                return
            rect = win32gui.GetWindowRect(hWnd)
            text = win32gui.GetWindowText(hWnd)
            windows.append({
                    "name": text, 
                    "handle": hWnd, 
                    "dimentions": [rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]]
                }
            )
        windows = []
        win32gui.EnumWindows(callback, windows)
        return windows

    def checkBoundaries(self, boundaries):
        if(
            boundaries[2] <= win32api.GetSystemMetrics(0) and 
            boundaries[2] > 0 and 
            boundaries[3] <= win32api.GetSystemMetrics(1) and 
            boundaries[3] > 0
        ):
            if(
                boundaries[0] < win32api.GetSystemMetrics(0) and
                boundaries[0] >= 0 and
                boundaries[1] < win32api.GetSystemMetrics(1) and
                boundaries[1] >= 0
            ):
                self.logger.debug("Boundaries for window are valid, proceeding.")
                return True
                
        self.logger.debug("Boundaries for the window are invalid, closing application.")
        return False

    def ready_thread(self, lecture):

        # If the date time matches one in the config.
        if datetime.now().hour >= lecture["meeting_time"][0] and datetime.now().hour < lecture["meeting_time"][1]:

            # If the lecture hasn't been opened, open it.
            if self.recording[lecture["class_name"]]["opened_meeting_tab"] == False:
                self.logger.info("Time for your {} meeting.".format(lecture["class_name"]))
                self.recording[lecture["class_name"]]["opened_meeting_tab"] = True
                startfile(lecture["meeting_link"])
            
            # Iterates the windows.
            for win in self.getWindowSizes():
                if win["name"] == "Waiting for Host":
                    self.logger.info("Currently waiting on the host...")
                    continue

                if win["name"] == "Zoom Meeting":
                    if self.checkBoundaries(win["dimentions"]):
                        if self.recording[lecture["class_name"]]["started_recording_tab"] == False:
                            self.recording[lecture["class_name"]]["started_recording_tab"] = True
                            self.proc = subprocess.Popen(f"""ffmpeg -f gdigrab -framerate 20 -offset_x {win["dimentions"][0]} -offset_y {win["dimentions"][1]} -video_size {win['dimentions'][2]}x{win['dimentions'][3]} -thread_queue_size 1024 -i desktop -c:v hevc_nvenc -qp 0 -c:a aac -strict -2 -ac 2 -b:a 128k -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" {self.filename}.mkv""")
                    else:
                        exit(1)

        # For every recording lesson in the dictionary, set to false.
        else:
            if not all(value == False for value in conf.CLASS_MAP):
                for i in conf.CLASS_MAP:
                    self.recording[conf.CLASS_MAP[i]] = {
                        "opened_meeting_tab": False, 
                        "started_recording_tab": False
                    }
            
    def main(self):
        while True:

            # Get the current day in words, "Monday, Tuesday, etc.."
            current_day = conf.WEEKDAYS[date.today().weekday()]

            # Itearate through the enteriest for the current day and 
            # pass in the values for the thread.
            for i in conf.ENTRIES[current_day]:
                self.ready_thread(conf.ENTRIES[current_day][i])

            sleep(1)