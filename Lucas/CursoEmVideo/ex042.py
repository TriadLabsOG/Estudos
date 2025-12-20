l1 = int(input('Digite o valor do primeiro segmento: '))
l2 = int(input('Digite o valor do segundo segmento: '))
l3= int(input('Digite o valor do terceiro segmento: '))
#Calculamos o valor de dois lados e se for maior que o unico que sobrou, dá para formar um triangulo
if l1<l2 + l3 and l2< l1 +l3 and l3< l1 + l2:
    print('É possivel montar um triangulo com esses segmentos, sendo um triangulo', end=' ' )
    if l1 == l2 == l3:
        print('Equilatero')
    elif l1 != l2 != l3 != l1:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Não é possivel fazer um triangulo com esses segmentos')