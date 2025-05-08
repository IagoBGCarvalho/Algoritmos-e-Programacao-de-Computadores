def decimal2bin(n):
    return bin(n)[2:].zfill(8)

def reverse(s):
    return s[::-1]

def decodifica(codigoBinario, codigoUnario):
    n = len(codigoUnario)
    if n % 2 == 1:  
        zero = codigoBinario[n-1]
        for c in codigoBinario:
            if c != zero:
                um = c
                break
    else:         
        um = codigoBinario[n-1]
        for c in codigoBinario:
            if c != um:
                zero = c
                break
    return zero, um

def converte2alien(zero, um, code):
    binario = decimal2bin(int(code))
    return "".join(zero if bit == "0" else um for bit in binario)

def converte2decimal(zero, um, code):
    binario = "".join("0" if c == zero else "1" for c in code)
    return int(binario, 2)

def isBigEndian(codigoBinario, codigoUnario):
    n = len(codigoUnario)
    zero, um = decodifica(codigoBinario, codigoUnario)
    binario = "".join("0" if c == zero else "1" for c in codigoBinario)
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
    code = input().strip()
    if code.isdigit():
        resultado = converte2alien(zero, um, code)
        if bigEndian:
            resultado = LittleEndian2BigEndian(resultado)
        print(resultado)
    else:
        if bigEndian:
            code = BigEndian2LittleEndian(code)
        print(converte2decimal(zero, um, code))
