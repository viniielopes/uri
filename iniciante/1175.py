lista = []

while len(lista) != 20:
  valor = input()
  lista.append(valor)

tamanho = len(lista) - 1

for i in range(10):
  aux = lista[tamanho - i]
  lista[tamanho - i] = lista[i]
  lista[i] = aux

for i in range(20):
  print("N[{}] = {}".format(i, lista[i]))