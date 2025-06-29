def JaChegou(n, s):
  """
  Imprime a string 's' um total de 'n' vezes usando recursão.
  """
  # Se n for igual a 0, não há mais nada a fazer.
  if n == 0:
    return

  # Processamento e Ação do Passo Atual
  # Imprime a string 's' na iteração atual.
  print(s)

  # chama a si mesma com o problema reduzido (n - 1).
  JaChegou(n - 1, s)