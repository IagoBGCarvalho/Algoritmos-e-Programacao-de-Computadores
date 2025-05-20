palavra = input()
letra = input()
contador = 0

def contador(palavra, letra):
    contador = 0
    for i in palavra:
        if i == letra:
            contador += 1
    return contador

print(contador(palavra, letra))
