linha1 = input()
linha2 = input()

dados_linha1 = linha1.split(" ")
codigo1 = dados_linha1[0]
numero_pecas1 = dados_linha1[1]
valor_unitario1 = dados_linha1[2]

dados_linha2 = linha2.split(" ")
codigo2 = dados_linha2[0]
numero_pecas2 = dados_linha2[1]
valor_unitario2 = dados_linha2[2]

valor_pecas1 = float(numero_pecas1) * float(valor_unitario1)
valor_pecas2 = float(numero_pecas2) * float(valor_unitario2)

valor_total = valor_pecas1 + valor_pecas2
print("VALOR A PAGAR: R$", format(valor_total, ".2f"))