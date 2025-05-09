# Declaração de variáveis
valor_pizza_grande = 60.00
valor_final = 0.00
acrescimo_embalagem = 0.00

# Entrada de dados
forma_consumo, quantidade = input().split()
quantidade = int(quantidade)

# Processamento
if quantidade >= 3:
    valor_pizza_grande = 50.00

if forma_consumo == "leva":
    acrescimo_embalagem = 5.00 * quantidade

valor_final = valor_pizza_grande * quantidade + acrescimo_embalagem

# Saída de dados
print(f"{valor_final:.2f}")