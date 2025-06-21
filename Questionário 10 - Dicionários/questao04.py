# Declaracao
dicionario_turma = {} # Dicionário principal que contera o nome dos alunos como chaves e um dicionario como valor para cada aluno

# Entrada de dados
quantidade_alunos = int(input())

for i in range(quantidade_alunos):
    nome_aluno, email_aluno, nota1, nota2, nota3, nota4 = input().split()
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    nota4 = float(nota4)

    informacoes_aluno = { # Dicionario que servirá para armazenar as informações dos alunos
        'email': email_aluno,
        'notas': [nota1, nota2, nota3, nota4]
    }

    dicionario_turma[nome_aluno] = informacoes_aluno # Adiciona o dicionário de informações ao que contém o nome dos alunos

aluno_destinatario = input()

# Processamento e saída
if aluno_destinatario in dicionario_turma:
    dados_aluno = dicionario_turma[aluno_destinatario]
    email_destinatario = dados_aluno["email"]
    notas_destinatario = dados_aluno["notas"]
    media_destinatario = sum(notas_destinatario) / len(notas_destinatario)

    if media_destinatario >= 5.0:
        print(f"Destinatário: {email_destinatario}")
        print(f"O aluno {aluno_destinatario} foi aprovado com média {media_destinatario:.2f}.")
    else:
        print(f"Destinatário: {email_destinatario}")
        print(f"O aluno {aluno_destinatario} foi reprovado com média {media_destinatario}.")
else:
    print(f"O aluno {aluno_destinatario} não está na turma.")