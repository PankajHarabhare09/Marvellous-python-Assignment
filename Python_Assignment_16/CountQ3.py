import os

def main():
    print("Enter The File Name That You Want To Read: ")
    FileName = input()

    chkfile = os.path.exists(FileName)

    if chkfile == True:
        Fobj = open(FileName , "r")

        data = Fobj.readlines()

        line_count = len(data)
        print("Count Of Lines: ",line_count)

        word_count = 0
        char_count = 0
        for count in data:
            word_count = word_count + len(count.split())
            char_count = char_count + len(count)

        print("Count OF Words id: ",word_count)
        print("Count OF Characters is: ",char_count)
        


if __name__ == "__main__":
    main()

'''
    OUTPUT
    Enter The File Name That You Want To Read:
    Student.txt
    Count Of Lines:  5
    Count OF Words id:  5
    Count OF Characters is:  25
'''