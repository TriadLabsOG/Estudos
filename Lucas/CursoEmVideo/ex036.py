import sys
valor = float(input('Digite o valor da casa: '))
parcelas = int(input('Digite a quantiddade de parcelas que ira ser pagado: '))
salario = float(input('Digite o salario do devedor: '))
prestacao = valor / parcelas #Valor pago por mês
limite = salario * 0.30 #Valor para conseguir o emprestimo
if prestacao>limite:
    print('\033[1;31;41mEmprestimo Negado!\033[m')
else:
    print('\033[1;32;42mEmprestimo Autorizado!\033[m')
    sys.exit()