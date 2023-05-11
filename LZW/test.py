def encoder(string):
    lis = []
    table = dict()
    nextcode = 257
    current = ''

    for i in range(256):
        table[chr(i)] = i

    for i in string:
        current += i
        if current not in table:
            table[current] = nextcode
            nextcode += 1
            current = current[:-1]
            lis.append(table[current])
            current = i
    lis.append(table[current])
    return lis


def decoder(lis):
    table = dict()
    ans = ''
    previous = ''
    nextcode = 257

    for i in range (256):
        table[i] = chr(i)
    
    for i in lis:
        ans += table[i]
        if previous != '':
            table[nextcode] = previous + table[i][0]
            nextcode += 1
        previous = table[i]
    return ans 


def main():
    lis = []
    ans = ''
    inputstring = input("Enter input:")
    lis = encoder(inputstring)
    print("After compression:",lis)
    ans = decoder(lis)
    print("After decompression:",ans)


main()