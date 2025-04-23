# Declaração de variáveis
pergunta1 = "O programa funciona?"
pergunta2 = "Você entende o que fez?"
pergunta3 = "Você sabe onde está o erro?"
pergunta4 = "Acha que pode solucionar sozinho?"
pergunta5 = "Já pesquisou no Google?"
pergunta6 = 'Já foi na tutoria?'

# Entrada e saída de dados
print(pergunta1)
resposta1 = input()

if resposta1 == "SIM":
    print(pergunta2)
    resposta2 = input()
    if resposta2 == "SIM":
        print("Ótimo. Então não mexe!")
    else:
        print(pergunta6)
        resposta3 = input()
        if resposta3 == "SIM":
            print("Choremos!")
        else:
            print("Temos um time a disposição!")
else:
    print(pergunta3)
    resposta4 = input()
    if resposta4 == "SIM":
        print(pergunta4)
        resposta5 = input()
        if resposta5 == "SIM":
            print("Então mão na massa!")
        else:
            print(pergunta5)
            resposta6 = input()
            if resposta6 == "SIM":
                print(pergunta6)
                resposta7 = input()
                if resposta7 == "SIM":
                    print("Choremos!")
                else:
                    print("Temos um time a disposição!")
            else:
                print("Corre lá então!")
    else:
        print(pergunta6)
        resposta8 = input()
        if resposta8 == "SIM":
            print("Choremos!")
        else:
            print("Temos um time a disposição!")