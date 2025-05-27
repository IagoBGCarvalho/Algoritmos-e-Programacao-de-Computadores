# Declaração de variáveis
nome_professor = "Raimundo Nonato"

# Entrada de dados
quantidade_periodos = int(input())

# Processamento
for i in range(quantidade_periodos):
    periodo = input()

    frase_final = nome_professor + " " + periodo
    
    # Saída de dados
    print(frase_final)