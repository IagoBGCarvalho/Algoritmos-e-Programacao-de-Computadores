# Declaração de variáveis
maior_salario = 0.00

# Entrada e processamento
while True:
    nome_colaborador, salario_colaborador = input().split(",")
    if nome_colaborador == "Fim":
        break

    salario_colaborador = float(salario_colaborador)

    if salario_colaborador > maior_salario:
        maior_salario = salario_colaborador

# Saída de dados
if maior_salario != 0.00:
    print(f"{maior_salario:.2f}")
else:
    print("Não tem")