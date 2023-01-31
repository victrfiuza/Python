from datetime import datetime
cont = 0
cont2 = 0
idade = 0
hj = datetime.now().year
for i in range(1, 8):
    ano = int(input('ANO DE NASCIMENTO: '))
    idade = hj - ano
    if idade < 18:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print(f'{cont} PESSOAS NÃO ATINGIRAM A MAIORIDADE PENAL!')
print(f'{cont2} PESSOAS ATINGIRAM A MAIORIDADE PENAL!')
