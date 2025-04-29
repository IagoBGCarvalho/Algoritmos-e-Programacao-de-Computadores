raiz_aproximada = 0

# Entrada de dados
numero = int(input())
aproximacao = int(input())

# Processamento
while True:
    print(aproximacao)

    raiz_aproximada = (((2 * aproximacao ** 3) + numero) / (3 * aproximacao ** 2))

    if raiz_aproximada == aproximacao: # pode continuar por muito tempo
        break

    aproximacao = raiz_aproximada