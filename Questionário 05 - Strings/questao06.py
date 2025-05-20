# Declaração de variáveis
frase_censurada = ""

# Entrada de dados
tweet = input()
censura = input()

# Processamento
if censura in tweet:
    frase_censurada = tweet.replace(censura, "*")
    print(frase_censurada)
else:
    print("tudo certo :)")