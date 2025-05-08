# Declaração de variáveis
contador_diferencas = 0

# Entrada de dados
frase = input()
tamanho = len(frase)

# Processamento
for i in range(tamanho // 2):
    if frase[i] != frase[-i - 1]:
        contador_diferencas += 1

# Saída de dados 
if contador_diferencas == 1:
    print("ON")
elif contador_diferencas == 0:
    if tamanho % 2 == 1:
        print("ON")
    else:
        print("OFF")
else:
    print("OFF")