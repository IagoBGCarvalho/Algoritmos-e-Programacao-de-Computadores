# Declaração de variáveis
indices_impares = ""
palavra_sem_espacos = ""

# Entrada de dados
palavra = input()

# Processamento
for i in range(len(palavra)):
    if i % 2 != 0:
        indices_impares += palavra[i]

for i in indices_impares:
    if i != " ":
        palavra_sem_espacos = palavra_sem_espacos + i

# Saída de dados
print(palavra_sem_espacos)