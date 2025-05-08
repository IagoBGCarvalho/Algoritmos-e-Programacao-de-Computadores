def decimal2bin(n):
    return bin(n)[2:].zfill(8)

def reverse(s):
    return s[::-1]

def decodifica(codigoBinario, codigoUnario):
    n = len(codigoUnario)
    if n % 2 == 0:
        zero = codigoBinario[n-1]
        um = [c for c in codigoBinario if c != zero][0]
    else:
        um = codigoBinario[n-1]
        zero = [c for c in codigoBinario if c != um][0]
    
    return zero, um

def converte2alien(zero, um, code):
    binario = decimal2bin(int(code))
    return "".join(um if bit == "1" else zero for bit in binario)

def converte2decimal(zero, um, code):
    binario = "".join("1" if c == um else "0" for c in code)
    return int(binario, 2)

def isBigEndian(codigoBinario, codigoUnario):
    n = len(codigoUnario)
    zero, um = decodifica(codigoBinario, codigoUnario)
    
    binario = "".join("1" if c == um else "0" for c in codigoBinario)
    return int(binario, 2) != n

def BigEndian2LittleEndian(codigoBinario):
    return reverse(codigoBinario)

def LittleEndian2BigEndian(codigoBinario):
    return reverse(codigoBinario)

codigoBinario, codigoUnario = input().split()
n = len(codigoUnario)

bigEndian = isBigEndian(codigoBinario, codigoUnario)
if bigEndian:
    codigoBinario = BigEndian2LittleEndian(codigoBinario)

zero, um = decodifica(codigoBinario, codigoUnario)

for _ in range(n):
    code = input()
    if code.isdigit():
        resultado = converte2alien(zero, um, code)
        if bigEndian:
            resultado = LittleEndian2BigEndian(resultado)
        print(resultado)
    else:
        if bigEndian:
            code = BigEndian2LittleEndian(code)
        print(converte2decimal(zero, um, code))