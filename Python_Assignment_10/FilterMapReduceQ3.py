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
Using Filter Function:  [78, 85]
Using Map Function:  [88, 64, 75, 33, 106, 95, 62, 66, 35, 24]
Using Reduce Function:  52369584583680000
'''