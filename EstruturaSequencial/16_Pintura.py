#16 Faça um programa para uma loja de tintas.
#  O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#  Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#  em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
tamanhoMQ = int(input("Digite o tamanho da área que você deseja pintar em metros quadrados: "))
litros = tamanhoMQ / 3
latas = litros // 18
if (litros % 18 != 0):
    latas += 1
print("Para pintar {} metros quadrados você precisará de {} latas de tinta".format(tamanhoMQ,int(latas)))
print("e isso custará {} reais.".format(int(latas * 80)))