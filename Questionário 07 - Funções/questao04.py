def nota(n):
    lista_nota = ["|"]
    
    for i in range(n):
        lista_nota += "★"

    for i in range (10 - n):
        lista_nota += "☆"

    lista_nota += "|"

    print("".join(lista_nota)) # Une todos os elementos da lista em uma única strings. o "" indica o separador, ou seja, nada.