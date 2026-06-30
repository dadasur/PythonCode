
def Grade(No1):
    if No1 >= 75:
        return "Distiction"
    elif No1 >= 60:
        return "First Class"
    elif No1 >= 50:
        return "second class"
    else:
        return "Fail"
    
def main():
    value1 = int(input("enter marks : "))
    ret = Grade(value1)
    print(ret)
     
if __name__ == "__main__":
    main()
