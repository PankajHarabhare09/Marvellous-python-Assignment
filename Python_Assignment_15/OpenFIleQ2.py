import os

def  main():
    print("Enter File Name that you want to Open And read Data: ")
    FileName = input()

    ret = os.path.exists(FileName)

    if ret == True:
        print("Given ",FileName," is Present in Directory..!!")
    else:
        File = open(FileName , "w")
        print("Enter Data In Your File: ")
        WriteData = input()

        File.write(WriteData)
        File.close()

        ReadFile = open(FileName , "r")
        ReadData = ReadFile.read()
        print("Given Data of file ",FileName," is: ",ReadData)

        File.close()
if __name__ == "__main__":
    main()

'''
    OUTPUT
    Enter File Name that you want to Open And read Data:
    Demo.txt
    Enter Data In Your File:
    Jay Ganesh..!!!
    Given Data of file  Demo.txt  is:  Jay Ganesh..!!!
'''