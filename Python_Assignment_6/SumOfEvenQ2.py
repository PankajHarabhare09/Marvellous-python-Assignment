
def main():
    add = 0 
    for i in range(0 , 101):
        if i % 2 == 0:
            add = add + i
        
    print("sum of even number between 1 to 100: ",add)

if __name__ == "__main__":
    main()

'''
OUTPUT
sum of even number between 1 to 100:  2550
'''