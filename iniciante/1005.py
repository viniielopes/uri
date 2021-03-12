pesonumero1 = 3.5
pesonumero2 = 7.5
numero1 = input()
numero2 = input()
multnumero1 = float(numero1) * pesonumero1 
multnumero2 = float(numero2) * pesonumero2
somapesos = pesonumero1 + pesonumero2
somanumeros = multnumero1 + multnumero2
media = somanumeros / somapesos

# media = ((float(numero1) * pesonumero1 ) + (float(numero2) * pesonumero2)) / (pesonumero1 + pesonumero2)
print("MEDIA =", format(media,".5f"))