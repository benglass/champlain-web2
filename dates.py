import datetime

START_DATE = datetime.date(2015, 1, 12)
END_DATE = datetime.date(2015, 5, 1)
HOLIDAYS = [
    datetime.date(2015, 3, 9)
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
