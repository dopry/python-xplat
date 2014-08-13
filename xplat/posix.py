import pwd


def get_username():
    return pwd.getpwuid(os.geteuid())[0]
