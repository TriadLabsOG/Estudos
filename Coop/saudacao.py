''' Exercício 1: O "Olá Mundo" da Colaboração
Objetivo: Garantir que ambos conseguem enviar código para o mesmo repositório sem erros básicos.

Dev A: Cria um arquivo saudacao.py. Escreve um código que pergunta o nome do usuário e imprime "Olá, [Nome]!". Faz o commit e push.

Dev B: Dá git pull. Abre o arquivo e adiciona uma linha extra perguntando "Como você está hoje?". Faz o commit e push.

Dev A: Dá git pull para ver a atualização.'''

nome = input('Digite o seu nome: ')
print(f'Olá, {nome}. Como você está hoje?')