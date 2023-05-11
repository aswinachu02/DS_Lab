import socket
from _thread import *

localip = '127.0.0.1'
port = 12345
client_names = {}
client_list = []


def send_all(client,message):
    for tc in client_list:
        if tc != client:
            try:
                tc.send(message.encode())
            except:
                tc.close()
                client_list.remove(client)


def handle(client, addr):
    name = client_names[addr[0]]
    client.send(f"SERVER >>> Welcome, {name}".encode())
    while True:
        try:
            msg_enc = client.recv(1024)
            if msg_enc:
                message = name + " >> " + msg_enc.decode()
                print(message)
                send_all(client,message)
        except Exception as e:
            print(e)
            continue



def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((localip,port))
    s.listen(100)
    while True:
        c,addr = s.accept()
        name = c.recv(1024).decode()
        client_names[addr[0]] = name
        client_list.append(c)
        print(f"{name} connected")
        start_new_thread(handle, (c,addr))
    s.close()



main()