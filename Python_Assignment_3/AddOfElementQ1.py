#Assignment 3>Q1. Addition of element in list

def main():
    print("Enter Number of Element: ")
    num = int(input())

    element = list()

    print("ENter Elements: ")
    for i in range(num):
        ele = int(input())
        element.append(ele)

    add = sum(element)
    print("ELements Are: ",element)
    print("Adddition of ELement is: ",add)

if __name__ == "__main__":
    main()

'''
    This question is about addition of elements in list
    so for that we have to create list first and after that accept number of element from user 
    and after that accpets the values from users and add that value in list with the help of append method
    after that we have sum method to add the all elements of lists and that addition we stored in one variable 
    and at the end we print that elements and print the addition of that elements.

    OUTPUT
    Enter Number of Element:
    5
    ENter Elements:
    10
    20
    30
    40
    50
    ELements Are:  [10, 20, 30, 40, 50]
    Adddition of ELement is:  150
'''