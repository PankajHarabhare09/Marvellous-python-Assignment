
def main():
    print("Enter 1st Number:")
    num1 = int(input())
    pow1 = lambda a: (2 ** a)
    print("Power is: ",pow1(num1))

    print("Enter 2nd Number: ")
    num2 = int(input())
    pow2 = lambda b: (2 ** b)
    print("Power is: ",pow2(num2))


if __name__ == "__main__":
    main()

'''
OUTPUT
Enter 1st Number:
4
Power is:  16
Enter 2nd Number:
6
Power is:  64
'''