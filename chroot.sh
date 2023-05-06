#!/bin/bash
mkdir -p /home/chroot
mkdir -p /home/chroot/dev/
cd /home/chroot/dev/
mknod -m 666 null c 1 3
mknod -m 666 tty c 5 0
mknod -m 666 zero c 1 5
mknod -m 666 random c 1 8
chown root:root /home/chroot
chmod 0755 /home/chroot
#设计牢笼
#design chroot chmod
##################################
mkdir -p /home/chroot/bin
cp -v /bin/bash /home/chroot/bin/
#查看bash所需环境,配置所需环境,注入bash解释器
#Configuration Environment，
#ldd /bin/bash
mkdir -p /home/chroot/lib/x86_64-linux-gnu
mkdir -p /home/chroot/lib64
cp -v /lib/x86_64-linux-gnu/{libtinfo.so.6,libdl.so.2,libc.so.6} /home/chroot/lib/x86_64-linux-gnu/
cp -v /lib64/ld-linux-x86-64.so.2 /home/chroot/lib64/
####################################
#配置牢笼账户
#set chroot user
useradd Administrator;echo Administrator:'M6tb3kRKtv@nj&jaAqVQFB8iQ4vF3mhA' | chpasswd
mkdir /home/chroot/etc
chsh -s /bin/bash Administrator
grep Administrator /etc/passwd
#cp -vf /etc/{passwd,group} /home/chroot/etc/
#chmod 755 /home/chroot/ -R
#set sshd
echo Match User Administrator >> /etc/ssh/sshd_config
echo ChrootDirectory /home/chroot >> /etc/ssh/sshd_config
systemctl restart sshd
service sshd restart
#insert command
cp -v /bin/su /home/chroot/bin/
cp -v /lib/x86_64-linux-gnu/{libpam.so.0,libpam_misc.so.0,libutil.so.1,libc.so.6,libaudit.so.1,libdl.so.2,libcap-ng.so.0} /home/chroot/lib/x86_64-linux-gnu/