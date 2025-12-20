n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2) / 2
if media >7.0:
    print(f'Sua media foi de {media}. Parabens, você \033[1;32;42mPASSOU DE ANO\033[m')
elif media > 5 and media <=6.9:
    print(f'Com esta media de {media}, você esta de recuperação. Estude muito!')
else:
    print(f'Com esta media de {media}, você \033[1;31;41mREPROVOU\033[m de ano. ESTUDE mais ano que vem!')