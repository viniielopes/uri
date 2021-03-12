pesonumero1 = 2
pesonumero2 = 3
pesonumero3 = 5
numero1 = input()
numero2 = input()
numero3 = input()
multiplica_numero1 = float(numero1) * pesonumero1 
multiplica_numero2 = float(numero2) * pesonumero2
multiplica_numero3 = float(numero3) * pesonumero3
somapesos = pesonumero1 + pesonumero2 + pesonumero3
somanumeros = multiplica_numero1 + multiplica_numero2 + multiplica_numero3
media = somanumeros / somapesos

# media = ((float(numero1) * pesonumero1 ) + (float(numero2) * pesonumero2)) / (pesonumero1 + pesonumero2)
print("MEDIA =", format(media,".1f"))