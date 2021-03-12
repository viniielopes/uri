menor = 1
while menor > 0:    
  valor = input()

  a = int(valor.split()[0])
  b = int(valor.split()[1])

  maior = a
  menor = b

  if b > a:
    maior = b
    menor = a

  if menor > 0:
    total = 0
    for i in range(menor, maior + 1):
      total += i
      print(i, end=" ")
    print("Sum={}".format(total))