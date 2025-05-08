# Declaração de variáveis
linha = ""
linha_decodificada = ""
letra = ""
numero = ""
contador = 0

# Entrada de dados
quantidade_linhas = int(input())

# Processamento
for i in range(quantidade_linhas):
    linha = input()
    linha_decodificada = ""
    contador = 0

    while contador < len(linha):
        letra = linha[contador]
        contador += 1
        numero = ""

        while contador < len(linha) and linha[contador].isdigit():
            numero += linha[contador]
            contador += 1
        
        linha_decodificada += letra * int(numero)

    # Saída de dados
    print(linha_decodificada)
