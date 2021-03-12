nome_vendedor = input()
salario_fixo = input()
montante_vendas = input()

salario_com_bonus = float(salario_fixo) + float(montante_vendas) * 0.15

print("TOTAL = R$", format(salario_com_bonus, ".2f"))