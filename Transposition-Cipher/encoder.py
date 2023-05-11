import socket, math

localip = '127.0.0.1'
port = 12345
key = 'HACK'

def encoder(pt):
    ciphertext = ''
    msg_len = len(pt)
    msg_lst = list(pt)
    key_lst = sorted(list(key))
    key_indx = 0
    col = len(key)
    row = int(math.ceil(msg_len/col))
    fill_null = int((col * row) - msg_len)
    msg_lst.extend(' ' * fill_null)
    matrix = [msg_lst[i:i+col] for i in range(0,len(msg_lst),col)]
    for _ in range(col):
        current_indx = key.index(key_lst[key_indx])
        ciphertext += ''.join(row[current_indx] for row in matrix)
        key_indx += 1
    return ciphertext 



s = socket.socket()
s.connect((localip,port))

plaintext = input("Enter plaintext:")
ciphertext = encoder(plaintext)
print("Ciphertext:",ciphertext)
s.send(ciphertext.encode())

s.close()

