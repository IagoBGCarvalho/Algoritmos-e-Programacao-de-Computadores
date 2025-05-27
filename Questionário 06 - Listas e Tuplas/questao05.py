# Entrada de dados
lista_numeros_str = input().split()
fatiamento_str = input().split()

# Processamento
lista_numeros_int = [int(numero_str) for numero_str in lista_numeros_str]

fatiamento_int = [int(idx_str) for idx_str in fatiamento_str]

indice_inicial = fatiamento_int[0]
indice_final = fatiamento_int[1] 

lista_fatiada = lista_numeros_int[indice_inicial:indice_final]

# Saída de dados
print(lista_fatiada)