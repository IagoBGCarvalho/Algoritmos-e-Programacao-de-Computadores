# Processamento
def simples():
  """
  Lê uma string e, se for "repete", imprime uma mensagem e
  chama a si mesma novamente.
  """
  # Entrada
  a = input()

  if a == "repete":
    # Ação
    print("Olá! Vamos repetir!")
    # Chamada recursiva para continuar o processo
    simples()
  
simples()