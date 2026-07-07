import threading

def rangee(no):
    for i in range(1,no+1):
        print(f"{i}: Therad  id is {threading.get_ident()}")        
       

def reverseofrange(no):
    for i in range(no,0,-1):
        print(f"reverse {i}: Therad  id is {threading.get_ident()}")        
       

def main():
    print(f"main thread id is : {threading.get_ident()} {threading.current_thread().name}")
    t1 = threading.Thread(target=rangee,args=(50,))
    t2 = threading.Thread(target=reverseofrange,args=(50,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()