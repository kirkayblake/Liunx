import os
# ufw status verbose检查防火墙状态
# 	Status: inactive非活动
# 	Status: active已激活
# ufw status numbered检查规则
# 配置文件/etc/default/ufw
# 	ufw allow ssh
# 	ufw allow sshd
# 	ufw allow 51221/tcp
# 	ufw deny 22
# 打开ufw enable
# 关闭ufw disable


def main():
    if (os.system("ufw status verbose") != 0):
        if (os.system("apt-get install ufw -y") == 0):
            print("success install ufw")
        else:
            print("Unable to install ufw,please check the network and try again.")
            print("apt-get install ufw -y")
            exit()
    os.system("ufw allow ssh")
    os.system("ufw allow 51221/tcp")
    os.system("ufw deny 22")
    os.system("ufw status verbose")
    os.system("ufw enable")

if __name__ == '__main__':
    main()