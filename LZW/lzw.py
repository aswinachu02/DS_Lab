def encoder(string):
    table = dict()
    lis = []

    for i in range(256):
        table[chr(i)] = i

    current = ''
    nxt_code = 257

    for i in string:
        current += i
        if (current not in table):
            table[current] = nxt_code
            nxt_code += 1
            current = current[:-1]
            lis.append(table[current])
            current = i
    lis.append(table[current])
    return lis

def decoder(lis):
    table = dict()
    for i in range(256):
        table[i] = chr(i)
    previous = ''
    nextcode = 257
    ans = ''
    for i in lis:
        ans += table[i]
        if (previous != ''):
            table[nextcode] = previous + table[i][0]
            nextcode += 1
        previous = table[i]
    return ans

def main():
    lis = []
    ans = ''
    msg = input("Enter input:")
    lis = encoder(msg)
    print("After compression:",lis)
    ans = decoder(lis)
    print("after decompression:",ans)

main()