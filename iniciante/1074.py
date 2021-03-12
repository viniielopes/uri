numeros = []

x = int(input())

for i in range(x):
  valor = int(input())
  numeros.append(valor)


def imprimi(numeros):
  for num in numeros:
    if num == 0:
      print("NULL")
    else:
      if num % 2 == 0 and num < 0:
        print("EVEN NEGATIVE")
      
      if num % 2 == 0 and num > 0:
        print("EVEN POSITIVE")

      if num % 2 != 0 and num < 0:
        print("ODD NEGATIVE")
      
      if num % 2 != 0 and num > 0:
        print("ODD POSITIVE")
      
imprimi(numeros)