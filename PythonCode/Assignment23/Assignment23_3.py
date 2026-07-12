from multiprocessing import Pool
import os

def EvenCount(no):
    
    count =  no//2
    print(f"procss id {os.getpid()} input number {no} even count id {count} ")
        
def main():
    Data = [1000000,2000000,3000000,4000000]
    with Pool(processes=4) as pool:
          pool.map(EvenCount,Data)

if __name__ == "__main__":
    main()