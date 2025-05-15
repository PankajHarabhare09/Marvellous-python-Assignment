#Assignment 3>Q5. Addition of Prime Numbers
from MarvellousNum import ChkPrime

elements = list()

def ListPrime():
    no = 0
    for el in elements:
        if ChkPrime(el):
            no = no + el
    
    print("Sum of Prime Number is: ",no)


def main():
    print("Enter The number Of Elements: ")
    num = int(input())

    print("Enter Elements In List: ")
    for i in range(num):
        val = int(input())
        elements.append(val)
    
    ListPrime()
    print("Elements in List Are: ",elements)


if __name__ == "__main__":
    main()

'''
    This question is about addition of prime number which is stored in list.
    for that we have to create one list for storing elements after that we have to decide how much  elements we want to store in it
    after that we can accpet the elements and store in the list We call the another module where the ChkPrime() function is available
    after that we can check each and every element is prime or not for that we have to create one seperate function which is ListPrime()
    in that we can check elements are prime or not and after that if element is prime number then we can add with another prime number
    and at the end we can print elements of lists and addition of prime numbers.
    OUTPUT 
    Enter The number Of Elements:
    5
    Enter Elements In List:
    10
    5
    7
    2
    15
    Sum of Prime Number is:  14
    Elements in List Are:  [10, 5, 7, 2, 15]
'''