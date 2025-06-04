class Rectangle:
    def __init__(self , len , wid):
        self.length = len
        self.width = wid

    def Area(self):
        area = 0.0
        area = self.length * self.width
        print("Area of Rectangle is: ",area)

    def Perimeter(self):
        perimeter = 0.0
        perimeter = 2 * (self.length + self.width)
        print("Perimeter of Rectangle is: ",perimeter)

def main():
    Robj = Rectangle(5 , 2.5)
    Robj.Area()
    Robj.Perimeter()

if __name__ == "__main__":
    main()


"""
OUTPUT
Area of Rectangle is:  12.5
Perimeter of Rectangle is:  15.0
"""