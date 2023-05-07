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
def AES256CBC_base64():
    key = get_random_bytes(32)
    a = "abc123不要埋怨那种因为你穷而离开你的人，人生路还很长，总有一天你会知道，还有人因为你丑而离开你你。"
    a = bytes(a,"UTF-8")
    b = base64.b64encode(a)
    print(len(b)/16)
    cipher = AES.new(b"1E571258CE38D08672352587686B63D3", AES.MODE_CBC,b'f2\xc5\xdf\xa4b\xd39\xd0N\x05hZ\xa5C\xb0')
    z = cipher.encrypt(b)
    iv = cipher.iv
    print(z)
    print(iv)
    cipher = AES.new(b"1E571258CE38D08672352587686B63D3", AES.MODE_CBC,b'f2\xc5\xdf\xa4b\xd39\xd0N\x05hZ\xa5C\xb0')
    x = cipher.decrypt(z)
    print(x)
    c = base64.b64decode(x)
    s = str(c,"UTF-8")
    print(s)
def AES256CBC():
    key = get_random_bytes(32)
    print(key)
    a = "abc123不要埋怨那种因为你穷而离开你的人，人生路还很长，总有一天你会知道，还有人因为你丑而离开你你。"
    a = bytes(a,"UTF-8")
    print(len(a)/16)
    iv = b"\xbfQj\xb6\xe1n\pos\ulp\w"
    cipher = AES.new(b"1E571258CE38D08672352587686B63D3", AES.MODE_CBC,iv)
    z = cipher.encrypt(a)
    iv = cipher.iv
    print(len(iv),iv)

    cipher = AES.new(b"1E571258CE38D08672352587686B63D3", AES.MODE_CBC,iv)
    x = cipher.decrypt(z)
    s = str(x,"UTF-8")
    print(s)