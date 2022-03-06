from binascii import *

keyBytes = input().encode()
plaintextBytes = input().encode()

byteArr = bytearray()
for i in range(len(plaintextBytes)):
    remainder = i % len(keyBytes)
    byteArr.append(keyBytes[remainder] ^ plaintextBytes[i])

print(b2a_hex(byteArr).decode())