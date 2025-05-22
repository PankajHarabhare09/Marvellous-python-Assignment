def ChkEvenOdd(no):
    if(no / 2 == 0):
        print(no ,"is Even")
    else:
        print(no , "is Odd")
    
def main():
    print("Enter Number: ")
    num = int(input())

    ChkEvenOdd(num)

if __name__ == "__main__":
    main()

'''
OUTPUT 1
Enter Number:
41
41 is Odd

OUTPUT 2
Enter Number:
2
2 is Odd
'''