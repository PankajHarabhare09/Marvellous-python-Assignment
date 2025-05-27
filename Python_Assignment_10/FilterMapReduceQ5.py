def main():
    Element = list()
    print("Enter the Number of Element: ")
    num = int(input())

    print("Enter the Elements in List: ")
    for i  in range(num):
        val = int(input())
        Element.append(val)

    #filter List
    Filtered_List = list(filter(lambda n: n % 2 == 0 , Element))
    print("Using Filter Function: " , Filtered_List)

    #Map List
    Maped_List = list(map(lambda x: x * 2 , Element))
    print("Using Map Function: " , Maped_List)

    #Maximum Number
    MaxNum = max(Element)
    print("Maximum number: ",MaxNum)

if __name__ == "__main__":
    main()
'''
OUTPUT
Enter the Number of Element:
10
Enter the Elements in List:
45
65
75
95
21
56
32
78
95
74
Using Filter Function:  [56, 32, 78, 74]
Using Map Function:  [90, 130, 150, 190, 42, 112, 64, 156, 190, 148]
Maximum number:  95
'''