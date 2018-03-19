#13 Tendo como dados de entrada a altura e o sexo de uma pessoa
# , construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 (h = altura)
#Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
genero = int(input("Digite 1 se você for homem e 2 se você for mulher: "))
altura = float(input("Digite sua altura: "))
if genero == 1:
    pesoideal = (72.7 * altura) - 58
    pesoatual = float(input("Diga quanto você pesa: "))
    if pesoatual < pesoideal:
        print("Você esta abaixo do peso ideal, você esta pesando {} e seu peso ideal é {}.".format(pesoatual,int(pesoideal)))
    elif pesoatual > pesoideal:
        print("Você esta acima do peso ideal, você esta pesando {} e seu peso ideal é {}.".format(pesoatual,int(pesoideal)))
    else:
        print("Seu peso esta perfeito!! Parabéns.")
elif genero == 2:
    pesoideal = (62.1 * altura) - 44.7
    pesoatual = float(input("Diga quanto você pesa: "))
    if pesoatual < pesoideal:
        print("Você esta abaixo do peso ideal, você esta pesando {} e seu peso ideal é {}.".format(pesoatual,int(pesoideal)))
    elif pesoatual > pesoideal:
        print("Você esta acima do peso ideal, você esta pesando {} e seu peso ideal é {}.".format(pesoatual,int(pesoideal)))
    else:
        print("Seu peso esta perfeito!! Parabéns.")
else :
    print("Digite o numero certo sobre seu sexo.")
