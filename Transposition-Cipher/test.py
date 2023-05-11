import math

def encoder(pt,k):
    ciphertext = ''
    key_indx = 0
    msg_lst = list(pt)
    msg_len = len(pt)
    key_lst = sorted(list(k))
    col = len(k)
    row = int(math.ceil(msg_len/col))
    fill_null = int(col * row - msg_len)
    msg_lst.extend(' ' * fill_null)
    matrix = [msg_lst[i:i+col] for i in range(0,len(msg_lst),col)]
    for _ in range(col):
        current_indx = k.index(key_lst[key_indx])
        ciphertext += ''.join(row[current_indx] for row in matrix)
        key_indx += 1
    return ciphertext


def decoder(ct,k):
    msg_len = len(ct)
    msg_lst = list(ct)
    msg_indx = 0
    key_lst = sorted(list(k))
    key_indx = 0
    plaintext = ''
    col = len(k)
    row = int(math.ceil(msg_len/col))
    decipher = []
    for _ in range(row):
        decipher += [[None]*col]
    for _ in range(col):
        currentindx = k.index(key_lst[key_indx])
        for j in range(row):
            decipher[j][currentindx] = msg_lst[msg_indx]
            msg_indx += 1
        key_indx += 1
    plaintext = ''.join(sum(decipher,[]))
    return plaintext


def main():
    plaintext = input("Enter pt:")
    key = 'HACK'
    ciphertext = encoder(plaintext,key)
    print("ciphertext is ",ciphertext)
    ans = decoder(ciphertext,key)
    print("After deocdeing:",ans)

main()