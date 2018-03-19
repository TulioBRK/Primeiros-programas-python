#15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
#  8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
ganhoh = int(input("Quanto você ganha por hora? : "))
horast = int(input("Quantas horas você trabalhou? : "))
salariob = ganhoh * horast
print("+ Salário Bruto: R$ {}".format(salariob))
print("- Imposto de Renda: R$ {}".format(11 / 100 * salariob))
print("- INSS: R$ {}".format(8 / 100 * salariob))
print("- Sindicato: R$: {}".format(5 / 100 * salariob))
print("= Salário Liquido: R$ {}".format(salariob - (5 / 100 * salariob) - (8 / 100 * salariob) - (11 / 100 * salariob)))