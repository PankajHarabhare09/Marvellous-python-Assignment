def main():
    for i in range (1 , 6 , 1):
        for j in range(1 , i ):
            print("*" , end = " ")
        print()

if __name__ == "__main__":
    main()

'''
OUTPUT
*
* *
* * *
* * * *
'''