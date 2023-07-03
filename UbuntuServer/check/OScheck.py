import platform
import subprocess

import os
import logging










def OS_Linux_RAM_Disk():
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
    mem_gib = mem_bytes/(1024.**3)  # e.g. 3.74
    print("RAM space:",mem_gib)
    import shutil
    # Path
    path = "/home"
    # Get the disk usage statistics
    # about the given path
    stat = shutil.disk_usage(path)
    # Print disk usage statistics
    print("Disk space:",stat)




def OS_Linux_Oilne():
    print("Number of online users:")
    os.system("who")
    print("login history:")
    os.system("last")








