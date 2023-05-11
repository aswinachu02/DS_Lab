import socket

localip = '127.0.0.1'
port = 12345

def cipher(pt,k):
    ciphertext = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    lalp = len(alphabets)
    lpt = len(pt)
    lk = len(k)
    for i in range(0,lpt):
        ch = pt[i]
        for j in range(0,lalp):
            if ch == alphabets[j]:
                break
        if j < lalp-lk:
            j += lk
        else:
            j = j - lalp + lk
        ciphertext += alphabets[j]
    return ciphertext 



s = socket.socket()
s.bind((localip,port))
s.listen(5)

c,addr = s.accept()
plaintext = input("Enter plain text:")
key = input("Enter key")
ciphertext = cipher(plaintext,key)
print("ciphertext is ",ciphertext)
finaldata = ciphertext + " " + key
c.send((finaldata).encode())

c.close()
