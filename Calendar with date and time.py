### First import the libraries needed for the project ###

import calendar
from datetime import date
from datetime import time
from datetime import timezone
from datetime import datetime

### and here is to print the calendar and current date. ###
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2019, 1, 0, 0)
print(st)
now = datetime.now()
print(now.strftime("The current date is: %x"))
print("and")
print(now.strftime("The current time is: %X"))
enter = input()