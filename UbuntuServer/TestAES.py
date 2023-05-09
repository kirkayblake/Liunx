import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
MODE_ECB = 1        #: Electronic Code Book (:ref:`ecb_mode`)
MODE_CBC = 2        #: Cipher-Block Chaining (:ref:`cbc_mode`)
MODE_CFB = 3        #: Cipher Feedback (:ref:`cfb_mode`)
MODE_OFB = 5        #: Output Feedback (:ref:`ofb_mode`)
MODE_CTR = 6        #: Counter mode (:ref:`ctr_mode`)
MODE_OPENPGP = 7    #: OpenPGP mode (:ref:`openpgp_mode`)
MODE_CCM = 8        #: Counter with CBC-MAC (:ref:`ccm_mode`)
MODE_EAX = 9        #: :ref:`eax_mode`
MODE_SIV = 10       #: Galois Counter Mode (:ref:`gcm_mode`)
MODE_GCM = 11       #: Synthetic Initialization Vector (:ref:`siv_mode`)
MODE_OCB = 12       #: Offset Code Book (:ref:`ocb_mode`)
#256/4/2=32 4个二进制=一个16进制 2个十六进制=一个字符

def Repair_Date_AES_16(date):
    date = bytes("0000","UTF-8") + date
    int1 = len(date)
    int2 = int(int1/16)
    int3 = int1 - int2*16
    int4 = 16-int3
    str1 = str(int4).zfill(4)
    if(int3 != 0):
        for loopA in range(16 - int3):
            date = date + b"0"
    date = bytes(str1,"UTF-8") + date[4:len(date)]
    return date

def Build_Date_AES_16(date):
    int1 = int(date[0:4])
    date = date[4:len(date) - int1]
    return date

def AES256_CBC_Base64_Encrypt(date,key_size,iv):
    date = bytes(date,"UTF-8")
    date = base64.b64encode(date)
    date = Repair_Date_AES_16(date)
    cipher = AES.new(key_size,AES.MODE_CBC,iv)
    encrypt = cipher.encrypt(date)
    return encrypt

def AES256_CBC_Base64_Decrypt(date,key_size,iv):
    cipher = AES.new(key_size, AES.MODE_CBC, iv)
    decrypt = cipher.decrypt(date)
    date = Build_Date_AES_16(decrypt)
    date = base64.b64decode(date)
    date = str(date, "UTF-8")
    return date






def AES256CBC_base64(key_size,iv):
    a = "abc123不要埋怨2315那种因为你穷gsdh而离开你的人，人435生gfg路还很长，213124总有一天你会知道，还有人因为你丑而离开你你..。。///"
    a = bytes(a,"UTF-8")
    b = base64.b64encode(a)
    b = Repair_Date_AES_16(b)
    cipher = AES.new(key_size, AES.MODE_CBC,iv)
    z = cipher.encrypt(b)
    # iv = cipher.iv
    cipher = AES.new(key_size, AES.MODE_CBC,iv)
    x = cipher.decrypt(z)
    x = Build_Date_AES_16(x)
    c = base64.b64decode(x)
    s = str(c,"UTF-8")
    print(s)
def AES256CBC():
    key = get_random_bytes(32)
    print(key)
    a = "abc123不要埋怨那种因为你穷而离开你的人，人生路还很长，总有一天你会知道，还有人因为你丑而离开你你。"
    a = bytes(a,"UTF-8")
    iv = get_random_bytes(16)
    print(len(iv))
    cipher = AES.new(b"1E571258CE38D08672352587686B63D3", AES.MODE_CBC,iv)
    z = cipher.encrypt(a)
    iv = cipher.iv
    print(len(iv),iv)

    cipher = AES.new(b"1E571258CE38D08672352587686B63D3", AES.MODE_CBC,iv)
    x = cipher.decrypt(z)
    s = str(x,"UTF-8")
    print(s)

if __name__ == '__main__':
    key_size = get_random_bytes(32)
    iv = get_random_bytes(16)
    ct = "abc123不要埋怨2315那种因为你穷gsdh而离开你的人，人435生gfg路还很长，213124总有一天你会知道，还有人因为你丑而离开你你..。。///"
    ct = AES256_CBC_Base64_Encrypt(ct,key_size,iv)
    ct = AES256_CBC_Base64_Decrypt(ct,key_size,iv)
    print(key_size,"   ",iv)
