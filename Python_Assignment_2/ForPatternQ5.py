#Assignment 2>Q5. Pattern 

def main():
    print("Enter Number: ")
    no = int(input())

    for i in range(no , 0 , -1):
        for j in range(i):
            print("*" , end = " ")
        print()

if __name__ == "__main__":
    main()

'''
    This Question is about printing reveser pattern , 
    in this question , i have use 2 for loop 1st for loop is for printing rows and 2nd is for columns
    in 1st for loop i used revese condition means input is my start , 0 is my stop and -1 is step 
    and my 2nd for loop is totally depends on 1st for loop , in range function ill give i it means 
    the value of i is store in j which is colums and after that ill give print function in that i have 
    given * and end keyword with the help of end keyword at the end of statement the compiler are not 
    going to next line the output will print on same line till the if condition get false and at the end 
    i have given 1 empty print function for the next line.
    
    OUTPUT
    Enter Number:
    5
    * * * * *
    * * * *
    * * *
    * *
    *
    '''