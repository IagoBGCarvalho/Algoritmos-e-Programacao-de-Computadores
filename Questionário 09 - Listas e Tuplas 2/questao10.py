# Entrada (Parte 1: Lendo a LISTA DE COMPRAS de Seu Januário - CORRIGIDO)
try:
    n = int(input()) # Quantidade de itens na lista de compras
except (ValueError, EOFError):
    n = 0

lista_de_compras = {} # Dicionário para a lista de compras
for _ in range(n):
    produto, quantidade_str = input().split()
    lista_de_compras[produto] = int(quantidade_str)


# Entrada (Parte 2: Lendo o CATÁLOGO da feira - CORRIGIDO)
try:
    m = int(input()) # Quantidade de itens no catálogo
except (ValueError, EOFError):
    m = 0

catalogo_feira = {} # Dicionário para guardar os produtos e seus preços
for _ in range(m):
    produto, preco_str = input().split()
    catalogo_feira[produto] = float(preco_str)


# Processamento e Saída (Esta parte já estava correta)
valor_total = 0.0

# Percorremos cada item na lista de compras do Seu Januário
for produto, quantidade in lista_de_compras.items():
    
    # Verificamos se o produto da lista de compras existe no catálogo da feira
    if produto in catalogo_feira:
        # Se existir, calculamos o custo e somamos ao total
        preco_unitario = catalogo_feira[produto]
        valor_total += preco_unitario * quantidade
    else:
        # Se não existir, imprimimos a mensagem de erro
        print(f"{produto} esta em falta")

# Ao final, imprimimos o valor total da compra formatado
print(f"{valor_total:.2f}")