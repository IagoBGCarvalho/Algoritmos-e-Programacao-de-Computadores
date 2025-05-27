# Declaração de variáveis
todos_os_jogadores = []

# Entrada de dados
quantidade_jogadores = int(input())

for _ in range(quantidade_jogadores):
    username_atual = input()
    todos_os_jogadores.append(username_atual)

# Processamento
impostores = input().split()

crewmates = []

for jogador in todos_os_jogadores:
    if jogador not in impostores:
        crewmates.append(jogador)

# Saída de dados
print(*crewmates)