import threading
import time

def Pattern():
    for i in range(6):
        print(i)

def main():
    t1 = threading.Thread(target = Pattern)
    t2 = threading.Thread(target = Pattern)
    t3 = threading.Thread(target = Pattern)

    print("1st Thread")
    t1.start()
    time.sleep(1)
    print("2nd Thread After 1 sec")
    t2.start()
    time.sleep(1)
    print("3rd Thread After 1 sec")
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()

'''
OUTPUT
1st Thread
0
1
2
3
4
5
2nd Thread
0
1
2
3
4
5
3rd Thread
0
1
2
3
4
5
'''