from oracle import *
import sys


def addBlocks(blocks, curr):
    test = [blocks[i] for i in range(0, len(blocks)-2)]
    rc = Oracle_Send(test + curr, len(blocks))
    return rc == 1

def deciphering(blocks, deciphered, lastblock):
    decipheredblock = {}
    prev = blocks[-2]
    curr = blocks[-1]
    padding = 1
    for i in range(15, -1, -1):
        preblockcopy = prev[:]
        for j in decipheredblock:
            preblockcopy[j] = decipheredblock[j] ^ preblockcopy[j] ^ padding

        ithbyte = preblockcopy[i]
        for j in range(0, 256):
            preblockcopy[i] = j ^ ithbyte ^ padding
            if addBlocks(blocks, preblockcopy + curr):
                if lastblock:
                    if padding == 1 and padding == j:
                        continue
                decipheredblock[i] = j
                break
        padding += 1

    for k in decipheredblock:
        deciphered.append(decipheredblock[k])

if len(sys.argv) < 2:
    print "Usage: python decipher.py <ciphertext_filename>"
    sys.exit(-1)

f = open(sys.argv[1])
msg = f.read()
f.close()

a = [(int(msg[i:i+2], 16)) for i in range(0, len(msg), 2)]
Oracle_Connect()

print("Please Wait...")


blocks = [a[i:i+16] for i in range(0, len(a), 16)]

deciphered = []

for i in range(1, len(blocks)):
    if i == len(blocks)-1:
        deciphering(blocks[0:i+1], deciphered, True)
        break
    deciphering(blocks[0:i+1], deciphered, False)
    print i, " finished"

deciphered = deciphered[0:len(deciphered) - deciphered[-1]]

finalResult = ""
for i in deciphered:
    finalResult += chr(i)

print finalResult

Oracle_Disconnect()
