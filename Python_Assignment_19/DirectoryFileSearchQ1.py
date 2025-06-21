import time
import sys
import os

def Search_File(Dir , Ext):
    chkFile = os.path.isabs(Dir)
    if chkFile == False:
        chkFile = os.path.abspath(Dir)

    chkFile = os.path.exists(Dir)
    if chkFile == False:
        print("Path is Invalid..")
        return 
    
    chkFile = os.path.isdir(Dir)
    if chkFile == False:
        print("Path is Valid But Target is not present in Directory")
        return

    timestamp = time.ctime()

    filename = "FileSearchQ1Log%s.Log"%(timestamp)
    filename = filename.replace(" " , "_")
    filename = filename.replace(":" , "_")

    Fobj = open(filename , "w")

    for FolderName , SubFolderNames , FileNames in os.walk(Dir):
        for files in FileNames:
            if files == os.endswith(Ext):
                fobj.write(os.path.join(FolderName , files),"\n")
    
    fobj.close()

def main():

    try:
        DirName = sys.argv[1]
        Extention = sys.argv[2]

        if len(sys.argv) != 3:
            print("Usage: python DirectoryFileSearchQ1.py <-FileName-> <-Extension->")
            return
        
        Search_File(DirName , Extention)
    except Exception as e:
        print("Exception Found: ",e)

if __name__ == "__main__":
    main()