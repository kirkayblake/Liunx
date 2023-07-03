import os

path = "/etc/sysctl.conf"
f = open(path)
lines = f.readlines()
zi = []
f1 = 0
for loopA in lines:
    if (loopA.find("net.ipv4.icmp_echo_ignore_all") != -1):
        zi.append("net.ipv4.icmp_echo_ignore_all = 1\n")
        zi.append("net.ipv6.icmp.echo_ignore_all = 1\n")
        f1 = 1
    else:
        zi.append(loopA)
if (f1 == 1):
    with open(path, 'w') as f:
        f.writelines(zi)
else:
    with open(path, 'a') as f:
        f.writelines("net.ipv4.icmp_echo_ignore_all = 1\n")
        f.writelines("net.ipv6.icmp.echo_ignore_all = 1\n")
os.system("sysctl -p")


def main():
    OS_Ctrl_Alt_Del_SYSTEM()
    OS_Disable_USB()
    OS_Disable_ping()