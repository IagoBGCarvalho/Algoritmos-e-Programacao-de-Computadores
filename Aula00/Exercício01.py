# Declaração de variáveis
Numero = 0
Sucessor = 0
Antecessor = 0
Contador = 0

# Entrada de dados
while (Contador == 0):
    Numero = int(input("Digite um número: "))
    Sucessor = (Numero + 1)
    Antecessor = (Numero - 1)
    # Saída de dados
    print(f"Número: {Numero} Sucessorr: {Sucessor} Antecessor: {Antecessor}")
    Contador = input(f"Desejar repetir? Digite <S> para SIM e <N> para NÃO: ")
    
    if (Contador == "S"):
        Contador = 1