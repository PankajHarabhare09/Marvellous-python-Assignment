import time
import sys
import psutil

def FindRunningProcess(ProName):
    try:

        timestamp = time.ctime()

        filename = "RunnuningProcessLog%s.Log"%(timestamp)
        filename = filename.replace(" " , "_")
        filename = filename.replace(":","_")

        fobj = open(filename , "w")

        for pro in psutil.process_iter():
            ProcessInfo = Pro.as_dict(attrs = ['pid' , 'name' , 'username'])

            if ProcessInfo['name'] == ProName:
                fobj.write("Pid: ",ProcessInfo['pid'] , "Pname: ",ProcessInfo['name'] , "Username: ",ProcessInfo['username'])

        fobj.close()
    except (psutil.NoSuchProcess , psutil.AccessDenied) as e:
        print(e)

def main():
    try:
        if len(sys.argv) == 2:
            if len(sys.argv) == 1:
                print("Please Enter Process Name")
            else:
                ProcessName = sys.argv[1]
                FindRunningProcess(ProcessName)
        else:
            pass
    except Exception as e:
        print("Exception Occured: ",e)


if __name__ == "__main__":
    main()

