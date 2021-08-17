ganhou = "Bazinga!"
perdeu = "Raj trapaceou!"
empatou = "De novo!"

jogo = {
    "pedra": {
      "papel": perdeu,
      "tesoura": ganhou,
      "pedra": empatou,
      "Spock": perdeu,
      "lagarto": ganhou    
    },
    "tesoura": {
        "papel": ganhou,
        "pedra": perdeu,
        "tesoura": empatou,
        "Spock": perdeu,
        "lagarto": ganhou 
    },
    "papel": {
        "pedra": ganhou,
        "tesoura": perdeu,
        "papel": empatou,
        "Spock": ganhou,
        "lagarto": perdeu 
    },
    "lagarto": {
        "pedra": perdeu,
        "tesoura": perdeu,
        "papel": ganhou,
        "Spock": ganhou,
        "lagarto": empatou 
    },
     "Spock": {
        "pedra": ganhou,
        "tesoura": ganhou,
        "papel": perdeu,
        "Spock": empatou,
        "lagarto": perdeu 
    }
}

testes = int(input())

for i in range(1, testes + 1):
  valores = input()

  sheldon, raj = valores.split(" ")
  
  print("Caso #{}: {}".format(i, jogo[sheldon][raj]))
