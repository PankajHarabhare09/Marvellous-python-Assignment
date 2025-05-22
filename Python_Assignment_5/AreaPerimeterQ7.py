def ChkArea(l , b):
    area = 0
    area  = l * b
    return area

def ChkPerimeter(l , b):
    per = 0
    per = (2*(l + b))
    return per

def main():
    print("Enter Length: ")
    len = float(input())

    print("Enter Breadth: ")
    br = float(input())

    area = ChkArea(len , br)
    perimeter = ChkPerimeter(len , br)

    print("Area of Rectangle is: ",area)
    print("Perimeter Of Renctangle is: ",perimeter)

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter Length:
7
Enter Breadth:
2
Area of Rectangle is:  14.0
Perimeter Of Renctangle is:  18.0
'''