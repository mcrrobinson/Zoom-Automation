#!/usr/bin/env python3

import os
import traceback
import win32con as wcon
import win32api as wapi
import win32gui as wgui
import win32process as wproc

class GetApplicationInformation():
    def __init__(self, logger):
        self.logger = logger
        
        self.ZPToolBarParentWnd_found = False
        self.Zoom_client_found = False
        self.Zoom_meeting_found = False

        self.ZPToolBarParentWnd_vector_valid = False
        self.Zoom_client_vector_valid = False
        self.Zoom_meeting_vector_valid = False

        self.zoom_instances = {"ZPToolBarParentWnd": False, "Zoom_client": False, "Zoom_meeting": False}

    def EnumWindowProcedure(self, wnd, param):
        pid = param.get("pid", None)
        data = param.get("data", None)
        if pid is None or wproc.GetWindowThreadProcessId(wnd)[1] == pid:
            rect = wgui.GetWindowRect(wnd)
            text = wgui.GetWindowText(wnd)
            if text and rect:
                style = wapi.GetWindowLong(wnd, wcon.GWL_STYLE)
                if style & wcon.WS_VISIBLE:
                    if data is not None:
                        data.append((wnd, text, rect))

    def EnumProcessWindows(self, pid=None):
        data = []
        param = {
            "pid": pid,
            "data": data,
        }
        wgui.EnumWindows(self.EnumWindowProcedure, param)
        return data

    def FilterProcesses(self, processes, search_name=None):
        if search_name is None:
            return processes
        filtered = []
        for pid, _ in processes:
            try:
                proc = wapi.OpenProcess(wcon.PROCESS_ALL_ACCESS, 0, pid)
            except:
                self.logger.info("Process {0:d} couldn't be opened: {1:}".format(pid, traceback.format_exc()))
                continue
            try:
                file_name = wproc.GetModuleFileNameEx(proc, None)
            except:
                self.logger.info("Error getting process name: {0:}".format(traceback.format_exc()))
                wapi.CloseHandle(proc)
                continue
            base_name = file_name.split(os.path.sep)[-1]
            if base_name.lower() == search_name.lower():
                filtered.append((pid, file_name))
            wapi.CloseHandle(proc)
        return tuple(filtered)


    def EnumProcesses(self, process_name=None):
        procs = [(pid, None) for pid in wproc.EnumProcesses()]
        return self.FilterProcesses(procs, search_name=process_name)

    def CheckBoundaries(self, dimentions):
        if not(
            # Often if the application is minimised the values will be zero.
            # all(v == 0 for v in dimentions)
            # or
            # Larger than screen size...
            any(v > 1920 for v in dimentions)
            or 
            # Less than the screensized offset.
            any(v < -1920 for v in dimentions)
        ):
            return True
        else:
            return False

    def FindApplications(self, *args):
        proc_name = args[0] if args else None
        procs = self.EnumProcesses(process_name=proc_name)
        for pid, name in procs:
            data = self.EnumProcessWindows(pid)
            if data:
                for handle, text, rect in data:
                    if text == "Zoom Meeting":
                        self.zoom_instances["Zoom_meeting"] = {"handle": handle, "title": text, "dimentions": [rect[0],rect[1],rect[2]+rect[0],rect[3]+rect[1]]}
                        self.logger.debug("PID: {0:d} | HWND: {0:d} | Name: {1:s}".format(handle, text))
                        self.Zoom_meeting_found = True
                    if text == "Zoom":
                        self.zoom_instances["Zoom_client"] = {"handle": handle, "title": text, "dimentions": [rect[0],rect[1],rect[2]+rect[0],rect[3]+rect[1]]}
                        self.logger.debug("PID: {0:d} | HWND: {0:d} | Name: {1:s}".format(handle, text))
                        self.Zoom_client_found = True
                    if text == "ZPToolBarParentWnd":
                        self.zoom_instances["ZPToolBarParentWnd"] = {"handle": handle, "title": text, "dimentions": [rect[0],rect[1],rect[2]+rect[0],rect[3]+rect[1]]}
                        self.logger.debug("PID: {0:d} | HWND: {0:d} | Name: {1:s}".format(handle, text))
                        self.ZPToolBarParentWnd_found = True

        print(self.zoom_instances)
        if(self.Zoom_meeting_found):
            self.logger.debug("Zoom meeting was found testing the vector boundaries...")
            if(self.CheckBoundaries(self.zoom_instances["Zoom_meeting"]["dimentions"])): # pylint: disable=unsubscriptable-object
                self.logger.debug("Zoom meeting vector structure is valid. Proceeding.")
                return self.zoom_instances["Zoom_meeting"]
            else:
                self.logger.debug("Zoom meeting vector structure is invalid...")
        if(self.Zoom_client_found or self.ZPToolBarParentWnd_found):
            self.logger.info("The Zoom meeting was not found, but other windows were found but this is unlikely to record what you want, do you still with to proceed? (N) ")
            self.user_continue = input(">> ")
            if self.user_continue.upper() == "Y":
                if(self.Zoom_client_found):
                    self.logger.debug("Zoom client was found testing the vector boundaries...")
                    if(self.CheckBoundaries(self.zoom_instances["Zoom_client"]["dimentions"])): # pylint: disable=unsubscriptable-object
                        self.logger.debug("Zoom client vector structure is valid. Proceeding.")
                        return self.zoom_instances["Zoom_client"]
                    else:
                        self.logger.debug("Zoom client vector structure is invalid...")

                if(self.ZPToolBarParentWnd_found):
                    self.logger.debug("Zoom toolbar was found testing the vector boundaries...")
                    if(self.CheckBoundaries(self.zoom_instances["ZPToolBarParentWnd"]["dimentions"])): # pylint: disable=unsubscriptable-object
                        self.logger.debug("Zoom toolbar vector structure is valid. Proceeding.")
                        return self.zoom_instances["ZPToolBarParentWnd"]
                    else:
                        self.logger.debug("Zoom toolbar vector structure is invalid...")
                    self.logger.error("Although Zoom processes were found, none contained a valid vector structure.")
                    return False
                else:
                    self.logger.error("The if check failed, this shouldn't happen.")
                    return False
            else:
                self.logger.error("Not proceeding.")
                return False
        else:
            self.logger.error("Zoom was not found, you're fucked... Next time make sure it is open geezer.")
            return False