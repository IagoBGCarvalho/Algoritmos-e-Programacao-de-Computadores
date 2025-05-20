# Declaração de variáveis
menor_salario = 999999999.99
menor_assalariado = ""

# Entrada e processamento
while True:
    nome_colaborador, salario_colaborador = input().split(",")
    salario_colaborador = float(salario_colaborador)
    
    if nome_colaborador == "Fim":
        break

    if salario_colaborador < menor_salario and salario_colaborador != 0.00:
        menor_salario = salario_colaborador
        menor_assalariado = nome_colaborador

# Saída de dados
if menor_assalariado != "":
    print(menor_assalariado)
else:
    print("Não tem")
