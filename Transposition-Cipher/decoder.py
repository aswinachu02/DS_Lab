import socket, math

localip = '127.0.0.1'
port = 12345
key = 'HACK'

def decoderdat(ct):
    msg_len = len(ct)
    msg_lst = list(ct)
    msg_indx = 0
    key_lst = sorted(list(key))
    key_indx = 0
    plaintext = ''
    col = len(key)
    row = int(math.ceil(msg_len/col))
    decipher = []
    for _ in range(row):
        decipher += [[None]*col]
    for _ in range(col):
        current_indx = key.index(key_lst[key_indx])
        for j in range(row):
            decipher[j][current_indx] = msg_lst[msg_indx]
            msg_indx += 1
        key_indx += 1
    plaintext = ''.join(sum(decipher,[]))
    return plaintext




s = socket.socket()
s.bind((localip,port))
s.listen(5)

c,addr = s.accept()
ciphertext = c.recv(1024).decode()
print("Ciphertext:",ciphertext)
plaintext = decoderdat(ciphertext)
print("Plaintext:",plaintext)