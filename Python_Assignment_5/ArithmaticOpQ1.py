def Sum(num1 , num2):
    sum = 0
    sum = num1 + num2
    return sum

def Difference(num1 , num2):
    diff = 0
    diff = num1 - num2
    return diff

def Product(num1 , num2):
    product = 0
    product = num1 * num2
    return product

def Division(num1 , num2):
    div = 0
    div = num1 / num2
    return div

def main():
    input1 = int(input("Enter 1st number:  "))
    input2 = int(input("Enter 2nd number: "))

    add = Sum(input1 , input2)
    print("Sum is: ",add)

    sub = Difference(input1, input2)
    print("Difference is: ",sub)

    mul = Product(input1 , input2)
    print("Product is: ",mul)

    div = Division(input1 , input2)
    print("Division is: ",div)

if __name__== "__main__":
    main()

'''
OUTPUT
Enter 1st number:  10
Enter 2nd number: 2
Sum is:  12
Difference is:  8
Product is:  20
Division is:  5.0
'''