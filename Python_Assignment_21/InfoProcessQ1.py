import psutil
import sys
import time
def InfoProcess():
    Border = "-" * 25

    timestamp = time.ctime()
    filename = "InfoProcessLog%s.log"%(timestamp)
    filename = filename.replace(" " , "_")
    filename = filename.replace(":" , "_")

    fobj = open(filename , "w")
    print(Border)
    print("Current Rinning Processes: ")
    print(Border)

    for pro in psutil.process_iter():
        ProcessInfo = pro.as_dict(attrs = ['Pid' , 'name' , 'username'])
        fobj.write(ProcessInfo)

    fobj.close()


def main():
    try:
        InfoProcess()
    except Exception as e:
        print("Exception Occured" , e)

if __name__ == "__main__":
    main()