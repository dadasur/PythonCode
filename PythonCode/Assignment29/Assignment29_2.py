def main():
    fname = input("enter file name   : ")
    try:
        fobj = open(fname,"r")
        data = fobj.read()
        print(data)
        fobj.close()
    except FileNotFoundError as fobj:
        print("there is no such file")

if __name__ == "__main__":
    main()