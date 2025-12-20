peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / altura**2
if imc <18.5:
    print('Você esta abaixo do peso, alimente-se!')
elif imc >=18.5 and imc <=25:
    print('Você esta no peso ideal, continue assim!')
elif imc >=25 and imc <=30:
    print('Você esta lidando com sobrepeso, fique em alerta e cuide de seu corpo!')
elif imc >=30 and imc <=40:
    print('Você esta lidando com a obesidade, vá ao medico de se cuide!')
elif imc >40:
    print('Você esta em obesidade mórbida')
print('LEMBRE-SE DE SEMPRE CUIDAR DO SEU CORPO!')   
