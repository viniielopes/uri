a = 0
b = 1
while a != b:
  valor = input()

  a = int(valor.split()[0])
  b = int(valor.split()[1])

  if b != a:
    if b > a:
      print("Crescente")    

    if a > b:
      print("Decrescente")