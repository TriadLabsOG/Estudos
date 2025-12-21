#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))

if num > 1:

     # LISTA
     lista_de_divisao = []
     for i in range(2, num + 1):
          lista_de_divisao.append(num/i)

     # TESTE
     listateste = []
     for i in range(0, len(lista_de_divisao)):
          if lista_de_divisao[i].is_integer():
               listateste.append('inteiro')
          else:
               listateste.append('float')

     # PRINT
     if listateste.count('inteiro') > 1:
          print('O número não é primo')
     else:
          print('O número é primo')
else:
     print('O número não é primo')
