class Numbers:

    def __init__(self,num):
        self.Value = num

    def isPrime(self):
        if (self.Value <= 1):
            return False

        for i in range(2 , self.Value):
            if self.Value % i == 0:
                return False
        return True

    def isPerfect(self):
        print("---------------------------------------------")
        total = 0
        for i in range(1 , self.Value):
            if self.Value % i == 0:
                total = total + i

        if total == self.Value:
            return True
        return False

    def Factors(self):
        print("---------------------------------------------")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
            print()

    def SumFactors(self):
        print("---------------------------------------------")
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total
    
def main():

    Nobj1 = Numbers(28)
    PrimeRet = Nobj1.isPrime()
    print("IS PRIME(1ST NUM): ",PrimeRet)
    Perfectret = Nobj1.isPerfect()
    print("IS PERFECT(1ST NUM): ",Perfectret)
    Nobj1.Factors()
    Nobj1.SumFactors()


    Nobj2 = Numbers(10)
    PrimeRet = Nobj2.isPrime()
    print("IS PRIME(2ND NUM): ",PrimeRet)
    Perfectret = Nobj2.isPerfect()
    print("IS PERFECT(2ND NUM): ",Perfectret)
    Nobj2.Factors()
    Nobj2.SumFactors()

    Nobj3 = Numbers(7)
    PrimeRet = Nobj3.isPrime()
    print("IS PRIME(3RD NUM): ",PrimeRet)
    Perfectret = Nobj3.isPerfect()
    print("IS PERFECT(3RD NUM): ",Perfectret)
    Nobj3.Factors()
    Nobj.SumFactors()


if __name__ == "__main__":
    main()

'''
OUTPUT
IS PRIME(1ST NUM):  False
---------------------------------------------
IS PERFECT(1ST NUM):  True
---------------------------------------------
1
2
4
7
14
---------------------------------------------
IS PRIME(2ND NUM):  False
---------------------------------------------
IS PERFECT(2ND NUM):  False
---------------------------------------------
1
2
5
---------------------------------------------
IS PRIME(3RD NUM):  True
---------------------------------------------
IS PERFECT(3RD NUM):  False
---------------------------------------------
1
'''