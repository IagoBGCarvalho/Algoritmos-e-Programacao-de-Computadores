import math
# Uma função se trata de um bloco de código reutilizável. Deve ser declarada no começo do código. 
# Docstrings (""" """) são usadas para documentar funções

# Sintaxe de uma função
def alo_nome(nome): # Nome da função e parâmetros, podem ser declarados de 0 a n parâmetros
    """Função simples que apenas retorna um nome"""
    print(f"Alô, {nome}!")

# Chamando uma função
x = input("Digite o seu nome:")
alo_nome(x)

# Funções integradas
print(pow(2,3)) # Faz a potência do primeiro número pelo segundo
print(max(7, 11)) # Retorna o maior número entre os parâmetros

# Funções que retornam valores
def soma(a, b):
    """Esta função retorna uma soma"""
    resultado_soma = a + b
    return resultado_soma

print(soma(1, 2))

def func2grau(a, b, c):
    """Esta função retorna o resultado de uma função de segundo grau"""
    delta = b**2-4*a*c
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    return x1, x2

print(func2grau(2, -5, 3))

"""As variáveis dentro de uma função são locais, ou seja, não sofrem interferência do resto das variáveis do código, mas é possível tornar uma variável global utilizando a função global"""