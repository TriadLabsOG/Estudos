# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessario para pinta-lá, sabendo que cada litro de tinta pinta 2m²

b = float(input('Digite a largura da parede em metros: '))

h = float(input('Digite a altura da parede em metros: '))

a = b * h

l = a / 2

print(f'A área da sua parede é de {a}m², precisando de {l}L de tinta para pintar a parede')