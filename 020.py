from random import shuffle
name1 = str(input('Digite um nome:'))
name2 = str(input('Digite um nome:'))
name3 = str(input('Digite um nome:'))
name4 = str(input('Digite um nome:'))
lista = [name1, name2, name3, name4]

# ordem random
shuffle(lista)

print(f'ordem: {lista}')
