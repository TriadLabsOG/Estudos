frase = str(input('Digite uma frase:')).upper().strip().capitalize()
quantidade = frase.count('A')
primeira = frase.find('A')+1
ultima = frase.rfind('A')+1
print(f'A quantidade de letras "A" que apareceu foram {quantidade}')
print(f'A primeira letra "A" apareceu na posição {primeira}')
print(f'A ultima letra "A" aparece na {ultima}ª posição da frase')