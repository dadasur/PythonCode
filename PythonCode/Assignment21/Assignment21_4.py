from concurrent.futures import ThreadPoolExecutor
import threading
def addition(Data1):
    print(f"Addition thread id is : {threading.get_ident()}")
    sum = 0
    for i in Data1:
       sum = sum + i
    return sum

def square(Data1):
    print(f"Square thread id is : {threading.get_ident()}")
    sum = 1
    for i in Data1:
       sum = sum * i
    return sum


def main():
    values  = [1,2,3,4,5]
    with ThreadPoolExecutor(max_workers=2) as executor:
     future1 = executor.submit(addition, values)
     print("Addition is : ",future1.result())
     future2 = executor.submit(square, values)
     print("Product is : ",future2.result())


if __name__ == "__main__":
    main()