#Assignment 3>Q5. Module file Of PrimeAddition

def ChkPrime(n):
    if (n <= 1):
        return False

    for i in range(2 , n):
        if (n % i == 0):
            return False
    return True
