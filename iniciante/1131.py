novo = 0

grenal = 0

inter = 0
gremio = 0
empate = 0


while novo != 2:    
  grenal += 1
  gols = input()

  gols_inter = int(gols.split()[0])
  gols_gremio = int(gols.split()[1])

  if gols_inter > gols_gremio:
    inter += 1

  if gols_inter < gols_gremio:
    gremio += 1

  if gols_inter == gols_gremio:
    empate += 1

  
  print("Novo grenal (1-sim 2-nao)")

  novo = int(input())

print("{} grenais".format(grenal))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empate))

if inter > gremio:
  print("Inter venceu mais")

if gremio > inter:
  print("Gremio venceu mais")

if gremio == inter:
  print("Nao houve vencedor")