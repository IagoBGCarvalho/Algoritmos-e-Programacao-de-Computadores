# Entrada
# Lê N e M, e os converte para inteiros
N, M = [int(i) for i in input().split()]

# Lê a quantidade de projéteis
Q = int(input())

# Cria uma lista para guardar as coordenadas dos projéteis
projeteis = []
for _ in range(Q):
    # Lê as coordenadas, converte para inteiros e adiciona à lista
    coordenadas = [int(i) for i in input().split()]
    projeteis.append(coordenadas)

# Processamento

# 1. Cria a matriz (terreno) N por M, toda preenchida com zeros.
terreno = [[0 for _ in range(M)] for _ in range(N)]

# 2. Simula o lançamento de cada projétil
for x, y in projeteis:
    # Converte as coordenadas (base 1) para índices da lista (base 0)
    linha_idx = x - 1
    coluna_idx = y - 1

    # Adiciona 1 a todas as células da linha afetada
    for j in range(M):
        terreno[linha_idx][j] += 1
    
    # Adiciona 1 a todas as células da coluna afetada
    for i in range(N):
        terreno[i][coluna_idx] += 1
        
    # Como a célula (x,y) foi somada duas vezes, subtraímos 1 para corrigir.
    terreno[linha_idx][coluna_idx] -= 1


# 3. Encontra a maior profundidade e conta suas ocorrências
profundidade_maxima = 0
contagem_maxima = 0

# Primeiro, percorre a matriz para encontrar o valor máximo
for linha in terreno:
    for profundidade_celula in linha:
        if profundidade_celula > profundidade_maxima:
            profundidade_maxima = profundidade_celula

# Agora, percorre a matriz novamente para contar quantas células têm essa profundidade máxima
for linha in terreno:
    for profundidade_celula in linha:
        if profundidade_celula == profundidade_maxima:
            contagem_maxima += 1

# Saída
print(contagem_maxima)