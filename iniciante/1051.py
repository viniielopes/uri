salario = input()

salario = float(salario)
percentual = 0
imposto_renda = 0

if salario > 4500:
  percentual = 0.28
  valorsobreimposto = salario - 4500
  imposto_renda += valorsobreimposto * percentual
  salario = salario - valorsobreimposto

if salario > 3000 and salario <= 4500:
  percentual = 0.18
  valorsobreimposto = salario - 3000
  imposto_renda += valorsobreimposto * percentual
  salario = salario - valorsobreimposto

if salario > 2000 and salario <= 3000:
  percentual = 0.08
  valorsobreimposto = salario - 2000
  imposto_renda += valorsobreimposto * percentual
  salario = salario - valorsobreimposto

if imposto_renda == 0:
  print("Isento")
else:
  print("R$ {:.2f}".format(imposto_renda))