n = int(input())

for i in range(n):
  valor = input()

  a = int(valor.split()[0])
  b = int(valor.split()[1])

  maior = a
  menor = b

  if b > a:
    maior = b
    menor = a
  
  total = 0

  for j  in range(menor + 1, maior):
    if j % 2 == 1:
      total = total + j


  print(total)