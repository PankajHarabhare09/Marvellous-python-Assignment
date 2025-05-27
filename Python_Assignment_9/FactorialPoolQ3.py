import multiprocessing
import os

def is_Factorial(num):
    fact = 1
    for i in range(num , 1 , -1):
        fact = fact * i
    return fact

def main():
    NumList = [1,2,3,4,5,6,7,8,9,10]
    FactList = list()

    p = multiprocessing.Pool()

    FactList = p.map(is_Factorial , NumList)

    p.close()
    p.join()
    print(FactList)

if __name__ == "__main__":
    main()

'''
OUTPUT
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
'''