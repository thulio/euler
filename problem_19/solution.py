#!/usr/bin/env python3

import datetime

counter = 0
d_init = datetime.datetime(1901, 1, 1)
d_finish = datetime.datetime(2000, 12, 31)


while d_init < d_finish:
    if d_init.day == 1 and d_init.weekday() == 6:
        counter += 1

    d_init += datetime.timedelta(days=1)

print(counter)
