def main():
    value = list()
    print("Enter the Number of Element: ")
    ElNum = int(input())

    print("Enter the Elements: ")
    for i in range(ElNum):
        Elements = int(input())
        value.append(Elements)

    Maped_list = list(map(lambda val: val * 2 , value))
    print("Original List: ",value)
    print("Doubled List: ",Maped_list)

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter the Number of Element:
5
Enter the Elements:
2
4
6
8
10
Original List:  [2, 4, 6, 8, 10]
Doubled List:  [4, 8, 12, 16, 20]
'''