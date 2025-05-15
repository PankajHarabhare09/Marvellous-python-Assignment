#Assignment 2>Q6. Pattern 

def main():

    print("Enter Number: ")
    no = int(input())

    for i in range(no):
        for j in range(1 , no+1 , 1):
            print(j , end = " ")
        print()

if __name__ == "__main__":
    main()

'''
    This Question is about , printing pattern
    there are i used 2 for loops one for rows and one for columns
    1st for loop is used for store no in i it means if the value no is 5 so 5 is store in i and 1st loop is iterate 
    5 times
    in second loop i give 1 at start  , no + 1 in stop , 1 by step it means loop start from 1 and end with 5 + 1 and 
    increment by 1
    after that ill give print function in that i give j for printing their values and end keyword for same line
    at the end i have given print for next line

    Enter Number:
    5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5