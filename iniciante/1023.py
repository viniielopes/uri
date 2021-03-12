qtdimoveis = int(input())
cidade = 1

while qtdimoveis != 0:

  if cidade != 1:
    print()

  informacoes = []

  consumo_total = 0
  pessoas_total = 0

  for qtdimovel in range(qtdimoveis):

    dados = input()
    dados = dados.split()

    pessoas_total += int(dados[0])
    consumo_total += int(dados[1])

    informacoes.append({
         "qtdmorador": int(dados[0]),
         "consumo_por_pessoa": int(int(dados[1]) / int(dados[0]))
        })
  
    consumo_medio = int((consumo_total / pessoas_total) * 100)

    consumo_por_casa = []

    consumo_por_pessoa = sorted(informacoes, key=lambda k: k['consumo_por_pessoa'])


  print("Cidade# {}:".format(cidade))

  texto_pessoas = ""
  for consumo in consumo_por_pessoa:
    texto_pessoas += "{}-{} ".format(consumo["qtdmorador"], consumo["consumo_por_pessoa"])

  print(texto_pessoas)

  print("Consumo medio: {:.2f} m3.".format(consumo_medio / 100))

  cidade += 1
  qtdimoveis= int(input())