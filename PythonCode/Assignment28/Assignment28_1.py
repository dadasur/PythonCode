def main():
    linecount = 0
    fname = input("enter file name   : ")
    try:
        fobj = open(fname,"r")
        for line in  fobj:
            linecount = linecount+1
        fobj.close()
        print("total number of line in Demo.txt is",linecount)
    except FileNotFoundError as fobj:
        print("there is no such file")

if __name__ == "__main__":
    main()