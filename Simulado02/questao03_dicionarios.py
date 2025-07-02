def corrigirFrase(frase):
    dicionario_correcoes = {"9":"p","6":"b","5":"s","7":"t","0":"o","1":"i"}
    frase_corrigida_lista = []
    frase_final = ""

    for i in frase:
        if i in dicionario_correcoes:
            frase_corrigida_lista += dicionario_correcoes[i]
        else:
            frase_corrigida_lista += i
    
    frase_corrigida = "".join(frase_corrigida_lista)

    frase_corrigida_minuscula = frase_corrigida.lower()

    frase_corrigida_maiuscula = frase_corrigida_minuscula.capitalize()

    if frase_corrigida_maiuscula[-1] != ".":
        frase_final = frase_corrigida_maiuscula[:] + "."

    return frase_final

frase_maurinho = input()
print(corrigirFrase(frase_maurinho))