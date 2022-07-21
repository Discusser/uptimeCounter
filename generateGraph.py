import re
import time
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
from matplotlib import axes
from matplotlib import dates as mdates

mplDates = []
dates: [datetime] = []
datesLength = 0
durations = []
hasBounds = not input("Show all uptime? (Y/N) ").lower() == 'y'
global dateFrom, dateTo


def askLowerBound():
    global dateFrom
    dateFrom = input("Beginning date? (DD/MM/YYYY) ")
    if re.fullmatch(r"\d\d/\d\d/\d{1,4}", dateFrom) is None:
        askLowerBound()


def askUpperBound():
    global dateTo
    dateTo = input("End date? (DD/MM/YYYY) ")
    if re.fullmatch(r"\d\d/\d\d/\d{1,4}", dateTo) is None:
        askLowerBound()


if hasBounds:
    askLowerBound()
    askUpperBound()

with open(r"D:\Coding\Python\UptimeCounter\data.txt", 'r') as file:
    for time1 in re.findall(r"\d{19}", file.read()):
        dates.append(int(time1) / 1_000_000_000)
        dt = datetime.fromtimestamp(int(time1) / 1_000_000_000)
        mplDates.append(dt)

global dateTo1

if hasBounds:
    global dateTo1
    dateFrom1 = datetime.strptime(dateFrom, "%d/%m/%Y").timestamp()
    dateTo1 = (datetime.strptime(dateTo, "%d/%m/%Y") + timedelta(days=1)).timestamp()
    datesCopy = dates
    dates = [date for date in dates if dateFrom1 <= date <= dateTo1]
    # Check if first and last elements of array are shutdown times
    if datesCopy.index(dates[0]) % 2 != 0:
        dates.pop(0)
    if datesCopy.index(dates[-1]) % 2 != 0:
        dates.pop()
    mplDates = [datetime.fromtimestamp(date) for date in dates]

for i in range(0, len(dates), 2):
    for j in range(2):
        try:
            durations.append((dates[i + 1] - dates[i]) / 3600)
        except IndexError:
            pass

durations.append(((time.time() if not hasBounds else dateTo1) - dates[-1]) / 3600)

ax: axes.Axes
fig, ax = plt.subplots()
ax.plot(mplDates, durations)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
fig.autofmt_xdate()
plt.xlabel("Date")
plt.ylabel("Duration (hours)")
plt.title("Uptime")
plt.tight_layout()
plt.show()
