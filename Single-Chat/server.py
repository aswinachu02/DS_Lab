import socket

s = socket.socket()
localip = '127.0.0.1'
port = 12346
s.bind((localip,port))
s.listen(5)

c,addr = s.accept()
print("Connection established with: ",addr)
while(True):
    msg = input("You:")
    c.send(msg.encode())
    if msg == 'exit':
        break
    rcvmsg = c.recv(1024).decode()

    #msgaddrpair = c.recvfrom(1024)
    #msg = msgaddrpair[0]
    #address = msgaddrpair[1] 

    print("Client:",rcvmsg)
    if rcvmsg == 'exit':
        break


c.close()