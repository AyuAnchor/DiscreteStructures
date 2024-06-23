# x =  ( ∑ (rem[i]*pp[i]*inv[i]) ) % prod

from functools import reduce

def inverseMod(x, mod):
    M = mod
    t1 = 0; t2 = 1
    while x:
        q = mod // x
        r = mod % x
        t = t1 - q * t2
        mod, x = x, r
        t1, t2 = t2, t
    return t1 % M


n        = 3
coPrimes = [3, 4, 5]
rem      = [1, 2, 3]
prod     = reduce(lambda x, y: x*y, coPrimes)
pp       = [prod//i for i in coPrimes]
inv      = [inverseMod(pp[i], coPrimes[i]) for i in range(n)]

x = 0
for i in range(n):
    x = (x + pp[i] * inv[i] * rem[i]) % prod

print(x)