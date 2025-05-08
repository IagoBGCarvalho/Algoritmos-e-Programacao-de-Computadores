# Métodos de strings
palavra = " banana na mesa "
tamanho = len(palavra) # Retorna o tamanho da string
print(tamanho)

palavra_maiuscula = palavra.upper() # Transforma todas as letras da string em maiúsculas
print(palavra_maiuscula)

indice = palavra.find("na", 3) # Retorna o índice da primeira ocorrência da substring. O segundo argumenta indica de onde começar a busca. Pode receber mais um que indica onde parar.
print(indice)

palavara_sem_espaco = palavra.strip() # Remove os espaços em branco do início e do fim da string
print(palavara_sem_espaco)