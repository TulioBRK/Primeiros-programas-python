# Faça um Programa que peça a temperatura em graus Farenheit
# , transforme e mostre a temperatura em graus Celsius.
escolha = 3
while escolha >= 3:
    print("Digite um valor valido! ")
    escolha = int(input("Digite 1 para converter de Farenheit para Celsius e 2 para fazer o contrario: "))
if escolha == 1:
    F = int(input("Digite quantos graus Farenheit você deseja converter para Celsius: "))
    C = int((F - 32) // 1.8)
    print("O Resultado da conversão de {} graus Fahrenheit para Celsius foi de {} graus Celsius".format(F, C))
elif escolha == 2:
    C = int(input("Digite quantos graus Celsius você deseja converter para Farenheit: "))
    F = (C * 1.8) + 32
    print("O Resultado da conversão de {} graus Celsius para Farenheit foi de {} graus Farenheit".format(C,int(F)))