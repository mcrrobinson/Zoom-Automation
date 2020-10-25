import logging
from datetime import datetime, time, date
from time import sleep
from subprocess import Popen
import conf
import sys
from os import startfile
import get_handle
import ffmpeg_options

class WebLauncher:
    def __init__(self, logger, filenames):
        self.logger = logger
        self.filename = filenames
        self.recording = {}
        self.proc = None

        for i in conf.CLASS_MAP:
            self.recording[conf.CLASS_MAP[i]] = {
                "opened_meeting_tab": False, 
                "started_recording_tab": False
            }

    def readyThread(self, lecture):
        """ readyThread

        This function gets passed the current lecture, if it's time for the 
        lecture it'll then open up the corresponding zoom link. Once the 
        lecturer starts recording it'll then record the lecture until it is 
        over.

        Passes:
            lecture:
                A lecture row in the dictionar specified in the config python 
                file.

        """
        # If the date time matches one in the config.
        if datetime.now().hour >= lecture["meeting_time"][0] and datetime.now().hour < lecture["meeting_time"][1]:

            # If the lecture hasn't been opened, open it.
            if self.recording[lecture["class_name"]]["opened_meeting_tab"] == False:
                self.logger.info("Time for your {} meeting.".format(lecture["class_name"]))
                self.recording[lecture["class_name"]]["opened_meeting_tab"] = True
                startfile(lecture["meeting_link"])
                
            # Iterates the windows.
            for win in get_handle.Win32HandleZoom().getWindowSizes():
                advanced_settings = (
                    f"""-thread_queue_size 1024 -i desktop -c:v {ffmpeg_options.nvidia} -qp 0 -c:a aac -strict -2 -ac 2 -b:a 128k -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" {self.filename}.mkv"""
                )
                ffmpeg = (
                    f"""{ffmpeg_options.general} {win["dimentions"][0]} -offset_y {win["dimentions"][1]} -video_size {win['dimentions'][2]}x{win['dimentions'][3]} {advanced_settings}"""
                )

                if win["name"] == "Waiting for Host":
                    self.logger.info("Currently waiting on the host...")
                    continue

                if win["name"] == "Zoom Meeting":
                    
                    if get_handle.Win32HandleZoom().checkBoundaries(win["dimentions"]):
                        if self.recording[lecture["class_name"]]["started_recording_tab"] == False:
                            self.recording[lecture["class_name"]]["started_recording_tab"] = True
                            self.proc = Popen(ffmpeg)
                    else:
                        exit(1)

        # For every recording lesson in the dictionary, set to false.
        else:
            for i in conf.CLASS_MAP:
                if self.recording[conf.CLASS_MAP[i]]["started_recording_tab"] == True:
                    self.proc.terminate()
                    self.recording[conf.CLASS_MAP[i]] = {
                        "opened_meeting_tab": False, 
                        "started_recording_tab": False
                    }

    def main(self):
        """ main

        Gets the current day and iterates through the entries during that day 
        inside the config python file.
        """
        while True:

            # Get the current day in words, "Monday, Tuesday, etc.."
            current_day = conf.WEEKDAYS[date.today().weekday()]

            # Itearate through the enteriest for the current day and 
            # pass in the values for the thread.
            for i in conf.ENTRIES[current_day]:
                self.readyThread(conf.ENTRIES[current_day][i])

            sleep(1)