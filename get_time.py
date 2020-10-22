ggetimport logging
from datetime import datetime, time, date
from time import sleep
from threading import Thread
import os

class WebLauncher:
    def __init__(self):
        self.logger = logging
        self.database_systems_recording = False
        self.programming_recording = False
        self.core_computing_recording = False
        self.architecture_and_operating_systems_recording = False

    def record_database_systems_recording(self, moodle_link):
        os.startfile(moodle_link)
        while(self.database_systems_recording):
            self.logger.info("Started recording the databases...")
            sleep(1)

    def record_programming_recording(self, moodle_link):
        while(self.database_systems_recording):
            self.logger.info("Started recording programming...")
            sleep(1)

    def record_core_computing_recording(self, moodle_link):
        while(self.database_systems_recording):
            self.logger.info("Started recording core computing,. ...")
            sleep(1)

    def record_architecture_and_operating_systems_recording(self, moodle_link):
        while(self.database_systems_recording):
            self.logger.info("Started recording the databases...")
            sleep(1)

    def record_networks_recording(self, moodle_link):
        while(self.database_systems_recording):
            self.logger.info("Started recording the networks...")
            sleep(1)

            
    def main(self):
        while True:

            # Monday
            if date.today().weekday() == 0:
                if datetime.now().hour >= 9 and date.time().hour < 10:
                    if self.database_systems_recording == False:
                        self.database_systems_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_database_systems_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()
                        
                elif datetime.now().hour >= 10 and date.time().hour < 12:
                    if self.programming_recording == False:
                        self.programming_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_programming_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()

                elif datetime.now().hour >= 12 and date.time().hour < 13:
                    if self.core_computing_recording == False:
                        self.core_computing_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_core_computing_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()

                elif datetime.now().hour >= 13 and date.time().hour < 14:
                    if self.core_computing_recording == False:
                        self.core_computing_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_core_computing_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()

                elif datetime.now().hour >= 16 and date.time().hour < 17:
                    if self.architecture_and_operating_systems_recording == False:
                        self.architecture_and_operating_systems_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_architecture_and_operating_systems_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()

                else:
                    self.database_systems_recording = False
                    self.programming_recording = False
                    self.core_computing_recording = False
                    self.architecture_and_operating_systems_recording = False

            
            # Tuesday
            if date.today().weekday() == 1:
                if datetime.now().hour >= 11 and date.time().hour < 12:
                    if self.architecture_and_operating_systems_recording == False:
                        self.architecture_and_operating_systems_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_architecture_and_operating_systems_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()

                elif datetime.now().hour >= 12 and date.time().hour < 13:
                    if self.networks_recording == False:
                        self.networks_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_networks_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()

                elif datetime.now().hour >= 15 and date.time().hour < 16:
                    if self.database_systems_recording == False:
                        self.database_systems_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_database_systems_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()

                else:
                    self.architecture_and_operating_systems_recording = False
                    self.networks_recording = False
                    self.database_systems_recording = False

            # Wednesday
            if date.today().weekday() == 2:
                if datetime.now().hour >= 12 and date.time().minute < 21:
                    if self.networks_recording == False:
                        self.networks_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_networks_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()

                else:
                    self.logger.debug("Setting to false...")
                    self.networks_recording = False

            # Thursday
            if date.today().weekday() == 3:
                if datetime.now().hour >= 14 and date.time().hour < 15:
                    if self.core_computing_recording == False:
                        self.core_computing_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_core_computing_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()

                elif datetime.now().hour >= 17 and date.time().hour < 18:
                    if self.programming_recording == False:
                        self.programming_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_programming_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()
                
                else:
                    self.core_computing_recording = False
                    self.programming_recording = False
            
            # Friday
            if date.today().weekday() == 4:
                if datetime.now().hour >= 16 and date.time().hour < 17:
                    if self.core_computing_recording == False:
                        self.core_computing_recording = True
                        moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
                        newThread = Thread(target=self.record_core_computing_recording, args=(moodle_link,))
                        newThread.daemon = True
                        newThread.start()
                
                else:
                    self.core_computing_recording = False

            # if date.today().weekday() == 6:
            #     if datetime.now().minute > 56 and datetime.now().hour < 22:
            #         if self.database_systems_recording == False:
            #             self.database_systems_recording = True
            #             moodle_link = "zoommtg://port-ac-uk.zoom.us/join?action=join&confno=87537429380"
            #             newThread = Thread(target=self.record_database_systems_recording, args=(moodle_link,))
            #             newThread.daemon = True
            #             newThread.start()
                
            #     else:
            #         self.database_systems_recording = False

            sleep(1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
    WebLauncher().main()