def main():
    word = ""
    frqency = 0
    fname = input("enter file name   : ")
    search = input("enter word name   : ")
    try:
        fobj = open(fname,"r")
        for line in  fobj:
            for ch in line:
                if ch !=" " and ch !="\n" and ch !="\t":
                 word = word + ch
                else:
                    if word == search:
                        frqency = frqency + 1
                    word = ""
        if word == search:
         frqency = frqency + 1
        fobj.close()
        print(f"{frqency} {search} appears in ",fname)
    except FileNotFoundError as fobj:
        print("there is no such file")

if __name__ == "__main__":
    main()