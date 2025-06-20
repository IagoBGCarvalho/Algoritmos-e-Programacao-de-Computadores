# Declaracao
alunos_com_mesma_nota = []
dicionario_alunos_notas = {}

# Entrada de dados
quantidade_alunos = int(input())

for i in range(quantidade_alunos):
    nome_aluno, nota_aluno = input().split(",")
    nome_aluno = str(nome_aluno)
    nota_aluno = float(nota_aluno)
    dicionario_alunos_notas[nome_aluno] = nota_aluno # A cada loop, um aluno e uma nota são adicionados ao dicionário

nota_referencia = float(input())

# Processamento
for nome_aluno, nota_aluno in dicionario_alunos_notas.items():
    if nota_aluno == nota_referencia: 
        alunos_com_mesma_nota.append(nome_aluno) # Para procurar um valor em um dicionário, é necessário percorrer ele utilizando duas variáveis dentro do for, uma para a chave e a outra para o valor.

# Saída de dados
if len(alunos_com_mesma_nota) < 1:
    print("Você foi o único aluno com essa nota.")
else:
    nomes_ordenados = sorted(alunos_com_mesma_nota)
    print("/".join(nomes_ordenados)) # O join une todos os items da lista em uma única string e adiciona a barra como separador entre cada item