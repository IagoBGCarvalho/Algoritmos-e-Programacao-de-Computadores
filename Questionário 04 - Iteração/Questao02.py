# Declaração de variáveis
quantidade = 0
salario_total = 0.00
salario_medio = 0.00

# Entrada de dados e processamento
while True:
    nome_colaborador, salario_colaborador = input().split(",")
    if nome_colaborador == "Fim":
        break
    salario_colaborador = float(salario_colaborador)
    quantidade += 1
    salario_total += salario_colaborador
    salario_medio = salario_total / quantidade

# Saída de dados
print(f"{salario_medio:.2f}")