class Calculator:
    def __init__(self , val1 , val2):
        self.Num1 = val1
        self.Num2 = val2

    def Addition(self):
        add = 0
        add = self.Num1 + self.Num2
        print("Addition is: ",add)
    
    def Substraction(self):
        sub = 0
        sub = self.Num1 - self.Num2
        print("Addition is: ",sub)
    
    def Multiplication(self):
        mul = 0
        mul = self.Num1 * self.Num2
        print("Addition is: ",mul)

    def Division(self):
        div = 0
        div = self.Num1 / self.Num2
        print("Addition is: ",div)
    
def main():
    value1 = int(input("Enter 1st Number: "))
    value2 = int(input("Enter 2nd Number: "))

    Cobj = Calculator(value1 , value2)

    Cobj.Addition()
    Cobj.Substraction()
    Cobj.Multiplication()
    Cobj.Division()


if __name__ == "__main__":
    main()

'''
OUTPUT
Enter 1st Number: 10
Enter 2nd Number: 2
Addition is:  12
Addition is:  8
Addition is:  20
Addition is:  5.0
'''