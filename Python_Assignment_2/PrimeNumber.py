#Assignment 2>Q4. Prime Number

def isPrime(n):
    if (n <= 1):
        return False

    for i in range(2 , n):
        if (n % i == 0):
            return False
    return True

def main():
    print("Enter The Number: ")
    num = int(input())

    if (isPrime(num)):
        print("Prime Number..")
    else:
        print("Not Prime Number")

if __name__ == "__main__":
    main()

'''
    this question is about prime number , prime number means the number is divisible only itself
    so for that i want to create one function in that i create one if condition as you know 0 or 1 
    are not prime number so for that i have checked my number is greater than 1 or not if it is less than or equal to 1
    then it will return the false or it is greater than 1 it will return true after that i have created one for loop 
    for chhecking greater than 1 number is prime or not so for that in range function i have given Start 2 beacuse its the
    next greater number to 1 and stop is my input and in that for loop i give if condition for checking prime number in 
    that condition i check the given number is divided by 2 or reminder is 0 or not if reminder is zero it returns false
    or else true after that inn main function i have checked that function with the help of if condition if that function
    is correct then print prime number or else print not prime number..
    OUTPUT
    Enter The Number:
    5
    Prime Number..

    Enter The Number:
    4
    Not Prime Number
    '''