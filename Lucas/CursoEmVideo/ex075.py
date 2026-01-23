
num = (int(input('Digite um número: ')), # Lê os valores e guardando em uma tupla
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Você digitou os valores {num}')


print(f'O valor 9 apareceu {num.count(9)} vezes') # A) Conta quantas vezes apareceu o valor 9


if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição') # B) Em que posição foi digitado o primeiro valor 3
else:
    print('O valor 3 não foi digitado em nenhuma posição')


print('Os valores pares digitados foram: ', end='') # C) Quais foram os números pares
for n in num:
    if n % 2 == 0:
        print(n, end=' ')