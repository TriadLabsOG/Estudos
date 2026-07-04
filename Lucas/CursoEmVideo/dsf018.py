# Faça um programa que leia um ângulo qualquer e mostre seu seno, conseno e tangente desse ângulo
from math import sin, cos, tan, radians

a = float(input('Digite o valor do angulo: '))

c = cos(radians(a))

s = sin(radians(a))

t = tan(radians(a))

print(f'O ângulo {a} tem como seu seno {s}, seu coseno {c} e sua tangente {t}')
