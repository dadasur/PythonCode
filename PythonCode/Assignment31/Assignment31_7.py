import sys
import os
import time
import schedule
import shutil
import datetime

def CopiFile(sourcepath,DestinationDirectoryPath):
    
    timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    LogFileName = f"Marvellous_{timestamp}.log"
    Ret = os.path.exists(sourcepath)
    if(Ret == False):
        print("Marvellous Automation Error : There is no such file with name ",SourceFilePath)
        return
       
    Ret = os.path.isdir(DestinationDirectoryPath)
  
    if(Ret == False):
        print("Marvellous Automation Error : It is not a directory with name ",DestinationDirectoryPath)
        return
    dirpath = os.path.join(DestinationDirectoryPath)
    fobj = open(sourcepath,"r")
    fobj1 = open(LogFileName,"w")
    fobj1.write(fobj.read())
    fobj.close()
    fobj1.close()

    shutil.copy(LogFileName, dirpath)    
    print("Bacup completed successfully at ", datetime.datetime.now().strftime("%d_%m_%Y %H_%M_%S"))

    
def main():
    schedule.every(2).hours.do(CopiFile,sys.argv[1],sys.argv[2])
       
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()