import socket

def xor(a,b):
    result = []
    for i in range(0, len(b)):
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


def encodedata(data,key):
    lkey = len(key)
    appendeddata = data + '0'*(lkey-1)
    remainder = mod2div(appendeddata,key)
    finaldat = data + remainder
    return finaldat



port = 1234
localip = '127.0.0.1'
s = socket.socket()
s.connect((localip,port))

inputstring  = input("Enter data:")
data = (''.join(format(ord(x),'b')for x in inputstring))
print("Data in binary format:",data)
key = "1001"

encdata = encodedata(data,key)
s.send(encdata.encode())
print("Feedback from Client:",s.recv(1024).decode())
s.close()