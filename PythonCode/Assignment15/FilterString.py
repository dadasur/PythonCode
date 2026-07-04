
checkstring = lambda value : (len(value)==5)
            
def main():
    Values = list(map(str,input("Enter the String in list").split()))
    ret = list(filter(checkstring,Values))
    print(ret)

if __name__ == "__main__":
    main()