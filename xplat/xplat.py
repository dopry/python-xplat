import sys

if sys.platform == 'win32':
    import win32 as client
else:
    import posix as client


def get_username():
    return client.get_username()


if __name__ == '__main__':
    print "Xplat (splat) cross platform tools"
    print "\tplatform: " + sys.platform
    print "\tusername: " + get_username()
