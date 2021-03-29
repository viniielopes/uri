qtd = int(input())

for i in range(qtd):
  n = int(input())

  valor = 0
  for j in range(n):
    valor += j  

    if valor == n:
      print("{} eh perfeito".format(n))
      break
    elif valor > n:
      print("{} nao eh perfeito".format(n))
      valor = n
      break

  if valor != n:
    print("{} nao eh perfeito".format(n))
