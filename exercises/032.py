ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} NÃO É UM ANO BISSEXTO')
