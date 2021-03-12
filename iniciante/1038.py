total = 0.00
lanches = [4.00, 4.50, 5.00, 2.00, 1.50]

ids = input()

id = ids.split()[0]
quantidade = ids.split()[1]

total = lanches[int(id) - 1] * int(quantidade)

print("Total: R$ {:.2f}".format(total))