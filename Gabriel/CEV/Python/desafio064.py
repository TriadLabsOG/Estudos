numero = 0
quantidade_numeros = 0
numero_chave = 0
 
while numero_chave != 999:
    numero_chave = int(input('Digite um número [999 para parar]: '))
    numero += numero_chave
    quantidade_numeros += 1
 
quantidade_numeros -= 1
numero -= 999
 
print(f'Você digitou {quantidade_numeros} números e a soma deles é {numero}')
