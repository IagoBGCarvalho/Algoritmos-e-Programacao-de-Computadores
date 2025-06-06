def pode_ser_palindromo(p):
    palindromo_contrario = ""
    palindromo_sem_espacos = ""
    for i in p:
        if i != " ":
            palindromo_sem_espacos = palindromo_sem_espacos + i # Está tirando os espaços em branco

    for i in range(len(palindromo_sem_espacos)):
        palindromo_contrario += palindromo_sem_espacos[-1 - i] # Está invertendo a frase

    if palindromo_contrario == palindromo_sem_espacos:
        print("ON")
    else:
        print("OFF")

palindromo = input()
pode_ser_palindromo(palindromo)