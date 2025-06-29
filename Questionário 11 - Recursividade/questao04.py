def controle(n, c):
  """
  Simula o controle diário de Julie ao tomar seus comprimidos de vitamina,
  imprimindo uma mensagem a cada dia.

  n: número total de comprimidos no pote (constante).
  c: quantidade de comprimidos já consumidos até o dia anterior.
  """

  # Incrementamos a contagem de comprimidos consumidos.
  consumidos_agora = c + 1
  
  # Calcula quantos comprimidos ainda restam.
  restantes = n - consumidos_agora

  if consumidos_agora == n:
    # Se for o último, imprime a mensagem final e a função para aqui (return implícito).
    print(f"Parabens Julie! Voce tomou todos os {n} comprimidos!")
  
  else: # Se não for o último comprimido.
    # Imprime a mensagem de status para o dia atual.
    print(f"Voce ja tomou {consumidos_agora} comprimidos, restam {restantes}.")
    
    # Chama a si mesma para simular o próximo dia com o novo número de comprimidos consumidos (consumidos_agora)
    controle(n, consumidos_agora)
    