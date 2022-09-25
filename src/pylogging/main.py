from cmath import log
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

def openfile(filename="py-logging.log"):
    try:
        global logf
        logf = open(filename, "w")
    except FileNotFoundError:
        createlog()
        openfile("py-logging.log")


def logline(logfile, str):
    gettime()
    #logf = open(logfile, "w")
    logf.write("\n")
    logf.write(LogTime + str)
    # logf.close()
    return


os.system("cls")

openfile()

logline("py-logging.log", "This is a test1")
logline("py-logging.log", "This is a test2")
logline("py-logging.log", "This is a test3")
logline("py-logging.log", "This is a test4")
