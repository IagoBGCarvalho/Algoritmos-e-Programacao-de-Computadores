# --- Aula de Dicionários ---

# --- Guardando dados com listas ---
estoque = [
    ["Sal", "Kg"],
    ["Leite", "L"],
    ["Chocolate", "Cx"],
    ["Ovo", "Dz"]
]

# Para procurar algum ítem na lista:
for produto, unidade in estoque: # Desempacota a sublista e procura partir da string
    if produto == "Sal":
        print("Achou")

# Ou pode-se usar:
for item in estoque:
    if "Sal" in item:
        print("Achou")

# Usar listas é interessante, mas leva muito tempo, 
# pois cada loop deve ser analisado caso a caso"""

# --- Dicionários ---

"""Um dicionário é um tipo mapeado, ou seja, mapeiam e referenciam todos os dados. 
Mapeiam chaves para valores, chave é qualquer tipo imutável (string) e um valor pode ser qualquer tipo."""

ingles_portugues = {} # Cria um dicionário
ingles_portugues["computer"] = "computador" # Está atribuindo a frase "computador" para a chave "computer"
ingles_portugues["assignment"] = "atribuição"
print(ingles_portugues)

ing2port = {"one":"um", "two":"dois"}
print(ing2port)

# Deletando um par-chave de um dicionário:
estoque_dicionario = {"maçã":130,"pera":50,"banana":10}
del estoque_dicionario["banana"] # Ao usar o del para apagar a chave, também apaga automaticamente o valor
print(estoque_dicionario)

print(len(estoque_dicionario)) # Mostra a quantidade de pares-chaves no dicionário
print("banana" in estoque_dicionario) # in e not in podem ser usados para verificar se existe uma chave no dicionário
print("banana" not in estoque)

# --- Métodos de dicionário ---

# Usar métodos: objeto.método()
print(estoque_dicionario.keys()) # Mostra as chaves presentes no dicionário
print(estoque_dicionario.values()) # Mostra os valores presentes no dicionário
print(estoque_dicionario.items()) # Mostra todos os presentes no dicionário

""" Utiliza-se "help(dict) para ver todos os métodos de dicionários no interpretador do python"""

# --- Aliasing ---

# É possível fazer com que dois dicionários referenciem o exato mesmo objeto
# Quando um é alterado, o outro também é
oposto = {"Alto":"baixo","direito":"esquerdo"}
contrario = oposto
oposto["Frente"] = "Trás"
print(contrario) # Para que isso não dê problemas, é extremamente necessário criar uma cópia do primeiro dicionário, para que se tenha uma versão "preservada" dele.

# --- Matrizes Esparsas ---

# Ao invés de representar matrizes com listas, como:
matriz_lista = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0], # Isso ocupa muito espaço na memória
    [0, 0, 0, 3, 0]
]

matriz_dicionario = {(0,3): 1,(2,1): 2,(4,3): 3} # Está usando tuplas para representar os eixos x e y da matriz e identificar os números que não são 0.

print(matriz_dicionario[2,1]) # Por fim, é possível utilizar as chaves para encontrar o valor na matriz de forma mais fácil
