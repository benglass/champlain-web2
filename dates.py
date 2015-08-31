import datetime

START_DATE = datetime.date(2015, 9, 1)
END_DATE = datetime.date(2015, 12, 11)
HOLIDAYS = [
    datetime.date(2015, 10, 13)
]
CLASS_INTERVAL = datetime.timedelta(days=7)

def is_holiday(date):
    for holiday in HOLIDAYS:
        if (new_date == holiday):
            return True
    return False

class_dates = [START_DATE]
while (1):
    new_date = class_dates[-1] + CLASS_INTERVAL

    if (new_date > END_DATE):
        break

    while (is_holiday(new_date)):
        new_date = new_date + CLASS_INTERVAL

    class_dates.append(new_date)

for date in class_dates:
    print date.strftime('%m/%d/%y')
