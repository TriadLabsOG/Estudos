# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano para ver se ele é bissexto: '))

if ano % 4 == 0:
    print('Este ano é bissexto!')

else:
    print('Este ano não é bissexto!')