def main():

    print("Enter 2 numbers for Multiplication: ")
    no1 = int(input())
    no2 = int(input())

    Multiplication = lambda a , b: a * b

    print("Multiplication is: " , Multiplication(no1 , no2))

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter 2 numbers for Multiplication:
4
2
Multiplication is:  8
'''