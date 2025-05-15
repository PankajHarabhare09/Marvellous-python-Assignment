#Assignment 3>Q2. Maximum Element in list

def main():

    elements = list()
    print("Enter Number of Element: ")
    num = int(input())

    print("Enter The ELements in list: ")
    for i in range(num):
        val = int(input())
        elements.append(val)

    maxNum = max(elements)
    print("Elements Of List are: ",elements)
    print("Maximum Number In List is: ",maxNum)

if __name__ == "__main__":
    main()

'''
    This Question is About finding maximum number from list.
    for that we have to create list first and after that accept number of element from user 
    and after that accpets the values from users and add that value in list with the help of append method
    after that we have max method to find maximum  elements in the list and that maximum number we stored in one variable 
    and at the end we print that elements and print the maximum element from list.

    OUTPUT
    Enter Number of Element:
    5
    Enter The ELements in list:
    10
    2080
    45
    52
    785
    Elements Of List are:  [10, 2080, 45, 52, 785]
    Maximum Number In List is:  2080
'''