#06 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#Fiz um programa que facilita para o usuário , só souber o diametro do circulo.
from math import pi
escolha = int(input("Digite 1 se você já tiver o raio do circulo e 2 se você só tiver o diâmetro: "))
if escolha == 1:
    raio = int(input("Diga o raio do circulo: "))
    area = pi * (raio ** 2)
    print(area)
elif escolha == 2:
    diâmetro = int(input("Diga o diametro do circulo: "))
    raio = diâmetro // 2
    area = pi * (raio ** 2)
    print(area)
else:
    print("Digite um numero valido!")