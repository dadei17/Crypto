from oracle import *
from helper import *

n = 119077393994976313358209514872004186781083638474007212865571534799455802984783764695504518716476645854434703350542987348935664430222174597252144205891641172082602942313168180100366024600206994820541840725743590501646516068078269875871068596540116450747659687492528762004294694507524718065820838211568885027869
e = 65537
msg = "Crypto is hard --- even schemes that look complex can be broken"

def gcd(a, b): 
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gcd(b % a, a)
        return g, x - y * int(round(b/a, 0)), y

def inv(a, n):
    return gcd(a, n)[1] % n

Oracle_Connect()
m = ascii_to_int(msg)

mult = (Sign(2) * Sign(m/2)) % n
result = (mult * inv(Sign(1), n)) % n 

if Verify(m, result):
    print result

Oracle_Disconnect()    

