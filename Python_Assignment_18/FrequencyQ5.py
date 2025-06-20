import os

def main():

    FileName = input("Enter The File Name That you want to Create: ")

    ret = os.path.exists(FileName)

    if ret == True:
        print("Given ",FileName," is Present in Directory..!!")
    else:
        FWObj = open(FileName , "w")
        print("Enter Data in file: ")
        writeData = input()
        FWObj.write(writeData)

        FWObj.close()
        
        Word = input("Enter Name Of Word That you want to Search: ")
        FRObj = open(FileName , "r")

        readData = FRObj.read()
        for freq in range(readData.count(Word) , 1 ,-1):
            freq = freq + 1

        print("Frequency Of That Word: ",freq)

        FRObj.close()

    
if __name__ == "__main__":
    main()