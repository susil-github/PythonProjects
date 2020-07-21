import time;
print(time.time())
def getCurrentTime():
    return time.localtime()
print("current time is ",getCurrentTime())

print("printing formatted time ",time.asctime(time.localtime(time.time())))