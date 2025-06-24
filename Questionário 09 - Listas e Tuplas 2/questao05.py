# Entrada
n = int(input())
t = int(input())

lista_de_listas = []

# Loop para ler as 'n' listas de inteiros
for _ in range(n):
    # Lê a linha, divide em strings, e converte cada uma para inteiro
    sublista = [int(numero) for numero in input().split()]
    lista_de_listas.append(sublista)

# Processamento
# Usamos a função sorted() com uma chave (key) customizada via lambda.
# Para cada 'sublista' em 'lista_de_listas', a chave de ordenação será a tupla (sublista[t], sum(sublista)).
listas_ordenadas = sorted(lista_de_listas, key=lambda sublista: (sublista[t], sum(sublista)))

# Saída
# Percorremos a lista já ordenada
for sublista in listas_ordenadas:
    # Para imprimir os números separados por espaço, primeiro os convertemos
    # de volta para string e depois usamos o método .join().
    lista_de_strings = [str(numero) for numero in sublista]
    linha_para_imprimir = " ".join(lista_de_strings)
    print(linha_para_imprimir)