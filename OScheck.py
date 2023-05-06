import platform
import subprocess
import fileinput
import os
#CPU,显示CPU的逻辑核心，和物理核心，当前运行频率，和主频。手动观察与服务商提供的是否一致
def get_linux_cpu_speed():
    for line in fileinput.input('/proc/cpuinfo'):
        if 'MHz' in line:
            value = line.split(':')[1].strip()
            value = float(value)
            speed = round(value / 1024, 1)
            return "{speed} GHz".format(speed=speed)
def OS_CPU_information():
    #Total Cores
    print("Number of CPU cores on this device:")
    os.system("cat /proc/cpuinfo | grep processor | wc -l")
    #CPU Single core base frequency
    print("CPU base frequency:" + get_linux_cpu_speed())
    #CPU company
    os.system("cat /proc/cpuinfo | grep 'model name' | uniq")
    os.system("cat /proc/cpuinfo | grep 'cache size' | uniq")
    os.system("cat /proc/cpuinfo | grep 'microcode' | uniq")
    return True
#system 操作系统版本，运行位数。手动观察是否和服务商提供的一致
def OS_Linux_information():
    a = platform.platform()
    b = platform.architecture()
    print("system version:",a,b)
    return True
#RAM disk 大小。手动观察是否和服务商提供的一致
def OS_Linux_RAM_Disk():
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
    mem_gib = mem_bytes/(1024.**3)  # e.g. 3.74
    print("system RAM space:",mem_gib)
    import shutil
    # Path
    path = "/home"
    # Get the disk usage statistics
    # about the given path
    stat = shutil.disk_usage(path)
    # Print disk usage statistics
    print("Disk usage statistics:",stat)
    return True
#检查日志文件是否符合第一次登录的大小要求
def getdirsize(dir):
    from os.path import join, getsize
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size
def OS_Frist_Checklog():
    path = "/var/log/"
    size = getdirsize(path)
    print(size)
    if(int(size) <= 95478342):
        return True
    else:
        os.system("du -lh /var/log/*")
        return False
#重置openssh-server
def OS_opensshserver_config():
    if(os.system("ps -e |grep ssh") == 0):
        os.system("rm /etc/ssh/ssh_host_*")
        os.system("dpkg-reconfigure openssh-server")
        print("openssh-server RSA host key ,you can save it.SHA256:")
        os.system("ssh-keygen -E sha256 -lf /etc/ssh/ssh_host_rsa_key.pub")
        print("openssh-server RSA host key ,you can save it.MD5:")
        os.system("ssh-keygen -E md5 -lf /etc/ssh/ssh_host_rsa_key.pub")
    else:
        print("haven't openssh_server!!!")
        os.system("apt-get install openssh-server -y")

def main():
    OS_CPU_information()
    OS_Linux_information()
    OS_Linux_RAM_Disk()
    OS_Frist_Checklog()
    OS_opensshserver_config()
if __name__ == '__main__':
    main()