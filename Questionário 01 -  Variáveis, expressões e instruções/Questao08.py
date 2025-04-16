# Entrada de dados
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

sequencia1 = input()
sequencia2 = input()

# Processamento
primeiro_resultado = (sequencia1 * (numero1 + numero2))
segundo_resultado = (sequencia2 * (numero2 + numero3))
terceiro_resultado = (primeiro_resultado + segundo_resultado)
ultimo_resultado = (terceiro_resultado * (numero1 + numero3))

# Saída de dados
print(ultimo_resultado)