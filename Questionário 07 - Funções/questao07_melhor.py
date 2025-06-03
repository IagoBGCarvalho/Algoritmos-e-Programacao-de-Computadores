def refrao(n):
    lista_refrao = ["A mamãe gritou", "Quá, quá, quá, quá!", "Mas só " + str(n - 1) + " patinhos", "Voltaram de lá", "Agora só falta aprender a fazer loop!"]
    for item in lista_refrao:
        print(item)

def estrofe(n):
    for i in range(n):
        lista_estrofe = [str(n - i) +" patinhos", "Foram passear", "Além das montanhas", "Para brincar"]
        for item in lista_estrofe:
            print(item)
        refrao(n)

estrofe(2)