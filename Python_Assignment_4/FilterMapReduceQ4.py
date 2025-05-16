#Assignment 4>Q4. Filter Map Reduce

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
    Maped_List = list(map(lambda x: x * x , Element))
    print("Using Map Function: " , Maped_List)

    #Reduce List
    Reduce_List = reduce(lambda p , q: p + q , Element)
    print("Using Reduce Function: ",Reduce_List)

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter the Number of Element:
5
Enter the Elements in List:
17
8
9
4
6
Using Filter Function:  [8, 4, 6]
Using Map Function:  [289, 64, 81, 16, 36]
Using Reduce Function:  44
'''