# Entrada de dados
numero1 = int(input())
numero2 = int(input())

# Saída de dados
print(f"I1 = {numero1}, I2 = {numero2}")
print(f"I1 = {numero1:<10}, I2 = {numero2}") # <10 = alinhamento a esquerda com 10 caracteres
print(f"I1 = {numero1}, I2 = {numero2:>5}") # >5 = alinhamento a direita com 5 caracteres
print(f"I1 = {numero1:<10}, I2 = {numero2:0>4}") # 0>4 = alinhamento a direita com 4 caracteres e preenchimento com 0
print(f"I1 = {numero1:0>6}, I2 = {numero2:0>4}") # 0>6 = alinhamento a direita com 6 caracteres e preenchimento com 0