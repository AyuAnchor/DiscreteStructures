# r2 inverse (modulo r1)
# 13 inverse (modulo 60)


def findInverse(r2, r1):
    M = r1
    t1 = 0; t2 = 1
    print("q\t r1 \t r2 \t r\t t1\t t2\t t")
    while r2:
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2
        print(q,'\t', r1, '\t',r2, '\t',r,'\t', t1,'\t', t2,'\t', t)
        r1, r2 = r2, r
        t1, t2 = t2, t
    return t1 % M


r1 = 5
r2 = 3

print(f'\n1/{r2} mod {r1} = {findInverse(r2, r1)}')
