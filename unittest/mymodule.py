'''
mymodule
'''
import datetime

def datestring2date(datestring):
    datelist=datestring.split('-')
    if not len(datelist) == 3:
        raise ValueError('need exactly three elements for a date string')
    year=datelist[0]
    month=datelist[1]
    day=datelist[2]
    try:
        date = datetime.date(int(year),int(month),int(day))
    except ValueError:
        raise ValueError('this date does not exist')
    return date

def is_workingday(datestring):
    if not type(datestring) is str:
        raise TypeError
    date = datestring2date(datestring)
    saturday = 6
    sunday = 7
    if date.isoweekday() == saturday or date.isoweekday() == sunday:
        return False
    else:
        return True

