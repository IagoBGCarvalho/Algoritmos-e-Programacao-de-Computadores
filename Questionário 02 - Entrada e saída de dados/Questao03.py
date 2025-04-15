# Entrada de dados
sabores = input().split() # Separa a string em uma lista de sub-strings
sabores_str = (f"{sabores[0]}, {sabores[1]} e {sabores[2]}") # o [] se refere ao índice da lista (gerada pelo split) vai de 0 a n
cobertura = input().split(",") # Especifica o que será considerado como separador
cobertura_str = (f"{cobertura[0]} e {cobertura[1]}")
calda = input()

# Saída de dados
print(f"Sorvete de {sabores_str} com coberturas de {cobertura_str} e calda de {calda}!")
print(f"Não esqueça a banana!")