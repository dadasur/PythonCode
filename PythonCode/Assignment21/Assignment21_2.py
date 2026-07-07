import threading


def MaxElement(Data1):
    max = Data1[0]
    for i in Data1:
       if i > max:
          max = i
    print(f"max  number is {max} thread id is : {threading.get_ident()}")

def MinElement(Data1):
    min = Data1[0]
    for i in Data1:
       if i < min:
          min = i
    print(f"min  number is {min} thread id is : {threading.get_ident()}")

def main():
      
      n = input("Enter All N Number sepreated by space : ")
      values = []
      for i in n.split():
        values.append(int(i))
      print(f"main thread id is : {threading.get_ident()}")
      t1 = threading.Thread(target=MaxElement,args=(values,))
      t2 = threading.Thread(target=MinElement,args=(values,))
      t1.start()
      t2.start()
      t1.join()
      t2.join()


if __name__ == "__main__":
    main()