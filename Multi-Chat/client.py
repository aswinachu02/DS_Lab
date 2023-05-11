import socket
import sys, select
from _thread import *

localip = '127.0.0.1'
port = 12345

def main():
    server = socket.socket()
    server.connect((localip,port))
    name = input("Enter name:")
    server.send(name.encode())
    while True:
        socket_list = [sys.stdin,server]
        rd,wr,err = select.select(socket_list,[],[])
        for socks in rd:
            if socks == server:
                message_enc = socks.recv(1024)
                if message_enc:
                    print(message_enc.decode())
            else:
                message = sys.stdin.readline()
                server.send(message.encode())
                sys.stdout.write("<You>" + message)
                sys.stdout.flush()



main()