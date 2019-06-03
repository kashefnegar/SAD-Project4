import urllib
import urllib.request


class AttendanceOp:
    def __init__(self):
        link = "http://142.93.134.194:8088/api/attendance"
        with urllib.request.urlopen(link) as url:
            s = url.read().decode('utf8')
            print(s)
