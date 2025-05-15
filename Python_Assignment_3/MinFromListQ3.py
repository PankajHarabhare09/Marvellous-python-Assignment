#Assignment 3>Q3. Minimum Element in list

def main():

    elements = list()
    print("Enter Number of Element: ")
    num = int(input())

    print("Enter The ELements in list: ")
    for i in range(num):
        val = int(input())
        elements.append(val)

    minNum = min(elements)
    print("Elements Of List are: ",elements)
    print("Maximum Number In List is: ",minNum)

if __name__ == "__main__":
    main()

'''
    This Question is About finding Minimum number from list.
    for that we have to create list first and after that accept number of element from user 
    and after that accpets the values from users and add that value in list with the help of append method
    after that we have min method to find minimum  elements in the list and that minimum number we stored in one variable 
    and at the end we print that elements and print the minimum element from list.

    OUTPUT
    Enter Number of Element:
    5
    Enter The ELements in list:
    11
    55
    75
    86
    02
    Elements Of List are:  [11, 55, 75, 86, 2]
    Maximum Number In List is:  2
'''