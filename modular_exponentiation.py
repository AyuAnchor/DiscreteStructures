a = 5; b = 5; M = 10**9 + 7

x = 1; power = a % M
while b:
    if b & 1:
        x = (x * power) % M
    power = (power * power) % M
    b = b >> 1

print(x)