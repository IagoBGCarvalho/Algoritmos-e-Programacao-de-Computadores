# --- Aula Recursividade ---

# Recursividade refere-se à capacidade de uma função chamar a si mesma durante
# sua execução. Em outras palavras, é quando uma função se auto-invoca dentro
# do seu próprio corpo.

# A recursividade permite resolver problemas de forma elegante, dividindo-os
# em subproblemas menores e resolvendi cada um deles até atingir uma condição
# de parada.

# --- Implementação de funções utilizando rescursividade ---
def fatorial(n):
    if n == 0: # Primeiro faz o caso base, onde a função deve parar
        return 1
    else: # Se o caso base não acontecer, faz a operação recursiva visando chegar ao caso base
        return n * fatorial(n - 1)
    
print(fatorial(5))

def contagem_regressiva(n):
    """Esta função utiliza recursividade para 
    imprimir uma contagem regressiva no terminal"""
    if n == 0:
        print("Acabou!")
    else:
        print(n)
        contagem_regressiva(n - 1)

print(contagem_regressiva(10))

def contagem_progressiva(n, atual=0):
    if atual > n:
        print("Acabou!")
    else:
        print(atual)
        contagem_progressiva(n, atual + 1)

print(contagem_progressiva(5))