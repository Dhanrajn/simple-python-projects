# Unix timestamp Convertor

from datetime import datetime

# Unix Time to Readable date time


def get_time(unix_time):
    if len(str(unix_time)) > 10:
        unix_time = int(unix_time)/1000
    converted = (datetime.utcfromtimestamp(unix_time)).strftime('%Y-%m-%d %H:%M:%S')

    return converted
