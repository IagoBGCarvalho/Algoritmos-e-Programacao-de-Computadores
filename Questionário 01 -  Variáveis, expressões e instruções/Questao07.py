# Entrada de dados
nota1, nota2, nota3 = input().split()

nota1_float = float(nota1)
nota2_float = float(nota2)
nota3_float = float(nota3)

peso1, peso2, peso3 = input().split()

peso1_int = int(peso1)
peso2_int = int(peso2)
peso3_int = int(peso3)

# Processamento
media = (nota1_float * peso1_int + nota2_float * peso2_int + nota3_float * peso3_int) / (peso1_int + peso2_int + peso3_int)

# Saída de dados
print(f'{media:.6f}')