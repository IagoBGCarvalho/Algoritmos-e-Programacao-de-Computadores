# Declaração de variáveis
nome = ""
nome_final = ""
nota = 0.0
nota_final = 0.0

# Entrada de dados
quantidade_alunos = input()
quantidade_alunos = int(quantidade_alunos)

# Processamento
for i in range(quantidade_alunos):
    nome, nota = input().split()
    nota = float(nota)
    if nota > nota_final:
        nota_final = nota
        nome_final = nome

# Saída de dados
print(nome_final)