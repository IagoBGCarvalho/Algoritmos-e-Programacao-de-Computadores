def corretor_frase(frase):
    """Esta função buscar corrigir os erros presentes em uma frase. Primeiro trasnforma todos os caracteres em minúsculos, troca os números pelos caracteres corretos, trasnforma a primeia letra em maiúscula e adiciona um ponto final."""
    frase_minuscula = frase.lower()
    lista_frase = list(frase_minuscula)
    lista_frase_bkp = lista_frase[:]
    tamanho = len(lista_frase_bkp)

    for i in range(tamanho):
        item = lista_frase_bkp[i]

        if item == "9":
            lista_frase_bkp[i] = "p"
        elif item == "6":
            lista_frase_bkp[i] = "b"
        elif item == "5":
            lista_frase_bkp[i] = "s"
        elif item == "7":
            lista_frase_bkp[i] = "t"
        elif item == "0":
            lista_frase_bkp[i] = "o"
        elif item == "1":
            lista_frase_bkp[i] = "i"

    lista_frase_bkp[0] = lista_frase_bkp[0].upper()
    
    if lista_frase_bkp[-1] != ".":
        lista_frase_bkp.append(".")

    frase_corrigida = "".join(lista_frase_bkp)
    print(frase_corrigida)

frase_maurinho = input()
corretor_frase(frase_maurinho)