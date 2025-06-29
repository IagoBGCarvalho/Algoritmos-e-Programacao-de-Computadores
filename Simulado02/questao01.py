def contagem_progressiva(n):
    if n < -10:
        return
    contagem_progressiva(n - 1)
    print(n)