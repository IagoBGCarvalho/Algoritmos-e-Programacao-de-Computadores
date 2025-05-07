palavra = input()
letra = input()
inicio_busca = int(input())

def find(palavra, letra, inicio_busca):
    indice = inicio_busca
    while indice < len(palavra):
        if palavra[indice].lower() == letra.lower():
            return indice
        indice += 1
    return -1

print(find(palavra, letra, inicio_busca))
