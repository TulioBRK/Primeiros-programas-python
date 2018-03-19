#4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.
#Fiz de uma forma mais útil, de forma que não há limite de quantidade de notas.
notas = 0
notas_quantidade = int(input("Quantas notas você ira medir: "))
limite = notas_quantidade
while notas_quantidade != 0:
    notas = notas + int(input("Digite uma nota para somar: "))
    notas_quantidade -= 1
else:
    média = notas / limite
    print("O Resultado da média das notas inseridas foi: {} ".format(média))
