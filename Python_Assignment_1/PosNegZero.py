#Assignment 1>Q6. Checking number is Positive , Negative  or Zero

def NumChk(no):
    if(no == 0):
        print("Number is  Zero..!!")
    elif(no > 0):
        print("Number is Positive..!!")
    elif(no < 0):
        print("Number is Negative..!!")
    else:
        print("Enter the Correct Number..!!")

def main():
    print("Enter Number: ")
    number = int(input())

    NumChk(number)

if __name__ == "__main__":
    main()

#in this Question , i used if else ladder which is ELIF for checking more than one condition.
''' in this question i used if else ladder for checking more than one condition.

OUTPUT 1
Enter Number:
20
Number is Positive..!!

OUTPUT 2
Enter Number:
-2
Number is Negative..!!

OUTPUT 3
Enter Number:
0
Number is  Zero..!!
