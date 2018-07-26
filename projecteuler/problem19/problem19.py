import datetime

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
start_day=datetime.date(1901,1,1)
end_day=datetime.date(2000,12,31)


def is_sunday(d):
    return d.weekday() == 6


def main():
    print('problem 19')
    d1=datetime.date(1900, 1, 1)
    print('Is', d1, 'a sunday?', is_sunday(d1))
    d1=datetime.date(1950, 1, 1)
    print('Is', d1, 'a sunday?', is_sunday(d1))
    oneweek=datetime.timedelta(7)
    d2=datetime.date(1950, 1, 1)
    print('One week after', d2, ':', d2+oneweek)
    d2=datetime.date(1950, 1, 29)
    print('One week after', d2, ':', d2+oneweek)
    d2=datetime.date(1950, 2, 27)
    print('One week after', d2, ':', d2+oneweek)
    nr_sundays=0
    for year in range(start_day.year,end_day.year+1):
        for month in range(1,13):
            d = datetime.date(year,month,1)
            if is_sunday(d):
                print(d)
                nr_sundays += 1
    print('Number of sundays:', nr_sundays)



main()


