import re
import time
from datetime import datetime

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
    for time1 in re.findall(r"\d{19}(?!;$)", file.read()):
        dates.append(int(time1) / 1_000_000_000)
        dt = datetime.fromtimestamp(int(time1) / 1_000_000_000)
        mplDates.append(dt)

if hasBounds:
    dateFrom1 = datetime.strptime(dateFrom, "%d/%m/%Y").timestamp()
    dateTo1 = datetime.strptime(dateTo, "%d/%m/%Y").timestamp()
    dates = [date for date in dates if dateFrom1 <= date <= dateTo1]
    mplDates = [datetime.fromtimestamp(date) for date in dates]

for i in range(0, len(dates), 2):
    for j in range(2):
        durations.append((dates[i + 1] - dates[i]) / 3600)

mplDates.append(datetime.now())
durations.append((time.time() - dates[-1]) / 3600)

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





