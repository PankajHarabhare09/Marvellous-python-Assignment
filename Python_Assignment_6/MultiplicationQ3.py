def main():
    print("Enter Number: ")
    num = int(input())
    mul = 0

    for i in range(1 , 11):
        mul = num * i
        print(num , " * " , i ," = ",mul)

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter Number:
7
7  *  1  =  7
7  *  2  =  14
7  *  3  =  21
7  *  4  =  28
7  *  5  =  35
7  *  6  =  42
7  *  7  =  49
7  *  8  =  56
7  *  9  =  63
7  *  10  =  70
'''