# Declaração de variáveis
lista1 = []
lista2 = []
list_tuple = []
medias = []

# Entrada de dados
for _ in range(5):
    numero = int(input())
    lista1.append(numero)

for _ in range(5):
    numero = int(input())
    lista2.append(numero)

# Processamento
list_tuple = list(zip(lista1, lista2))

#  Saída da Lista de Tuplas
print(list_tuple)

for tupla in list_tuple:
    soma_elementos_tupla = tupla[0] + tupla[1]
    media_elementos_tupla = soma_elementos_tupla / 2.0 
    medias.append(media_elementos_tupla)

# Saída da Lista de Médias
print(medias)