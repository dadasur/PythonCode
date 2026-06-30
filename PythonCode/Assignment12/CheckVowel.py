from msvcrt import getch
def CheckVowel(ch):
    if ch == 'a' or ch == 'i' or ch == 'e' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'I' or ch == 'E' or ch == 'O' or ch == 'U':
        return True
    else:
        return False
    

def main():
    print("enter one character")
    value = getch().decode('utf-8')
    ret = CheckVowel(value)
    if ret == True:
        print("yes "+value+" is vowel")
    else:
        print("No "+value+" is not vowel")
    

if __name__ == "__main__":
    main()




