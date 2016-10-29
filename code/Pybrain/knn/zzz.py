
def prime(n):
    if n == 2 or n == 5:
        return n
    for i in range(2, n/2):
        if n%i == 0:
            return
        else:
            return n


res = []
for j in range(2, 10000):
    temp = prime(j)
    if temp is not None:
        res.append(temp)
new = res[0:99]


s = 0
for i in new:
    s = s + i**2

print s%3