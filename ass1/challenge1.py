import base64 

hexString = input()
string = bytes.fromhex(hexString).decode('utf-8')
b = string.encode('ascii')
b64 = base64.b64encode(b)
result = b64.decode('ascii')
print(result)