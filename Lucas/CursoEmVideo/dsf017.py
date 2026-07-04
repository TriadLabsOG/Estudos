# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math
co = float(input('Digite o valor do cateto oposto: '))

ca = float(input('Digite o valor do cateto adjascente: '))

h = math.hypot(co, ca)

print(f'A hipotenusa do triangulo é igual à {h}')