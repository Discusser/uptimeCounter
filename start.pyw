import time

with open("data.txt", 'a') as file:
    file.write("start=" + str(time.time_ns()) + ";")
