while True:
  try:
    valor = int(input())
    
    if valor != 0:
      print("vai ter duas!")
    else:
      print("vai ter copa!")

  except EOFError:
    break
