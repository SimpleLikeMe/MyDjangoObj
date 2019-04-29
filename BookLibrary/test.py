import datetime


def get_last_month(now):
    if now.month >= 28:
        if now.month == 1:
            month = now.month + 2
            day = now.day
    month = now.month + 1
    d = datetime.datetime(year=now.year, month=month, day=now.day, hour=now.hour, minute=now.minute, second=now.second, microsecond=now.microsecond)
    print(d)
    return d


print(dir(datetime))
print(dir(datetime.datetime))
print(datetime.datetime.now())
d = datetime.datetime.now()
get_last_month(d)
