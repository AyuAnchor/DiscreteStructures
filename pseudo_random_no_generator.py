from datetime import datetime

M = 120   # modulus 
a = 2     # multiplier
c = 34    # increment
x0 = 0    # seed

# x(n+1) = (a*x(n) + c) % m

while True:
    n = input('\nPress enter to generate, 0 to quit')
    if n == '0': break
    x1 = (a * x0 + c) % M
    x0 = x1
    c = datetime.now().second
    print(x1)