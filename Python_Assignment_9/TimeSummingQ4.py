import time
import threading
import multiprocessing

def SummingFun():
    sum = 0
    for i in range(1 , 10000000 , 1):
        sum = sum + i
    print("Addition: ",sum)

def main():

    #function
    FunStart = time.time()
    SummingFun()
    FunEnd = time.time()

    FunTimeTaken = FunEnd - FunStart
    print("Function Taken Time For Execution: ",FunTimeTaken)

    #THREADING
    ThStart = time.time()
    t1 = threading.Thread(target = SummingFun)

    t1.start()
    t1.join()
    ThEnd = time.time()
    ThTimeTaken = ThEnd - ThStart
    print("Thread Taken Time For Execution: ",ThTimeTaken)

    #Processing
    ProStart = time.time()
    p1 = multiprocessing.Process(target = SummingFun)

    p1.start()
    p1.join()
    ProEnd = time.time()

    print("Prodcess Taken Time For Execution: ",ProEnd - ProStart)


if __name__ == "__main__":
    main()

'''
OUTPUT
Addition:  49999995000000
Function Taken Time For Execution:  0.8917698860168457
Addition:  49999995000000
Thread Taken Time For Execution:  0.8794641494750977
Addition:  49999995000000
Prodcess Taken Time For Execution:  1.1534857749938965
'''