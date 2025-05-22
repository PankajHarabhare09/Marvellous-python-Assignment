def main():
    print("Enter Number: ")
    num = int(input())
    fact = 1
    for i in range(num , 1, -1):
        fact = fact * i
    print("Factorial of ",num , " is: ",fact)

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter Number:
6
Factorial of  6  is:  720
'''