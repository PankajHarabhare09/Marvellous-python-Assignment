def main():
    EvenList = list()

    print("Enter Number of Elements: ")
    ElNum = int(input())

    print("Enter The Elements in List: ")
    for i in range(ElNum):
        Elements = int(input())
        EvenList.append(Elements)

    Flitered_List = list(filter(lambda val: (val % 2 == 0) , EvenList))

    print("Original list: ",EvenList)
    print("Filtered List: ",Flitered_List)

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter Number of Elements:
5
Enter The Elements in List:
2
4
5
6
1
Original list:  [2, 4, 5, 6, 1]
Filtered List:  [2, 4, 6]
'''