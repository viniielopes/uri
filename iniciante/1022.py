import math

qtdcontas = int(input())

for qtd in range(qtdcontas):  
  valores = input()

  dados = valores.split()

  n1 = int(dados[0])
  d1 = int(dados[2])

  operador = dados[3]

  n2 = int(dados[4])
  d2 = int(dados[6])


  def soma(n1,n2, d1,d2):
    n1 = n1 * d2 + n2 * d1
    d1 = d1 * d2
    return [n1, d1]


  def subtrai(n1,n2, d1,d2):
    n1 = n1 * d2 - n2 * d1
    d1 = d1 * d2
    return [n1, d1]

    
  def multiplica(n1,n2, d1,d2):
    n1 = n1 * n2
    d1 = d1 * d2
    return [n1, d1]
    
  def dividir(n1,n2, d1,d2):
    n1 = n1 * d2
    d1 = n2 * d1
    return [n1, d1]


  def simplifica(n1, n2, d1, d2, operador): 
    simplificado = []

    if operador == '+':
      valores = soma(n1, n2, d1, d2)

    if operador == '-':
      valores = subtrai(n1, n2, d1, d2)

    if operador == '*':
      valores = multiplica(n1, n2, d1, d2)

    if operador == '/':
      valores = dividir(n1, n2, d1, d2)

    for valor in valores:    
      mdc = math.gcd(int(valores[0]), int(valores[1]))
      simplificado.append(valor / mdc)

    print('{}/{} = {}/{}'.format(int(valores[0]), int(valores[1]), int(simplificado[0]), int(simplificado[1])))
  

  simplifica(n1, n2, d1, d2, operador)
