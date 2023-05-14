import random
import string
import socket
def random_string(munber):
  random_str = ''.join(random.sample(string.ascii_letters + string.digits, munber))
  return random_str

def ran_send():
  randomstr = ""
  for loopA in range(random.randint(1, 64)):
    str1 = random_string(random.randint(1, 62))
    randomstr = randomstr + str1
  return randomstr


client = socket.socket(socket.AF_PACKET, socket.SOCK_STREAM)

print(socket.AF_PACKET)
client.bind("10.8.0.2:0")
client.connect(('192.168.44.1', 50007))
key_size = b'f\xc8\xd9\x87\x99\xcd\x17B\x93\x8aWHwd\xb1\x0e\x1b.\xcf\xe4\xbb$\x90\xfa\x84\xd1\xd3\xcb\x9c\x9d^\xd7'
iv = b'5\xc6\x88\x91\xd0\xb9\xcc\xe7\xb2\xc8\xe8\x17]>\x911'
ci = 0
while True:
    if(ci == 3):
        break
    ci = ci + 1
    from_server = client.recv(4096)
    if not from_server: break
    print(from_server)
    date = bytes(ran_send(),"UTF8")
    client.send(date)
client.close()