numeros = []

for numero in range(1, 101):
  valor = int(input())
  numeros.append(valor)

maior = numeros[0]
posicao = 0

for idx, num in enumerate(numeros):
  if num > maior:
    maior = num
    posicao = idx

print(maior)
print(posicao + 1)