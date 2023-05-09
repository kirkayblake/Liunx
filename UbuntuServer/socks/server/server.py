import random
import string
import socket
import AES256CBC
import os
SOCKS_VERSION = 1
#win"127.0.0.1" liunx\macos"0.0.0.0"
IPv4 = "127.0.0.1"
IPv6 = ""
port = 50007
# socket.AF_UNIX
# socket.AF_INET IPV4
# socket.AF_INET6 IPV6
# AF_UNIX Unix Domain Socket
# AF_CAN send CAN
# AF_PACKET liunx
# AF_RDS  efficient send data
AddressFamily = socket.AF_INET
# socket.SOCK_STREAM TCP
# socket.SOCK_DGRAM UDP
# socket.SOCK_RAW ICMP、IGMP
# socket.SOCK_RDM
# socket.SOCK_SEQPACKET
SocketKind = socket.SOCK_STREAM
def random_string(munber):
  random_str = ''.join(random.sample(string.ascii_letters + string.digits, munber))
  return random_str

def ran_send():
  randomstr = ""
  for loopA in range(random.randint(1, 64)):
    str1 = random_string(random.randint(1, 62))
    randomstr = randomstr + str1
  return randomstr

def create_socket(AddressFamily,SocketKind):
  createsocket = socket.socket(AddressFamily, SocketKind)
  return createsocket


# while True:
#   conn, addr = serv.accept()
#   from_client = ''
#   while True:
#     data = conn.recvmsg(4096)
#     if not data: break
#     from_client += data.decode('utf8')
#     print (from_client)
#     conn.send("I am SERVER\n".encode())
#   conn.close()
# print ('client disconnected and shutdown')
#
if __name__ == '__main__':
  key_size = b'f\xc8\xd9\x87\x99\xcd\x17B\x93\x8aWHwd\xb1\x0e\x1b.\xcf\xe4\xbb$\x90\xfa\x84\xd1\xd3\xcb\x9c\x9d^\xd7'
  iv = b'5\xc6\x88\x91\xd0\xb9\xcc\xe7\xb2\xc8\xe8\x17]>\x911'
  server = create_socket(AddressFamily,SocketKind)
  server.bind((IPv4, port))
  server.listen(SOCKS_VERSION)
  while True:
    conn, addr = server.accept()
    while True:
      str2 = AES256CBC.AES256_CBC_Base64_Encrypt(ran_send(),key_size,iv)
      conn.send(str2)
      date = conn.recv(4096)
      if not date: break
      date = AES256CBC.AES256_CBC_Base64_Decrypt(date,key_size,iv)
      print(date)
  conn.close()
os.system("pause")