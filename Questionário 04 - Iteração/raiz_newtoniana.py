print("Calculadora Newtoniana de raiz quadrada!\n")

# Entrada de dados
a = int(input("Digite o número que se deseja saber a raiz: "))
b = int(input("Digite número a ser a aproximação: "))

# Processamento e saída de dados
while True:
    print(b)
    raiz_aproximada = (b + (a/b))/2
    if raiz_aproximada == b:
        break
    b = raiz_aproximada