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
Using Filter Function:  [98, 36, 68, 48]
Using Map Function:  [1681, 25, 9604, 1296, 625, 2025, 4624, 2304, 225, 1225]
Using Reduce Function:  416
'''