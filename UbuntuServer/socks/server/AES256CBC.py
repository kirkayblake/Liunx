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

def Repair_data_AES_16(data):
    data = bytes("0000","UTF-8") + data
    int1 = len(data)
    int2 = int(int1/16)
    int3 = int1 - int2*16
    int4 = 16-int3
    str1 = str(int4).zfill(4)
    if(int3 != 0):
        for loopA in range(16 - int3):
            data = data + b"0"
    data = bytes(str1,"UTF-8") + data[4:len(data)]
    return data

def Build_data_AES_16(data):
    int1 = int(data[0:4])
    data = data[4:len(data) - int1]
    return data


def Encrypt_Salf_Data(data):
    if (len(data) >= 16):
        s1 = data[0:1]
        s2 = data[len(data) - 1:len(data)]
        s3 = data[1:len(data) - 1]
        data = s2 + s3 + s1
        return data
    else:
        return data


def AES256_CBC_Base64_Encrypt(data,key_size,iv):
    data = bytes(data,"UTF-8")
    data = base64.b64encode(data)
    data = Repair_data_AES_16(data)
    cipher = AES.new(key_size,AES.MODE_CBC,iv)
    encrypt = cipher.encrypt(data)
    encrypt = Encrypt_Salf_Data(encrypt)
    return encrypt

def Decrypt_Censor(data):
    if(len(data) - int(len(data)/16)*16 == 0 ):
        return True
    else:
        return False


def AES256_CBC_Base64_Decrypt(data,key_size,iv):
    data = Encrypt_Salf_Data(data)
    if(Decrypt_Censor(data) == False):
        return "failed"
    cipher = AES.new(key_size, AES.MODE_CBC, iv)
    decrypt = cipher.decrypt(data)
    data = Build_data_AES_16(decrypt)
    data = base64.b64decode(data)
    data = str(data, "UTF-8")
    return data


