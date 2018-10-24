import sys
from _datetime import datetime

time_tuple = (2012,  # Year
              9,  # Month
              6,  # Day
              0,  # Hour
              38,  # Minute
              0,  # Second
              0,  # Millisecond
              )

def set_time(time_tuple):
    if sys.platform == 'linux2' or sys.platform == 'linux':
        _linux_set_time(time_tuple)

    elif sys.platform == 'win32':
        _win_set_time(time_tuple)


def _win_set_time(time_tuple):
    
    print('setando windows')
    import win32api
    dayOfWeek = datetime(*time_tuple).isocalendar()[2]
    t = time_tuple[:2] + (dayOfWeek,) + time_tuple[2:]
    win32api.SetSystemTime(*t)


def _linux_set_time(time_tuple):
    
    print('setando linux')
    import subprocess
    import shlex

    time_string = datetime(*time_tuple).isoformat()

    subprocess.call(shlex.split("timedatectl set-ntp false"))  # May be necessary
    subprocess.call(shlex.split("sudo date -s '%s'" % time_string))
    subprocess.call(shlex.split("sudo hwclock -w"))

if __name__ == '__main__':
    set_time(time_tuple)