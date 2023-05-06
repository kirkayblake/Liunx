import os
def OS_Ctrl_Alt_Del_SYSTEM():
    #disable ctrl alt del restart ubuntu system
    os.system("systemctl mask ctrl-alt-del.target")
    os.system("systemctl daemon-reload")
    os.system("systemctl status ctrl-alt-del.target")

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
    usegram = ["adm","lp","news","uucp","mail","games","dip"]
    for loopA in uesr:
        os.system("userdel -r " + loopA)
    for loopB in usegram:
        os.system("groupdel " + loopB)
    #disable user usermod -L -e 1 username
    disuser = ["lxd","systemd-coredump","sshd","usbmux","pollinate","landscape","tcpdump",
               "uuidd","tss","_apt","messagebus","nobody","gnats","irc","list","backup",
               "www-data","man"]
    for loopA in disuser:
        os.system("passwd " + loopA +" -l")
    #disable group
    path = "/etc/group"
    f = open(path)
    lines = f.readlines()
    zi = []
    for loopA in lines:
        f = loopA.rfind(":")
        if(f != -1):
            s1 = loopA[0:f+1] + "\n"
            zi.append(s1)
    with open(path, 'w') as f:
        f.writelines(zi)

def OS_time():
    #以美国中部时间为准
    os.system("timedatectl set-timezone US/Central")
    #更改时区为美国中部
    os.system("timedatectl")
    #同步时间
    #os.system("timedatectl list-timezones")
    os.system("date")

def OS_Disable_USB():
    #Disable USB port storage
    os.system("mv /lib/modules/$(uname -r)/kernel/drivers/usb/storage/usb-storage.ko /home/ubuntu/usb-storage.ko")
    DisableUSB = ["blacklist usb_storage\n","blacklist uas\n"]
    with open("/etc/modprobe.d/blacklist.conf", 'a') as f:
        f.writelines(DisableUSB)

def OS_sshd_config():
    #修改登录端口，禁止root登录，登录15s无操作自动断连。
    # revise login port,diseble root login,Automatic disconnection after 15s of no operation after login
    # 只监听单独协议，只能一个，默认所有
    # AddressFamily inet 只监听 IPv4。
    # AddressFamily inet6 只监听 IPv6。
    #/etc/init.d/ssh start
    path = "/etc/ssh/sshd_config"
    f = open(path)
    lines = f.readlines()
    zi = []
    for loopA in lines:
        if(loopA.find("#Port ") != -1):
            zi.append("AllowUsers ubuntu,Administrator\nPort 51221\n")
        elif(loopA.find("#LoginGraceTime ") != -1):
            zi.append("LoginGraceTime 30s\n")
        elif(loopA.find("#PermitRootLogin ") != -1):
            zi.append("PermitRootLogin no\n")
        elif(loopA.find("#StrictModes") != -1):
            zi.append("StrictModes yes\n")
        elif(loopA.find("#MaxAuthTries") != -1):
            zi.append("MaxAuthTries 2\n")
        elif(loopA.find("#MaxSessions") != -1):
            zi.append("MaxSessions 2\n")
        elif(loopA.find("#ClientAliveInterval") != -1):
            zi.append("ClientAliveInterval 15\n")
        elif(loopA.find("#ClientAliveCountMax") != -1):
            zi.append("ClientAliveCountMax 0\n")
        else:
            zi.append(loopA)
    with open(path, 'w') as f:
        f.writelines(zi)
    os.system("systemctl restart ssh")
    os.system("service sshd restart")

def OS_Disable_ping():
    path = "/etc/sysctl.conf"
    f = open(path)
    lines = f.readlines()
    zi = []
    f1 = 0
    for loopA in lines:
        if(loopA.find("net.ipv4.icmp_echo_ignore_all") != -1):
            zi.append("net.ipv4.icmp_echo_ignore_all = 1\n")
            f1 = 1
        else:
            zi.append(loopA)
    if(f1 == 1):
        with open(path, 'w') as f:
            f.writelines(zi)
    else:
        with open(path, 'a') as f:
            f.writelines("net.ipv4.icmp_echo_ignore_all = 1\n")
    os.system("sysctl -p")

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
