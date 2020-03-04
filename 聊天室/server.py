import socket
import threading
import logging
import datetime
import sys


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

class ChatServer:
    def __init__(self,ip='192.168.100.22',port=9999):
        self.addr = (ip,port)
        self.sock = socket.socket()
        self.clients = {}

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen() #服务启动

        threading.Thread(target=self.accept,name='迎接进程').start()

    def accept(self):
        while True: #一般一个线程
            s,raddr = self.sock.accept() #阻塞
            logging.info('\n来了个新家伙\n')
            
            threading.Thread(target=self.recv,name='接收进程',args=(s,raddr)).start()
            
    def recv(self,sock,addr):
        '''先命名客户端id，然后无限接收消息'''
        sock.send('请输入你的id\n'.encode())
        name = sock.recv(1024).decode()
        self.clients[addr] = (sock,name) #远程地址：(socket对象（用来改送和接受数据）,用户名）
        
        while True: #很多线程
            try :
                data = sock.recv(1024) #阻塞，bytes
                text = data.decode()
                msg = '\\\\\\from:{0} {1}/// \n{2}\n'.format(
                    self.clients[addr][1],
                    datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S"),
                    text).encode()
                sendlist = []
                for s in self.clients.values():
                    sendlist.append(s[0])
                sendlist.remove(sock)
                for sr in sendlist:
                    sr.send(msg) 

            except  ConnectionAbortedError:
                sb = 'someone was left'
                logging.info(sb)
                self.clients.pop(sock.getpeername())
                for s in self.clients.values():
                    s[0].send(sb.encode())
                break
            
            except   ConnectionResetError:
                sb = 'someone was left'
                logging.info(sb)
                self.clients.pop(sock.getpeername())
                for s in self.clients.values():
                    s[0].send(sb.encode())
                break
        
    def stop(self):
        for s in self.clients.values():
            s[0].close()
        self.sock.close()

cs = ChatServer()
cs.start()
while True:
    cmd = input('>>>')
    if cmd.strip() == 'byebye':
        cs.stop()
        break
    
    if cmd.strip() == 'now':
        logging.info(threading.enumerate())
        
    if cmd.strip() == 'who':
        for k,v in cs.clients.items():
            print(v[1],end = ': ')
            print(k)
       
