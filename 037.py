
print('-=-'*20)
n = int(input('DIGITE O NUMERO QUE DESEJA CONVERTER: '))
print('-=-'*20)
print('ESCOLHA A BASE DE CONVERSÃO: \n')
base = int(input('[1]BINARIO\n[2]OCTAL\n[3]HEXADECIMAL\n\n SELECIONE: '))
print('-=-'*20)
if base == 1:
    # calculo binario
    print(f'O NUMERO DIGITADO CONVERTIDO PARA BINARO É: {bin(n)[2:]}')
elif base == 2:
    # calculo octal
    print(f'O NUMERO DIGITADO CONVERTIDO PARA OCTAL É: {oct(n)[2:]}')

elif base == 3:
    # calculo hexadecimal
    print(f'O NUMERO DIGITADO CONVERTIDO PARA HEXADECIMAL É: {hex(n)[2:]}')
