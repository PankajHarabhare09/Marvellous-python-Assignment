#Assignment 1>Q7. return true if number is divisible by 5 or return false

def DivByFive(num):
    if(num % 5 == 0):
        #return True  giving space as a output means Nothing 
        print("True")
    else:
        #return False  giving space as a output means Nothing 
        print("False")

def main():
    print("Enter Number: ")
    number = int(input())

    DivByFive(number)

if __name__ == "__main__":
    main()

# This Question is about if else condtion.
''' in this question , i used if else condition for checking the number is divisable by 5 or not.

OUTPUT 1
Enter Number:
5
True

OUTPUT 2
Enter Number:
7
False'''