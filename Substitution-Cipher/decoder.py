import socket

localip = '127.0.0.1'
port = 12345

def decoder(ct,k):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    lalp = len(alphabets)
    lk = len(k)
    lct = len(ct)
    plaintext = ''
    for i in range(0,lct):
        ch = ct[i]
        for j in range(0,lalp):
            if ch == alphabets[j]:
                break
        if j > lk-1:
            j -= lk
        else:
            j = lalp - lk + j
        plaintext += alphabets[j]
    return plaintext


s = socket.socket()
s.connect((localip,port))

msg = s.recv(1024).decode()
d = msg.split(' ')
data = d[0]
key = d[1]

print("Encoded message:",data)
plaintext = decoder(data,key)
print("plaintext: ",plaintext)
print("key: ",key)

s.close()