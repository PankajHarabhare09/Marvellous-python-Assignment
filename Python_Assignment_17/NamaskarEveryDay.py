import schedule
import time

def PrintMsg():
    print("Namaskar..!!!")

def main():
    schedule.every().day.at("9:00").do(PrintMsg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()