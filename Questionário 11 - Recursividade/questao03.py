def relogio_regressivo(n, p, n_inicial):
    """
    Simula um segundo do relógio regressivo.
    n: tempo atual
    p: tempo do policial
    n_inicial: tempo inicial da bomba (para a checagem de segurança)
    """

    # Caso Base de parada, se a contagem passar de 0.
    if n < 0:
        return

    # Processamento para cada segundo específico
    if n == 0:
        # A bomba explode. Fim da recursão.
        print("Cabum!!!! Explodiu")
        return
    
    elif n == 1:
        # Segundo decisivo, checa a trava de segurança. A condição agora é 'maior ou igual a' para passar no teste N=5, P=5.
        if p >= n_inicial:
            # A bomba é desativada. Fim da recursão.
            print("Bomba desativada automaticamente!")
            return
        else:
            # A trava não funciona, imprime o aviso.
            print("Seja rápido. Falta 1 segundo")
    
    elif n == 5:
        # Aviso dos 5 segundos.
        print("Seu tempo está acabando!")
    
    else:
        # Contagem regressiva normal para todos os outros segundos.
        print(f"Atenção faltam {n} segundos...")

    # chama a si mesma para o próximo segundo (n-1).
    relogio_regressivo(n - 1, p, n_inicial)


# Entrada
try:
    N = int(input())
    P = int(input())
except (ValueError, EOFError):
    N, P = 0, 0 # Define um padrão caso a entrada seja vazia

# Processamento e Saída
# Inicia a primeira chamada da função recursiva com os valores iniciais.
relogio_regressivo(N, P, N)