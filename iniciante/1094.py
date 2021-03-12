n = int(input())

coelho = 0
sapo = 0
rato = 0

for i in range(n):
  linha = input()
  valor = int(linha.split()[0])
  animal = linha.split()[1]

  if animal == 'C':
    coelho += valor
  
  if animal == 'S':
    sapo += valor

  if animal == 'R':
    rato += valor


total = coelho + sapo + rato

percentual_coelho = coelho / total * 100
percentual_rato = rato / total * 100
percentual_sapo = sapo / total * 100


print("Total: {} cobaias".format(total))

print("Total de coelhos: {}".format(coelho))
print("Total de ratos: {}".format(rato))
print("Total de sapos: {}".format(sapo))

print("Percentual de coelhos: {:.2f} %".format(percentual_coelho))
print("Percentual de ratos: {:.2f} %".format(percentual_rato))
print("Percentual de sapos: {:.2f} %".format(percentual_sapo))
