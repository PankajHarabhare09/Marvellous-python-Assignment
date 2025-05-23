def main():
    print("Enter String")
    string = str(input())

    rev_string = ""

    for i in string:
        rev_string = i + rev_string 

    if string == rev_string:
        print(string," is Palindrome")
    else:
        print(string," is not Palindrome")

if __name__ == "__main__":
    main()

'''
OUTPUT 1 
Enter String
radar
radar  is Palindrome

OUTPUT 2 
Enter String
pankaj
pankaj  is not Palindrome
'''