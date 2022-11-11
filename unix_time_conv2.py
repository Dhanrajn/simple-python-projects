# Unix timestamp Convertor to convert both way
import datetime

# Unix Time to Readable date time


def get_time(unix_time):
    if len(str(unix_time)) > 10:
        unix_time = int(unix_time)/1000
    converted = datetime.datetime.fromtimestamp(unix_time)

    return converted

# Readable date time to unix time stamp.


def get_date_time(month, date, year, hour, minute, seconds):
    date_time = f'{month}/{date}/{year}, {hour}:{minute}:{seconds}'
    date_format = datetime.datetime.strptime(date_time, "%m/%d/%Y, %H:%M:%S")
    unix_time = datetime.datetime.timestamp(date_format)

    return unix_time
