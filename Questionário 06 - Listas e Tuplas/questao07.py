# Declaração de variáveis
maior_distancia_segura_geral = 0

# Entrada de dados
linha_m_n = input().split()
m = int(linha_m_n[0])       
n = int(linha_m_n[1])   

# Processamento
for _ in range(m):
    linha_fileira_str_list = input().split() 
    
    fileira_atual = [int(cadeira_str) for cadeira_str in linha_fileira_str_list]

    for j in range(n):
        if fileira_atual[j] == 0:
            distancia_minima_nesta_cadeira = float('inf')

            for k in range(n):
                if fileira_atual[k] == 1:
                    distancia = abs(j - k) 
                    if distancia < distancia_minima_nesta_cadeira:
                        distancia_minima_nesta_cadeira = distancia
            
            if distancia_minima_nesta_cadeira != float('inf'):
                if distancia_minima_nesta_cadeira > maior_distancia_segura_geral:
                    maior_distancia_segura_geral = distancia_minima_nesta_cadeira

# Saída de dados
print(maior_distancia_segura_geral)