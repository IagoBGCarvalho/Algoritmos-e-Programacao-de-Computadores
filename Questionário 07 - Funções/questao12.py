def ehPrimo(x):
    if x <= 1:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0

    i = 3
    while i * i <= x:
        if x % i == 0:
            return 0 
        i += 2  

    return 1

def divisoresPrimos(x):
    contador_divisores_primos = 0
  
    divisores_primos_encontrados = set()

    if ehPrimo(x) == 1:
        return 0
    
    for i in range(2, x): 
        if x % i == 0: 
            if ehPrimo(i) == 1:
                divisores_primos_encontrados.add(i)
    
    return len(divisores_primos_encontrados)
