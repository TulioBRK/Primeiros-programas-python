#8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
ganho = int(input("Quanto você ganha por hora: "))
horas_trabalhadas = int(input("Quantas horas você trabalhou: "))
print("Você trabalhou por {} horas , ganhando {} reais por hora e no total você recebeu {} reais de salário".format(horas_trabalhadas,ganho,ganho * horas_trabalhadas))