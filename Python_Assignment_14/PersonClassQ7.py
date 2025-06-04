class Person:
    def __init__(self , name , age):
        self.Pname = name
        self.Page = age


class Teacher(Person):
    
    def __init__(self , sub , sal , name , age):
        super().__init__(name , age)
        self.Subject = sub
        self.Salary = sal
        

    def DisplayTeacherInfo(self):
        print("Name of Teacher: ",self.Pname)
        print("Age of Teacher: ",self.Page)
        print("Subject of Teacher: " , self.Subject)
        print("Salary of Teacher: ", self.Salary)
    

def main():

    Tobj = Teacher("PYTHON ML" , 45000 , "Piyush " , 28)
    Tobj.DisplayTeacherInfo()

if __name__ == "__main__":
    main()

'''
OUTPUT
Name of Teacher:  Piyush
Age of Teacher:  28
Subject of Teacher:  PYTHON ML
Salary of Teacher:  45000
'''