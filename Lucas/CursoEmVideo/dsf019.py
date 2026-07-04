# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
n1 = str(input('Digite o nome do primeiro aluno: ')).capitalize()
n2 = str(input('Digite o nome do segundo aluno: ')).capitalize()
n3 = str(input('Digite o nome do terceiro aluno: ')).capitalize()
n4 = str(input('Digite o nome do quarto aluno: ')).capitalize()

sequencia = n1, n2, n3, n4

esc = random.choice(sequencia)

print(f'O escolhido para apagar o quadro foi o(a) {esc}. Que sortudo!')