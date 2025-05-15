#Assignment 3>Q4. Frequency Of Number from list
def main():

    elements = list()
    print("Enter The Number Of Element: ")
    num = int(input())

    print("Enter Elements in List: ")
    for i in range(num):
        val = int(input())
        elements.append(val)

    print("Enter Element To Search: ")
    search = int(input())
    count = 0
    for fre in elements:
        if(fre == search):
            count = count + 1
    
    print("Elements In List: ", elements)
    print("Frequency of Serached Number: ",count)


if __name__ == "__main__":
    main()

''' 
    This question is about frequency of searched number
    for that we have to create list first and after that accept number of element from user 
    and after that accpets the values from users and add that value in list with the help of append method
    after that we have to create one more variable for store sreached value after that we have to comapre each element 
    of list with search variable and after that we have to create count variable for store the count of repeated element
    for comparision we craeted if condition and compare searched and each element of list and increment count + 1 and 
    after that we print the list and frequency of element.

    OUTPUT
    Enter The Number Of Element:
    3
    Enter Elements in List:
    1
    2
    1
    Enter Element To Search:
    1
    Elements In List:  [1, 2, 1]
    Frequency of Serached Number:  2
'''