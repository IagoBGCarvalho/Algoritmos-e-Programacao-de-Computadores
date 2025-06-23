def erase(l):
    """
    Recebe uma lista de tuplas e retorna uma nova lista sem as tuplas vazias.
    """
    
    lista_filtrada = [] # Cria uma nova lista vazia para guardar o resultado.

    for tupla_atual in l: # Percorre cada tupla na lista de entrada 'l'.
        
        if tupla_atual: # Verifica se a tupla atual não é vazia.
            lista_filtrada.append(tupla_atual) # Se não for vazia, adiciona à nossa nova lista.
            
    return lista_filtrada # A função retorna a lista final para quem a chamou.