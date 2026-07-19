  
def main():
    fname = input("enter file name   : ")
    search = input("enter search word   : ")
    try:
        fobj = open(fname,"r")
        data = fobj.read()
        if search in data:
            print(f"{search} is found in {fname} file")
        else:
            print(f"{search} is not found in {fname} file")

    except FileNotFoundError as fobj:
        print("there is no such file")

if __name__ == "__main__":
    main()