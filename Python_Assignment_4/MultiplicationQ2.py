#Assignment 4>Q2. Multiplication of 2 two Number Using lambda Function

def  main():
    print("Enter  Numbers: ")
    num1 = int(input())
    num2 = int(input())

    mul = lambda a , b: (a * b)
    print("Multiplication Is: " , mul(num1 , num2))

if __name__ == "__main__":
    main()

'''
    this question is about multiply two numbers with the help of lambda function.
    so for that we have to take 2 different input from users and after that we have to create one lambda function
    in that function we can give one expression and multply that numbers and print as a input.
    
    OUTPUT
    Enter  Numbers:
    4
    3
    Multiplication Is:  12
'''