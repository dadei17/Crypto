from binascii import *

# http://cs.wellesley.edu/~fturbak/codman/letterfreq.html

prob = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406,
    'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,  's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074, ' ': 20.00
}

def countScore(s):
    result = 0
    for i in s:
        lowerChar = chr(i).lower()
        if lowerChar in prob:
            result += prob[lowerChar]

    return result

def findMatch(keyString, dataBytes):
    keyBytes = keyString.encode()
    plaintextBytes = dataBytes

    byteArr = bytearray()
    for i in range(len(plaintextBytes)):
        remainder = i % len(keyBytes)
        byteArr.append(keyBytes[remainder] ^ plaintextBytes[i])
    return byteArr.decode()

def hammingDist(f, s):
    result = 0
    for b1, b2 in zip(f, s):
        for a, b in zip(bin(b1)[2:], bin(b2)[2:]):
            result += int(a) ^ int(b)

    return result
    
def averageDist(keyMas):
    pairs = []
    for i in range(0, len(keyMas)-1):
        for j in range(i+1, len(keyMas)):
            pairs.append((keyMas[i], keyMas[j]))
    return  sum([hammingDist(f, s) / len(pairs) for f,s in pairs])

def filledDistance(cyph):
    distances = []
    for keySize in range(2, 41):
        keyMas = []
        for i in range(0, len(cyph), keySize):
            keyMas.append(cyph[i:i+keySize])
        
        keyMas = keyMas[:4]
        if len(keyMas[-1]) < keySize: break

        avgDistance = averageDist(keyMas)
        distances.append((avgDistance/keySize, keySize))
    distances.sort()
    return distances[:10] 

cyph = a2b_base64(input().encode())
finalResult = ''
bestScore = 0

for x, size in filledDistance(cyph):
    allKeys = ''

    for i in range(size):
        arr = bytearray()

        for j in range(i, len(cyph), size):
            arr.append(cyph[j])

        s = hexlify(arr)
        key = 0
        finalByteArr = ""
        maxScore = 0
        for i in range(257):
            ch = chr(i).encode()[0]
            first = a2b_hex(s)
            byteArr = bytearray()
            for j in range(len(first)):
                byteArr.append(first[j]^ch)
            if countScore(byteArr) > maxScore:
                finalByteArr = byteArr
                maxScore = countScore(finalByteArr)
                key = i

        allKeys+=chr(key)

    matched = findMatch(allKeys, cyph)
    eachScore = countScore(matched.encode())
    if eachScore > bestScore:
        finalResult = matched
        bestScore = eachScore

print(finalResult)