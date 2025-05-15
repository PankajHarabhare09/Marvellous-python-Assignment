#Assignment 2>Q10. Addition  of Digits
def main():
    print("Enter the Number: ")
    num = int(input())

    add = 1
    for i in range(1,num , 1):
        add = add + i
    print(add)

if __name__ == "__main__":
    main()