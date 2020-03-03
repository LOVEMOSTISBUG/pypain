import socket
import threading
import logging
import datetime

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

class ChatServer:
    def __init__(self,ip='localhost',port=9999):
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
            
            self.clients[raddr] = s  #远程地址：socket对象（用来改送和接受数据）
            threading.Thread(target=self.recv,name='接收进程',args=(s,raddr)).start()
            
    def recv(self,sock,addr):
        while True: #很多线程
            try :
                data = sock.recv(1024) #阻塞，bytes
                #logging.info(data) 收到的二进制消息
                if data == b'quit':
                    self.clients.pop(sock.getpeername())
                    break
                text = data.decode()
                msg = ' {2}  \\\\\\from:{0} {1}///'.format(
                    addr,
                    datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S"),
                    text).encode()

                for s in self.clients.values():
                    s.send(msg)

            except  ConnectionAbortedError:
                sb = 'someone was left'
                logging.info(sb)
                self.clients.pop(sock.getpeername())
                for s in self.clients.values():
                    s.send(sb.encode())
                break
            
            except   ConnectionResetError:
                sb = 'someone was left'
                logging.info(sb)
                self.clients.pop(sock.getpeername())
                for s in self.clients.values():
                    s.send(sb.encode())
                break
        
    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()

cs = ChatServer()
cs.start()
while True:
    cmd = input('>>>')
    if cmd.strip() == 'byebye':
        cs.stop()
        threading.event.wait(3)
        break
    
    if cmd.strip() == 'now':
        logging.info(threading.enumerate())
        
    if cmd.strip() == 'who':
        for n in cs.clients.keys():
            print(n)
       
