from pygame.examples.midi import NullKey

# classe=("Barbaro","Paladino","Assasino")
#
# def escolhaDeClasse(opcao):
#     if (opcao == "barbaro"):
#         print("teste barbaro funcionou")
#         vida = 35
#         ataque = 7
#         Crit_chance = [0]
#         Atq_Crit = 0
#         return vida, ataque, Crit_chance, Atq_Crit ## VER UMA MELHOR FORMA DE LOCALIZAR O ATQ_CRIT
#     elif (opcao == "paladino"):
#         print("teste paladino funcionou")
#         vida = 50
#         ataque = 3
#         Crit_chance = [1]
#         Atq_Crit = 0
#         return vida, ataque, Crit_chance, Atq_Crit
#     elif (opcao == "assasino"):
#         print("teste assasino funcionou")
#         vida = 20
#         ataque = 6
#         Crit_chance = [1,2,3]
#         Atq_Crit = 0
#         return vida, ataque, Crit_chance, Atq_Crit
class Barbaro ():
    def __init__(self):
        vida = 35
        ataque = 7