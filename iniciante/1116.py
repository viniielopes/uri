valor = int(input())

for i in range(valor):
  valores = input().split()

  x = float(valores[0])
  y = float(valores[1])

  try:
    res = x / y
    print(res)
  except:
    print("divisao impossivel")
