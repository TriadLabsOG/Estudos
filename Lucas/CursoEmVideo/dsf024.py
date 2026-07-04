# Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cdd = str(input('Digite o nome da cidade: '))

divisao = cdd.split()

santo = divisao[0].find('Santo')

if santo == 0:
    print('Esta cidade começa com "Santo"')
else:
    print('Esta cidade não começa com "Santo"')