# Declaracao de variaveis
lista_final = []

# Entrada de dados
sequencia_de_numeros = input().split()
numero_n = int(input())

# Processamento
lista_de_numeros = [int(numero) for numero in sequencia_de_numeros] # Converte a sequência de números em uma lista de inteiros

for i in lista_de_numeros:
    if i % numero_n == 0:
        lista_final.append(i)

# Saida de dados
print(*lista_final)