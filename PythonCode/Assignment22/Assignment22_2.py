from multiprocessing import Pool
import os

def factorial(no):
    result = 1
    for i in range(1, no + 1):
        result = result * i
    print(f"procss id {os.getpid()} input number {no} fact is {result} ")
        
def main():
    Data = [10,15,20,25]
    with Pool(processes=4) as pool:
          pool.map(factorial,Data)

if __name__ == "__main__":
    main()