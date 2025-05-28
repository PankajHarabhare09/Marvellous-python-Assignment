def CountZeros(no):
    if no == 0:
        return 1

    if no < 10:
        return 0 

    if no % 10 == 0:
        return 1 + CountZeros(no // 10) #Seperates the last digit 
    else:
        return CountZeros(no // 10)

def main():
    ret = CountZeros(10200300040000)
    print(ret)

if __name__ =="__main__":
    main()

'''
OUTPUT
10
'''