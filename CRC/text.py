import socket

localip = '127.0.0.1'
port = 500

def xor(a,b):
    ans = []
    for i in range(0,len(b)):
        if a[i] == b[i]:
            ans.append('0')
        else:
            ans.append('1')
    return ''.join(ans)

def mod2div(adata,k):
    pick = len(k)
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
    

def encoder(data,key):
    appenddata = data + '0'*(len(key)-1)
    remainder = mod2div(appenddata,key)
    finaldata = data + remainder
    return finaldata

s = socket.socket()
s.connect((localip,port))

key = "1001"
inputstring= input("Enter data to be sent:")
data = ''.join(format(ord(x),'b')for x in inputstring)
print("Data in binary form:",data)
encdata = encoder(data,key)
print("Encoded data:")
s.send(encdata.encode())
s.close()