fibonacci = [0, 1, 1, 2, 3]

t = int(input())

for i in range(t):
  pos = int(input())

  if len(fibonacci) > pos:
    print("Fib({}) = {}".format(pos, fibonacci[pos]))

  else:
    while pos > len(fibonacci) - 1:
      fim = len(fibonacci)
      valor = int(fibonacci[fim - 1]) + int(fibonacci[fim - 2])
      fibonacci.append(valor)
    
    print("Fib({}) = {}".format(pos, fibonacci[pos]))