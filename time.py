import datetime

def subtract_days(timestamp, days):
    dt = datetime.datetime.fromtimestamp(timestamp)
    dt -= datetime.timedelta(days=days)
    new_timestamp = dt.timestamp()
    return new_timestamp
def show_details(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    date = dt.strftime("%d/%m/%Y")
    time = dt.strftime("%H:%M:%S")
    print("Ngày: ", date)
    print("Giờ: ", time)
def main():
    timestamp = 1686755697
    show_details(timestamp)
main()
