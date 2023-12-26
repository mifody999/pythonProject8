s = set()
for n in range(150, 1001):
    r = str(bin(n))[2:]
    r = r.replace('0', '')
    r = int(r, 2)
    s.add(r)
    print(r)
print(len(s))








