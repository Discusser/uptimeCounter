import time

with open("data.txt", 'a') as file:
    file.write("end=" + str(time.time_ns()) + ";")
