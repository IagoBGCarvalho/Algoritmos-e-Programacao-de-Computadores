# A função auxiliar que faz o trabalho recursivo de desenhar linha por linha.
def desenha_linhas_recursivo(deslocamento, tamanho_atual, tamanho_base):
    """
    Desenha uma linha do triângulo e chama a si mesma para a próxima linha.
    """
    
    # Caso Base: Se o tamanho da linha atual ultrapassar o tamanho da base,
    # significa que já desenhou tudo. A função para.
    if tamanho_atual > tamanho_base:
        return

    # Processamento
    # Calcula o espaçamento necessário para centralizar a linha.
    espacos_centralizar = (tamanho_base - tamanho_atual) // 2
    
    # Calcula o recuo total da esquerda.
    recuo_total = deslocamento + espacos_centralizar
    
    # Monta a string da linha a ser impressa.
    linha_impressao = (' ' * recuo_total) + ('+' * tamanho_atual)
    
    # Saída
    print(linha_impressao)
    
    # Chama a função para desenhar a próxima linha,
    # que terá 2 caracteres a mais.
    desenha_linhas_recursivo(deslocamento, tamanho_atual + 2, tamanho_base)


def triangulo(x, size):
    """
    Inicia o processo recursivo para desenhar um triângulo.
    """
    # Apenas chama a função auxiliar com os valores iniciais corretos.
    # Começa com uma linha de tamanho 1.
    desenha_linhas_recursivo(x, 1, size)
