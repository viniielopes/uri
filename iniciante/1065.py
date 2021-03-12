numeros = []
numero = 0
contador = 0

while numero < 5:
  valor = input()
  numeros.append(valor)
  numero += 1


for num in numeros:
  if float(num) % 2 == 0:
    contador += 1
    

print("{} valores pares".format(contador))