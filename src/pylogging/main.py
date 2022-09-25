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


def createlog(name="py-logging.log"):
    gettime()
    error = "File already exists."
    try:
        f = open(name, 'r')
        f.close()
    except FileNotFoundError:
        a = open(name, 'x')
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
    gettime()

    try:
        logf.close()
    except AttributeError:  # try to close old file
        print('')

    try:
        logf = open(filename, "w")  # try to open file
        logf.write(LogTime + "===LOGS OPENED===\n")
    except FileNotFoundError:
        createlog(filename)  # create the file
        openLog(filename)  # open the file by recalling this


def closeLog():
    global logf
    gettime()

    try:
        logf.write(LogTime + "===LOGS CLOSED===")
        logf.close()
        logf = ''
    except AttributeError:
        return "Log Closed."


def logline(str):
    if not logf:
        return print("No log opened: openLog")
    gettime()
    logf.write(LogTime + str)
    logf.write("\n")
    return


os.system("cls")
