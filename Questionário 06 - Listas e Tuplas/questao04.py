# Declaração de variáveis
somatorio = 0.0  # Usaremos esta variável como nosso "acumulador"

# Entrada de dados
lista_de_strings_numeros = input().split() # Ex: ['1', '2', '3', '4']

# Processamento
numeros_int = [int(texto_numero) for texto_numero in lista_de_strings_numeros]

if len(numeros_int) >= 2:
    primeiro_numero = float(numeros_int[0])
    segundo_numero = float(numeros_int[1])

    somatorio = (primeiro_numero * 2.0) + (segundo_numero * 0.5)

    for i in range(2, len(numeros_int)):
        proximo_numero = float(numeros_int[i])
        somatorio = (somatorio * 2.0) + (proximo_numero * 0.5)

# Saída de dados
print(f"{somatorio:.2f}")