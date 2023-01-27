n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero:'))
n3 = float(input('Digite mais um numero: '))
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'Maior:{n1} Menor:{n3}')
if n2 > n1 and n2 > n3 and n1 > n3:
    print(f'Maior:{n1} Menor:{n3}')

