total = 0
idades = []

idade = int(input())

while idade > 0:
  idades.append(idade)
  total += idade
  idade = int(input())

print("{:.2f}".format(total / len(idades)))