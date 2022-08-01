#!/usr/bin/env python3

## brute force

# 1 Jan 1901 to 31 Dec 2000

import datetime

months = range(1, 13)

years = range(1901, 2001)

how_many_sunday = 0
for year in years:
    for month in months:
        week_day = datetime.datetime(year, month, 1).weekday()
        if week_day == 6:
            how_many_sunday += 1

print(how_many_sunday)
