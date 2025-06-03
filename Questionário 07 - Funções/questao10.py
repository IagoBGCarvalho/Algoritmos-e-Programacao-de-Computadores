def paron(lista_de_palavras):
    vogais = "aeiou"
    palavras_filtradas = []

    for palavra in lista_de_palavras:
        contador_vogais = 0

        for letra in palavra:
            if letra.lower() in vogais:
                contador_vogais += 1
        
        if contador_vogais % 2 == 0:
            palavras_filtradas.append(palavra)

    return palavras_filtradas
