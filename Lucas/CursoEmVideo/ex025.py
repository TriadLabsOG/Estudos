nome = str(input('Qual seu nome completo: '))
nome1 = nome.capitalize()
nome2 = nome1.strip()
print(f'Seu nome tem Silva? {'Silva' in nome2}')