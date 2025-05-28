def Sum_Digit(no):
    if (no < 1):
        return 0
    else:
        return no % 10 + Sum_Digit(no // 10)

def main():
    ret = Sum_Digit(1234)
    print(ret)

if __name__ == "__main__":
    main()

'''
OUTPUT
10
'''