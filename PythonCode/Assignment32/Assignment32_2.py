import os
import schedule
import datetime
import time
import sys

def MonitorFile(FilePath):

    LogFileName = "FileSizeLog.txt"
    get_Size = os.path.getsize(FilePath)
    fobj = open(LogFileName,"a")
    fobj.write(f"File Path: {os.path.abspath(FilePath)}\n")
    fobj.write(f"File size in bytes is: {get_Size}\n")
    fobj.write(f"Date and time: {datetime.datetime.now()}\n")
    print("Log file is created.")
    fobj.close()

def main():
    
    if not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)

    MonitorFile(sys.argv[1])
    schedule.every(30).seconds.do(MonitorFile,sys.argv[1])
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()