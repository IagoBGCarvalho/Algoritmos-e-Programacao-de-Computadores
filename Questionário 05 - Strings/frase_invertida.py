frase = input("Escreva uma frase: ")
esarf = ""

for i in range(len(frase)):
    esarf += frase[-1 - i]

print(f"Frase invertida: {esarf}")
print(f"frase cortada: {frase[0:4]}")
print(frase[::-1]) # : -> fateamento da frase todaa, ::-1 -> Frase toda ao contrário
# Fatiamento = de onde começa : até onde vai : como vai (-1 = de trás pra frente)