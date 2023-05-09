import os
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA512
def key_size32():
    key_size = get_random_bytes(32)
    return key_size

def iv16():
    iv = get_random_bytes(16)
    return iv

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
    date = bytes(date, "UTF-8")
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