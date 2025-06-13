import schedule

def JayGanesh():
    print("Jay Ganesh..!!!")

def main():
    schedule.every(2).seconds.do(JayGanesh)
    while True:
        schedule.run_pending()
        time.sleep(1)
    print("After 2 seconds")
if __name__ == "__main__":
    main()
'''
OUTPUT
Jay Ganesh..!!!
Jay Ganesh..!!!
'''