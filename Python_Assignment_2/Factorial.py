#Assignment 2>Q3. Factorial number

def main():
    print("Enter the Number: ")
    num = int(input())

    fact = 1
    for i in range(num ,0,-1):
        fact = fact * i
    print(fact)

if __name__ == "__main__":
    main()

''' 
    this question is about Factorial number , factorial number means multiplyiing the pervious number of given number
    for ex: 6 ->6*5*4*3*2*1 = 720
    so for that i have to take two variable first is input and second is fact which is store the multiplication
    after that i have taken for loop and range , in range ill give decrement order of numbers beacuase of i want 
    multipliction of biggest number to lowest number after that i Want to do multiplication of those numbers
    for that i use fact variable and multiply it with the I which is varible of range means the value of i will 
    change after every iteration and beacuse of this fact are get multiply with i and stored in fact and at the end 
    the fact will be printed

    OUTPUT
    Enter the Number:
    6
    720
    '''