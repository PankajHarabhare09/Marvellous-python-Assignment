#Assignment 1>Q3. Addition of 2 numbers

def Add(num1 , num2):
    return num1 + num2
    

def main():
    print("Enter 1st number: ")
    no1 = int(input())

    print("Enter 2nd Number: ")
    no2 = int(input())

    addition = Add(no1 , no2)
    print("Addition is: " , addition)

if __name__ == "__main__":
    main()


#This Question is About Parameterized Constructor.
#so in this question i have give 2 values directly to the Add() function for the return the addtion of that values.
#and i wrote the actual logic in  main() function.

'''OUTPUT
Enter 1st number:
123456789
Enter 2nd Number:
987654321
Addition is:  1111111110'''