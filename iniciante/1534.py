while True:
  try:
    valor = int(input())
  
    for i in range(1, valor + 1):

      for j in range(1, valor + 1):
        dig = 3

        if i == j:
          dig = 1
        
        if valor - i + 1 == j:
          dig = 2

        print(dig, end='')
        

      print()
  except EOFError:
    break