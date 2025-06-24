# Entrada
# Lê N, M e K
N, M, K = [int(i) for i in input().split()]

# A linha com a quantidade de produtos em cada loja não é estritamente necessária,
# pois podemos ler as linhas de preços diretamente.
input() 

# Lista que vai guardar as listas de preços de cada loja
lojas = []
# Loop para ler os produtos de cada uma das N lojas
for _ in range(N):
    # Lê a linha de preços, converte para inteiros e já ordena em ordem crescente
    precos_da_loja = sorted([int(p) for p in input().split()])
    lojas.append(precos_da_loja)

# Processamento
# Flag para controlar se a simulação falhou em algum momento
foi_possivel_comprar_tudo = True

# O loop de fora representa as 'K' rodadas de compra
for rodada in range(K):
    # O loop de dentro representa a visita a cada uma das 'N' lojas na rodada
    for i_loja in range(N):
        
        # VERIFICAÇÃO 1: A loja ainda tem produtos para vender?
        if not lojas[i_loja]: # Se a lista de preços da loja está vazia
            foi_possivel_comprar_tudo = False
            break # Para o loop das lojas

        # Pega o preço do produto mais barato (o primeiro da lista ordenada)
        preco_mais_barato = lojas[i_loja][0]

        # VERIFICAÇÃO 2: Heverton tem dinheiro para comprar?
        if M >= preco_mais_barato:
            # Se sim, a compra é efetuada
            M -= preco_mais_barato       # Subtrai o valor do dinheiro
            lojas[i_loja].pop(0)         # Remove o item comprado da loja
        else:
            # Se não, a compra falha
            foi_possivel_comprar_tudo = False
            break # Para o loop das lojas
    
    # Se a compra já falhou na rodada atual, não adianta começar a próxima
    if not foi_possivel_comprar_tudo:
        break # Para o loop das rodadas

# Saída
# No final, verificamos o estado da nossa flag
if foi_possivel_comprar_tudo:
    print("Sim")
else:
    print("Nao")