# Declaração de variáveis
contador = 0
letras = "0123456789"

# Entrada de dados
palavra = input()

# Processamento
for i in palavra:
    if i in letras:
        contador += 1

# Saída de dados
print(contador)