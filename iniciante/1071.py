x = int(input())
y = int(input())

maior = x
menor = y

def soma_impares(maior, menor):
  total = 0
  for num in range(menor + 1, maior):
    if num % 2 != 0:
      total += num
  print(total)


if y > x:
  maior = y
  menor = x

soma_impares(maior, menor)