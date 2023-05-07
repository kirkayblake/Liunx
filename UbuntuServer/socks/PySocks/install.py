import os
import sys
import platform

def main(version):
    try:
        import socks
    except:
        if(version == 0):
            os.system("pip3 install PySocks")
        elif(version == 1):
            os.system("pip3 install PySocks")
        else:
            print("PySocks install fail")

def UsePlatform():
    sysstr = platform.system()
    if(sysstr =="Windows"):
        return 1
    elif(sysstr == "Linux"):
        return 0
    else:
        return 3

if __name__ == '__main__':
    main(UsePlatform())