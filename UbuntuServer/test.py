from Crypto.Random import get_random_bytes
def key_size32():
    key_size = get_random_bytes(32)
    return key_size

def iv16():
    iv = get_random_bytes(16)
    return iv


a = key_size32()
b = iv16()
# print(len(a))
data = b'"\xc6I=~\x8d\x84\x9a=\xa0\x1d\xd5\rk\x9b-\x88\xa5\x12\xdf\x19%03s6\xe6\xe6\x1b\xfb\xdb\xc4\xcd\x1e\xca\xc3\xd1$\xe2\x1c[\xa1\x1a\xb2\x85\xe8\r%\x04\xda\xfc\x87Ql=Bv\xe5Vr\xc4$I\xad\xdc \xa7\x02\x11\xab\x0e\xe0\x80\xa0\x08\xd1\x80*\x03.\xf5=^;\x08f\xf2$\x97\xb5\x10g\xc3k\xd5U'


s1 = data[0:1]
print(type(s1))
s2 = data[len(data) - 1:len(data)]
s3 = data[1:len(data) - 2]
print(s1, s2,s3)
data = s2 + s3 + s1














