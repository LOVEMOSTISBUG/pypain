import socket
import threading
from random import randint

class client:
    def __init__(self):
        self.sock = socket.socket()
    def connect(self,addr):
        self.sock.connect(addr)
        self.addr = self.sock.getsockname()
        print(self.addr)
        print('连接成功')
        
    def send(self,msg):
        bmsg = msg.encode()
        self.sock.send(bmsg)

    def recv(self):
        while True:
            data,msgaddr = self.sock.recvfrom(1024)
            msg = data.decode()
            print(msg)

    def work(self):
        threading.Thread(target=self.recv,name='接收进程').start()

try:
    a = client()
    ip = input('请输入ip\n本机ip可cmd arp -a查看\n')
    port = int(input('请输入端口\n一般8000\n'))
    IPADDR = (ip,port)
    ssln = (IPADDR)
    a.connect(ssln)
    a.work()
    name = input('')
    a.send(name)
except Exception as e:
        print (str(e))
        print(f'总之哪里出错了 debug去吧。\n')
        os.system('pause')
while True:
    try:
        msg = input()
        a.send(msg)
    except Exception as e:
        print (str(e))
        print(f'总之哪里出错了 debug去吧。\n')
        os.system('pause')

        
        
