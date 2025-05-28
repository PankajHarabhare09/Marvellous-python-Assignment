def Pattern(no):
    for i in range(1 , no , 1):
        for j in range(i):
            print(" * ", end = " ")
        print()

def main():
    Pattern(6)

if __name__ == "__main__":
    main()

'''
OUTPUT
 *
 *   *
 *   *   *
 *   *   *   *
 *   *   *   *   *
 '''