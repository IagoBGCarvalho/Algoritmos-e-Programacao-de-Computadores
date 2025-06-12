chuva = []

while True:
    try:
        linha = input()

        if "{!dia}" in linha:
            # Usando .split() para extrair o dia, sem depender de posições fixas.
            dia_str = linha.split('{!dia}')[1].split('{~dia}')[0]
            
            # Usando .split() para extrair o volume.
            volume_str = linha.split('{!volume}')[1].split('{~volume}')[0]

            dia = int(dia_str)
            volume = float(volume_str)
            
            chuva.append([dia, volume])

    except EOFError:
        # Quando não houver mais linhas para ler, o input() dará um erro EOFError, por isso é importante capturá-lo e usar o break.
        break