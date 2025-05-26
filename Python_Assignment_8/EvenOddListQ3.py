import threading

def EvenList(*Elist):
    evens = list()

    for i in Elist:
        if i % 2 == 0:
            evens.append(i)
    sum = 0
    for add in evens:
        sum = sum + add
    print("Addition of Even Numbers: ",sum)

def OddList(*Olist):
    odds = list()

    for i in Olist:
        if i % 2 == 0:
            odds.append(i)
    sum = 0
    for add in Olist:
        sum = sum + add
    print("Addition of Odd Numbers: ",sum)

def main():

    t1 = threading.Thread(target = EvenList , args = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
    t2 = threading.Thread(target = OddList , args = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

'''
OUTPUT
Addition of Even Numbers:  110
Addition of Odd Numbers:  210
'''
