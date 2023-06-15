import os


def OS_Set_GRUB():
    #ubuntu set GRUB password
    print("grub password:","Jq@uS%61Gy1@y8Fy!Qzgxm0edk1oGaSi")
    # os.system("grub-mkpasswd-pbkdf2")
    grub=["cat << EOF\n",'set superusers="cyberithub"\n',
          "password_pbkdf2 cyberithub grub.pbkdf2.sha512.10000.",
          "1C368C813F7D07A954CD9F4193FAFD23D69859764946FA4A55DD4BCDF2F9AE3B0F325393AFA55F6B58AE28FE50FE41",
          "36362CBDFBC41E5C9400290DBD9163E78F.002A78EA8C32CFF36C03C982DDF8C7AAAD6A73A78D3857EC169F9706303",
          "CD9DF84E59B512720B883DC3BA7EFF1C7122D071B739D5CEA4E3DD54CA0699F9EA6F8\n",
          "EOF\n"
          ]
    with open("/etc/grub.d/00_header", 'a') as f:
        f.writelines(grub)
    os.system("update-grub")



def OS_Create_root_password():
    #create root password
    def GenPassword(length):
        import random
        import string
        chars=string.ascii_letters+string.digits
        return ''.join([random.choice(chars) for i in range(length)])
    #copy root password
    print("root password:",GenPassword(256))
    os.system("passwd root")



def OS_Del_userandgram():
    #del lot of user and usergram
    uesr = ["adm","bin","lp","sync","shutdown","halt","news","mail","uucp","operator","games",
            "gopher","ftp","postfix"]
    usegram = ["adm"]


    #disable user usermod -L -e 1 username
    disuser = ["lxd","systemd-coredump","sshd","usbmux","pollinate","landscape","tcpdump",
               "uuidd","tss","_apt","messagebus","nobody","gnats","irc","list","backup",
               "www-data","man"]
    for loopA in disuser:
        os.system("passwd " + loopA +" -l")
    #disable group










def OS_Revise_Loginconfig():
    path = "/etc/login.defs"
    f = open(path)
    lines = f.readlines()
    zi = []
    for loopA in lines:
        if(loopA.find("UMASK		022") != -1):
            zi.append("UMASK		000\n")
        elif(loopA.find("LOGIN_RETRIES		5") != -1):
            #number of retries
            zi.append("LOGIN_RETRIES		2\n")
        elif(loopA.find("LOGIN_TIMEOUT		60") != -1):
            #login timeout
            zi.append("LOGIN_TIMEOUT		15\n")
        else:
            zi.append(loopA)
    with open(path, 'w') as f:
        f.writelines(zi)

def main():
    OS_Ctrl_Alt_Del_SYSTEM()
    #OS_Set_GRUB()
    OS_Create_root_password()
    OS_Del_userandgram()
    #OS_time()
    OS_Disable_USB()
    OS_sshd_config()
    OS_Disable_ping()
    OS_Revise_Loginconfig()
if __name__ == '__main__':
    main()
