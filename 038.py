n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print(f'{n1} FOI O PRIMEIRO VALOR DIGITADO E É MAIOR QUE {n2}')
elif n2 > n1:
    print(f'{n2} FOI O SEGUNDO VALOR DIGITADO E É MAIOR QUE {n1}')
else:
    print('OS VALORES SÃO IGUAIS')
