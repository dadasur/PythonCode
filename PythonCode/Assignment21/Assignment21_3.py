import threading

counter = 0
lock = threading.Lock()

def incrementnmber():
    global counter
    for i in range(300000):
        lock.acquire()
        counter += 1
        lock.release()

def main():

    t1 = threading.Thread(target=incrementnmber)
    t2 = threading.Thread(target=incrementnmber)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(counter)


if __name__ == "__main__":
    main()