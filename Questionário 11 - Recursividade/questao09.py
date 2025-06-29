# Declaração
contagem_chamadas = {} # Dicionário para guardar a contagem de chamadas para cada fibonacci(k).

def fibonacci(k):
    """
    Calcula o k-ésimo termo de Fibonacci e, ao mesmo tempo,
    conta quantas vezes foi chamada para o valor 'k'.
    """
    # A primeira coisa que a função faz é registrar que ela foi chamada
    # para o número 'k', incrementando sua contagem no dicionário.
    contagem_chamadas[k] += 1

    # Casos Base da recursão
    if k == 0:
        return 0
    if k == 1:
        return 1
    
    # chama a si mesma para os dois termos anteriores.
    return fibonacci(k - 1) + fibonacci(k - 2)


# Entrada 
n = int(input())

# Processamento

# Inicializa o dicionário com chaves de 0 a n e valores 0.
for i in range(n + 1):
    contagem_chamadas[i] = 0

# Faz a chamada inicial para calcular o termo e popular o dicionário de contagem.
termo_n = fibonacci(n)

# Saída
print(f"Termo: {termo_n}")
print("Quantidades:")

# Imprime a contagem de chamadas para cada valor de 0 a n.
for i in range(n + 1):
    print(f"fibonacci({i}) - {contagem_chamadas[i]}")