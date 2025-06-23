def convert(lista_de_tuplas):
    """
    Converte uma lista de tuplas (chave, valor) em um dicionário,
    agrupando os valores de chaves iguais em uma lista.
    """
    
    dicionario_agrupado = {} # Dicionário vazio para guardar o resultado.

    for chave, valor in lista_de_tuplas:
        # Percorre cada tupla na lista de entrada.
        # Desempacota a tupla diretamente em 'chave' e 'valor' para facilitar.
        
        if chave in dicionario_agrupado:
            # Verifica se a 'chave' já existe no dicionário
            # Se SIM: a chave já existe. Pega a lista de valores
            # que já está lá e adiciona o novo valor a ela.
            dicionario_agrupado[chave].append(valor)
        else:
            # Se NÃO:
            # Cria a entrada para esta chave e atribui a ela uma
            # nova lista contendo o 'valor' atual como seu primeiro item.
            dicionario_agrupado[chave] = [valor]
            
    return dicionario_agrupado # Retorna o dicionário por completo