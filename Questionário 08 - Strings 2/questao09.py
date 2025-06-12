def cifra_de_cesar():

    operacao = int(input())
    deslocamento = int(input())
    mensagem = input()

    mensagem_final = ""
    VALOR_A = ord('A')

    for caractere in mensagem:
        if caractere == ' ':
            mensagem_final += ' '
            continue

        valor_letra = ord(caractere) - VALOR_A

        if operacao == 1:
            novo_valor = (valor_letra + deslocamento) % 26
        else:
            novo_valor = (valor_letra - deslocamento) % 26


        nova_letra = chr(novo_valor + VALOR_A)

        mensagem_final += nova_letra

    print(mensagem_final)

cifra_de_cesar()