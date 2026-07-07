def DisplyFirstTenEvenNumber(name):
    count = 0
    for i in name:
        count = count + 1
    return count 
              

def main():
    value1 = input("Enter name")
    ret = DisplyFirstTenEvenNumber(value1)
    print(ret)


if __name__ == "__main__":
    main()
