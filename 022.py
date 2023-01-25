name = str(input('name: '))
print(f'Upper:{name.upper()}')  # A
print(f'Lower:{name.lower()}')  # a
fullname = name.replace(' ', '')
print(f'Full name: {len(fullname)}')
# foi divido e agora o 0 representa a primeira palavra.
fname = name.split()
print(f'First name: {fname[0]}')
print(f'First name: {len(fname[0])}')
