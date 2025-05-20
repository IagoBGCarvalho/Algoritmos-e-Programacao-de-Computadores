# Entrada de dados
nota1, nota2, nota3 = input().split()

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

tipo_media = input()

if tipo_media == "P":
    peso1, peso2, peso3 = input().split()
    peso1 = float(peso1)
    peso2 = float(peso2)
    peso3 = float(peso3)

# Processamento
if tipo_media == "A":
    media = (nota1 + nota2 + nota3) / 3
elif tipo_media == "P":
    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
elif tipo_media == "H":
    media = 3 / (1/nota1 + 1/nota2 + 1/nota3)
else:
    print("Operacao inexistente")

# Saída de dados
if tipo_media == "A":
    print("Aritmetica")
    print(f"{media:.2f}")
elif tipo_media == "P":
    print("Ponderada")
    print(f"{media:.2f}")
elif  tipo_media == "H":
    print("Harmonica")
    print(f"{media:.2f}")
