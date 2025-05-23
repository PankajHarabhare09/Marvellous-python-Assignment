from functools import reduce

def main():
    ProductList = list()
    print("Enter The Number Of Element: ")
    ElNum = int(input())

    print("Enter Elements in list: ")
    for i in range(ElNum):
        value = int(input())
        ProductList.append(value)

    Reduce_List = reduce(lambda val1 , val2: (val1 * val2) , ProductList)

    print("Original List: ",ProductList)
    print("Reduced List: ",Reduce_List)

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter The Number Of Element:
5
Enter Elements in list:
2
4
6
8
10
Original List:  [2, 4, 6, 8, 10]
Reduced List:  3840
'''