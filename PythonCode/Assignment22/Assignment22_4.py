from multiprocessing import Pool
import time


def sumfifthpowers(no):
    res = (no * no * (no + 1) * (no + 1) * (2 * no * no + 2 * no - 1)) // 12
    return res

def main():
    Data = [1000000,2000000,3000000,4000000]
    starttime = time.perf_counter()
    with Pool(processes=4) as pool:
          result = pool.map(sumfifthpowers,Data)
    print(result)
    endttime = time.perf_counter()
    print(f"time require is : {endttime-starttime:.5f} second")

if __name__ == "__main__":
    main()