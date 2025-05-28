def PowerFun(no1 , no2):
    if (no2 == 0):
        return 1
    else:
        return no1 * PowerFun(no1 , no2 - 1)

def main():
    ret = PowerFun(2 , 3)
    print(ret)
if __name__ == "__main__":
    main()
'''
OUTPUT
8
'''