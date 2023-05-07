import socks
import socket
SOCKS_VERSION = 1
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 50007  # 设置端口
serv.bind(("127.0.0.1", port))  # 绑定端口
serv.listen(5)
while True:
  conn, addr = serv.accept()
  from_client = ''
  while True:
    data = conn.recv(4096)
    if not data: break
    from_client += data.decode('utf8')
    print (from_client)
    conn.send("I am SERVER\n".encode())
  conn.close()
print ('client disconnected and shutdown')