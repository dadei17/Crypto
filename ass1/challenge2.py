first = input()
second = input()

for i in range(len(first)):
    intNum = int(first[i],16)^int(second[i],16)
    print(format(intNum, 'x'), end='')