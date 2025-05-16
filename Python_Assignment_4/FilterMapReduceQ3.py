#Assignment 4>Q3. Filter Map Reduce

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
    Filtered_List = list(filter(lambda n: 70 <= n <=90 , Element))
    print("Using Filter Function: " , Filtered_List)

    #Map List
    Maped_List = list(map(lambda x: x + 10 , Element))
    print("Using Map Function: " , Maped_List)

    #Reduce List
    Reduce_List = reduce(lambda p , q: p * q , Element)
    print("Using Reduce Function: ",Reduce_List)

if __name__ == "__main__":
    main()

'''
    OUTPUT
    Enter the Number of Element:
    10
    Enter the Elements in List:
    55
    65
    25
    85
    95
    75
    35
    45
    89
    75
    Using Filter Function:  [85, 75, 89, 75]
    Using Map Function:  [65, 75, 35, 95, 105, 85, 45, 55, 99, 85]
    Using Reduce Function:  569051637451171875
'''