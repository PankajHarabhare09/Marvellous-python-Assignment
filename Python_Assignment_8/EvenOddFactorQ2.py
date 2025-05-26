import threading
import multiprocessing

def EvenFactor(Number):
    sum = 0
    for i in range(Number):
        if i % 2 == 0:
            sum = sum + i
    print("addition of Even Number: ",sum)

def OddFactor(Number):
    sum = 0
    for i in range(Number):
        if i % 2 != 0:
            sum = sum + i
    print("Addition of Odd Number:",sum)

def main():
    t1 = multiprocessing.Process(target = EvenFactor , args = (54,))
    t2 = multiprocessing.Process(target = OddFactor , args = (55,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ =="__main__":
    main()

'''
OUTPUT
addition of Even Number:  702
Addition of Odd Number: 729
'''