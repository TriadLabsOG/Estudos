numero = int(input('Digite um valor: '))

acumuladora = 0

contadora = 0

while numero != 999:
    
    acumuladora += numero

    contadora +=1
    
    numero = int(input('Digite um valor: '))

print(f'Você digitou {contadora} numeros e a soma de todos eles é {acumuladora}')

