from multiprocessing import Pool

def CheckPrime(No):
    if No <= 1:
        return False
    for i in range(2, int(No), 1):
        if No % i == 0:
            return False
    return True

def CountPrimes(No1):
    count = 0
    for i in range(1, No1 + 1):
        if CheckPrime(i):
            count += 1
    print(f"Prime numbers between 1 and {No1} = {count}")
        
def main():
    Data = [10,20,30,40]
    with Pool(processes=4) as pool:
          pool.map(CountPrimes,Data)
    

if __name__ == "__main__":
    main()
