def main():
    linecount = 0
    word = True
    fname = input("enter file name   : ")
    try:
        fobj = open(fname,"r")
        for line in  fobj:

            for ch in line:
                if ch !=" " and ch !="\n" and ch !="\t":
                    if  word:
                        linecount = linecount+1
                        word = False
                else:
                    word = True
        fobj.close()
        print("total number of word in Demo.txt is",linecount)
    except FileNotFoundError as fobj:
        print("there is no such file")

if __name__ == "__main__":
    main()