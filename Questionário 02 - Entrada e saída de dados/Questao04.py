# Entrada de dados
horario = input().split(":")

# Processamento de dados
horas = int(horario[0]) # Colocando a substring de índice 0 em uma variável inteira
minutos = int(horario[1])
segundos = int(horario[2])

total_segundos = (horas * 3600) + (minutos * 60) + segundos # Somando os segundos de cada variável

# Saída de dados
print(f"La se foram {total_segundos} segundos que nao voltam mais...")