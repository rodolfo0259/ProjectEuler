#!/bin/python
#how many sundays from 1901/1/1 to 2000/12/31 i.e. the 20th century
import datetime

start = datetime.date(1901, 1, 1)
print(start.month)
print(start.strftime("%A")) #format strings
year = 1901
sunday_count = 0
while year <= 2000:
    for month in range(1,13):
        timetravel = datetime.date(year, month, 1)
        if timetravel.strftime("%A") == 'Sunday':
            sunday_count += 1
    year += 1

print(sunday_count)

