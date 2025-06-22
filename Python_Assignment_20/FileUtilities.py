import os
import hashlib

def ChkDirectory(Dirname):
    chkfile = os.path.isabs(Dirname)
    if chkfile == False:
        chkfile = os.path.abspath(Dirname)

    chkfile = os.path.exists(Dirname)
    if chkfile == False:
        print("Path is Invalid")
    
    chkfile = os.path.isdir(Dirname)
    if chkfile == False:
        print("Directory is present but given target file is not present")


def CalculateChecksum(path , BlockSize = 1024):
    fobj = open(path , "rb")
    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()
