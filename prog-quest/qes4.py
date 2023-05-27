def zeyad_prime_number(a):
    z = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            z += 1
    if z == 0:
        return a

z_l = [z for z in range(2, 1001) if zeyad_prime_number(z)]
print(z_l)
            