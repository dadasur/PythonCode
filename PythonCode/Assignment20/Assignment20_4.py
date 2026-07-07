import threading

def checkupperstring(s):
    uppercount = 0
    for ch in s:
        ascii_value = ord(ch)
        if ascii_value >= ord('A') and ascii_value <= ord('Z'):
            uppercount = uppercount + 1
    print(f"uppercount is {uppercount}: Therad name and id is {threading.get_ident()} {threading.current_thread().name}")        
       

def checklowerstring(s):
    lowercount = 0
    for ch in s:
        ascii_value = ord(ch)
        if ascii_value >= ord('a') and ascii_value <= ord('z'):
            lowercount = lowercount + 1
    print(f"lowercount is {lowercount}: Therad name and id is {threading.get_ident()} {threading.current_thread().name}")

def checkdigitstring(s):
    digitcount = 0

    for ch in s:
        ascii_value = ord(ch)
        if ascii_value >= ord('0') and ascii_value <= ord('9'):
            digitcount = digitcount + 1
    print(f"digitcount is {digitcount}: Therad name and id is {threading.get_ident()} {threading.current_thread().name}")

def main():
    print(f"main thread id is : {threading.get_ident()} {threading.current_thread().name}")
    t1 = threading.Thread(target=checkupperstring,args=("Marvellous",),name="Capital")
    t2 = threading.Thread(target=checklowerstring,args=("Marvellous",),name="Small")
    t3 = threading.Thread(target=checkdigitstring,args=("Marvellous123",),name="Digit")
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()