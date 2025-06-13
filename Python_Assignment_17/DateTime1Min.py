import schedule
import time
import datetime

def ShowDateTime():
    print("Current Date And Time is: ",datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(ShowDateTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

'''
OUTPUT
Current Date And Time is:  2025-06-12 17:36:51.372546
Current Date And Time is:  2025-06-12 17:37:51.400655
'''