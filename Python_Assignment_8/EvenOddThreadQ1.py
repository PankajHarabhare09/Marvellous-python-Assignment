
import multiprocessing

def EvenNo():
    for i in range(1 , 21 ,1):
        if i % 2 == 0:
            Even = i
            print("Even Number is",Even)
    print("-----------------------------------------")
        
def OddNo():
    for i in range(1 , 20 , 1):
        if i % 2 != 0:
            Odd = i
            print("Odd Number is: ",Odd)




def main():
    #t1 = threading.Thread(target = EvenNo )
    #t2 = threading.Thread(target = OddNo)
    
    t1 = multiprocessing.Process(target = EvenNo)
    t2 = multiprocessing.Process(target = OddNo)

    t1.start()
    
    t2.start()

    t1.join()
    t2.join()   

if __name__ == "__main__":
    main()

'''
OUTPUT

Even Number is 2
Even Number is 4
Even Number is 6
Even Number is 8
Even Number is 10
Even Number is 12
Even Number is 14
Even Number is 16
Even Number is 18
Even Number is 20
-----------------------------------------
Odd Number is:  1
Odd Number is:  3
Odd Number is:  5
Odd Number is:  7
Odd Number is:  9
Odd Number is:  11
Odd Number is:  13
Odd Number is:  15
Odd Number is:  17
Odd Number is:  19
'''