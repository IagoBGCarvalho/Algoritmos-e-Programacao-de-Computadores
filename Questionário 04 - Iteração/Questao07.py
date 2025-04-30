# Entrada de dados
numero = int(input())

# Saída de dados
for i in range(numero + 1):
    if i % 3 == 0 and i % 7 == 0:
        print(i, end=" ")
