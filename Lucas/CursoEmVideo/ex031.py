distancia = int(input('Qual a distancia da viagem? '))
if distancia <200:
    print(f'O valor total da passagem é R${(distancia * 0.50)}')
else:
    print(f'O valor total ira ser R${(distancia * 0.45)}')
