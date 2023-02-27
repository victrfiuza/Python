name = str(input('name: '))
print(f'Upper:{name.upper()}')  # A
print(f'Lower:{name.lower()}')  # a
print(f'full name: {len(name)-name.count(" ")}')
# vai achar o primeiro espaco e fala quantas casas tem antes
print(f'seu nome tem: {name.find(" ")} letras')
