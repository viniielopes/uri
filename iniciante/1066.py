numeros = []
numero = 0
pares = 0
impares = 0
positivos = 0
negativos = 0

while numero < 5:
  valor = input()
  numeros.append(valor)
  numero += 1


for num in numeros:
  if float(num) % 2 == 0:
    pares += 1
  else:
    impares += 1

  if float(num) < 0:
    negativos += 1
  
  if float(num) > 0:
    positivos += 1

print("{} valor(es) par(es)".format(pares))
print("{} valor(es) impar(es)".format(impares))
print("{} valor(es) positivo(s)".format(positivos))
print("{} valor(es) negativo(s)".format(negativos))