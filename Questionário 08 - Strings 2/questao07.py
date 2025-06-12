def calcular_operacoes(a, b):
    tamanho_max_substring = 0

    for i in range(len(a)):
        for j in range(i, len(a)):
            substring_atual = a[i : j+1]

            if substring_atual in b:
                tamanho_atual = len(substring_atual)
                
                if tamanho_atual > tamanho_max_substring:
                    tamanho_max_substring = tamanho_atual

    operacoes_necessarias = len(a) + len(b) - 2 * tamanho_max_substring

    print(operacoes_necessarias)

string_a = input()
string_b = input()
calcular_operacoes(string_a, string_b)