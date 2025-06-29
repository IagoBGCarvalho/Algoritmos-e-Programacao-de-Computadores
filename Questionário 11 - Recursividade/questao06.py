def corrida(a, b, c):
  """
  Simula uma corrida de F1 recursivamente.
  """
  
  if a == 0:
    # Se não há mais voltas a serem iniciadas, a corrida acabou.
    print("A corrida chegou ao fim.")
    return

  # Se a corrida não acabou, simula a conclusão de uma volta. O estado no FINAL desta volta será (a-1, b-1).
  voltas_restantes_apos_esta = a - 1
  pneu_restante_apos_esta = b - 1

  # A mensagem de troca de pneu só aparece se duas condições forem verdadeiras:
  # Os pneus se desgastaram nesta volta (pneu_restante_apos_esta == 0)
  # E a corrida AINDA CONTINUA (voltas_restantes_apos_esta > 0)
  if pneu_restante_apos_esta == 0 and voltas_restantes_apos_esta > 0:
    print(f"Faltam {voltas_restantes_apos_esta} voltas, hora de trocar os pneus.")
    # Próxima chamada é com pneus novos (vida útil 'c')
    corrida(voltas_restantes_apos_esta, c, c)
  else:
    corrida(voltas_restantes_apos_esta, pneu_restante_apos_esta, c)