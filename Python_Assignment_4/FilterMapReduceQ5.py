#Assignment 4>Q5. Filter Map Reduce
from functools import reduce

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
    46
    78
    13
    68
    95
    43
    15
    85
    68
    100
    Using Filter Function:  [46, 78, 68, 68, 100]
    Using Map Function:  [92, 156, 26, 136, 190, 86, 30, 170, 136, 200]
    Maximum number:  100
'''