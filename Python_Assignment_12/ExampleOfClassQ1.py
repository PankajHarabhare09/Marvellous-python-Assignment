class Demo:
    num3 = 10
    def __init__(self , no1 , no2):
        self.num1 = no1
        self.num2 = no2

    def Fun(self):
        print("Num1 Value Is (FUN): ",self.num1)
        print("Num2 Value Is (FUN): ",self.num2)
        print("Num3 value is (FUN): ",self.num3)

    def Gun(self):
        print("Num1 Value Is (GUN): ",self.num1)
        print("Num2 Value Is (GUN): ",self.num2)
        print("Num3 value is (GUN): ",self.num3)

def main():
    Fobj = Demo(100 , 200)
    Gobj = Demo(101 , 201)

    Fobj.Fun()
    Gobj.Fun()
    Fobj.Gun()
    Gobj.Gun()

if __name__ == "__main__":
    main()

'''
OUTPUT
Num1 Value Is (FUN):  100
Num2 Value Is (FUN):  200
Num3 value is (FUN):  10
Num1 Value Is (FUN):  101
Num2 Value Is (FUN):  201
Num3 value is (FUN):  10
Num1 Value Is (GUN):  100
Num2 Value Is (GUN):  200
Num3 value is (GUN):  10
Num1 Value Is (GUN):  101
Num2 Value Is (GUN):  201
Num3 value is (GUN):  10
'''