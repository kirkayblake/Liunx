import random
import string
import socket
import AES256CBC
def random_string(munber):
  random_str = ''.join(random.sample(string.ascii_letters + string.digits, munber))
  return random_str

def ran_send():
  randomstr = ""
  for loopA in range(random.randint(1, 64)):
    str1 = random_string(random.randint(1, 62))
    randomstr = randomstr + str1
  return randomstr


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 50007))
key_size = b'f\xc8\xd9\x87\x99\xcd\x17B\x93\x8aWHwd\xb1\x0e\x1b.\xcf\xe4\xbb$\x90\xfa\x84\xd1\xd3\xcb\x9c\x9d^\xd7'
iv = b'5\xc6\x88\x91\xd0\xb9\xcc\xe7\xb2\xc8\xe8\x17]>\x911'
while True:

    from_server = client.recv(4096)
    if not from_server: break
    from_server = AES256CBC.AES256_CBC_Base64_Decrypt(from_server, key_size, iv)
    print(from_server)
    date = AES256CBC.AES256_CBC_Base64_Encrypt(ran_send(), key_size, iv)
    client.send(date)

client.close()
print("exit")