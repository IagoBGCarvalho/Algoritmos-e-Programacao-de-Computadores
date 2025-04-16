# Entrada de dados
primeira_onomatopeia, segunda_onomatopeia, terceira_onomatopeia = input().split()

# Processamento
onomatopeia_final = (primeira_onomatopeia + (segunda_onomatopeia * 3) + (terceira_onomatopeia * 2))

# Saída de dados
print(onomatopeia_final)