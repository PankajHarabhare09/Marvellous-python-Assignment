#Assignment 2>Q6. Pattern 

def main():
    print("Enter Number: ")
    no = int(input())

    for i in range(1 , no+1 , 1):#no = 5
        for j in range(1 , i+1):
            print(j , end = " ")
        print()

if __name__ == "__main__":
    main()

'''
    this question is about printing pattern.
    here i used 2 for loops one for rows and one for columns
    1st for loop is used for iterate for no times it means if the value no is 5 so 5 is store in i and 1st loop is iterate 
    5 times
    in second loop i give 1 at start  , i + 1 in stop it means loop start from 1 and end with i + 1
    after that in print statement ill give j for printing its value and end keyword for same line
    at the end print() for new line

    OUTPUT
    Enter Number:
    5
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
'''