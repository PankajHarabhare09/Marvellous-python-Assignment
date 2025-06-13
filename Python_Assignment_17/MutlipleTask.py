import schedule
import time

def LunchMsg():
    print("Lunch Time..!!!")

def WorkMsg():
    print("Wrap Your Work..!!!")

def main():
    schedule.every().day.at("13:00").do(LunchMsg)
    schedule.every().day.at("18:00").do(WorkMsg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()