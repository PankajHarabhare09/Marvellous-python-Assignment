#Assignment 2>Q1. Main Class

import ArithmaticOp

def main():
    print("Enter 1st Number: ")
    val1 = int(input())

    print("Enter 2nd Number: ")
    val2 = int(input())

    add = ArithmaticOp.add(val1 , val2)
    sub = ArithmaticOp.sub(val1 , val2)
    mul = ArithmaticOp.mul(val1 , val2)
    div = ArithmaticOp.div(val1 , val2)

    print("1st Number: ",val1)
    print("2nd Number: ",val2)

    print("Addition of This Numbers: ",add)
    print("Substraction of This Numbers: ",sub)
    print("Multiplication of This Numbers: ",mul)
    print("Division of This Numbers: ",div)


if __name__ == "__main__":
    main()

''' In this file i imported ArithmaticOp module with the help of import keyword which contain only function
    after that i accept two values from user after that i have given that value to that functions at the of
    calling that function after and store that function in one variable after that i'll print that variable 
    in print statement.

    OUTPUT
    Enter 1st Number:
    10
    Enter 2nd Number:
    5
    1st Number:  10
    2nd Number:  5
    Addition of This Numbers:  15
    Substraction of This Numbers:  5
    Multiplication of This Numbers:  50
    Division of This Numbers:  2.0
    '''