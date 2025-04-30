# Declaração de variáveis
anos = 0

# Entrada de dados
populacaoA, populacaoB, crescimentoA, crescimentoB = input().split()

populacaoA = int(populacaoA)
populacaoB = int(populacaoB)
crescimentoA = float(crescimentoA)
crescimentoB = float(crescimentoB)

# Processamento e saída
if crescimentoA <= crescimentoB and populacaoA < populacaoB:
    print("A nunca alcancara B.")
else:
    while populacaoA < populacaoB:
        populacaoA = int(populacaoA * (1 + crescimentoA / 100))
        populacaoB = int(populacaoB * (1 + crescimentoB / 100))
        anos += 1

        if anos > 1000:
            print("Mais de um milenio.")
            break

    if anos <= 1000 and populacaoA >= populacaoB:
        print(f"Vai alcancar em {anos} ano(s).")