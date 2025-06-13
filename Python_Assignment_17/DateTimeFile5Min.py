import schedule
import time
import datetime

def TimeToFile():
    CurrentTime = datetime.datetime.now()

    FileName = input("Enter File Name For Date Time: ")
    Fobj = open(FileName , "a")
    Fobj.write(CurrentTime)
    print("Time Is Written in File is: ",CurrentTime)
    Fobj.close()

def main():
    schedule.every(5).minutes.do(TimeToFile)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()