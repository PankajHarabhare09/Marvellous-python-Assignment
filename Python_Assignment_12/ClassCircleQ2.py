class Circle:
    PI = 3.14
    def __init__(self , rad):
        self.radius = rad

    def CalculateArea(self):
        Area = 0.0
        Area = self.PI * (self.radius * self.radius)
        return Area
    
    def CalculateCircumferance(self):
        circumfarence = 0.0
        circumfarence = 2 * self.PI * self.radius
        return circumfarence

def main():
     Cobj = Circle(2.2)

     AreaRet = Cobj.CalculateArea()
     CirRet = Cobj.CalculateCircumferance()

     print("Area of Circle: ",AreaRet)
     print("Circumfarence of Circle: ",CirRet)

if __name__ == "__main__":
    main()

'''
OUTPUT
Area of Circle:  15.197600000000003
Circumfarence of Circle:  13.816000000000003
'''
