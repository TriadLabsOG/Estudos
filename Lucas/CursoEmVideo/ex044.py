import sys
valor = float(input('Qual é o valor do item? '))
print('[1] Dinheiro(10% de desconto)')
print('[2] Cartão(5% de desconto)')
print('[3] 2x no cartão(Sem desconto)')
print('[4] 3x ou mais no cartão(20% de juros)')
opcao = int(input('Digite qual opção você ira escolher: '))
if opcao == 1:
    print(f'Você ira pagar R${valor - (valor * 0.10)}')
elif opcao == 2:
    print(f'Você ira pagar R${valor - (valor * 0.05):.2f}')
elif opcao == 3:
    print(f'Você ira pagar R${valor}')
elif opcao == 4:
    print(f'Você ira pagar R${valor + (valor * 0.2 * 2)}')
else:
    print('Erro: esta opção não existe!')
    sys.exit()
print('\033[1;34;44mObrigado por comprar aqui, volte sempre!\033[m')