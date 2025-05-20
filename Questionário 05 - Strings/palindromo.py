palindromo_contrario = ""
palindromo_sem_espacos = ""
palindromo = input("Digite um candidato a palíndromo: ")

for i in palindromo:
    if i != " ":
        palindromo_sem_espacos = palindromo_sem_espacos + i # Está tirando os espaços em branco

for i in range(len(palindromo_sem_espacos)):
    palindromo_contrario += palindromo_sem_espacos[-1 - i] # Está invertendo a frase

if palindromo_contrario == palindromo_sem_espacos:
    print("É um palíndromo!")
else:
    print("Não é palíndromo...")

print(palindromo_contrario)