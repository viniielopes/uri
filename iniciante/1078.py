x = int(input())

def tabuada(x):
  for num in range(1, 11):
    valor = x * num
    print("{} x {} = {}".format(num, x, valor))


tabuada(x)