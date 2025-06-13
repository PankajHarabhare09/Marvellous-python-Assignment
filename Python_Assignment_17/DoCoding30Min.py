import schedule
import datetime
import time

def PrintMsg():
    print(datetime.datetime.now())
    print("Do Coding..!!!")

def main():
    schedule.every(30).minutes.do(PrintMsg)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ ==  "__main__":
    main()