n = str(input('Digite um numero: '))
n = '0000' + n
print(f'Unidade: {n[-3]}')
print(f'Dezena: {n[-2]}')
print(f'Centena: {n[-1]}')
print(f'Milhar: {n[-0]}')
