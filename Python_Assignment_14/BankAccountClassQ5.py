class BankAccount:
    def __init__(self ,acc_no, name , amt):
        self.Account_number = acc_no
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

    def Display(self):
        print("---------------------------------------------")
        print("Account Number: ",self.Account_number)
        print("Name Of person: ",self.Name)
        print("Amount in Account: ",self.Amount)

def main():
    BAobj = BankAccount(1874565 , "Pankaj Harabhare" , 2000)

    DRet = BAobj.Deposite()
    print("Total Amount After Deposite: ",DRet)

    WRet = BAobj.Withdrawal()
    print("Total AMount After Withdrawal: ",WRet)

    BAobj.Display()

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter Amount to Deposite:
3000
Total Amount After Deposite:  5000.0
Enter Amount to Withdrawal:
4500
Total AMount After Withdrawal:  500.0
---------------------------------------------
Account Number:  1874565
Name Of person:  Pankaj Harabhare
Amount in Account:  500.0
'''