def tem_letra_maiúscula(s):
    for letra in s:
        if letra in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            return True
            
    return False