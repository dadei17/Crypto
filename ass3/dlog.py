import math

# 375374217830

def prepareHashTable(hashTable, g, h, b, p):
	forMatch = h % p
	inv = pow(g, p-2, p)
	for x1 in range(0, b):
		hashTable[forMatch] = x1
		forMatch = forMatch * inv % p

	
# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def discrete_log(g, h, p, max_x):
	hashTable = {}
	b = int(math.sqrt(max_x))
	prepareHashTable(hashTable, g, h, b, p)
	toMatch = 1
	
	for x0 in range (0,b):
		if toMatch in hashTable:
			print x0*b + hashTable[toMatch]
			break
		toMatch = toMatch * pow(g, b, p) % p

def main():
	p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
	g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
	h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
	max_x = 1 << 40 # 2^40
	discrete_log(g, h, p, max_x)

if __name__ == '__main__':
	main()


