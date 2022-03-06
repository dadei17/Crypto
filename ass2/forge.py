from oracle import *
import sys

def xorStr(a, b):
    byteArr = bytearray()
    for i in range(len(bytearray(a))):
        byteArr.append(bytearray(a)[i] ^ bytearray(b)[i])
    return byteArr

if len(sys.argv) < 2:
    print "Usage: python forge.py <challenge_filename>"
    sys.exit(-1)

f = open(sys.argv[1])
msg = f.read()
f.close()
l = 32
msg2 = msg[:l]

Oracle_Connect()
tag = Mac(msg2, len(msg2))
for i in range(len(msg) / 32 - 1): 
    xoredStr = xorStr(str(tag), msg[l:l+16])
    newBlock = xoredStr + msg[l+16:l+32]
    tag = Mac(newBlock, 32)
    l += 32

if Vrfy(msg, len(msg), tag) == 1:
    print "Verified"
else:
    print "Message verification failed."

Oracle_Disconnect()
