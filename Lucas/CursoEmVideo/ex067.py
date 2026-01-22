# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


while True:
    numero = int(input('Digite um valor para a tabuada: '))

    if numero < 0: # Se o número for menor do que 0 (negativo), o programa ira parar
        break
    
    contador = 1
    
    while contador <= 10:
        print(f'{numero} x {contador} = {numero * contador}')
        contador += 1

print('FIM DO PROGRAMA')