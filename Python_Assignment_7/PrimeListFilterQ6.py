def ChkkPrime(no):
    if (no <= 1):
        return False

    for i in range(2 , no):
        if (no % i == 0):
            return False
    return True

#function of filter the prime numbers
def Filtered(Primelist):
    return list(filter(ChkkPrime , Primelist))

def main():
    PrimeList = list()
    print("Enter The number of Element")
    ElNum = int(input())

    for i in range(ElNum):
        value = int(input())
        PrimeList.append(value)

    prime_list = Filtered(PrimeList)
    print("Original List: ",PrimeList)
    print("Filtered List: ",prime_list)
    

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter The number of Element
5
4
7
1
2
6
Original List:  [4, 7, 1, 2, 6]
Filtered List:  [7, 2]
'''
    