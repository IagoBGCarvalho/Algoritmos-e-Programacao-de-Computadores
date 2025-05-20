# Entrada de dados
sabor_bolo, quantidade_pedacos = input().split() # split separa os dados em várias variáveis

# Processamento
quantidade_pedacos = int(quantidade_pedacos) # converte a string em inteiro
valor_final = (quantidade_pedacos * 3.25)

# Saída de dados
print(f"Foram {quantidade_pedacos} pedaços de bolo de {sabor_bolo}, então fica {valor_final:.2f} reais")