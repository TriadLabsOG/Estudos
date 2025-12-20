largura = float(input('Qual é a largura da sua parede: '))
altura = float(input('Qual é a altura da sua parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a proporção de {largura} x {altura} e sua área total é de {area}m²\n Para pintar esa parede, você precisara usar {tinta}l de tinta')