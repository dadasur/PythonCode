import sys
def main():
    
    fname= sys.argv[1]
    try:
        fobj = open(fname,"r")
        data = fobj.read()
        fobj1 = open("Demo1.txt","w")
        fobj1.write(data)
        fobj.close()
        fobj1.close()
    except FileNotFoundError as fobj:
        print("there is no such file")

if __name__ == "__main__":
    main()