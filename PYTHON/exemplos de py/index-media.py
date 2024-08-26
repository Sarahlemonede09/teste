notaA = float(input("INFORME A PRIMEIRA NOTA: "))
notaB = float(input("INFORME A SEGUNDA NOTA: "))

#calcular media
mediafinal = (notaA + notaB)/2

#verificação
if mediafinal >= 7.0:
    print(" A MEDIA: %.1f - APROVADO " % mediafinal)
elif 6.9 >= mediafinal >= 5.0:
    print("A MEDIA: %.1f - RECUPERAÇÃO " % mediafinal)
else:
    print("A MEDIA: %.1f - REPROVADO " % mediafinal)