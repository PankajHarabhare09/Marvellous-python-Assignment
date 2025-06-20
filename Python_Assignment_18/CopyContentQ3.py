import sys
import os

def main():
    if len(sys.argv) != 2:
        print("USAGE: python CopyContentQ3.py Source File")
        return 
    
    source_file = sys.argv[1]
    Destination_file = "Demo.txt"

    SourceObj = open(source_file , "r")
    DestObj = open(Destination_file , "w")

    Content = SourceObj.read()
    DestObj.write(Content)

    print("Content Copied")
    
if __name__ == "__main__":
    main

