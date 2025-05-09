#Assignment 1>Q8. Printing * using for loop and range.

def pattern(num):
    for n in range (num):
        print("*" , end = " ")

def main():
    print("Enter the Number: ")
    no = int(input())

    pattern(no)

if __name__ == "__main__":
    main()

#this question is about printing pattern using for loop and range function.
'''
OUTPUT
Enter the Number:
5
* * * * *
'''