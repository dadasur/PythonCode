import os
def main():
    fname = input("enter file name   : ")
    if(os.path.exists(fname)):
     print("File exists in current directory")
    else:
     print("File not exists in current directory")
    

if __name__ == "__main__":
    main()