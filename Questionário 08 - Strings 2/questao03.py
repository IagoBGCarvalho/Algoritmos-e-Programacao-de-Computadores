def nao_possui_a_letra_u(palavra):
    """Esta função retorna False caso a letra "u" esteja na string "palavra" e True caso não tenha."""
    palavra_minuscula = palavra.lower()
    for letra in palavra_minuscula:
        if letra == 'u' or letra == 'ú' or letra == 'ü' or letra == "ù":
            return False
    return True