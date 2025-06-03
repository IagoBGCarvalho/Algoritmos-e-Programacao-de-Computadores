def stockmarket(lista_de_blocos_de_acoes):
    valores_por_data = {}

    for bloco_de_acao in lista_de_blocos_de_acoes:
        data_de_compra = bloco_de_acao[0]
        preco_de_compra = bloco_de_acao[1]
        numero_de_acoes = bloco_de_acao[2]
        valor_gasto_nesta_compra = preco_de_compra * numero_de_acoes

        if data_de_compra in valores_por_data:
            valores_por_data[data_de_compra] += valor_gasto_nesta_compra
        else:
            valores_por_data[data_de_compra] = valor_gasto_nesta_compra
            
    return valores_por_data