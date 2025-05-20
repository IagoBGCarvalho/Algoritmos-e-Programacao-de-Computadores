# Declaração de variáveis
maior_salario = 0.00
menor_salario = 1000000000.00
media_salarial = 0.00
salario_total = 0.00
maior_assalariado = ""
menor_assalariado = ""

# Entrada de dados
quantidade = int(input())

# Processamento
for i in range(quantidade):
    nome_colaborador, salario_colaborador = input().split(",")
    salario_colaborador = float(salario_colaborador)

    salario_total += salario_colaborador

    if (salario_colaborador > maior_salario):
        maior_salario = salario_colaborador
        maior_assalariado = nome_colaborador

    if (salario_colaborador < menor_salario):
        menor_salario = salario_colaborador
        menor_assalariado = nome_colaborador

# Saída de dados
if quantidade > 0:
    media_salarial = salario_total / quantidade
    print(f"{media_salarial:.2f}")
else:
    print("Não tem média")

if (maior_assalariado != ""):
    print(f"{maior_assalariado} {maior_salario:.2f}")
else:
    print("Não tem")

if (menor_assalariado != ""):
    print(f"{menor_assalariado} {menor_salario:.2f}")
else:
    print("Não tem")