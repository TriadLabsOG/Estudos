# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada
import random
aluno1 = input("Nome do primeiro aluno: ")
aluno2 = input("Nome do segundo aluno: ")
aluno3 = input("Nome do terceiro aluno: ")
aluno4 = input("Nome do quarto aluno: ")

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista_alunos)

print("A ordem de apresentação será:")
for i, aluno in enumerate(lista_alunos, 1):
    print(f"{i}. {aluno}")