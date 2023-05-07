import os
import sys
import platform

def main(version):
    try:
        from Crypto.Cipher import AES
    except:
        path = os.getcwd() + "\pycryptodome-3.17\\"
        print(path,version)
        if(version == 0):
            os.system("cd " + path)
            os.system("python3 setup.py install")
        elif(version == 1):
            os.system("install.cmd")
        else:
            print("pycryptodome-3.17 install fail")

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