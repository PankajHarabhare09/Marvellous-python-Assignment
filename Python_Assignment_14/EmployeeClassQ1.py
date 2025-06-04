class Employee:
    def __init__(self , id , name , salary):
        self.emp_id = id
        self.emp_name = name 
        self.emp_salary = salary

    def Accept(self):
        print("Employee Id is: ",self.emp_id)
        print("Employee Name is: ",self.emp_name)
        print("Employee Salary is: ",self.emp_salary)

def main():
    Eobj = Employee(1 , "Pankaj" , 45000)
    Eobj.Accept()


if __name__ == "__main__":
    main()

'''
OUTPUT
Employee Id is:  1
Employee Name is:  Pankaj
Employee Salary is:  45000
'''