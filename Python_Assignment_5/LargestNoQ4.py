def ChkLargeNo(no1 , no2 , no3):
    if(no1 > no2 and no1 > no3):
        print(no1 , "is greater")
    elif(no2 > no1 and no2 > no3):
        print(no2 , "is greater")
    else:
        print(no3 , "is greater")




def main():
    print("Enter 3 Numbers")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    ChkLargeNo(n1 , n2 , n3)

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter 3 Numbers
2
5
1
5 is greater
'''