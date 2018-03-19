#14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#  João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
# Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.
peso = int(input("Digite quantos quilos de peixe você pescou: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print("Você ultrapassou o limite de 50 quilos de peixes, pescando {} quilos a mais".format(excesso))
    print("E terá de pagar uma multa de {} reais".format(multa))
else:
    print("A quantidade de peixe que você pescou não excedeu o limite.")
    print("E não terá de pagar multa nenhuma.")