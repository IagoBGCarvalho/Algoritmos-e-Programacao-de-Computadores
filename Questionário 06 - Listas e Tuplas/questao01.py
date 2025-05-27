# Declaração de variáveis
nome = []
todos_os_nomes = []

# Entrada de dados
quantidade_alunos = int(input())

for _ in range(quantidade_alunos):
    nome = input()
    todos_os_nomes.append(nome)

# Processamento
todos_os_nomes.sort(reverse=True)

# Saída de dados
for i in range(quantidade_alunos):
    print(todos_os_nomes[i])