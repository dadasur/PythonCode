import sys
def main():
    
    sfname= sys.argv[1]
    dfname= sys.argv[2]
    try:
        fobj = open(sfname,"r")
        data = fobj.read()
        fobj1 = open(dfname,"r")
        data1 = fobj1.read()
        if data == data1:
            print("success")
        else:
            print("Failure")
        fobj.close()
        fobj1.close()
    except FileNotFoundError as fobj:
        print("there is no such file")

if __name__ == "__main__":
    main()