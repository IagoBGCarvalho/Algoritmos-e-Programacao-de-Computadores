# Declaração de variáveis
peso1 = 3.5
peso2 = 7.5
soma_pesos = (peso1 + peso2)

# Entrada de dados
valor1 = float(input())
valor2 = float(input())

valor1_peso = (valor1 * peso1)
valor2_peso = (valor2 * peso2)

# Processamento
media_ponderada = ((valor1_peso + valor2_peso) / soma_pesos)

# Saída de dados
print(f"MEDIA = {media_ponderada:.5f}")