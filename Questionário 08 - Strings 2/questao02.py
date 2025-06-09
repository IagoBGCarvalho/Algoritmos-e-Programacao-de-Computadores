def pode_ser_palindromo(s):
    comprimento = len(s)
    diferencas = 0

    for i in range(comprimento // 2):
        if s[i] != s[comprimento - 1 - i]:
            diferencas += 1

    if diferencas == 1:
        print("ON")
    elif diferencas == 0:
        if comprimento % 2 == 1:
            print("ON")
        else:
            print("OFF")
    else:
        print("OFF")

palindromo = input()
pode_ser_palindromo(palindromo)