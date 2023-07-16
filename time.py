import datetime

def subtract_days(timestamp, days):
    dt = datetime.datetime.fromtimestamp(timestamp)
    dt -= datetime.timedelta(days=days)
    new_timestamp = dt.timestamp()
    return new_timestamp
timestamp = 1686755697
new_timestamp = subtract_days(timestamp, 3)
print(new_timestamp)
