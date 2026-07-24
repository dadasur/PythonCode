import os
import schedule
import datetime
import time
import sys

def DisplayContainOfFile(FilePath):
      
     if not os.path.exists(FilePath):
        print("File does not exist.")

     if os.path.getsize(FilePath) == 0:
      print("File is empty.")

     if not os.access(FilePath, os.R_OK):      
       print("No read permission.")

     if not os.access(FilePath, os.W_OK):      
       print("No read permission.")

     TimeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")    
     LogFileName = "File_%s.txt"%(TimeStamp)
     fobj = open(FilePath,"r")
     fobj1 = open(LogFileName,"w")
     fobj1.write(fobj.read())
     fobj.close()
     fobj1.close()

def main():
    
    if not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)

    DisplayContainOfFile(sys.argv[1])
    schedule.every(1).minute.do(DisplayContainOfFile,sys.argv[1])
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()