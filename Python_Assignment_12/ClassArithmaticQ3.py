class Arithmatic:
    def __init__(self , num1 , num2):
        self.val1 = num1
        self.val2 = num2

    def Addition(self):
        add = 0
        add = self.val1 + self.val2
        return add

    def Subsrtaction(self):
        sub = 0
        sub = self.val1 - self.val2
        return sub

    def Multiplication(self):
        mul = 0
        mul = self.val1 * self.val2
        return mul

    def Division(self):
        div = 0
        div = self.val1 / self.val2
        return div

def main():
    Aobj = Arithmatic(10 , 2)

    AddRet=Aobj.Addition()
    SubRet=Aobj.Subsrtaction()
    MulRet=Aobj.Multiplication()
    DivRet=Aobj.Division()

    print("Addition is: ",AddRet)
    print("Substraction is: ",SubRet)
    print("Multiplication is: ",MulRet)
    print("Division is: ",DivRet)

if __name__ == "__main__":
    main()


"""
OUTPUT
Addition is:  12
Substraction is:  8
Multiplication is:  20
Division is:  5.0
"""
