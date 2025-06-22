# Declaracao
dicionario_corredores = {} # Dicionário principal que vai armazenar o número dos corredores como chaves e que recebe outros dicionário com as informações dos produtos como valor
lista_produtos_corredor = []
lista_numero_corredores = []

# Entrada de dados
numero_corredores = input()
numero_corredores_int = int(numero_corredores)

for i in range(1, numero_corredores_int + 1):
    # Loop para criar uma lista com todos os números de corredores existentes
    lista_numero_corredores.append(i)

for i in range(1, numero_corredores_int + 1):
    # Loop para receber a linha com os produtos e preços e para criar uma lista que separa cada produto e preço em um item de uma lista
    produtos_precos = input()
    lista_produtos_precos = produtos_precos.split()

    produtos_deste_corredor = {} # Dicionário temporário para os produtos

    for j in range(0, len(lista_produtos_precos), 2):
        # Loop para armazenar os pares de produtos e precos no dicionário temporário
        produto = lista_produtos_precos[j]
        lista_produtos_corredor.append(produto)
        preco = float(lista_produtos_precos[j + 1])
        produtos_deste_corredor[produto] = preco
    
    dicionario_corredores[i] = produtos_deste_corredor # Está atribuindo o dicionário temporário como valor para cada chave do dicionário principal

numero_corredor_desejado = int(input())

# Processamento e saída
if numero_corredor_desejado not in lista_numero_corredores: # Caso o corredor desejada não exista na lista de corredores existentes...
    print("Esse corredor não existe no mercado.")
else:
    produtos_encontrados = dicionario_corredores[numero_corredor_desejado]

    lista_precos = list(produtos_encontrados.values()) # Cria uma lista de preços utilizando .values() para apenas retornar os valores do dicionário
    preco_medio = sum(lista_precos) / len(lista_precos) # Somatório da lista de preços dividida pelo tamanho dela

    lista_produtos = list(produtos_encontrados.keys()) # Cria uma lista de produtos utilizando .keys() para retornar somente as chaves do dicionário

    produtos_formatados = ", ".join(lista_produtos) # O join junta todos os items da lista de produtos em uma string só, mas utiliza ", " para separar as palavras do jeito que o enunciado pede

    print(f"No corredor {numero_corredor_desejado} encontramos:")
    print(produtos_formatados)
    print(f"E o preço médio é {preco_medio:.2f}.")
