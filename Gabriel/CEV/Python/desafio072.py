# Exercício Python 72: Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    index = int(input('Digite o número por extenso que deseja ver: '))
    if index > 20:
        print(f"{'':-^49}")
        print('ERRO: Não é permitido números maiores do que 20.\n')
        print(f"{'TENTE NOVAMENTE':-^49}\n")
    else:
        print(f'Seu numero é {numeros[index]}.')
        break