from multiprocessing import Pool

def sumofsquares(no):    
    return no * (no + 1) * (2 * no + 1) // 6
        
def main():
    Data = [1000000,2000000,3000000,4000000]
    with Pool(processes=4) as pool:
          result = pool.map(sumofsquares,Data)
    print(result)

if __name__ == "__main__":
    main()
