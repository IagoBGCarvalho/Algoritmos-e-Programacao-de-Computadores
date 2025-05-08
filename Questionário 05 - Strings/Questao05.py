# Declaração de variáveis
numero = ""
frase_final = ""

# Entrada de dados
texto = input()

# Processamento
if "zeroum" in texto:
    frase_final = texto.replace("zeroum", "01")
elif "zero" in texto:
    frase_final = texto.replace("zero", "0")
elif "um" in texto:
    frase_final = texto.replace("um", "1")
elif "dois" in texto:
    frase_final = texto.replace("dois", "2")
elif "três" in texto:
    frase_final = texto.replace("três", "3")
elif "quatro" in texto:
    frase_final = texto.replace("quatro", "4")
elif "cinco" in texto:
    frase_final = texto.replace("cinco", "5")
elif "seis" in texto:
    frase_final = texto.replace("seis", "6")
elif "sete" in texto:
    frase_final = texto.replace("sete", "7")
elif "oito" in texto:
    frase_final = texto.replace("oito", "8")
elif "nove" in texto:
    frase_final = texto.replace("nove", "9")

# Saída de dados
print(frase_final)