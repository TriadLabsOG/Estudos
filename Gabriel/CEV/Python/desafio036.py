'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('\033[30mDigite o valor da casa que deseja comprar:\033[m '))
salario = float(input('\033[30mQual o salario:\033[m '))
meses = int(input('\033[30mPagamento em quantos anos:\033[m ')) * 12

prestacao = casa/meses
excedencia = 0.3 * salario


if prestacao > excedencia:
    print(f'\033[31mNão foi aprovado pois o valor da parcela \033[1;33m({prestacao:.2f})\033[31m passou de \033[1;33m30%\033[31m do seu salario.\033[m')
else:
    print('\033[1;32mAprovado\033[m')
    print(f'\033[36mVão ser \033[33m{meses}\033[36m parcelas de \033[33mR${prestacao:.2f}\033[36m por \033[33m{int(meses/12)}\033[36m anos.\033[m')
