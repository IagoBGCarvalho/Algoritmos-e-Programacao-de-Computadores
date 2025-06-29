def fibonacci(n):
    """
    Imprime os 'n' primeiros termos da sequência de Fibonacci.
    """
    
    # Dicionário que servirá de "cache" para guardar os resultados já calculados (Memoização) começando com os casos base já preenchidos.
    cache = {0: 0, 1: 1}

    def fib_recursivo(k):
        """
        Calcula e retorna o k-ésimo termo de Fibonacci, usando o cache.
        """
        # Se o valor para 'k' já foi calculado, pega do cache e retorna.
        if k in cache:
            return cache[k]
        
        # Se não, calcula o valor recursivamente.
        resultado = fib_recursivo(k - 1) + fib_recursivo(k - 2)
        
        # ANTES de retornar, guardam o resultado no cache para uso futuro.
        cache[k] = resultado
        return resultado
    
    # Cria uma lista para guardar os termos que serão calculados.
    termos_da_sequencia = []
    
    # loop for para gerar os 'n' primeiros termos (de 0 a n-1).
    for i in range(n):
        # Para cada 'i', chama a função recursiva e converte o resultado para string.
        termo = str(fib_recursivo(i))
        termos_da_sequencia.append(termo)
    
    # join() para juntar todos os termos da lista em uma única string, separados por espaços.
    print(" ".join(termos_da_sequencia))
