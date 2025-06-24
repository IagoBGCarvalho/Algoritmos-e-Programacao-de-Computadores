# Entrada
# CORREÇÃO AQUI: Guardamos o valor de M em vez de usar _
N, M, K = [int(i) for i in input().split()]

# Cria o mapa Jogador -> Time.
jogador_para_equipe = [int(i) for i in input().split()]

# Ignora a linha com a contagem de jogadores por empresário.
input() 

# Lista para guardar os IDs dos empresários que podem manipular
agentes_manipuladores = []

# Processamento
# O loop agora pode usar a variável M, que foi definida corretamente.
for id_empresario in range(1, M + 1):
    # Lê a lista de jogadores agenciados por este empresário
    jogadores_do_agente = [int(i) for i in input().split()]
    
    # Cria um conjunto vazio para armazenar os times únicos deste agente
    equipes_deste_agente = set()

    # Para cada jogador agenciado, descubra seu time e adicione ao conjunto
    for jogador in jogadores_do_agente:
        # Pega o time do jogador usando o mapa
        time_do_jogador = jogador_para_equipe[jogador - 1]
        equipes_deste_agente.add(time_do_jogador)

    # Verifica se o empresário atende à condição de manipulação
    if len(equipes_deste_agente) == K:
        agentes_manipuladores.append(id_empresario)

# Saída
# Verifica se a lista de manipuladores está vazia
if not agentes_manipuladores:
    print("-1")
else:
    # Se não estiver vazia, imprime os IDs separados por espaço.
    print(" ".join([str(id) for id in agentes_manipuladores]))