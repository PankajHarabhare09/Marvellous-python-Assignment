def ChkPrime(no):
    for i in range(2 , no):
        if no % i == 0:
            return True
    return False

def main():
    print("Enter Number: ")
    prime = int(input())

    if(ChkPrime(prime)):
        print(prime , " is Prime Number")
    else:
        print(prime , " is not Prime Number")
    
if __name__ == "__main__":
    main()