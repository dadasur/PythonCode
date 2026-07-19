def main():
    fname1 = input("enter Source file name   : ")
    fname2= input("enter Destination file name   : ")
    try:
        fobj = open(fname1,"r")
        data = fobj.read()
        fobj1 = open(fname2,"w")
        fobj1.write(data)
        fobj.close()
        fobj1.close()
    except FileNotFoundError as fobj:
        print("there is no such file")

if __name__ == "__main__":
    main()