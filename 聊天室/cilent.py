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
            data = self.sock.recv(1024)
            msg = data.decode()
            print(msg)

    def work(self):
        threading.Thread(target=self.recv,name='接收进程').start()
        
a = client()
ssln = ('192.168.100.22',9999)
a.connect(ssln)
a.work()
while True:
    msg = input()
    a.send(msg)

    
        
        
