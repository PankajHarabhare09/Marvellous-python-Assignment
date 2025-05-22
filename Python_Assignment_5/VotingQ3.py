def ChkAge(age):
    if(age >=18):
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

def main():
    print("Enter Age for Voting: ")
    vote = int(input())

    ChkAge(vote)

if __name__ == "__main__":
    main()

'''
OUTPUT 1
Enter Age for Voting:
15
You are not eligible to vote

OUTPUT 2
Enter Age for Voting:
18
You are eligible to vote

OUTPUT 3
Enter Age for Voting:
21
You are eligible to vote
'''