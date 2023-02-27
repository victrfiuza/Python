from math import hypot
ad = float(input('cateto adjacente: '))
op = float(input('cateto oposto: '))
hi = hypot(ad, op)
print(f'hipotenusa vai medir:{hi:.2f}')
