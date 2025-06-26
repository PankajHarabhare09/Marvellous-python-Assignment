import os
import hashlib
import time
from email.message import EmailMessage
import smtplib #SIMPLE MAIL TRRANSFER PROTOOCOL
import shutil

def Find_CheckSum(FilePath , BlockSize = 1024):

    try:
        fobj = open(FilePath , "rb")
        hobj = hashlib.md5()

        buffer = fobj.read(BlockSize)
        while(len(buffer) > 0):
            hobj.update(buffer)
            buffer = fobj.read(BlockSize)

        fobj.close()
        return hobj.hexdigest()
    except Exception as e:
        print("Exception Occured in Find_CheckSum(): ",e)

def DeleteDuplicates(DirectoryName):
    try:
        Total_Files = 0
        Duplicates = []
        timestamp = time.ctime()
        filename = "DuplicateRemovel%s.Log"%(timestamp)
        filename = filename.replace(" " , "_")
        filename = filename.replace(":" , "_")

        fobj.open(filename , "w")

        for FolderName , SubFoldeNames , FileNames in os.walk(DirectoryName):
            for files in FileNames:
                Total_Files = Total_Files + 1
                full_path = os.path.join(DirectoryName , files)
                checksum = Find_CheckSum(full_path)

                if checksum in Duplicates:
                    DuplicatesLog = Duplicates.append(full_path)
                    fobj.write(DuplicatesLog)
                    os.remove(full_path)
                else:
                    Duplicates[checksum] = full_path
    except Exception as e:
        print("Exception Occued In DeleteDuplicates(): ",e)


def SendMail(log_path , receiver_mail):
    try:
        message = EmailMessage()
        message['Subject'] = "Duplicate File Removel Report"
        message['From'] = "pankajharabhare17@gmail.com"
        message['To'] = receiver_mail

        fobj = open(log_path , "rb")
        message.add_attachment(fobj.read() , maintype = "text" , stbtype = "plaintext" , filename = os.path.basename(log_path))
        server = smtplib.SMTP("smtp.gmail.com" , 587)
        server.starttls()

        server.login("pankajharabhare17@gmail.com" , "Seema@09")
        server.send_message(message)

    except Exception as e:
        print("Exception Occured in SendMail(): ",e)



