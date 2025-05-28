def PrintNum(no):
    
    if(no <= 5):
        print(no , end = " ")
        no = no + 1
        PrintNum(no)

def main():
    PrintNum(1)

if __name__ == "__main__":
    main()

'''
OUTPUT
1 2 3 4 5
'''