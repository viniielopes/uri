salario = input()

salario = float(salario)
reajuste = 0
percentual = 0

if salario > 0 and salario <= 400:
  percentual = 0.15
  reajuste = salario * percentual
  salario = salario + reajuste

elif salario > 400 and salario <= 800:
  percentual = 0.12
  reajuste = salario * percentual
  salario += reajuste

elif salario > 800 and salario <= 1200:
  percentual = 0.10
  reajuste = salario * percentual
  salario += reajuste

elif salario > 1200 and salario <= 2000:
  percentual = 0.07
  reajuste = salario * percentual
  salario += reajuste

elif salario > 2000:
  percentual = 0.04
  reajuste = salario * percentual
  salario += reajuste

print("Novo salario: {:.2f}".format(salario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {:.0f} %".format(percentual * 100))