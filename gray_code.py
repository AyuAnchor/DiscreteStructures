'''
01
01
11
10
'''

# GRAY CODE

n = int(input('Number of bits for which you want to generate the gray code for:\n'))
x = 0
while x < 1<<n:
    i = n-1
    print(x>>i & 1, end='')
    while i:
        print((x>>i & 1) ^ (x>>(i-1) & 1), end='')
        i -= 1
    print()
    x += 1