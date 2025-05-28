def SumNatrual(no):
    if no == 1:
        return 1
    return no + SumNatrual(no - 1)

def main():
    ret = SumNatrual(5)
    print(ret)

if __name__ == "__main__":
    main()
'''
OUTPUT
15
'''