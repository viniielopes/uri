combustivel = 0

alcool = 0
gasolina = 0
diesel = 0

while combustivel != 4:
  combustivel = int(input())

  if combustivel == 1:
    alcool += 1

  if combustivel == 2:
    gasolina += 1

  if combustivel == 3:
    diesel += 1


print("MUITO OBRIGADO")
print("Alcool: {}".format(alcool))
print("Gasolina: {}".format(gasolina))
print("Diesel: {}".format(diesel))