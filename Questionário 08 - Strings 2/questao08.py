def encontrar_tesouro(mapa):
    pos_pericles = mapa.find('P')
    pos_tesouro = mapa.find('X')

    if pos_tesouro == -1:
        print("Péricles, não tem tesouro")
        return

    indice_inicio_caminho = min(pos_pericles, pos_tesouro)
    indice_fim_caminho = max(pos_pericles, pos_tesouro)

    caminho = mapa[indice_inicio_caminho + 1 : indice_fim_caminho]

    if '#' in caminho:
        print("Péricles esse caminho não funciona")
        return 
    distancia = pos_tesouro - pos_pericles

    print(f"Péricles, {distancia} passos")

mapa_caverna = input()
encontrar_tesouro(mapa_caverna)