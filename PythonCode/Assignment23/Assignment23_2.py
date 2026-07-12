from multiprocessing import Pool
import os

def square(no):
    
    no1 =  (no+1)//2
    no1 = no1 * no1
    print(f"procss id {os.getpid()} input number {no} sum of odd number {no1} ")
        
def main():
    Data = [1000000,2000000,3000000,4000000]
    with Pool(processes=4) as pool:
          pool.map(square,Data)

if __name__ == "__main__":
    main()