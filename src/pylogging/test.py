import random
import time
import main as pylog


pylog.openLog()
while True:
    num = 0
    time.sleep(.1)
    pylog.logline(num)
    num = num + 1
