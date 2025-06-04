class Vehicle:
    def Start(self):
        print("Inside Vehicle Class")
        print("Vehicle is Ready to Start..!!!!")

class Car(Vehicle):
    
    def Start(self):
        super().Start()
        print("Inside Car Class")
        print("Car is started..")

def main():

    Cobj = Car()

    Cobj.Start()
if __name__ == "__main__":
    main()

'''
OUTPUT
Inside Vehicle Class
Vehicle is Ready to Start..!!!!
Inside Car Class
Car is started..
'''
