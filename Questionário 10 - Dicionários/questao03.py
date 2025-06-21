# Declaracao
dicionario_catalogo_precos = {}
valor_total = 0.0

# Entrada de dados / Montagem do dicionário do catálogo
str_items_precos = input()

lista_item_precos = str_items_precos.split()# Cria uma lista onde cada item se trata de cada palavra da string

for i in range(0, len(lista_item_precos), 2): # Para pular de 2 em 2, é necessário ajustar o início, o fim e o passo do range. Começa do 0, vai até o fim da lista e, a cada loop, ele anda de 2 em 2 passos.
    nome_produto = lista_item_precos[i]
    preco_produto_str = lista_item_precos[i + 1]
    preco_produto = float(preco_produto_str)

    dicionario_catalogo_precos[nome_produto] = float(preco_produto)

pedido_cliente = input()
lista_pedido_cliente = pedido_cliente.split()

for i in range(0, len(lista_pedido_cliente), 2):
    nome_produto_cliente = lista_pedido_cliente[i]
    quantidade_produto_cliente_str = lista_pedido_cliente[i + 1]
    quantidade_produto_cliente = int(quantidade_produto_cliente_str)
    # Processamento
    preco_unitario = dicionario_catalogo_precos[nome_produto_cliente]
    valor_total += preco_unitario * quantidade_produto_cliente

# Saida de dados
print(f"R$ {valor_total:.2f}")