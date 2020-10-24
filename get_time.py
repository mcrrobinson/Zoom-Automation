import logging
from datetime import datetime, time, date
from time import sleep
import subprocess
import conf
import get_handle as handle
import sys
import os

class WebLauncher:
    def __init__(self, logger):
        self.logger = logger
        self.filename = "Lecture_" + str(datetime.now().isoformat()).replace(".", "_").replace(":","-")
        self.recording = {}

        for i in conf.CLASS_MAP:
            self.recording[conf.CLASS_MAP[i]] = False

    def ready_thread(self, lecture):
        if datetime.now().hour >= lecture["meeting_time"][0] and datetime.now().hour < lecture["meeting_time"][1]:
            if self.recording[lecture["class_name"]] == False:
                self.recording[lecture["class_name"]] = True

                # Block until it starts.
                os.popen(lecture["meeting_link"])
                zoom_information = handle.GetApplicationInformation(self.logger).FindApplications(*sys.argv[1:])
                if(zoom_information):
                    proc = subprocess.Popen(f"""ffmpeg -f gdigrab -framerate 20 -offset_x {0} -offset_y {0} -video_size {zoom_information['dimentions'][2]}x{zoom_information['dimentions'][3]} -thread_queue_size 1024 -i desktop -c:v hevc_nvenc -qp 0 -c:a aac -strict -2 -ac 2 -b:a 128k -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" {self.filename}.mkv""")
                else:
                    self.logger.debug("Windows had issues handling the application. This is why I reccomend linux.")

        # For every recording lesson in the dictionary, set to false.
        else:
            proc.terminate(self)
            # If not all the values are set to false in the dictionary iterate
            # and set them all to false.
            if not all(value == False for value in conf.CLASS_MAP):
                for i in conf.CLASS_MAP:
                    self.recording[conf.CLASS_MAP[i]] = False
            
    def main(self):
        while True:

            # Get the current day in words, "Monday, Tuesday, etc.."
            current_day = conf.WEEKDAYS[date.today().weekday()]

            # Itearate through the enteriest for the current day and 
            # pass in the values for the thread.
            for i in conf.ENTRIES[current_day]:
                self.ready_thread(conf.ENTRIES[current_day][i])

            sleep(1)