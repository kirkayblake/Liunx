import os
#inconfig = /etc/fail2ban/
#jail.conf
def main():
    if(os.system("fail2ban-client status sshd") != 0):
        if (os.system("apt-get install fail2ban -y") == 0):
            print("success install fail2ban")
        else:
            print("Unable to install fail2ban,please check the network and try again.")
            print("apt-get install fail2ban -y")
            exit()
    path = "/etc/fail2ban/jail.conf"
    f = open(path)
    lines = f.readlines()
    zi = []
    for loopA in lines:
        if(loopA.find("bantime  = 10m") != -1):
            zi.append("bantime  = 8h\n")#lock time
        elif(loopA.find("findtime  = 10m") != -1):
            zi.append("findtime  = 1m\n")#error interval time
        elif(loopA.find("maxretry = 5") != -1):
            zi.append("maxretry = 1\n")#number of retries
        else:
            zi.append(loopA)
    with open(path, 'w') as f:
        f.writelines(zi)
    os.system("systemctl restart fail2ban")


if __name__ == '__main__':
    main()