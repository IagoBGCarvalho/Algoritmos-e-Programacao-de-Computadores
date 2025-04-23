# Entrada de dados
indiceReclamacao = int(input())
percentReclamResolPrim = int(input())
percentCliCancel = int(input())
indiceIndisponibilidade = int(input())
canceladoPorProblema = int(input())

# Processamento
if percentReclamResolPrim >= 60: # Reclamações
    indice = indiceReclamacao - 5
else:
    indice = indiceReclamacao + 15
ii_reclamacoes = indice

if percentCliCancel >= 10: # Cancelamentos
    if canceladoPorProblema == 1:
        indice += 80
    else:
        indice -= 30
else:
    if canceladoPorProblema == 1:
        indice += 50
    else:
        indice -= 10
ii_cancelamentos = indice

if indiceIndisponibilidade >= 10: # Indisponibilidade
    indice += 70
else:
    indice -= 20
ii_indisponibilidade = indice

# Saída de dados
print(ii_reclamacoes)
print(ii_cancelamentos)
print(ii_indisponibilidade)