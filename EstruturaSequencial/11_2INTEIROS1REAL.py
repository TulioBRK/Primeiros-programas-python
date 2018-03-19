#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1 - o produto do dobro do primeiro com metade do segundo .
# 2 - 0 a soma do triplo do primeiro com o terceiro.
# 3 - 0 o terceiro elevado ao cubo.

int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número Real: "))

print("O resultado do dobro de {} com metade de {} é: {}".format(int1, int2, (int1*2) + (int2 / 2)))
print("O resultado da soma do triplo de {} com {} é: {}".format(int1, real, (int1 * 3) + real))
print("Ao elevar {} ao cubo o resultado é: {}".format(real, real ** 3))
