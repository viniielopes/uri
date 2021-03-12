numeros = []

x = int(input())

def imprimi(x):
  for num in range(10001):
    if num % x == 2:
      print(num)
      
imprimi(x)