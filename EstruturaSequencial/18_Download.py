# 18 Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps),
#  calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = int(input("Digite o tamanho do arquivo que você irá baixar (Em MegaBytes): "))
velocidade = int(input("Digite a velocidade de download da sua internet (Em MegaBytes/Segundo): "))
tempob = tamanho / velocidade
tempo = tempob // 60
tempos = tempob % 60
print("Para baixar este arquivo de {} MB a uma velocidade de {} MB/S você ira levar {} minutos e {} segundos".format(tamanho,velocidade,int(tempo),int(tempos)))
