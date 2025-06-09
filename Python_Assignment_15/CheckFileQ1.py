import os

def main():
    print("Enter FileName Which you want to Check(Exist or Not): ")
    FileName = input()

    ret = os.path.exists(FileName)

    if ret == True:
        print("Given ",FileName," is Present in Directory..!!")
    else:
        print("Given ",FileName," is not Present in Directory..!!")

if __name__ == "__main__":
    main()
'''
OUTPUT

Enter FileName Which you want to Check(Exist or Not):
Demo.txt
Given  Demo.txt  is not Present in Directory..!!
'''