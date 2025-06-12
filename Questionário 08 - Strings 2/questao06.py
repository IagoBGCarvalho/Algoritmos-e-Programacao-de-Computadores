def validar_senha(senha):
    if not (6 <= len(senha) <= 32):
        print("Senha invalida.")
        return 
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:
        if not caractere.isalnum():
            print("Senha invalida.")
            return
        
        if caractere.islower():
            tem_minuscula = True
        elif caractere.isupper():
            tem_maiuscula = True
        elif caractere.isdigit():
            tem_numero = True

    if tem_maiuscula and tem_minuscula and tem_numero:
        print("Senha valida.")
    else:
        print("Senha invalida.")

senha_para_verificar = input()
validar_senha(senha_para_verificar)