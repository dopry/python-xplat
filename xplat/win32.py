try:
    import win32api
except:
    raise ImportError("Ensure the pywin32 module is installed. "
                      + " http://sourceforge.net/projects/pywin32")


def get_username():
    return win32api.GetUserName()
