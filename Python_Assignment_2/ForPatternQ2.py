#Assignment 2>Q2. Pattern 1st

def main():
    print("Enter The Value: ")
    num = int(input())

    for i in range(num):#rows
        for j in range(num):#cols
            print("*" ,end = " ")
        print()

if __name__ == "__main__":
    main()

'''
    in this question i am trying to print basic pattern of *.
    so firstly i accept the value from user means how much row and columns i want ,
    then i create 1 for loop which helps me to print rows till the compared value gets false

    
    OUTPUT
    Enter The Value:
    5
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *