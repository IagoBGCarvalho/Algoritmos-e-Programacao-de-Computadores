def troco(x):
    moedas_valores = [50, 25, 10, 5, 1]
    moedas_nomes = ["50 centavos", "25 centavos", "10 centavos", "cinco centavos", "1 centavo"]

    for i in range(len(moedas_valores)):
        valor_moeda = moedas_valores[i]
        nome_moeda = moedas_nomes[i]

        quantidade = x // valor_moeda 

        if valor_moeda == 50:
            print(f"{quantidade} moedas de 50 centavos")
        elif valor_moeda == 25:
            print(f"{quantidade} moedas de 25 centavos")
        else:
            print(f"{quantidade} moedas de {nome_moeda}")

        x = x % valor_moeda
