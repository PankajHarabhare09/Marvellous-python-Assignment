
def main():
    print("enter Character: ")
    ch = input()
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        print(ch , "is Vowel")
    else:
        print(ch,"is Consonant")
    
if __name__ == "__main__":
    main()

'''
OUTPUT 1
enter Character:
p
p is Consonant

OUTPUT 2
enter Character:
a
a is Vowel
'''