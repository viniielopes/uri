x = int(input())

def imprimi_quadrado_pares(numero):
  for num in range(1, x + 1):
    if num % 2 == 0:
      quadrado = num ** 2
      print("{}^2 = {}".format(num, quadrado))
      
imprimi_quadrado_pares(x)