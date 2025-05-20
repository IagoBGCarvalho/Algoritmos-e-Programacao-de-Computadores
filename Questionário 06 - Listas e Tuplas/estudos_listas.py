# Atribuição de uma lista a uma variável
lista = ["Oi", 2.5, 10, [10, 20, 30, 40]] # Pode receber qualquer tipo de valor
print(lista)

# Listas são mutáveis
lista_mutavel = [1, 2, 3, 4]
lista_mutavel[3] = 5
print(lista_mutavel) # Por serem mutáveis, é interessante realizar cópias de uma lista.

# Operador in funciona com listas
print(4 in lista_mutavel)
print(5 in lista_mutavel)

# Percorrendo uma lista
for i in lista_mutavel:
    print(i)

for i in range(len(lista_mutavel)):
    lista_mutavel[i] = lista_mutavel[i] * 2 # Está percorrendo a lista e atualizando o valor de cada elemento
print(lista_mutavel)

# Operadores com listas
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b # O operador + cocatena as listas
print(c)

d = c * 3 # O operador * repete a lista
print(d)

# Fatiamento de listas
lista_a_ser_fatiada = ['a', 'b', 'c', 'd', 'e', 'f']
print(lista_a_ser_fatiada[1:3])
print(lista_a_ser_fatiada[:4])
print(lista_a_ser_fatiada[3:])

lista_fatiada = lista_a_ser_fatiada[1:3] # É possível criar novas listas a partir do fatiamento de outras listas
print(lista_fatiada)

lista_a_ser_fatiada[1:3] = ['x', 'y'] # Também é possível atualizar vários elementos em uma lista utilizando fatias

# Métodos de listas
lista_a_ser_fatiada.append('d') # append() adiciona um novo elemento no final da lista

l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']
l1.extend(l2) # extend() pega uma lista como argumento e adiciona todos os elementos a outra lista
print(l1)

lista_fora_de_ordem = ['d', 'c', 'e', 'b', 'a']
lista_fora_de_ordem.sort() # Classifica os elementos em ordem ascedente
print(lista_fora_de_ordem)

# Mapeamento, filtragem e redução
def soma_total(a):
    total = 0
    for i in a:
        total += i
    return total # Esta função soma todas os elementos da lista. Cada vez que o programa passa pela lista, i recebe um elemento da lista e a variável "total" incrementa o valor de i

print(soma_total(a))
print(sum(a)) # O python possui uma função integrada que faz exatamente o que a função acima faz