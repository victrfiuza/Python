casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Em quantos anos vai pagar? '))
mensal = casa / (anos*12)
pr = (salario*30) / 100
if mensal > pr:
    print(f'EMPRESTIMO NEGADO! A PRESTAÇÃO SERÁ DE R${mensal:.2f}')
else:
    print(f'EMPRESTIMO APROVADO! VALOR DA PRESTACÃO MENSAL DE R${mensal:.2f}')
