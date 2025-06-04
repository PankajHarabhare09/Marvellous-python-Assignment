class Student:
    School_name = "Marvellous"
    def __init__(self , roll , name):
        self.Roll_No = roll
        self.S_name = name

    def DisplayStudentInfo(self):
        print("Student Roll No is: ",self.Roll_No)
        print("Student Name is: ",self.S_name)

    @classmethod
    def SchoolName(cls):
        print("School name Before Change: ",cls.School_name)

def main():
    Sobj = Student(1 , "Pankaj")

    Sobj.DisplayStudentInfo()
    Student.SchoolName()
    Student.School_name = "Marvellous InfoSystem"
    print("School Name After Change: ",Student.School_name)


if __name__ == "__main__":
    main()

'''
OUTPUT
Student Roll No is:  1
Student Name is:  Pankaj
School name Before Change:  Marvellous
School Name After Change:  Marvellous InfoSystem
'''