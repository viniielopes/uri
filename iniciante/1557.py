valor = -1

while valor != 0:


  valor = int(input())
  if valor == 0:
    break
  
  padding = 0

  coluna = 1
  # contabiliza e verifica qual é o ultimo numero e define o padding
  for i in range(1, valor + 1):

    linha = coluna
    for j in range(1, valor + 1):
      if i == valor and j == valor:
        padding = len(str((linha))) + 1

      linha = linha * 2
    coluna = coluna * 2
   
  # contabiliza e exibe os numeros utilizando padding definido
  contlinha = 1
  contcoluna = 1
  for i in range(1, valor + 1):

    contlinha = contcoluna
    for j in range(1, valor + 1):

      if j == 1:
        print("{:{padding}d}".format(contlinha, padding=padding - 1), end='')
      else:
        print("{:{padding}d}".format(contlinha, padding=padding), end='')

      contlinha = contlinha * 2
    contcoluna = contcoluna * 2
    print()
  print()