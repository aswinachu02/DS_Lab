import socket

s = socket.socket()
localip = '127.0.0.1'
port = 12346
s.connect((localip,port))

while(True):
    recieved = s.recv(1024).decode()
    print("Server: ",recieved)
    if recieved == 'exit':
        break
    msg = input("You: ")
    s.send(msg.encode())

    #s.sendto(str.encode(msg),(localip,port))
    
    if msg == 'exit':
        break
s.close()
