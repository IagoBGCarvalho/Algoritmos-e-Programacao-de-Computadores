# Entrada de dados
numeros1 = input().split()
numeros2 = input().split()

# Processamento de dados
f1 = float(numeros1[0]) # Colocando a substring de índice 0 em uma variável de ponto flutuante
f2 = float(numeros1[1])
d1 = float(numeros2[0])
d2 = float(numeros2[1])

# Saída de dados
print(f"F1 = {f1}, F2 = {f2}")
print(f"D1 = {d1}, D2 = {d2}")
print()
print(f"F1 = {f1:.2f}, F2 = {f2:.2f}")
print(f"D1 = {d1:.2f}, D2 = {d2:.2f}")
print()
print(f"F1 = {f1:.5f}, F2 = {f2:.5f}")
print(f"D1 = {d1:.5f}, D2 = {d2:.5f}")
print()
print(f"F1 = {f1:.10f}, F2 = {f2:.10f}")
print(f"D1 = {d1:.10f}, D2 = {d2:.10f}")
print()
print(f"F1 = {f1:.28f}, F2 = {f2:.28f}")
print(f"D1 = {d1:.28f}, D2 = {d2:.28f}")
print()
print(f"F1 = {f1:.3E}, F2 = {f2:.3E}") # :.3E = 3 casas decimais e notação científica
print(f"D1 = {d1:.3E}, D2 = {d2:.3E}")
print()
print(f"F1 = {f1:.0f}, F2 = {f2:.0f}") # :.0f = 0 casas decimais (inteiro)
print(f"D1 = {d1:.0f}, D2 = {d2:.0f}")