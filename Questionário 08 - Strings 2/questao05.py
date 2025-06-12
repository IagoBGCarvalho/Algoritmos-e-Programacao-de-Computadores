def split_mais_poderoso(string):
    letras = "ABCÇDEFGHIJKLMNOPQRSTUVWXYZabcçdefghijklmnopqrstuvwxyz"
    
    palavra_atual = ""

    for caractere in string:
        if caractere in letras:
            palavra_atual += caractere
        else:
            if palavra_atual != "":
                print(palavra_atual)
            
            palavra_atual = ""

    if palavra_atual != "":
        print(palavra_atual)

frase_de_entrada = input()
split_mais_poderoso(frase_de_entrada)