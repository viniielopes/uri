numeros = []
numero = 0
contador = 0

while numero < 6:
  valor = input()
  numeros.append(valor)
  numero += 1


for num in numeros:
  if float(num) > 0:
    contador += 1
    

print("{} valores positivos".format(contador))