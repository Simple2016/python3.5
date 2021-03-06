import win32api, win32gui, win32con
import time


def setWallPaper(pic):
    # open register
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey, "WallpaperStyle", 0, win32con.REG_SZ, "1")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic, win32con.SPIF_SENDWININICHANGE)


def getOldWallPaper():
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS)
    value, key_type = win32api.RegQueryValueEx(regKey, 'Wallpaper')
    return value;




if __name__ == '__main__':
    getOldWallPaper()
