class BankAccount:
    ROI = 10.5
    T = 2
    SI = 0.0
    def __init__(self , name , amt):
        self.Name = name
        self.Amount = amt
    
    def Deposite(self):
        deposite = 0.0
        print("Enter Amount to Deposite: ")
        deposite = float(input())
        self.Amount = self.Amount + deposite
        return self.Amount

    def Withdrawal(self ):
        Withdraw = 0.0
        print("Enter Amount to Withdrawal: ")
        Withdraw = float(input())
        self.Amount = self.Amount - Withdraw
        return self.Amount

    def CalculateInterest(self):
        
        self.SI = (self.Amount * self.ROI * self.T) /100
        print("Simple Interest is: ",self.SI)

    def Display(self):
        print("---------------------------------------------")
        print("Name Of person: ",self.Name)
        print("Amount in Account: ",self.Amount)

def main():
    BAobj = BankAccount("Pankaj Harabhare" , 2000)

    DRet = BAobj.Deposite()
    print("Total Amount After Deposite: ",DRet)

    WRet = BAobj.Withdrawal()
    print("Total AMount After Withdrawal: ",WRet)

    BAobj.CalculateInterest()

    BAobj.Display()

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter Amount to Deposite:
5000
Total Amount After Deposite:  7000.0
Enter Amount to Withdrawal:
2500
Total AMount After Withdrawal:  4500.0
Simple Interest is:  945.0
---------------------------------------------
Name Of person:  Pankaj Harabhare
Amount in Account:  4500.0

'''