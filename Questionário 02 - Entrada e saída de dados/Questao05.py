# Entrada de dados
data = input().split("/")

# Processamento de dados
dia = (data[0])
mes = (data[1])
ano = (data[2])

# Saída de dados
print(f"{dia}-{mes}-{ano}")
print(f"{mes}-{dia}-{ano}")
print(f"{ano}/{mes}/{dia}")