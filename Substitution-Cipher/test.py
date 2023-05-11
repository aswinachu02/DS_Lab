def encoder(pt,k):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ''
    lalp = len(alphabets)
    lpt = len(pt)
    lk = len(k)
    for i in range (0,lpt):
        ch = pt[i]
        for j in range(0,lalp):
            if ch == alphabets[j]:
                break
        if j < lalp - lk:
            j += lk
        else:
            j = j - lalp + lk
        ciphertext += alphabets[j]
    return ciphertext

def decoder(ct,k):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = ''
    lalp = len(alphabets)
    lct = len(ct)
    lk = len(k)
    for i in range(0,lct):
        ch = ct[i]
        for j in range(0,lalp):
            if ch == alphabets[j]:
                break
        if j > lk - 1:
            j -= lk
        else:
            j = lalp + j - lk
        plaintext += alphabets[j]
    return plaintext


def main():
    plaintext = input("Enter pt:")
    key = "aswin"
    ciphertext = encoder(plaintext,key)
    print("ciphertext is ",ciphertext)
    ans = decoder(ciphertext,key)
    print("After deocdeing:",ans)

main()