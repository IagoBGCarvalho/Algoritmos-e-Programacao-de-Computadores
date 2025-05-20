import math

# Entrada de dados
x1 = int(input()) # Carêncio
y1 = int(input())
x2 = int(input()) # Outra pessoa
y2 = int(input())

# Processamento
distancia = math.sqrt((x2 -x1) ** 2 + (y2 - y1) ** 2)

# Saída de dados
if distancia <= 100:
    print("É o amor da minha vida!")
elif distancia > 100 and distancia <= 200:
    print("Talvez dê certo")
else:
    print("Não vale a pena investir")