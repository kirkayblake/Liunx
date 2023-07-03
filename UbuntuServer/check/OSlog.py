




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