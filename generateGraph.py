import re
from datetime import datetime

import matplotlib.pyplot as plt

datesReadable = []
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
    for time in re.findall(r"\d{19}(?!;$)", file.read()):
        dates.append(int(time) / 1_000_000_000)
        dt = datetime.fromtimestamp(int(time) / 1_000_000_000)
        datesReadable.append(dt.strftime("%d %b %Y %H:%M:%S"))

if hasBounds:
    dateFrom1 = datetime.strptime(dateFrom, "%d/%m/%Y").timestamp()
    dateTo1 = datetime.strptime(dateTo, "%d/%m/%Y").timestamp()
    dates = [date for date in dates if dateFrom1 <= date <= dateTo1]
    datesReadable = [datetime.fromtimestamp(date).strftime("%d %b %Y %H:%M:%S") for date in dates]

for i in range(0, len(dates), 2):
    for j in range(2):
        durations.append((dates[i + 1] - dates[i]) / 3600)

fig, ax = plt.subplots()
plt.plot(datesReadable, durations)
plt.xlabel("Date")
plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45, ha="left", rotation_mode="anchor")
plt.ylabel("Duration (hours)")
plt.title("Uptime")
plt.tight_layout()
plt.show()
