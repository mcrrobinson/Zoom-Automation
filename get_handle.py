from win32con import GW_OWNER, GWL_EXSTYLE, WS_EX_TOOLWINDOW, WS_EX_APPWINDOW
import win32api
import win32gui

class Win32HandleZoom:
    def __init__(self):
        pass

    def isRealWindow(self, hWnd):
        ''' isRealWindow
        
        Gets passed in the handle and checks to see weather or not the
        corresponding window is real with correct dimentions.

        Passes:
            hWnd:
                This is the handle, gotten from iterating on enumWindows
        
        Returns:
            True:
                If the window being checked is real it will return true.
            False:
                If the window being checked is invalid it will return false.
        '''
        if not win32gui.IsWindowVisible(hWnd):
            return False
        if win32gui.GetParent(hWnd) != 0:
            return False
        hasNoOwner = win32gui.GetWindow(hWnd, GW_OWNER) == 0
        lExStyle = win32gui.GetWindowLong(hWnd, GWL_EXSTYLE)
        if (((lExStyle & WS_EX_TOOLWINDOW) == 0 and hasNoOwner)
        or ((lExStyle & WS_EX_APPWINDOW != 0) and not hasNoOwner)):
            if win32gui.GetWindowText(hWnd):
                return True
        return False

    def getWindowSizes(self):
        ''' getWindowSizes

        Returns a list of tuples that include the name handle and dimentions
        of the application being checked.

        Returns:
            windows:
                A tuple of the window being iterated upon including the; name,
                handle and dimentions of the window.
        '''
        def callback(hWnd, windows):
            if not self.isRealWindow(hWnd):
                return
            rect = win32gui.GetWindowRect(hWnd)
            text = win32gui.GetWindowText(hWnd)
            windows.append({
                    "name": text, 
                    "handle": hWnd, 
                    "dimentions": [
                        rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]
                    ]
                }
            )
        windows = []
        win32gui.EnumWindows(callback, windows)
        return windows

    def checkBoundaries(self, boundaries):
        """ checkBoundaries
        
        The isRealWindow checks to see weather or not the window is real,
        this function checks to see if the boundaries are real due to the
        fact that windows has some unusual results when the application
        is opened but minimized. This checks it against the resolution of
        the display.

        Returns:
            True:
                If the boundaries are valid, it returns true.
            False:
                If the boundaries are invalid, returns false.
        """
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
                return True
        return False