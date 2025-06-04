class Product:
    def __init__(self , name , price):
        self.Pname = name
        self.Pprice = price

    def __eq__(self , other):
        return self.Pprice == other.Pprice

def main():
    Pobj1 = Product("A" , 10)
    Pobj2 = Product("B" , 20)
    Pobj3 = Product("C" , 10)

    print(Pobj1 == Pobj2)
    print(Pobj1 == Pobj3)
if __name__ == "__main__":
    main()

'''
OUTPUT
False
True
'''