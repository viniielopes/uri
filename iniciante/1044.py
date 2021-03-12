valores = input()

a = float(valores.split()[0])
b = float(valores.split()[1])

res = a * b

maior = a
menor = b

if a < b:
  maior = b
  menor = a

if maior % menor == 0:
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")