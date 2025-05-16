#Assignment 4>Q1. Power Of Numbers using lambda function

def main():
    print(" 1st Number: ")
    no1 = int(input())
    num1 = lambda a: (2 ** a)
    print(num1(no1))

    print("2nd Number: ")
    no2 = int(input())
    num2 = lambda b: (2 ** b)
    print(num2(no2))

if __name__ == "__main__":
    main()

'''
    this question is about find the power of two using different numbers with the help of lambda function.
    so for that we have to take 2 different input from users and after that we have to create one lambda function
    in that function we can give one expression and multply that number twice and after that print that anonymous
    number.
    
    OUTPUT
    1st Number:
    4
    16
    2nd Number:
    6
    64
'''