# Declaração de variáveis
dinheiro_total = 0

# Entrada de dados
quantidade_amigos, preco_ingresso = input().split()
quantidade_amigos, preco_ingresso = int(quantidade_amigos), int(preco_ingresso)

for i in range(quantidade_amigos):
    dinheiro = int(input())
    dinheiro_total += dinheiro

# Processamento
media = dinheiro_total // quantidade_amigos

# Saída de dados
print(f"media: {media}")
if media >= preco_ingresso:
    print("o rock reinara mais uma vez")
else:
    print("rockeiros trabalhando ja")