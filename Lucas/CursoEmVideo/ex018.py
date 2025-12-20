import math
angulo = float(input('Digite um ângulo: ')) 
sen = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno de {} é {:.2f}'.format(angulo, sen))
print('O cosseno de {} é {:.2f}'.format(angulo, cosseno))
print('A tangente de {} é {:.2f}'.format(angulo, tangente))
