def is_Factorial(no):
    
    if(no == 0 or no == 1):
        return 1
    else:
        return (no * is_Factorial(no - 1))

def main():
    ret = is_Factorial(5)
    print(ret)
    
if __name__ == "__main__":
    main()

'''
OUTPUT
120
'''