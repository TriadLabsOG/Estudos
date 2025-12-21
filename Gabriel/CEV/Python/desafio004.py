cor = {'limpa': '\033[m',
        'azul': '\033[36m',
        'vermelha': '\033[31m',
        'verde': '\033[32m',
        'fbranco': '\033[47m'}

string = input(f'{cor["fbranco"]}{cor["azul"]}Escreva algo:{cor["limpa"]} ')

def Simnao (TF):
    if TF is True:
        return cor['verde'] , "Sim"
    return cor['vermelha'] , "Não"

print(f'\n{cor["azul"]}É alfanúmerico? {Simnao(string.isalnum())[0]}{Simnao(string.isalnum())[1]}')
print(f'{cor["azul"]}É alfabético? {Simnao(string.isalpha())[0]}{Simnao(string.isalpha())[1]}')
print(f'{cor["azul"]}É númerico? {Simnao(string.isnumeric())[0]}{Simnao(string.isnumeric())[1]}')
print(f'{cor["azul"]}É minúsculo? {Simnao(string.islower())[0]}{Simnao(string.islower())[1]}')
print(f'{cor["azul"]}É maiúsculo? {Simnao(string.isupper())[0]}{Simnao(string.isupper())[1]}')
print(f'{cor["azul"]}É espaço? {Simnao(string.isspace())[0]}{Simnao(string.isspace())[1]}')
print(f'{cor["azul"]}Está capitalizado? {Simnao(string.istitle())[0]}{Simnao(string.istitle())[1]}{cor["limpa"]}')
