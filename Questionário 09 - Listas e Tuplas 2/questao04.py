# Entrada
N = int(input())

matriz = [] # Cria uma lista vazia para guardar a matriz

for _ in range(N):
    # Lê a linha, divide os caracteres pelo espaço e adiciona à matriz
    linha_de_caracteres = input().split()
    matriz.append(linha_de_caracteres)

# Processamento
eh_valido = True # "Flag" que começa como Verdadeira. Se encontrarmos qualquer erro, ela vira Falsa.

for linha in range(N):
    # Loop duplo para percorrer cada célula da matriz [linha][coluna]
    for coluna in range(N):
        # Pega o caractere na posição atual
        caractere_atual = matriz[linha][coluna]

        # Verifica se a posição atual está em uma das diagonais
        esta_na_diagonal = (linha == coluna) or (linha + coluna == N - 1)

        if esta_na_diagonal:
            # Se ESTÁ na diagonal, o caractere PRECISA ser 'X'.
            # Se não for, o Poneglifo é inválido.
            if caractere_atual != 'X':
                eh_valido = False
        else:
            # Se NÃO ESTÁ na diagonal, o caractere NÃO PODE ser 'X'.
            # Se for, o Poneglifo é inválido.
            if caractere_atual == 'X':
                eh_valido = False
        
        # Se em algum momento a flag se tornar falsa, podemos parar de checar
        if not eh_valido:
            break
    if not eh_valido:
        break

# Saída
if eh_valido:
    print("O one piece eh real!")
else:
    print("Talvez o tesouro seja os amigos que fizemos no caminho")