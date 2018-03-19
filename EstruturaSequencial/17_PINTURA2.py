# Faça um Programa para uma loja de tintas
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#  e que a tinta é vendida em latas de 18 litros
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga
# e sempre arredonde os valores para cima, isto é, considere latas cheias.
metros = int(input("Digite quantos metros quadrados você irá pintar: "))

litros = metros / 6 * 1.1
latas = litros // 18
galoes = litros // 3.6

if litros % 18 != 0:
    latas += 1
if litros % 3.6 != 0:
    galoes += 1

mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)
if litros - (mixLatas * 18.0) % 3.6 != 0:
    mixGaloes += 1

print("Para pintar {} metros quadrados irá custar: ".format(metros))
print("Somente com latas serão necessárias {} latas e ira custar {} reais".format(int(latas), int(latas * 80)))
print("Somente com galões serão necessárias {} galões e ira custar {} reais".format(int(galoes), int(galoes * 25)))
print("Misturando latas e galões serão necessárias {} latas e {} galões e ira custar {}".format(int(mixLatas), int(mixGaloes), int((mixLatas * 80) + (mixGaloes * 25))))
