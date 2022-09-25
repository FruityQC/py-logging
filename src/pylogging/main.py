import os
import time

LogTime = ''
logf = ''


def gettime():
    currenttime = time.ctime()
    global LogTime
    LogTime = "[" + currenttime + "]: "


def IsFileOpen():
    if logf:
        return True
    else:
        return False


def createlog(name="py-logging", ext=".log"):
    gettime()
    error = "File already exists."
    try:
        f = open(name + ext, 'r')
        f.close()
    except FileNotFoundError:
        a = open(name + ext, 'x')
        a.write(LogTime + "START OF LOGS")
        a.close()
        error = "File created."
    return print(error)


# def deletelog(filef="py-logging.log"):
#     try:
#         os.remove(filef)
#     except:
#         return print("Error, check file path.")

def openLog(filename="py-logging.log"):
    global logf

    try:
        logf.close()
    except AttributeError:  # try to close old file
        print('')

    try:
        logf = open(filename, "w")  # try to open file
    except FileNotFoundError:
        createlog()  # create the file
        openLog("py-logging.log")  # open the file by recalling this


def closeLog():
    global logf

    try:
        logf.close()
        logf = ''
    except AttributeError:
        return "Log Closed."


def logline(str):
    if not logf:
        return print("No log opened: openLog")
    gettime()
    logf.write("\n")
    logf.write(LogTime + str)
    return


os.system("cls")

openLog()

logline("This is a test1")
logline("This is a test2")
logline("This is a test3")
logline("This is a test4")

closeLog()

logline("This is a test3")

openLog()

logline("This is a test69")
