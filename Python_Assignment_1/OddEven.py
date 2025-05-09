#Assignment 1>Q2. checking number is odd or even.

def ChkNum():
    print("Enter The number: ")
    number = int(input())

    if(number%2 == 0):
        print("Number is Even..!!")
    else:
        print("Number is Odd..!!")
    
def main():
    ChkNum()

if __name__ == "__main__":
    main()

#This Question is about if else condition.
#in this question i checked the number is even or with the help of if else.

'''OUTPUT
Enter The number:
10
Number is Even..!!

Enter The number:
7
Number is Odd..!!'''