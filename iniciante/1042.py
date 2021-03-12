valores = input()

dados = valores.split()

dados_copia = valores.split()

i = 0
for numero in dados:
  aux = numero
  
  j = i
  while j < len(dados):
    if int(aux) > int(dados[j]):
      aux = dados[j]
      dados[j] = dados[i]
      dados[i] = aux
    j+=1
  i+=1

for dado in dados:
  print(dado)

print()

for dado in dados_copia:
  print("{}".format(dado))