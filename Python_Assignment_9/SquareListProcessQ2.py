import multiprocessing
import time
def Square_List(*num):
    Square = list()
    for i in num:
        sq = i * i
        Square.append(sq)
    print("List Of Square: ",Square)

def main():
    p1 = multiprocessing.Process(target = Square_List , args = (1,2,3,4,5,6,7,8,9,10))
    p2 = multiprocessing.Process(target = Square_List , args = (11,12,13,14,15,16,17,18,19,20))
    p3 = multiprocessing.Process(target = Square_List , args = (21,22,23,24,25,26,27,28,29,30))

    print("1st Process")
    p1.start()
    time.sleep(1)
    print("2nd Process")
    p2.start()
    time.sleep(1)
    print("3rd Process")
    p3.start()

    p1.join()
    p2.join()
    p3.join()

if __name__ == "__main__":
    main()
    
'''
OUTPUT
1st Process
List Of Square:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
2nd Process
List Of Square:  [121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
3rd Process
List Of Square:  [441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
'''