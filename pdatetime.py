import datetime

def print_datetime():
    print(datetime.datetime.now())
    print(datetime.timedelta(weeks=5))
    d= datetime.datetime.today()
    print(d.strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.timedelta(weeks=5))

    str_date = "2020-02-29 10:12:22"
    date = datetime.datetime.strptime(str_date,'%Y-%m-%d %H:%M:%S')
    print(date)