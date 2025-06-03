s1, s2, s3 = input().split()

def duplica(f):
    f()
    f()

def quadruplica(f):
    duplica(f)
    duplica(f)

def imprime_parte_linha1():
    print(" "+s1+s2+" ", end="")
    
def imprime_parte_linha1_fim():
    print()
    
def imprime_parte_linha2():
    print(s1+2*s3+s2, end="")
    
def imprime_parte_linha2_fim():
    print()
      
def imprime_linha1():
    quadruplica(imprime_parte_linha1)
    imprime_parte_linha1_fim()

def imprime_linha2():
    quadruplica(imprime_parte_linha2) 
    imprime_parte_linha2_fim() 
    
def imprime_um_padrao_horizontal():
    imprime_linha1()
    imprime_linha2()

def imprime_padrao_completo():
    quadruplica(imprime_um_padrao_horizontal)

imprime_padrao_completo()