def split_mais_poderoso(string):
    string_final = ""
    letras = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    flag = True
    lista_string = list(string)
    lista_string_bkp = lista_string[:]
    tamanho = len(string)

    for i in range(tamanho):
        item = lista_string_bkp[i]
        
        if item in letras:
            string_final += item
