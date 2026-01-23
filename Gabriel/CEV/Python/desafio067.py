#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

numero_tabuada = 0

while True:
    numero_tabuada = int(input('Digite o número que deseja ver a tabuada: '))
    if numero_tabuada < 0:
        break
    for conta in range (1, 11):
        print(f'{numero_tabuada} x {conta} = {numero_tabuada * conta}')

"""
ANTIGO

multiplicador = 1
while True:
    numero_tabuada = int(input('Deseja ver a tabuada de qual número: '))
    if numero_tabuada > 0:
        while multiplicador < 11:
            produto = numero_tabuada * multiplicador
            print(f'{numero_tabuada} x {multiplicador} = {produto}')
            multiplicador += 1
        multiplicador = 1
    else:
        print('Fim da tabuada!')
        break
"""
