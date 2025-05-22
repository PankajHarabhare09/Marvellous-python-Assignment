def main():

    print("Enter 5 Numbers: ")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    if n1>n2 and n1 >n3 and n1 > n4 and n1 > n5:
        print(n1 , " is greatest  Number")
    elif  n2 >n3 and n2 > n4 and n2 > n5:
        print(n2 , " is greatest  Number")
    elif n3 > n4 and n3 > n5:
        print(n3 , " is greatest  Number")
    elif n4 > n5:
         print(n4 , " is greatest  Number")
    else: 
        print(n5 , " is greatest  Number")


if __name__ == "__main__":
    main()

'''
OUTPUT
Enter 5 Numbers:
1
2
5
8
2
8  is greatest  Number