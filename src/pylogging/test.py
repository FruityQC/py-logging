import random
import time
import main as pylog

num = 0

pylog.openLog()
while True:
    time.sleep(.1)
    pylog.logline(num)
    num += 1
    print(num)
    if num > 10:
        pylog.closeLog()
        break
