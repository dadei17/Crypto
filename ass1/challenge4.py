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
    
finalByteArr = ""    
maxScore = 0
for j in range(int(input())):
    s = input()
    for i in range(257):
        ch = chr(i).encode()[0]
        first = a2b_hex(s)
        byteArr = bytearray()
        for i in range(len(first)):
             byteArr.append(first[i]^ch)
        if countScore(byteArr) > maxScore:
            finalByteArr = byteArr
            maxScore = countScore(finalByteArr)

print (finalByteArr.decode())