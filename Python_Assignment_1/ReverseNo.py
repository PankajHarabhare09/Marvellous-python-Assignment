#Assignment 1>Q5. Printing Numbers in Reverse Order.

def reverse():
    for n in range(10 , 0 , -1):
        print(n ,end = " ") #end parameter is used to avoid new line and print the number on same line.

def main():
    reverse()

if __name__ == "__main__":
    main()

#this question is about for Loop , range function and end = " " parameter.
'''in this question , i used for loop and range for printing number ,
but i want that numbers in reverse order so i took 3 parameters in range function 1.start 2.stop 3.displacement 
and as i say erlier i want number in reverse order so my displacement is in negative number 
and my starting point is greater than stop point.
after that i use END parameter for avoiding the new line as we know the print() function is going to new line automatically.
to avoid that we use END parameter.'''

''' OUTPUT 10 9 8 7 6 5 4 3 2 1 '''