class Employee:
    def __init__(self , name , dep , sal):
        self.Name = name
        self._department = dep
        self.__salary = sal

    def DisplayInfo(self):
        print("Name is: ",self.Name)
        print("Department is: ",self._department)
        print("Salary is: ",self.__salary)

def main():

    Eobj = Employee("A" , "SD" , 45000)
    Eobj.DisplayInfo()

    print(Eobj.Name)
    print(Eobj._department)
    print(Eobj.__salary)
if __name__ == "__main__":
    main()

"""
OUTPUT
Name is:  A
Department is:  SD
Salary is:  45000
A
SD
Traceback (most recent call last):
  File "C:\Users\ganes\Desktop\Python_Assignment_14\AccessEmployeeClassQ10.py", line 21, in <module>
    main()
  File "C:\Users\ganes\Desktop\Python_Assignment_14\AccessEmployeeClassQ10.py", line 19, in main
    print(Eobj.__salary)
          ^^^^^^^^^^^^^
AttributeError: 'Employee' object has no attribute '__salary'
"""