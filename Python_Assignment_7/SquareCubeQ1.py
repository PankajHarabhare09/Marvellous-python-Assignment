def main():
    print("Enter Number: ")
    num = int(input())

    square = lambda sq: (sq * sq)
    cube = lambda cb: (cb * cb * cb)

    print("Square is: ",square(num))
    print("Cube is: ",cube(num))

if __name__ == "__main__":
    main()

'''
OUTPUT 
Enter Number:
5
Square is:  25
Cube is:  125
'''