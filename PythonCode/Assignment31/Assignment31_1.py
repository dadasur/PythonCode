import schedule
import time

def Display(message):
    print(message)

def main():

    try:
        msg = input("Enter a message:   ")
        
        Intervals = int(input("Enter a time interval in seconds:    "))
    
        schedule.every(Intervals).seconds.do(Display,message=msg)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as ex:
        print("Kindly enter correct seconds",ex)

if __name__ == "__main__":
    main()

