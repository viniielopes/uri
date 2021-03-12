x = int(input())

def imprimi_seis_impares(numero):
  contador = 0
  for num in range(x, x + 15):
    if contador == 6:
      return

    if num % 2 != 0:
      print(num)
      contador += 1
      
imprimi_seis_impares(x)