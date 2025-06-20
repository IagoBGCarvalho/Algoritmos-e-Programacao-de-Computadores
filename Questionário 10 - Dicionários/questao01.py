# Declaracao de variaveis
d_v_t = {'d':0, 'v':0, 't':0} # Inicializa um dicionário com as chaves mas sem os valores

# Entrada de dados
frase_input = input()

# Processamento
frase_minuscula = frase_input.lower() # É necessário transformar tudo em minúsculo para contabilizar os ds vs e ts minúsculos

for letra in frase_minuscula:
    if letra in d_v_t:
        d_v_t[letra] += 1 # Altera o 0 no dicionária para o número de ocorrências da letra

# Saida de dados
chaves_ordenadas = sorted(d_v_t.keys()) # Está ordenando as chaves do dicionário de forma alfabética

for chave in chaves_ordenadas:
    valor = d_v_t[chave]
    if valor > 0: # Apenas printa a chave se o valor for diferente de 0
        print(f"{chave} {valor}")