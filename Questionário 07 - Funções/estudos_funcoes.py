# Funções são uma sequência nomeada de instruções que executa uma operação de computação
# Recebem argumentos e são chamadas por seus nomes próprios

# Funções comuns do python:
print(type(42)) # type é uma função nativa do python que recebe um argumento e retorna o seu tipo
print(int(45.99999)) # int recebe um argumento e retorna um número inteiro, sem arredondamentos
print(float(32)) # float retorna um número de ponto flutuantes
print(str(20.3)) # str retorna uma strings

# O Python tem um módulo matemático que oferece a maioria das funções matemáticas comuns. Um módulo é um arquivo que contém uma coleção de funções relacionadas.

# Antes que possamos usar as funções em um módulo, precisamos importá-lo com uma instrução de importação:
import math

# O objeto de módulo contém as funções e variáveis definidas no módulo. Para acessar uma das funções, é preciso especificar o nome do módulo e o nome da função, separados por um ponto. Este formato é chamado de notação de ponto.

print(math.sqrt(16))
print(10 * math.pi)

# Uma definição de função especifica o nome de uma nova função e a sequência de instruções que são executadas quando a função é chamada.

def printar_letra(): # Cabeçalho
    print("Batatinha quando nasce,") # Corpo
    print("Espalha a rama pelo chão")

printar_letra()

def repetir_letra():
    printar_letra() # É possível usar uma função dentro de outra função
    printar_letra()

repetir_letra()

# Funcoes com parâmetros
def printar_nome(nome): # O nome do parâmetro especificado na definição da função é simplesmente simbólico. Ao chamá-la, pode-se utilizar qualquer nome de variável para ser utilizado como argumento.
    print(nome)

nome_funcionario = "Iago"

printar_nome(nome_funcionario)
printar_nome(nome_funcionario * 4) # É possível utilizar expressões como argumentos

# Funções são locais
def printar_nome_gato(parte1, parte2):
    gato = (parte1 + parte2)
    printar_nome(gato)

printar_nome_gato('Floquinho', 'DeNeve')

# print(gato) Produz erro pois esta variável apenas existe na função printar_nome_gato

# Funções com resultado
math.sqrt(5) # Se apenas chamar uma função com resultado, o valor de retorno é perdido.
resultado = printar_nome("Iago")
print(resultado) # As funções nulas podem exibir algo na tela ou ter algum outro efeito, mas não têm um valor de retorno. Se você atribuir o resultado a uma variável, recebe um valor especial chamado None:
