def imprimeTermos(n):
    # Função recursiva que imprime os termos de uma sequência começando em n e decrescendo de 2 em 2, terminando em 0.
    if n < 0:
        # Se n for menor que zero, a recursão para.
        return
    
    print(n)

    if n > 1:
        "Se n for maior do que um, chama a função recursiva que faz n - 2"
        imprimeTermos(n-2)

    if n == 1:
        "Se n for 1, imprime o xero final."
        print(0)