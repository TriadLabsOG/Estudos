print('===== DESAFIO 1 =====')
nome = input('\033[31mQual é o seu nome? \033[1;32m')

#JEITO DO GUANABARA
print('\033[31mOlá\033[1;32m',nome,'\033[31m! É um prazer te conhecer.')

#METODO FORMAT
print(f'Olá \033[1;32m{nome}\033[31m! É um prazer te conhecer.')