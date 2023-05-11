import socket

def xor(a,b):
    result = []
    for i in range(1,len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(adata,key):
    pick = len(key)
    temp = adata[0:pick]
    while(pick<len(adata)):
        if temp[0] == '1':
            temp = xor(key,temp) + adata[pick]
        else:
            temp = xor('0'*pick,temp) + adata[pick]
        pick += 1
    if temp[0] == '1':
        temp = xor(key,temp)
    else:
        temp = xor('0'*pick,temp)
    return temp

def decodedata(data,key):
    lkey = len(key)
    appended_data = data + '0'*(lkey-1)
    remainder = mod2div(appended_data,key)
    return remainder


port = 1234
localip = '127.0.0.1'
s = socket.socket()
s.bind((localip,port))
s.listen(5)

c,addr = s.accept()
data = c.recv(1024).decode()
print("Recieved data:",data)

key = '1001'
decdata = decodedata(data,key)
temp = '0'*(len(key)-1)
if decdata == temp:
    c.send(("Recieved data -" + data + "with no errors").encode())
else:
    c.send("error found")

c.close()
